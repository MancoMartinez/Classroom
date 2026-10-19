{#
  ardm_lookback — third dev-facing data-access macro.

  Returns the union of:
    - The current run's `map_<name>` (full, unbounded — no registry filter).
    - source('prod', name) filtered to the last `max_months` months by the
      version's partition-day column.

  The time bound applies ONLY to production rows. Current-run mapping is always
  returned in full — by definition it's the freshest the run has.

  Why mapping (not enrichment) is the current side:
    Reading via mapping_source(name) avoids the enrich_<name> → enrich_<name>
    self-reference cycle when the macro is called from within an enrichment
    model that enriches the SAME table (e.g. enrich_ardm_recalledtransaction
    calling ardm_lookback('ardm_recalledtransaction') for save↔recall pair
    matching). The DAG is always: enrich_<X> depends on map_<Y> for any Y.
    No enrichment ever depends on another enrichment, which keeps the
    parse-time graph simple and the macro single-call.

  Historical transaction-id resolution:
    Both the current side and the prod-side NOT IN dedup go through
    `mapping_source(name)` — not `ref('map_' ~ name)` directly. mapping_source
    applies `resolve_historical_id` so clients with
    `historical_transaction_id_enabled: true` get V1-canonical transactionids
    on both sides of the UNION, matching the V1 IDs that pyardm wrote to
    ARDMPROD pre-cutoff. Reading map_<name> raw would emit V2 hashes on the
    current side while prod carries V1, producing a mix downstream and
    breaking the NOT IN dedup (V1 prod-hashes never appear in V2 map-hashes
    → same logical transaction surfaces twice).

    Trade-off: callers that want enrichment-recomputed values for the CURRENT
    run (e.g. base_ff_ardm_header walking c164's recomputed `subtotal` via
    LAG/LEAD) read enrichment_base separately for current rows and compose
    the union explicitly:
        WITH curr AS (SELECT * FROM enrichment_base('ardm_header')),
             hist AS (SELECT * FROM ardm_lookback('ardm_header') h
                      WHERE h.transactionid NOT IN (SELECT transactionid FROM curr)
                        AND <affected-key predicate>)
        SELECT cols FROM curr UNION ALL SELECT cols FROM hist

  Companion macros:
    mapping_base(name)     → in-window mapping ∪ in-window prod fallback   (registry-filtered)
    enrichment_base(name)  → in-window enrich  ∪ in-window prod fallback   (registry-filtered)
    ardm_lookback(name)    → full mapping       ∪ time-bounded historical prod (no registry)

  Use `mapping_base` / `enrichment_base` when you only need the current run window
  (cross-batch fallback for txids that didn't arrive this batch). Use
  `ardm_lookback` when you need historical context — last reload event for a card,
  the original transaction behind a recalled transaction, prior-day baselines, etc.

  Args:
    name        : table name (e.g. 'ardm_giftcard', 'ardm_header').
    max_months  : How far back to scan production by partition-day. Default 6.
                  Pass `none` for unbounded (discouraged — multi-billion-row scans).

  Performance contract:
    Callers MUST add affected-key WHERE/EXISTS/JOIN downstream of this macro to
    scope the prod scan. The 6-month bound is a safety floor; affected-key
    pruning is what makes it cheap. Per `.claude/rules/dbt-standards.md`, every
    read of a production table must include the partition-day column in the
    predicate where the bound is knowable; callers of this macro inherit that
    obligation when they JOIN/EXISTS against another production table.

  Usage (cross-table lookup):
    -- inside enrich_ardm_recalledtransaction.sql:
    LEFT JOIN {{ ardm_lookback('ardm_header') }} oh
        ON oh.transactionid = r.origtransactionid

  Usage (within-table lookback — no special parameter needed):
    WITH current_giftcard AS (
        SELECT * FROM {{ mapping_base('ardm_giftcard') }}
    ),
    affected_cards AS (
        SELECT DISTINCT cardno FROM current_giftcard WHERE cardno IS NOT NULL
    )
    SELECT *
    FROM {{ ardm_lookback('ardm_giftcard') }} gc
    WHERE EXISTS (SELECT 1 FROM affected_cards ac WHERE ac.cardno = gc.cardno)
      AND gc.stdactiontype IN (15, 16)

  Usage (framework fastfact when you need enrichment-computed current-run
  values — split current vs historical explicitly):
    WITH enriched_headers AS (SELECT * FROM enrichment_base('ardm_header')),
         historical_headers AS (
             SELECT cols FROM {{ ardm_lookback('ardm_header') }} h
             WHERE EXISTS (affected_positions matching h)
               AND h.transactionid NOT IN (SELECT transactionid FROM enriched_headers)
         )
    SELECT cols FROM enriched_headers
    UNION ALL
    SELECT cols FROM historical_headers
#}

{% macro ardm_lookback(name, max_months=6) %}
  {#- Current side: route through mapping_source(name) so historical-id
      resolution (resolve_historical_id) applies consistently with
      mapping_base. mapping_source still resolves to ref('map_' ~ name)
      internally, so the enrich_<name> → enrich_<name> self-reference cycle
      is still impossible by construction. The raw `map_ref` is kept only
      for column discovery — its column list is identical to mapping_source's
      projection. -#}
  {%- set map_ref = ref('map_' ~ name) -%}

  {#- Column-projection: pull map_<name>'s column list at execute time so the
      production-side SELECT can drop any prod-only enrichment / fastfact
      columns. Mirrors mapping_base / enrichment_base.

      _prod_side_projection self-heals on new mapping cols missing from
      prod (see comment in mapping_base.sql). -#}
  {%- set read_prod = _should_read_prod(name) -%}
  {%- if execute -%}
    {%- set current_cols = adapter.get_columns_in_relation(map_ref) -%}
    {%- if read_prod -%}
      {%- set prod_relation = adapter.get_relation(
            database=target.database,
            schema=target.schema,
            identifier=name | upper
      ) -%}
    {%- else -%}
      {%- set prod_relation = none -%}
    {%- endif -%}
    {%- set prod_select_exprs = _prod_side_projection(current_cols, prod_relation) -%}
  {%- else -%}
    {%- set prod_select_exprs = [] -%}
  {%- endif -%}

  {#- Per-table grain: detail tables (registry kind 'ardm_detail') carry a
      per-row sequence key alongside the transaction grain key; the single-
      grain table does not. Derived from the registry `kind` (find_table). -#}
  {%- set has_recordseqno = (find_table(name).kind == 'ardm_detail') -%}

  {#- Partition-day column for the prod time-bound. Resolved from the version
      key-columns capability hook (context-flattened, same dispatch pattern as
      column_spec's table_spec). The Base engine reads the `partition_day` slot
      and emits whatever column the version package returns — it names no
      schema column itself. -#}
  {%- set _key_columns_fn = context.get('_snowtime_key_columns') -%}
  {%- if not _key_columns_fn -%}
    {{ exceptions.raise_compiler_error(
        "snowtimeBase.ardm_lookback: capability hook '_snowtime_key_columns' is not "
        "resolvable. The active project must depend on snowtimeV2 or snowtimeV3, which "
        "ship this hook."
    ) }}
  {%- endif -%}
  {%- set partition_day = _key_columns_fn()['partition_day'] -%}

  (
    SELECT *
    FROM (
      -- Current-run side: full mapping output via mapping_source so
      -- transactionid is historical-id-resolved (V1 for pre-cutoff rows
      -- on clients with historical_transaction_id_enabled). No registry
      -- filter — the lookback intentionally covers all current-run rows.
      SELECT c.*
      FROM {{ mapping_source(name) }} c

      {%- if read_prod %}

      UNION ALL BY NAME

      -- Production rows projected to mapping schema. Time-bounded by the
      -- partition-day column (the safety floor) so even a missing affected-key
      -- filter can't degrade to an unbounded scan. A prod row is dropped only when
      -- the current side carries the same unique_key (prod_not_superseded), so a
      -- split transaction keeps its earlier parts; both sides carry V1-resolved
      -- transactionids so the key match holds.
      SELECT {% if prod_select_exprs | length > 0 %}{{ prod_select_exprs | join(', ') }}{% else %}*{% endif %}
      FROM {{ source('prod', name) }} prod_side
      WHERE
        {#- Two-sided + UTC-anchored (partition_day_window). The upper bound is NOT
            optional: partition_day is a business date off the POS clock, so a stuck
            register can stamp 2070 and a `>=`-only window would carry that row as
            lookback context forever. max_months=none drops the lower bound only. -#}
        {{ partition_day_window(partition_day, months=max_months) }}
        AND {{ prod_not_superseded(name, 'prod_side', mapping_source(name)) }}
      {%- endif %}
    )
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY transactionid{{ ', recordseqno' if has_recordseqno else '' }}
        ORDER BY updateddatetime DESC NULLS LAST
    ) = 1
  )
{% endmacro %}

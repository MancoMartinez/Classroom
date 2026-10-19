{{ client_mapping_config(layer='mapping') }}

/*
    Mapping ardm_item for c092_khl (Kohl's) — V2 format.
    Source: flat_postransactions_item (one row per Item element).
    Mirrors pyardm/us/c092khl/ardm/sql/load_sql_scripts/ARDM_2_Item.sql.

    recordseqno: item_appriss_seq_local (LATERAL FLATTEN index + 1, equivalent to
    pyardm's ApprissSeqLocal per ARDM_2_Item.sql:126). Tickets 42850/41510 put
    LineItemSequenceNumber "on hold"; pyardm actually uses ApprissSeqLocal.

    Three INSERT branches per pyardm:
      1. Main Item (ns0_item) — full mapping incl. reference_product receipt description
      2. Special Service (ns0_item where LineItemSpecialService present) — sequence + N items per
      3. Shipping Charge (ns0_ecommercetransactionshipment) — synthetic non-merch line per
         shipment per pyardm ARDM_2_Item.sql:611-685. Reads flat_postransactions_shipment.
         Filter: shipping_charge_amount <> 0 per pyardm. recordseqno = +20000 offset to
         avoid collision with main_item (1..N) and special_service (10001..10000+K).
         Dedup of overlapping Special Service / Shipping Charge with identical amount is
         a pyardm post-INSERT cleanup (ARDM_2_Item.sql:782-794) deferred to enrich_ardm_item.

    orig* columns are cross-batch lookback (enrich_ardm_recalledtransaction resolves).
    Item post-INSERT updates (linediscountamount, priceadjflg, saleflg/returnflg swap,
    ecomflg propagation, receiptedflg for ecom returns, isfirstscanneditemflg /
    islastscanneditemflg, mismatch/itemfix subtotal correction) are owned by
    enrich_ardm_item.sql per the V2 layer split.
*/

WITH ref_prod AS (
    -- pyardm joins reference_product on articleid to populate itemreceiptdescription.
    -- Reading from prod per dbt-mapping.md (reference_merge runs first).
    -- depends_on: {{ ref('reference_product') }}
    SELECT articleid, receiptdescription
    FROM {{ source('prod', 'reference_product') }}
),

oper_disc_agg AS (
    -- Aggregates LineItemDiscount rows per item to derive operatorreducedflg.
    -- Snowflake cannot do a nested LATERAL in the flat model (unsupported subquery type),
    -- so this join computes the flag from the already-exploded item_discount flat model.
    SELECT
        store_number, register_identifier, transaction_number, transaction_sales_date,
        transaction_end_datetime,
        item_line_item_sequence_number,
        BOOLOR_AGG(
            discount_type_code IN ('D', 'P')
            AND line_item_discount_reason_code IN ('701','703','706','707','708','709')
        ) as has_operator_reduction_discount
    FROM {{ ref('flat_postransactions_item_discount') }}
    GROUP BY 1, 2, 3, 4, 5, 6
),

rtn_txns AS (
    -- Transactions that have an RTN relationship type — returns WITH receipt (pyardm
    -- ARDM_2_Item.sql:271-278: apprissid IS NOT NULL AND RTN AND sale_return_code IN ('B','R')
    -- → refundwithreceiptflg=TRUE). Using DISTINCT on the natural key since one header can have
    -- multiple relationship rows; we only need existence per transaction.
    SELECT DISTINCT store_number, register_identifier, transaction_number, transaction_sales_date,
                    transaction_end_datetime
    FROM {{ ref('flat_postransactions_transaction_relationship') }}
    WHERE transaction_relationship_type_code = 'RTN'
),

rtn_info AS (
    -- Per-line original-receipt keys for returned items. pyardm ARDM_2_Item.sql:88-108
    -- joins ns0_ItemReturnInformation to items on LineItemSequenceNumber. These keys are
    -- NOT present on flat_postransactions_item (p.item_return_orig_* is always NULL there);
    -- they live in the sibling ItemReturnInformation feed, keyed by line_item_sequence_number.
    -- Dedup to one row per (txn natural key, line) — the feed has ~1.3K multi-orig-per-line
    -- rows that would otherwise fan out item rows.
    SELECT
        store_number, register_identifier, transaction_number, transaction_sales_date,
        transaction_end_datetime,
        line_item_sequence_number,
        item_return_orig_store_number,
        item_return_orig_register_identifier,
        item_return_orig_transaction_number,
        item_return_orig_transaction_sales_date
    FROM {{ ref('flat_postransactions_item_return_information') }}
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY store_number, register_identifier, transaction_number,
                     transaction_sales_date, transaction_end_datetime, line_item_sequence_number
        ORDER BY item_return_orig_transaction_sales_date DESC NULLS LAST,
                 item_return_orig_store_number, item_return_orig_transaction_number
    ) = 1
),

main_item AS (
    select
        {{ get_transaction_id('try_cast(p.store_number AS INT)',
                              'try_cast(p.register_identifier AS INT)',
                              'try_cast(p.transaction_number AS INT)',
                              "p.transaction_end_datetime", fourth_key="p.transaction_end_time") }} as transactionid,
        p.item_appriss_seq_local                                                                         as recordseqno,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as inserteddatetime,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as updateddatetime,
        p.transaction_end_datetime                                   as endtransdatetime,
        try_cast(p.store_number AS INT)                                                                as storeno,
        try_cast(p.register_identifier AS INT)                                                         as posno,
        try_cast(p.transaction_number AS INT)                                                          as ticketno,
        try_to_date(p.transaction_sales_date)                                                          as tradingday,
        null::VARCHAR                                                                                  as cashierno,
        p.transaction_end_datetime                                   as recorddatetime,
        -- articleid/upc normalized (strip leading zeros) so this resolves against
        -- reference_product.articleid regardless of which feed zero-pads the UPC — RCS-29237.
        substring(ltrim(trim(p.upc_number), '0'), 1, 20)::VARCHAR                                        as articleid,
        substring(trim(p.sku_number), 1, 20)::VARCHAR                                                    as skuid,
        substring(ltrim(trim(p.upc_number), '0'), 1, 20)::VARCHAR                                        as upc,
        trim(p.department_number)::VARCHAR                                                             as department,
        (CASE
           WHEN length(p.sku_number) = 7 AND substr(p.sku_number, 5) = '000' AND p.sale_return_code IN ('S','A') THEN 6
           WHEN length(p.sku_number) = 8 AND substr(p.sku_number, 6) = '000' AND p.sale_return_code IN ('S','A') THEN 6
           WHEN length(p.sku_number) = 7 AND substr(p.sku_number, 5) = '000' AND p.sale_return_code IN ('R','B') THEN 7
           WHEN length(p.sku_number) = 8 AND substr(p.sku_number, 6) = '000' AND p.sale_return_code IN ('R','B') THEN 7
           WHEN p.sale_return_code = 'S' THEN 0
           WHEN p.sale_return_code = 'R' THEN 3
           WHEN p.sale_return_code = 'A' THEN 9
           WHEN p.sale_return_code = 'B' THEN 10
           ELSE 99
         END)::INT                                                                                     as itemrecordtype,
        (CASE
           WHEN length(p.sku_number) = 7 AND substr(p.sku_number, 5) = '000' AND p.sale_return_code IN ('S','A') THEN 6
           WHEN length(p.sku_number) = 8 AND substr(p.sku_number, 6) = '000' AND p.sale_return_code IN ('S','A') THEN 6
           WHEN length(p.sku_number) = 7 AND substr(p.sku_number, 5) = '000' AND p.sale_return_code IN ('R','B') THEN 7
           WHEN length(p.sku_number) = 8 AND substr(p.sku_number, 6) = '000' AND p.sale_return_code IN ('R','B') THEN 7
           WHEN p.sale_return_code IN ('S', 'A') THEN 1
           WHEN p.sale_return_code IN ('R', 'B') THEN 2
           ELSE 99
         END)::INT                                                                                     as stditemrecordtype,
        1::NUMBER(38,6)                                                                                as quantity,
        0::INT                                                                                         as unitofmeasure,
        0::INT                                                                                         as stdunitofmeasure,
        (CASE
           WHEN p.sale_return_code IN ('S','A') AND try_cast(p.sold_quantity AS NUMBER(38,6)) < 0
             THEN -1 * try_cast(p.sold_quantity AS NUMBER(38,6))
           WHEN p.sale_return_code IN ('S','A') AND try_cast(p.sold_quantity AS NUMBER(38,6)) > 0
             THEN try_cast(p.sold_quantity AS NUMBER(38,6))
           WHEN p.sale_return_code IN ('B','R') AND try_cast(p.sold_quantity AS NUMBER(38,6)) < 0
             THEN try_cast(p.sold_quantity AS NUMBER(38,6))
           WHEN p.sale_return_code IN ('B','R') AND try_cast(p.sold_quantity AS NUMBER(38,6)) > 0
             THEN -1 * try_cast(p.sold_quantity AS NUMBER(38,6))
           ELSE coalesce(try_cast(p.sold_quantity AS NUMBER(38,6)), 0)
         END)::INT                                                                                     as numberofitems,
        (CASE
           WHEN p.net_charged_amount is not null AND p.sold_quantity is not null AND try_cast(p.sold_quantity AS NUMBER(38,6)) <> 0
             THEN try_cast(p.net_charged_amount AS NUMBER(38,6)) / try_cast(p.sold_quantity AS NUMBER(38,6))
           ELSE 0
         END)::NUMBER(38,6)                                                                            as pricechargedperuom,
        coalesce(try_cast(p.net_charged_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                      as amountcharged,
        (CASE
           WHEN p.customer_charged_amount is not null AND p.sold_quantity is not null AND try_cast(p.sold_quantity AS NUMBER(38,6)) <> 0
             THEN try_cast(p.customer_charged_amount AS NUMBER(38,6)) / try_cast(p.sold_quantity AS NUMBER(38,6))
           ELSE 0
         END)::NUMBER(38,6)                                                                            as originalpriceperuom,
        coalesce(try_cast(p.customer_charged_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                 as originalamount,
        (CASE
           WHEN p.net_charged_amount is not null AND p.customer_charged_amount is not null
             AND p.sold_quantity is not null AND try_cast(p.sold_quantity AS NUMBER(38,6)) <> 0
             THEN (try_cast(p.customer_charged_amount AS NUMBER(38,6)) - try_cast(p.net_charged_amount AS NUMBER(38,6)))
                  / try_cast(p.sold_quantity AS NUMBER(38,6))
           ELSE 0
         END)::NUMBER(38,6)                                                                            as pricediffperuom,
        0::NUMBER(38,6)                                                                                as manualdiscountamount,
        -- linediscountamount: pyardm ARDM_2_ItemDiscount.sql post-INSERT update from itemdiscount sum.
        -- Mapping = 0; enrich_ardm_item populates from item-discount aggregate.
        0::NUMBER(38,6)                                                                                as linediscountamount,
        0::NUMBER(38,6)                                                                                as trandiscountamount,
        (coalesce(try_cast(p.customer_charged_amount AS NUMBER(38,6)), 0)
         - coalesce(try_cast(p.net_charged_amount AS NUMBER(38,6)), 0))::NUMBER(38,6)                  as differenceamount,
        -- pyardm casts inputs + result to numeric(14,2) (ARDM_2_Item.sql:218-224).
        -- Replicate exact cast chain: input::numeric(14,2) / input::numeric(14,2) then ::numeric(14,2).
        (CASE
           WHEN coalesce(p.customer_charged_amount::NUMBER(14,2), 0) <> 0
                AND p.net_charged_amount IS NOT NULL
             THEN (p.net_charged_amount::NUMBER(14,2)
                   / p.customer_charged_amount::NUMBER(14,2))::NUMBER(14,2)
           ELSE 1
         END)::NUMBER(38,6)                                                                            as differencepercentage,
        coalesce(try_cast(p.tax_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                              as taxamount,
        -- entrymode: pyardm ARDM_2_Item.sql:236-245 derives from item_source_type_code.
        --   S/X/Y/Z scanned → 1; K/I/0 keyed → 2; else 99.
        (CASE p.item_source_type_code
            WHEN 'S' THEN 1 WHEN 'X' THEN 1 WHEN 'Y' THEN 1 WHEN 'Z' THEN 1
            WHEN 'K' THEN 2 WHEN 'I' THEN 2 WHEN '0' THEN 2
            ELSE 99
         END)::INT                                                                                     as entrymode,
        (CASE p.item_source_type_code
            WHEN 'S' THEN 1 WHEN 'X' THEN 1 WHEN 'Y' THEN 1 WHEN 'Z' THEN 1
            WHEN 'K' THEN 2 WHEN 'I' THEN 2 WHEN '0' THEN 2
            ELSE 99
         END)::INT                                                                                     as stdentrymode,
        -- voidedflg per pyardm ARDM_2_Item.sql:247-250
        (CASE
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN TRUE
            WHEN p.line_item_void_resolution_code = 'V' AND p.sale_return_code = 'R' THEN TRUE
            ELSE FALSE
         END)::BOOLEAN                                                                                 as voidedflg,
        coalesce(oda.has_operator_reduction_discount, FALSE)::BOOLEAN                                   as operatorreducedflg,
        FALSE::BOOLEAN                                                                                 as manualpriceflg,
        -- taxexemptflg: pyardm ARDM_2_Item.sql:256-261 — AssignedTaxIdentifier IS NOT NULL AND <> ''.
        (CASE
            WHEN p.tax_amount is not null AND try_cast(p.tax_amount AS NUMBER(38,6)) <> 0 THEN FALSE
            WHEN p.item_assigned_tax_identifier is not null AND p.item_assigned_tax_identifier <> '' THEN TRUE
            ELSE FALSE
         END)::BOOLEAN                                                                                 as taxexemptflg,
        -- refundwithreceiptflg: pyardm ARDM_2_Item.sql:262-279 tri-source logic.
        -- RTN relationship branch resolved via rtn_txns CTE (cross-table join).
        (CASE
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN FALSE
            WHEN p.line_item_void_resolution_code = 'V' AND p.sale_return_code = 'R' THEN FALSE
            WHEN p.item_correct_line_item_number is not null THEN FALSE
            WHEN p.sale_return_code IN ('B', 'R') AND rtn.store_number IS NOT NULL THEN TRUE
            WHEN p.sale_return_code IN ('B', 'R') AND p.item_return_orig_transaction_sales_date is not null THEN TRUE
            ELSE FALSE
         END)::BOOLEAN                                                                                 as refundwithreceiptflg,
        FALSE::BOOLEAN                                                                                 as pricecheckflg,
        -- itemreceiptdescription: pyardm joins reference_product on articleid (substring upc 1-20).
        rp.receiptdescription::VARCHAR                                                                 as itemreceiptdescription,
        -- cancelflg per pyardm ARDM_2_Item.sql:283-285 — itemcorrectlineitemnumber not null
        (CASE WHEN p.item_correct_line_item_number is not null THEN TRUE ELSE FALSE END)::BOOLEAN      as cancelflg,
        99::INT                                                                                        as voidreason,
        99::INT                                                                                        as stdvoidreason,
        FALSE::BOOLEAN                                                                                 as isfirstscanneditemflg,
        FALSE::BOOLEAN                                                                                 as islastscanneditemflg,
        (CASE WHEN p.sale_return_code IN ('S','A') THEN TRUE ELSE FALSE END)::BOOLEAN                  as saleflg,
        (CASE WHEN p.sale_return_code IN ('R','B') THEN TRUE ELSE FALSE END)::BOOLEAN                  as returnflg,
        -- ecomflg per pyardm initial value FALSE; UPDATEs from EcommerceItemPlannedShipment + header.linkno → enrich_ardm_item.
        FALSE::BOOLEAN                                                                                 as ecomflg,
        -- receiptedflg per pyardm uses same CASE as refundwithreceiptflg (NOT gift_receipt_indicator).
        (CASE
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN FALSE
            WHEN p.line_item_void_resolution_code = 'V' AND p.sale_return_code = 'R' THEN FALSE
            WHEN p.item_correct_line_item_number is not null THEN FALSE
            WHEN p.sale_return_code IN ('B', 'R') AND rtn.store_number IS NOT NULL THEN TRUE
            WHEN p.sale_return_code IN ('B', 'R') AND p.item_return_orig_transaction_sales_date is not null THEN TRUE
            ELSE FALSE
         END)::BOOLEAN                                                                                 as receiptedflg,
        FALSE::BOOLEAN                                                                                 as borisflg,
        -- priceadjflg per pyardm ARDM_2_Item.sql:728-742 — paired-sign self-join, enrich_ardm_item.
        FALSE::BOOLEAN                                                                                 as priceadjflg,
        FALSE::BOOLEAN                                                                                 as nonmerchflg,
        null::INT                                                                                      as origtransactionid,
        -- orig* keys sourced from the per-line ItemReturnInformation feed (ri), gated by the
        -- same refundwithreceiptflg logic (pyardm NULLs orig keys where refundwithreceiptflg=FALSE,
        -- ARDM_2_Item.sql:720-726). p.item_return_orig_* on flat_postransactions_item is always NULL.
        (CASE
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN NULL
            WHEN p.line_item_void_resolution_code = 'V' AND p.sale_return_code = 'R' THEN NULL
            WHEN p.item_correct_line_item_number is not null THEN NULL
            WHEN p.sale_return_code IN ('B', 'R') AND rtn.store_number IS NOT NULL
                THEN try_to_date(ri.item_return_orig_transaction_sales_date)
            WHEN p.sale_return_code IN ('B', 'R') AND ri.item_return_orig_transaction_sales_date is not null
                THEN try_to_date(ri.item_return_orig_transaction_sales_date)
            ELSE NULL
         END)                                                                                         as origtradingday,
        (CASE
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN NULL
            WHEN p.line_item_void_resolution_code = 'V' AND p.sale_return_code = 'R' THEN NULL
            WHEN p.item_correct_line_item_number is not null THEN NULL
            WHEN p.sale_return_code IN ('B', 'R') AND rtn.store_number IS NOT NULL
                THEN try_cast(ri.item_return_orig_store_number AS INT)
            WHEN p.sale_return_code IN ('B', 'R') AND ri.item_return_orig_transaction_sales_date is not null
                THEN try_cast(ri.item_return_orig_store_number AS INT)
            ELSE NULL
         END)                                                                                         as origstoreno,
        (CASE
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN NULL
            WHEN p.line_item_void_resolution_code = 'V' AND p.sale_return_code = 'R' THEN NULL
            WHEN p.item_correct_line_item_number is not null THEN NULL
            WHEN p.sale_return_code IN ('B', 'R') AND rtn.store_number IS NOT NULL
                THEN try_cast(ri.item_return_orig_register_identifier AS INT)
            WHEN p.sale_return_code IN ('B', 'R') AND ri.item_return_orig_transaction_sales_date is not null
                THEN try_cast(ri.item_return_orig_register_identifier AS INT)
            ELSE NULL
         END)                                                                                         as origposno,
        (CASE
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN NULL
            WHEN p.line_item_void_resolution_code = 'V' AND p.sale_return_code = 'R' THEN NULL
            WHEN p.item_correct_line_item_number is not null THEN NULL
            WHEN p.sale_return_code IN ('B', 'R') AND rtn.store_number IS NOT NULL
                THEN try_cast(ri.item_return_orig_transaction_number AS INT)
            WHEN p.sale_return_code IN ('B', 'R') AND ri.item_return_orig_transaction_sales_date is not null
                THEN try_cast(ri.item_return_orig_transaction_number AS INT)
            ELSE NULL
         END)                                                                                         as origticketno,
        0::NUMBER(38,6)                                                                                as origitempurchaseamount,
        99::INT                                                                                        as origentrymode,
        FALSE::BOOLEAN                                                                                 as origmanualpriceflg,
        FALSE::BOOLEAN                                                                                 as iteminorigreceiptflg,
        FALSE::BOOLEAN                                                                                 as qtyisweightflg,
        FALSE::BOOLEAN                                                                                 as taxoverrideflg,
        null::VARCHAR                                                                                  as returnreason,
        null::VARCHAR                                                                                  as priceoverridereason,
        null::INT                                                                                      as origitemseqno,
        null::VARCHAR                                                                                  as origorderno,
        FALSE::BOOLEAN                                                                                 as bopisflg,
        FALSE::BOOLEAN                                                                                 as boroflg,
        null::INT                                                                                      as ecomreceivallocation,
        null::INT                                                                                      as stdecomreceivallocation,
        null::INT                                                                                      as ecomfulfillmentlocation,
        null::INT                                                                                      as stdecomfulfillmentlocation,
        null::INT                                                                                      as pickupstoreno,
        null::NUMBER(38,6)                                                                             as amountchargedbase,
        null::NUMBER(38,6)                                                                             as originalamountbase,
        null::NUMBER(38,6)                                                                             as manualdiscountamountbase,
        null::NUMBER(38,6)                                                                             as linediscountamountbase,
        null::NUMBER(38,6)                                                                             as trandiscountamountbase,
        null::NUMBER(38,6)                                                                             as taxamountbase,
        null::NUMBER(38,6)                                                                             as costofgoodssold,
        null::INT                                                                                      as fulfillmentstoreno,
        -- x_* extensions
        -- x_itemsourcetypecode: pyardm ARDM_2_Item.sql:412-420 maps string→smallint for item_ext.
        (CASE p.item_source_type_code
            WHEN 'S' THEN 10 WHEN 'X' THEN 11 WHEN 'Y' THEN 13 WHEN 'Z' THEN 14
            WHEN 'K' THEN 17 WHEN 'I' THEN 15 WHEN '0' THEN 16
            ELSE COALESCE(TRY_TO_NUMBER(p.item_source_type_code), 99)
         END)::NUMBER(38,6)                                                                            as x_itemsourcetypecode,
        p.ownership_code::VARCHAR                                                                      as x_ownershipcode,
        -- item_ext columns (pyardm ARDM_2_Item.sql:344-428, ardm_item_ext_update, main items only)
        -- x_description: itemassignedtaxidentifier not null → 'True' else 'False' (:372-374).
        -- pyardm's tlog loader nullifies empty-string but KEEPS a single space, so its
        -- `is not null` is True for " " and False for "". Mirror with `<> ''` (NEVER trim —
        -- trimming would drop the space to '' and wrongly flip ~29.8M rows to False).
        (CASE WHEN p.item_assigned_tax_identifier is not null AND p.item_assigned_tax_identifier <> '' THEN 'True' ELSE 'False' END)::VARCHAR    as x_description,
        -- x_directshipfromvendorindicator: direct_ship_from_vendor_indicator='Y' → 1 else 0 (:402-405)
        (CASE WHEN p.direct_ship_from_vendor_indicator = 'Y' THEN TRUE ELSE FALSE END)::BOOLEAN          as x_directshipfromvendorindicator,
        -- x_itemcallbackindicator: pyardm ARDM_2_Item.sql:398-401 sources this from
        -- ItemLevelReturnProcessingIndicator (NOT ItemCallbackIndicator — a pyardm quirk).
        (CASE WHEN p.item_level_return_processing_indicator = 'Y' THEN TRUE ELSE FALSE END)::BOOLEAN     as x_itemcallbackindicator,
        -- x_itemdeptwastetype: item_callback_indicator='Y' → 1 else 0 (:361-364)
        (CASE WHEN p.item_callback_indicator = 'Y' THEN 1 ELSE 0 END)::INT                               as x_itemdeptwastetype,
        -- x_itemlevelreturnprocessingindicator: item_level_return_processing_indicator='Y' → 1 else 0 (:394-397)
        (CASE WHEN p.item_level_return_processing_indicator = 'Y' THEN TRUE ELSE FALSE END)::BOOLEAN     as x_itemlevelreturnprocessingindicator,
        -- x_itemstatuscode: numeric-guarded item_status_code, else 0 (:388-393)
        (CASE
            WHEN p.item_status_code is not null AND p.item_status_code <> ''
                 AND regexp_like(p.item_status_code, '^[0-9.]+$')
                THEN try_cast(p.item_status_code AS INT)
            ELSE 0
         END)::INT                                                                                      as x_itemstatuscode,
        -- x_merchandiseexceptionhandlingcode: merchandise_exception_handling_code::int else 99 (:383-387)
        (CASE
            WHEN p.merchandise_exception_handling_code is not null AND p.merchandise_exception_handling_code <> ''
                THEN try_cast(p.merchandise_exception_handling_code AS INT)
            ELSE 99
         END)::INT                                                                                      as x_merchandiseexceptionhandlingcode,
        -- x_pricesourcecode: I→1, K→2, else 99 (:375-379)
        (CASE p.price_source_code WHEN 'I' THEN 1 WHEN 'K' THEN 2 ELSE 99 END)::INT                      as x_pricesourcecode,
        -- x_skuerrorcode: sku_error_code::int when not null, else NULL (:380-382 — no ELSE branch)
        (CASE
            WHEN p.sku_error_code is not null AND p.sku_error_code <> ''
                THEN try_cast(p.sku_error_code AS INT)
            ELSE NULL
         END)::INT                                                                                      as x_skuerrorcode,
        -- x_subjecttotaxamount: subject_to_tax_amount, else 0 (:406-410)
        coalesce(p.subject_to_tax_amount, 0)::NUMBER(38,6)                                              as x_subjecttotaxamount,
        -- x_ticketreducedflg: pyardm i2.OverrideFlg (:365-368) — set when a prelim_price_override
        -- row exists, which uses the IDENTICAL discount filter (D/P + reason 701/703/706/707/708/709)
        -- as operatorreducedflg. Same expression as operatorreducedflg above.
        coalesce(oda.has_operator_reduction_discount, FALSE)::BOOLEAN                                    as x_ticketreducedflg,
        -- x_origorderno: BORIS overlay populated by enrich_ardm_item (orig header linkno).
        -- Mirrors recalled-side overlay in enrich_ardm_recalledtransaction.
        null::VARCHAR                                                                                  as x_origorderno,
        p.file_name::VARCHAR                                                                           as filename
    from {{ ref('flat_postransactions_item') }} p
    left join ref_prod rp on rp.articleid = ltrim(trim(p.upc_number), '0')
    left join oper_disc_agg oda
        on oda.store_number = p.store_number
       and oda.register_identifier = p.register_identifier
       and oda.transaction_number = p.transaction_number
       and oda.transaction_sales_date = p.transaction_sales_date
       -- scope to the specific transaction doc (dual-doc tickets); pyardm joins by apprissid
       and oda.transaction_end_datetime = p.transaction_end_datetime
       and oda.item_line_item_sequence_number = p.line_item_sequence_number
    left join rtn_txns rtn
        on rtn.store_number = p.store_number
       and rtn.register_identifier = p.register_identifier
       and rtn.transaction_number = p.transaction_number
       and rtn.transaction_sales_date = p.transaction_sales_date
       -- scope to the specific transaction doc (dual-doc tickets); pyardm joins by apprissid
       and rtn.transaction_end_datetime = p.transaction_end_datetime
    left join rtn_info ri
        on ri.store_number = p.store_number
       and ri.register_identifier = p.register_identifier
       and ri.transaction_number = p.transaction_number
       and ri.transaction_sales_date = p.transaction_sales_date
       -- scope to the specific transaction doc (dual-doc tickets); pyardm joins by apprissid
       and ri.transaction_end_datetime = p.transaction_end_datetime
       and ri.line_item_sequence_number = p.line_item_sequence_number
),

special_service_item AS (
    -- Branch 2: Special Service item (pyardm ARDM_2_Item.sql:441-567).
    -- Items with LineItemSpecialService.LineItemSequenceNumber present create a synthetic
    -- non-merch line. recordseqno = COALESCE(MAX(item.recordseqno) per TID, 0) + apprissseqlocal.
    -- Mapping emits with a high recordseqno offset (+10000) since we can't compute MAX(recordseqno)
    -- per TID without a downstream pass. enrich_ardm_item can re-base after framework dedup.
    select
        {{ get_transaction_id('try_cast(p.store_number AS INT)',
                              'try_cast(p.register_identifier AS INT)',
                              'try_cast(p.transaction_number AS INT)',
                              "p.transaction_end_datetime", fourth_key="p.transaction_end_time") }} as transactionid,
        (10000 + coalesce(try_cast(p.item_appriss_seq_local AS INT), 0))::INT                               as recordseqno,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as inserteddatetime,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as updateddatetime,
        p.transaction_end_datetime                                   as endtransdatetime,
        try_cast(p.store_number AS INT)                                                                as storeno,
        try_cast(p.register_identifier AS INT)                                                         as posno,
        try_cast(p.transaction_number AS INT)                                                          as ticketno,
        try_to_date(p.transaction_sales_date)                                                          as tradingday,
        null::VARCHAR                                                                                  as cashierno,
        p.transaction_end_datetime                                   as recorddatetime,
        lpad('', 20, '0')::VARCHAR                                                                     as articleid,
        lpad('', 20, '0')::VARCHAR                                                                     as skuid,
        lpad('', 20, '0')::VARCHAR                                                                     as upc,
        lpad('', 10, '0')::VARCHAR                                                                     as department,
        99::INT                                                                                        as itemrecordtype,
        5::INT                                                                                         as stditemrecordtype,
        (CASE WHEN p.sale_return_code = 'S' THEN 1 WHEN p.sale_return_code = 'R' THEN -1 ELSE 0 END)::NUMBER(38,6) as quantity,
        0::INT                                                                                         as unitofmeasure,
        0::INT                                                                                         as stdunitofmeasure,
        (CASE WHEN p.sale_return_code = 'S' THEN 1 WHEN p.sale_return_code = 'R' THEN -1 ELSE 0 END)::INT as numberofitems,
        (CASE
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            ELSE 0
         END)::NUMBER(38,6)                                                                            as pricechargedperuom,
        (CASE
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            ELSE 0
         END)::NUMBER(38,6)                                                                            as amountcharged,
        (CASE
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            ELSE 0
         END)::NUMBER(38,6)                                                                            as originalpriceperuom,
        (CASE
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'S' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) < 0
                THEN try_cast(p.special_service_amount AS NUMBER(38,6))
            WHEN p.sale_return_code = 'R' AND try_cast(p.special_service_amount AS NUMBER(38,6)) > 0
                THEN -1 * try_cast(p.special_service_amount AS NUMBER(38,6))
            ELSE 0
         END)::NUMBER(38,6)                                                                            as originalamount,
        0::NUMBER(38,6)                                                                                as pricediffperuom,
        0::NUMBER(38,6)                                                                                as manualdiscountamount,
        0::NUMBER(38,6)                                                                                as linediscountamount,
        0::NUMBER(38,6)                                                                                as trandiscountamount,
        0::NUMBER(38,6)                                                                                as differenceamount,
        0::NUMBER(38,6)                                                                                as differencepercentage,
        coalesce(try_cast(p.special_service_tax_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)              as taxamount,
        99::INT                                                                                        as entrymode,
        99::INT                                                                                        as stdentrymode,
        FALSE::BOOLEAN                                                                                 as voidedflg,
        FALSE::BOOLEAN                                                                                 as operatorreducedflg,
        FALSE::BOOLEAN                                                                                 as manualpriceflg,
        (CASE WHEN p.special_service_tax_amount is null OR try_cast(p.special_service_tax_amount AS NUMBER(38,6)) = 0
              THEN TRUE ELSE FALSE END)::BOOLEAN                                                       as taxexemptflg,
        FALSE::BOOLEAN                                                                                 as refundwithreceiptflg,
        FALSE::BOOLEAN                                                                                 as pricecheckflg,
        'Special Service'::VARCHAR                                                                     as itemreceiptdescription,
        FALSE::BOOLEAN                                                                                 as cancelflg,
        99::INT                                                                                        as voidreason,
        99::INT                                                                                        as stdvoidreason,
        FALSE::BOOLEAN                                                                                 as isfirstscanneditemflg,
        FALSE::BOOLEAN                                                                                 as islastscanneditemflg,
        (CASE WHEN p.sale_return_code = 'S' THEN TRUE ELSE FALSE END)::BOOLEAN                         as saleflg,
        (CASE WHEN p.sale_return_code = 'R' THEN TRUE ELSE FALSE END)::BOOLEAN                         as returnflg,
        TRUE::BOOLEAN                                                                                  as ecomflg,
        FALSE::BOOLEAN                                                                                 as receiptedflg,
        FALSE::BOOLEAN                                                                                 as borisflg,
        FALSE::BOOLEAN                                                                                 as priceadjflg,
        TRUE::BOOLEAN                                                                                  as nonmerchflg,
        null::INT                                                                                      as origtransactionid,
        null::DATE                                                                                     as origtradingday,
        0::INT                                                                                         as origstoreno,
        0::INT                                                                                         as origposno,
        0::INT                                                                                         as origticketno,
        0::NUMBER(38,6)                                                                                as origitempurchaseamount,
        99::INT                                                                                        as origentrymode,
        FALSE::BOOLEAN                                                                                 as origmanualpriceflg,
        FALSE::BOOLEAN                                                                                 as iteminorigreceiptflg,
        FALSE::BOOLEAN                                                                                 as qtyisweightflg,
        FALSE::BOOLEAN                                                                                 as taxoverrideflg,
        null::VARCHAR                                                                                  as returnreason,
        null::VARCHAR                                                                                  as priceoverridereason,
        null::INT                                                                                      as origitemseqno,
        null::VARCHAR                                                                                  as origorderno,
        FALSE::BOOLEAN                                                                                 as bopisflg,
        FALSE::BOOLEAN                                                                                 as boroflg,
        null::INT                                                                                      as ecomreceivallocation,
        null::INT                                                                                      as stdecomreceivallocation,
        null::INT                                                                                      as ecomfulfillmentlocation,
        null::INT                                                                                      as stdecomfulfillmentlocation,
        null::INT                                                                                      as pickupstoreno,
        null::NUMBER(38,6)                                                                             as amountchargedbase,
        null::NUMBER(38,6)                                                                             as originalamountbase,
        null::NUMBER(38,6)                                                                             as manualdiscountamountbase,
        null::NUMBER(38,6)                                                                             as linediscountamountbase,
        null::NUMBER(38,6)                                                                             as trandiscountamountbase,
        null::NUMBER(38,6)                                                                             as taxamountbase,
        null::NUMBER(38,6)                                                                             as costofgoodssold,
        null::INT                                                                                      as fulfillmentstoreno,
        (CASE p.item_source_type_code
            WHEN 'S' THEN 10 WHEN 'X' THEN 11 WHEN 'Y' THEN 13 WHEN 'Z' THEN 14
            WHEN 'K' THEN 17 WHEN 'I' THEN 15 WHEN '0' THEN 16
            ELSE COALESCE(TRY_TO_NUMBER(p.item_source_type_code), 99)
         END)::NUMBER(38,6)                                                                            as x_itemsourcetypecode,
        p.ownership_code::VARCHAR                                                                      as x_ownershipcode,
        -- item_ext columns: pyardm emits ardm_item_ext_update rows for MAIN ns0_item only, not for
        -- synthetic Special Service lines. Emit column defaults to keep the UNION aligned.
        'False'::VARCHAR                                                                               as x_description,
        FALSE::BOOLEAN                                                                                 as x_directshipfromvendorindicator,
        FALSE::BOOLEAN                                                                                 as x_itemcallbackindicator,
        0::INT                                                                                         as x_itemdeptwastetype,
        FALSE::BOOLEAN                                                                                 as x_itemlevelreturnprocessingindicator,
        0::INT                                                                                         as x_itemstatuscode,
        99::INT                                                                                        as x_merchandiseexceptionhandlingcode,
        99::INT                                                                                        as x_pricesourcecode,
        null::INT                                                                                      as x_skuerrorcode,
        0::NUMBER(38,6)                                                                                as x_subjecttotaxamount,
        FALSE::BOOLEAN                                                                                 as x_ticketreducedflg,
        -- x_origorderno: BORIS overlay populated by enrich_ardm_item.
        null::VARCHAR                                                                                  as x_origorderno,
        p.file_name::VARCHAR                                                                           as filename
    from {{ ref('flat_postransactions_item') }} p
    where p.special_service_line_item_seq is not null
),

shipping_charge_item AS (
    -- Branch 3: Ecommerce shipment charge (pyardm ARDM_2_Item.sql:611-685).
    -- Synthetic non-merch line per EcommerceTransactionShipment with
    --   amount = shipping_charge_amount, taxamount = shipping_tax_amount.
    -- pyardm filter: shipping_charge_amount <> 0.
    -- recordseqno: pyardm uses COALESCE(MAX(item.recordseqno) per TID, 0) + apprissseqlocal;
    -- V2 cannot compute the per-TID max in mapping, so a +20000 offset is used to keep these
    -- rows non-colliding with main_item (1..N) and special_service (10001..10000+K).
    -- Hardcoded literals (itemrecordtype=99, stditemrecordtype=5, quantity=1,
    -- entrymode=99, ecomflg=TRUE, nonmerchflg=TRUE, articleid/skuid/upc as 20×'0',
    -- department as 10×'0', itemreceiptdescription='Shipping Charge') mirror pyardm.
    select
        {{ get_transaction_id('try_cast(p.store_number AS INT)',
                              'try_cast(p.register_identifier AS INT)',
                              'try_cast(p.transaction_number AS INT)',
                              "p.transaction_end_datetime", fourth_key="p.transaction_end_time") }} as transactionid,
        (20000 + coalesce(try_cast(p.shipment_seq_local AS INT), 0))::INT                                 as recordseqno,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as inserteddatetime,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as updateddatetime,
        p.transaction_end_datetime                                   as endtransdatetime,
        try_cast(p.store_number AS INT)                                                                as storeno,
        try_cast(p.register_identifier AS INT)                                                         as posno,
        try_cast(p.transaction_number AS INT)                                                          as ticketno,
        try_to_date(p.transaction_sales_date)                                                          as tradingday,
        null::VARCHAR                                                                                  as cashierno,
        p.transaction_end_datetime                                   as recorddatetime,
        lpad('', 20, '0')::VARCHAR                                                                     as articleid,
        lpad('', 20, '0')::VARCHAR                                                                     as skuid,
        lpad('', 20, '0')::VARCHAR                                                                     as upc,
        lpad('', 10, '0')::VARCHAR                                                                     as department,
        99::INT                                                                                        as itemrecordtype,
        5::INT                                                                                         as stditemrecordtype,
        1::NUMBER(38,6)                                                                                as quantity,
        0::INT                                                                                         as unitofmeasure,
        0::INT                                                                                         as stdunitofmeasure,
        1::INT                                                                                         as numberofitems,
        coalesce(try_cast(p.shipping_charge_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                  as pricechargedperuom,
        coalesce(try_cast(p.shipping_charge_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                  as amountcharged,
        coalesce(try_cast(p.shipping_charge_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                  as originalpriceperuom,
        coalesce(try_cast(p.shipping_charge_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                  as originalamount,
        0::NUMBER(38,6)                                                                                as pricediffperuom,
        0::NUMBER(38,6)                                                                                as manualdiscountamount,
        0::NUMBER(38,6)                                                                                as linediscountamount,
        0::NUMBER(38,6)                                                                                as trandiscountamount,
        0::NUMBER(38,6)                                                                                as differenceamount,
        0::NUMBER(38,6)                                                                                as differencepercentage,
        coalesce(try_cast(p.shipping_tax_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                     as taxamount,
        99::INT                                                                                        as entrymode,
        99::INT                                                                                        as stdentrymode,
        FALSE::BOOLEAN                                                                                 as voidedflg,
        FALSE::BOOLEAN                                                                                 as operatorreducedflg,
        FALSE::BOOLEAN                                                                                 as manualpriceflg,
        -- taxexemptflg pyardm:649-653 — shipping_tax_amount null/0 → TRUE
        (CASE WHEN p.shipping_tax_amount is null OR try_cast(p.shipping_tax_amount AS NUMBER(38,6)) = 0
              THEN TRUE ELSE FALSE END)::BOOLEAN                                                       as taxexemptflg,
        FALSE::BOOLEAN                                                                                 as refundwithreceiptflg,
        FALSE::BOOLEAN                                                                                 as pricecheckflg,
        'Shipping Charge'::VARCHAR                                                                     as itemreceiptdescription,
        FALSE::BOOLEAN                                                                                 as cancelflg,
        99::INT                                                                                        as voidreason,
        99::INT                                                                                        as stdvoidreason,
        FALSE::BOOLEAN                                                                                 as isfirstscanneditemflg,
        FALSE::BOOLEAN                                                                                 as islastscanneditemflg,
        TRUE::BOOLEAN                                                                                  as saleflg,
        FALSE::BOOLEAN                                                                                 as returnflg,
        TRUE::BOOLEAN                                                                                  as ecomflg,
        FALSE::BOOLEAN                                                                                 as receiptedflg,
        FALSE::BOOLEAN                                                                                 as borisflg,
        FALSE::BOOLEAN                                                                                 as priceadjflg,
        TRUE::BOOLEAN                                                                                  as nonmerchflg,
        null::INT                                                                                      as origtransactionid,
        null::DATE                                                                                     as origtradingday,
        0::INT                                                                                         as origstoreno,
        0::INT                                                                                         as origposno,
        0::INT                                                                                         as origticketno,
        0::NUMBER(38,6)                                                                                as origitempurchaseamount,
        99::INT                                                                                        as origentrymode,
        FALSE::BOOLEAN                                                                                 as origmanualpriceflg,
        FALSE::BOOLEAN                                                                                 as iteminorigreceiptflg,
        FALSE::BOOLEAN                                                                                 as qtyisweightflg,
        FALSE::BOOLEAN                                                                                 as taxoverrideflg,
        null::VARCHAR                                                                                  as returnreason,
        null::VARCHAR                                                                                  as priceoverridereason,
        null::INT                                                                                      as origitemseqno,
        null::VARCHAR                                                                                  as origorderno,
        FALSE::BOOLEAN                                                                                 as bopisflg,
        FALSE::BOOLEAN                                                                                 as boroflg,
        null::INT                                                                                      as ecomreceivallocation,
        null::INT                                                                                      as stdecomreceivallocation,
        null::INT                                                                                      as ecomfulfillmentlocation,
        null::INT                                                                                      as stdecomfulfillmentlocation,
        null::INT                                                                                      as pickupstoreno,
        null::NUMBER(38,6)                                                                             as amountchargedbase,
        null::NUMBER(38,6)                                                                             as originalamountbase,
        null::NUMBER(38,6)                                                                             as manualdiscountamountbase,
        null::NUMBER(38,6)                                                                             as linediscountamountbase,
        null::NUMBER(38,6)                                                                             as trandiscountamountbase,
        null::NUMBER(38,6)                                                                             as taxamountbase,
        null::NUMBER(38,6)                                                                             as costofgoodssold,
        null::INT                                                                                      as fulfillmentstoreno,
        null::NUMBER(38,6)                                                                             as x_itemsourcetypecode,
        null::VARCHAR                                                                                  as x_ownershipcode,
        -- item_ext columns: pyardm emits ardm_item_ext_update rows for MAIN ns0_item only, not for
        -- synthetic Shipping Charge lines. Emit column defaults to keep the UNION aligned.
        'False'::VARCHAR                                                                               as x_description,
        FALSE::BOOLEAN                                                                                 as x_directshipfromvendorindicator,
        FALSE::BOOLEAN                                                                                 as x_itemcallbackindicator,
        0::INT                                                                                         as x_itemdeptwastetype,
        FALSE::BOOLEAN                                                                                 as x_itemlevelreturnprocessingindicator,
        0::INT                                                                                         as x_itemstatuscode,
        99::INT                                                                                        as x_merchandiseexceptionhandlingcode,
        99::INT                                                                                        as x_pricesourcecode,
        null::INT                                                                                      as x_skuerrorcode,
        0::NUMBER(38,6)                                                                                as x_subjecttotaxamount,
        FALSE::BOOLEAN                                                                                 as x_ticketreducedflg,
        null::VARCHAR                                                                                  as x_origorderno,
        p.file_name::VARCHAR                                                                           as filename
    from {{ ref('flat_postransactions_shipment') }} p
    where coalesce(try_cast(p.shipping_charge_amount AS NUMBER(38,6)), 0) <> 0
),

header_cashierno AS (
    SELECT transactionid, cashierno FROM {{ ref('map_ardm_header') }}
)

select
    d.* exclude (cashierno),
    coalesce(hc.cashierno, '0')::VARCHAR as cashierno
from (
    select * from main_item
    union all select * from special_service_item
    union all select * from shipping_charge_item
) d
left join header_cashierno hc on hc.transactionid = d.transactionid

{{ client_mapping_config(layer='mapping') }}

/*
    Mapping ardm_itemdiscount for c092_khl (Kohl's) — V2 format.
    Source: flat_postransactions_item_discount (one row per LineItemDiscount).
    Mirrors pyardm/us/c092khl/ardm/sql/load_sql_scripts/ARDM_2_ItemDiscount.sql.

    Two INSERT branches per pyardm:
      1. Main item discounts (LineItemDiscount), excludes discount_type_code IN ('E','G')
      2. Employee item discount (Item.EmployeeItemDiscount) — staff discount with
         employeediscountflg=1, staffid/cardtoken from associate_identifier.
         Source: flat_postransactions_item where employee_discount_line_item_seq is not null
         AND employee_discount_type_code NOT IN ('E','G'). pyardm ARDM_2_ItemDiscount.sql:
         225-388 (prelim_ItemDiscounts2) → 398-500 (INSERT).

    Joins ns0_item via lineitemsequencenumber to populate articleid/upc/originalamount/
    actualprice from the parent item row.

    recordseqno: pyardm uses row_number() ordered by ApprissSeqLocal (parent item's
    XML element position), then LineItemDiscountSequenceNumber. V2 mirrors this via
    item_appriss_seq_local (LATERAL FLATTEN index + 1) from the flat model.
*/

WITH parent_item AS (
    -- Join the parent item row to inherit articleid / upc / originalamount / actualprice
    -- per pyardm prelim_ItemDiscounts CTE (ARDM_2_ItemDiscount.sql:11-93).
    SELECT
        store_number,
        register_identifier,
        transaction_number,
        transaction_sales_date,
        transaction_end_datetime,
        line_item_sequence_number,
        item_appriss_seq_local,
        upc_number,
        sku_number,
        customer_charged_amount,
        net_charged_amount
    FROM {{ ref('flat_postransactions_item') }}
),

parent_transaction AS (
    -- pyardm prelim_ItemDiscounts2 joins ns0_transaction for associate_transaction_associate_identifier.
    SELECT
        store_number,
        register_identifier,
        transaction_number,
        transaction_sales_date,
        transaction_end_datetime,
        associate_transaction_associate_identifier
    FROM {{ ref('flat_postransactions') }}
),

all_item_discounts_numbered AS (
-- pyardm prelim_ItemDiscounts computes row_number() over ALL rows (including E/G)
-- BEFORE the E/G exclusion filter. Numbering first leaves gaps in recordseqno.

select
    {{ get_transaction_id('try_cast(p.store_number AS INT)',
                          'try_cast(p.register_identifier AS INT)',
                          'try_cast(p.transaction_number AS INT)',
                          "p.transaction_end_datetime", fourth_key="p.transaction_end_time") }} as transactionid,
    row_number() over (partition by
        try_cast(p.store_number AS INT),
        try_cast(p.register_identifier AS INT),
        try_cast(p.transaction_number AS INT),
        try_to_date(p.transaction_sales_date),
        -- per-doc: pyardm numbers recordseqno per h.transactionid (endtime-encoded, ARDM_2_ItemDiscount:27)
        p.transaction_end_datetime,
        p.file_name
        -- pyardm (ARDM_2_ItemDiscount.sql:27) orders by ApprissSeqLocal LEXICALLY
        -- (source string column): "10" sorts before "2". Mirror with ::VARCHAR so the
        -- gapped row_number lands on the same physical rows pyardm numbers. A numeric
        -- sort (2<10) reshuffles recordseqno for any txn with >=10 discounted items,
        -- mismatching every per-row column under composite-key AND content-rank.
        order by p.item_appriss_seq_local::VARCHAR,
                 p.line_item_discount_sequence_number::VARCHAR)::INT                                as recordseqno,
    p.file_arrival_time::TIMESTAMP_NTZ                                                             as inserteddatetime,
    p.file_arrival_time::TIMESTAMP_NTZ                                                             as updateddatetime,
    p.transaction_end_datetime                                   as endtransdatetime,
    try_cast(p.store_number AS INT)                                                                as storeno,
    try_cast(p.register_identifier AS INT)                                                         as posno,
    try_cast(p.transaction_number AS INT)                                                          as ticketno,
    try_to_date(p.transaction_sales_date)                                                          as tradingday,
    null::VARCHAR                                                                                  as cashierno,
    p.transaction_end_datetime                                   as recorddatetime,
    -- articleid / upc / skuid inherited from parent item per pyardm join.
    -- articleid/upc normalized (strip leading zeros) to match reference_product.articleid — RCS-29237.
    ltrim(trim(i.upc_number), '0')::VARCHAR                                                        as articleid,
    trim(i.sku_number)::VARCHAR                                                                    as skuid,
    ltrim(trim(i.upc_number), '0')::VARCHAR                                                        as upc,
    coalesce(try_cast(p.discount_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                         as amount,
    coalesce(try_cast(p.discount_percent AS NUMBER(38,6)), 0)::NUMBER(38,6)                        as percentage,
    99::INT                                                                                        as entrymode,
    99::INT                                                                                        as stdentrymode,
    -- promotionid: pyardm substring(credit_marketing_coupon_number, 1, 5)
    (CASE
        WHEN p.credit_marketing_coupon_number is not null AND p.credit_marketing_coupon_number <> ''
            THEN substring(p.credit_marketing_coupon_number, 1, 5)
        ELSE NULL
     END)::VARCHAR                                                                                 as promotionid,
    null::VARCHAR                                                                                  as discountcode,
    FALSE::BOOLEAN                                                                                 as discountvoidedflg,
    i.item_appriss_seq_local                                                                       as itemrecordseqno,
    coalesce(try_cast(i.customer_charged_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                 as originalamount,
    coalesce(try_cast(i.net_charged_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                      as actualprice,
    99::INT                                                                                        as voidreason,
    99::INT                                                                                        as stdvoidreason,
    99::INT                                                                                        as valuechangemethod,
    99::INT                                                                                        as stdvaluechangemethod,
    -- valuechangereason: pyardm ARDM_2_ItemDiscount.sql:143-151 — int cast w/ overflow guard
    (CASE
        WHEN p.line_item_discount_reason_code is not null AND p.line_item_discount_reason_code <> '' AND
             regexp_like(p.line_item_discount_reason_code, '^[0-9]+$') AND
             try_cast(p.line_item_discount_reason_code AS INT) > 32767 THEN 99
        WHEN p.line_item_discount_reason_code is not null AND p.line_item_discount_reason_code <> '' AND
             regexp_like(p.line_item_discount_reason_code, '^[0-9]+$')
             THEN try_cast(p.line_item_discount_reason_code AS INT)
        ELSE 99
     END)::INT                                                                                     as x_valuechangereason,
    -- valuechangetype: pyardm 19-branch CASE on discount_type_code (ARDM_2_ItemDiscount.sql:152-192)
    (CASE p.discount_type_code
        WHEN 'A' THEN 1  WHEN 'B' THEN 2  WHEN 'C' THEN 3  WHEN 'D' THEN 4
        WHEN 'E' THEN 5  WHEN 'F' THEN 6  WHEN 'G' THEN 7  WHEN 'H' THEN 8
        WHEN 'I' THEN 9  WHEN 'J' THEN 10 WHEN 'K' THEN 11 WHEN 'L' THEN 12
        WHEN 'P' THEN 13 WHEN 'Q' THEN 14 WHEN 'R' THEN 15 WHEN 'S' THEN 16
        WHEN 'T' THEN 17 WHEN 'W' THEN 18 WHEN 'X' THEN 19
        ELSE 99
     END)::INT                                                                                     as valuechangetype,
    coalesce(try_cast(p.line_item_discount_reason_code AS INT), 99)::INT                           as stdvaluechangereason,
    -- employeediscountflg: pyardm sets 0 for main branch (Branch 1).
    -- Branch 2 (Employee Item Discount) where it would be 1 is HALT (flat lacks fields).
    FALSE::BOOLEAN                                                                                 as employeediscountflg,
    null::VARCHAR                                                                                  as discountstaffid,
    null::VARCHAR                                                                                  as discountaccountno,
    null::VARCHAR                                                                                  as discountreason,
    coalesce(try_cast(p.discount_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                         as amountbase,
    null::NUMBER(38,6)                                                                             as originalamountbase,
    null::NUMBER(38,6)                                                                             as actualpricebase,
    -- cumulativediscountpercent ext (ARDM_2_ItemDiscount.sql:215-219)
    coalesce(try_cast(p.cumulative_transaction_discount_percent AS NUMBER(38,6)), 0)::NUMBER(38,6) as x_cumulativediscountpercent,
    -- x_transactiondiscountseqno: pyardm ARDM_2_ItemDiscount.sql:214 — ItemSeq::int, where
    -- ItemSeq = the parent item's ApprissSeqLocal (ARDM_2_ItemDiscount.sql:24). Same value as
    -- itemrecordseqno. Sourced from the parent item join (i.item_appriss_seq_local).
    i.item_appriss_seq_local::INT                                                                  as x_transactiondiscountseqno,
    p.file_name::VARCHAR                                                                           as filename,
    p.discount_type_code as _discount_type_code
from {{ ref('flat_postransactions_item_discount') }} p
left join parent_item i
    on i.store_number = p.store_number
   and i.register_identifier = p.register_identifier
   and i.transaction_number = p.transaction_number
   and i.transaction_sales_date = p.transaction_sales_date
   -- scope to the specific transaction doc (dual-doc tickets); pyardm joins item↔itemdiscount by apprissid
   and i.transaction_end_datetime = p.transaction_end_datetime
   and try_cast(i.line_item_sequence_number AS INT) = try_cast(p.item_line_item_sequence_number AS INT)

),

main_item_discount AS (
    -- pyardm excludes discount_type_code IN ('E','G') AFTER numbering (dup-elimination per ticket 41018),
    -- leaving gaps in recordseqno (e.g. [1, 3, 5] when rows 2 and 4 were E/G).
    select * exclude (_discount_type_code) from all_item_discounts_numbered
    where coalesce(_discount_type_code, '') not in ('E', 'G')
),

main_max_seq AS (
    -- pyardm prelim_itemdisc_seqno (ARDM_2_ItemDiscount.sql:391-396): MAX(recordseqno)
    -- of the inserted main-branch rows, per transaction. Drives the employee-branch offset.
    select transactionid, max(recordseqno) as max_main_seq
    from main_item_discount
    group by transactionid
),

employee_item_discount AS (
    -- Branch 2: Employee Item Discount (pyardm ARDM_2_ItemDiscount.sql:398-500).
    -- One staff-discount row per item with EmployeeItemDiscount.LineItemSequenceNumber.
    -- recordseqno: pyardm (ARDM_2_ItemDiscount.sql:402) = parent item's apprissseqlocal +
    -- MAX(main-branch recordseqno per TID), placing employee rows immediately after the
    -- main rows in the same numbering space. Mirrored here via main_max_seq join — matches
    -- pyardm exactly under composite-key AND content-rank (no static +30000 offset).
    -- employeediscountflg = TRUE; staffid + cardtoken from
    -- associate_transaction_associate_identifier on the parent transaction.
    select
        {{ get_transaction_id('try_cast(p.store_number AS INT)',
                              'try_cast(p.register_identifier AS INT)',
                              'try_cast(p.transaction_number AS INT)',
                              "p.transaction_end_datetime", fourth_key="p.transaction_end_time") }} as transactionid,
        (p.item_appriss_seq_local::INT + coalesce(mm.max_main_seq, 0))::INT                            as recordseqno,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as inserteddatetime,
        p.file_arrival_time::TIMESTAMP_NTZ                                                             as updateddatetime,
        p.transaction_end_datetime                                   as endtransdatetime,
        try_cast(p.store_number AS INT)                                                                as storeno,
        try_cast(p.register_identifier AS INT)                                                         as posno,
        try_cast(p.transaction_number AS INT)                                                          as ticketno,
        try_to_date(p.transaction_sales_date)                                                          as tradingday,
        null::VARCHAR                                                                                  as cashierno,
        p.transaction_end_datetime                                   as recorddatetime,
        -- articleid/upc normalized (strip leading zeros) to match reference_product.articleid — RCS-29237.
        ltrim(trim(p.upc_number), '0')::VARCHAR                                                        as articleid,
        null::VARCHAR                                                                                  as skuid,
        ltrim(trim(p.upc_number), '0')::VARCHAR                                                        as upc,
        coalesce(try_cast(p.employee_discount_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                as amount,
        coalesce(try_cast(p.employee_discount_percent AS NUMBER(38,6)), 0)::NUMBER(38,6)               as percentage,
        0::INT                                                                                         as entrymode,
        0::INT                                                                                         as stdentrymode,
        -- pyardm stores NULL (not '') for employee-discount promotionid in ARDMPROD
        null::VARCHAR                                                                                  as promotionid,
        null::VARCHAR                                                                                  as discountcode,
        FALSE::BOOLEAN                                                                                 as discountvoidedflg,
        p.item_appriss_seq_local                                                                       as itemrecordseqno,
        coalesce(try_cast(p.customer_charged_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                 as originalamount,
        coalesce(try_cast(p.net_charged_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                      as actualprice,
        -- voidreason per pyardm ARDM_2_ItemDiscount.sql:440-444 — '+'/'V' → 0, '-'/'R' → 1, else 0
        (CASE
            WHEN p.line_item_void_resolution_code IN ('+', 'V') THEN 0
            WHEN p.line_item_void_resolution_code IN ('-', 'R') THEN 1
            ELSE 0
         END)::INT                                                                                     as voidreason,
        0::INT                                                                                         as stdvoidreason,
        0::INT                                                                                         as valuechangemethod,
        0::INT                                                                                         as stdvaluechangemethod,
        0::INT                                                                                         as x_valuechangereason,
        -- valuechangetype: pyardm 19-branch CASE on employee_discount_type_code
        (CASE p.employee_discount_type_code
            WHEN 'A' THEN 1  WHEN 'B' THEN 2  WHEN 'C' THEN 3  WHEN 'D' THEN 4
            WHEN 'E' THEN 5  WHEN 'F' THEN 6  WHEN 'G' THEN 7  WHEN 'H' THEN 8
            WHEN 'I' THEN 9  WHEN 'J' THEN 10 WHEN 'K' THEN 11 WHEN 'L' THEN 12
            WHEN 'P' THEN 13 WHEN 'Q' THEN 14 WHEN 'R' THEN 15 WHEN 'S' THEN 16
            WHEN 'T' THEN 17 WHEN 'W' THEN 18 WHEN 'X' THEN 19
            ELSE 99
         END)::INT                                                                                     as valuechangetype,
        0::INT                                                                                         as stdvaluechangereason,
        TRUE::BOOLEAN                                                                                  as employeediscountflg,
        nullif(trim(t.associate_transaction_associate_identifier), '')::VARCHAR                        as discountstaffid,
        nullif(trim(t.associate_transaction_associate_identifier), '')::VARCHAR                        as discountaccountno,
        null::VARCHAR                                                                                  as discountreason,
        coalesce(try_cast(p.employee_discount_amount AS NUMBER(38,6)), 0)::NUMBER(38,6)                as amountbase,
        null::NUMBER(38,6)                                                                             as originalamountbase,
        null::NUMBER(38,6)                                                                             as actualpricebase,
        0::NUMBER(38,6)                                                                                as x_cumulativediscountpercent,
        -- x_transactiondiscountseqno: pyardm ARDM_2_ItemDiscount.sql:516 (ext_update employee
        -- branch) hardcodes 0.
        0::INT                                                                                         as x_transactiondiscountseqno,
        p.file_name::VARCHAR                                                                           as filename
    from {{ ref('flat_postransactions_item') }} p
    left join parent_transaction t
        on t.store_number = p.store_number
       and t.register_identifier = p.register_identifier
       and t.transaction_number = p.transaction_number
       and t.transaction_sales_date = p.transaction_sales_date
       -- scope to the specific transaction doc (dual-doc tickets) to avoid fan-out
       and t.transaction_end_datetime = p.transaction_end_datetime
    left join main_max_seq mm
        on mm.transactionid = {{ get_transaction_id('try_cast(p.store_number AS INT)',
                                                     'try_cast(p.register_identifier AS INT)',
                                                     'try_cast(p.transaction_number AS INT)',
                                                     "p.transaction_end_datetime", fourth_key="p.transaction_end_time") }}
    where p.employee_discount_line_item_seq is not null
      and coalesce(p.employee_discount_type_code, '') not in ('E', 'G')
),

header_cashierno AS (
    SELECT transactionid, cashierno FROM {{ ref('map_ardm_header') }}
)

select
    d.* exclude (cashierno),
    coalesce(hc.cashierno, '0')::VARCHAR as cashierno
from (
    select * from main_item_discount
    union all select * from employee_item_discount
) d
left join header_cashierno hc on hc.transactionid = d.transactionid

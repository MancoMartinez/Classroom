---
ticket: RCS-28052
cliente: TJX Europe / c181_tje (EU)
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS
sintoma: las ordenes eComm de la tienda 425 salen con SKU vacio y Tender Type Unknown
causa: dos bugs de pipeline, LATERAL FLATTEN sin envoltura TYPEOF pierde el item cuando la orden trae una sola linea, y el CASE de tender no contempla el valor mc, mas un tercer tema de duplicados en Secure por join a ardm_Customer sin RecordSeqNo=1
fix: envolver el FLATTEN con TYPEOF, agregar MC al CASE, filtrar RecordSeqNo=1 en Secure, y backfill desde 2026-06-30
nota_reutilizable: Snowflake guarda un hijo XML unico como OBJECT, FLATTEN sobre OBJECT expande pares clave valor y el filtro nunca hace match
confluence_id: 478142300172
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478142300172
---

# RCS-28052 — TJXEU: Item Level Details Missing from eComm (Store 425) Orders

Prepared: 03 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28052 |
| Customer | TJX Europe (c181_tje) |
| Issue Type | Incident |
| Priority | Medium |
| Status | WORK IN PROGRESS |
| Opened | 30 July 2026 |
| Reporter | Lucy Wood (lucy_wood@tjxeurope.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |

## 2. Problem Statement

eComm orders from store 425 (E COMMERCE, UK banner) show empty SKU ID and Tender Type "Unknown" in Secure. Approximately 3,000–3,500 unique orders per day affected since at least 30 June 2026. Two SnowTime pipeline bugs confirmed plus one Secure application issue.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c181_tje |
| ARDM Version | V2 |
| Snowflake Schema | ARDM_PRODUCTION.C181_TJE |
| Region | EU |
| Active Pipeline | SnowTime dbt (raw_sales XML feed — Apriss_Sales_*.pgp) |
| eComm Store | Store 425 (UK banner), Store 886 (non-UK banner) |

## 4. Investigation

### 4.1 Locate order in ARDM_HEADER

PASS. eComm orders use `ticketno = 0` (hardcoded); the actual order number is stored in `orderno`. Order 45103713 resolves to transactionid 2607235515699971671, storeno 425, posno 0.

### 4.2 Check ARDM_ITEM for the order

POINT OF FAILURE FOUND. 0 rows returned. Raw XML for order 45103713 confirmed exactly 1 `<Line>` child with `TJXStyleNumber = 25258472` — item detail is entirely absent in ARDM.

### 4.3 TYPEOF distribution for OrderLines (scale of impact)

POINT OF FAILURE FOUND. Single-child `<Line>` stored as OBJECT (TYPEOF=`XML`) — 9,776 orders (~40% of eComm) produce 0 ARDM_ITEM rows. `LATERAL FLATTEN` on an OBJECT expands key-value pairs, not children; `WHERE GET(line.value, '@') = 'Line'` never matches.

| orderlines_type | order_count |
| --- | --- |
| ARRAY | 14,813 |
| XML | 9,776 |

### 4.4 Check ARDM_TENDER for the order

POINT OF FAILURE FOUND. Raw XML shows `<CardType>mc</CardType>`. `upper('mc') = 'MC'` is not matched by `IN ('MASTER', 'MASTERCARD')`, so it falls to `else 99` (Unknown).

### 4.5 MasterCard feed volume (7-day)

PASS (quantification). 19,324 MasterCard orders per 7 days showing tendertype=99. Distribution: visa 26,692, PayPal 22,046, mc 19,324, amex 3,367, empty 1,088.

### 4.6 ARDM_CUSTOMER duplicate rows

PASS (by-design finding). 2 rows per eComm order is intentional (Ecom Billing seqno=1, Ecom Delivery seqno=2, mirrors pyardm). Secure's Order Number Search joins `ardm_Customer` without a `RecordSeqNo = 1` filter, producing 2 result rows in the UI.

## 5. Root Cause Statement

### Root Cause 1 — Single-item eComm orders produce 0 ARDM_ITEM rows

| Field | Detail |
| --- | --- |
| What broke | `flat_sales_order_line.sql:22` LATERAL FLATTEN on `<OrderLines>` |
| Why | Missing TYPEOF safety wrapper — Snowflake stores a single-child XML element as OBJECT; FLATTEN expands key-value pairs, not children; the WHERE filter never matches |
| Also affected | `flat_sales_returnorder_line.sql` — same code pattern |
| Scope | All eComm orders with exactly 1 line item; ~40% of volume (9,776 / 24,589 orders in a 3-day sample) |
| First affected | 30 June 2026 |
| Business impact | SKU ID empty in Secure for all single-item orders |

### Root Cause 2 — MasterCard shows Tender Type "Unknown"

| Field | Detail |
| --- | --- |
| What broke | `map_ardm_tender.sql` — MasterCard CASE in `ecom_order_tender` (~line 173) and `ecom_return_tender` (~line 312) |
| Why | Feed delivers `card_type = 'mc'`; CASE checks `IN ('MASTER', 'MASTERCARD')` only |
| Scope | All eComm MasterCard transactions; 19,324 orders per 7 days |
| Business impact | Tender Type displayed as "Unknown" for ~27% of eComm payment volume |

## 6. Additional Finding — Duplicate Rows in Order Number Search (Secure Application)

Secure's Order Number Search query joins `ardm_Customer` without a `RecordSeqNo = 1` filter. Fix is in Secure application SQL, not SnowTime.

## 7. Recommended Fix

### Fix 1 — flat_sales_order_line.sql:22 (and flat_sales_returnorder_line.sql)

```
lateral flatten(
    input => CASE
        WHEN TYPEOF(GET(XMLGET(p.ord, 'OrderLines'), '$')) = 'ARRAY'
        THEN GET(XMLGET(p.ord, 'OrderLines'), '$')
        ELSE ARRAY_CONSTRUCT(GET(XMLGET(p.ord, 'OrderLines'), '$'))
    END
) line
```

### Fix 2 — map_ardm_tender.sql (two locations)

```
when upper(o.card_type) in ('MASTER', 'MASTERCARD', 'MC') then 50
```

### Fix 3 — Secure Order Number Search (separate engineering track)

Add `AND T3.RecordSeqNo = 1` to the `ardm_Customer` LEFT JOIN.

Post-deploy: run `/backfill-ardm c181_tje --range 2026-06-30:<today>` to recover 31+ days of history.

## 8. Open Questions

1. Does `flat_sales_returnorder_line.sql` have the same single-child TYPEOF bug? (Assumed yes — confirm before deploy.)
2. Are there other eComm card type values not covered by the current CASE?
3. Which team owns the Secure `ardm_Customer` JOIN change?

## 9. Queries Run

| # | Description | Actual Result |
| --- | --- | --- |
| 1 | ARDM_HEADER WHERE orderno='45103713' | 1 row, storeno=425, posno=0, ticketno=0 |
| 2 | ARDM_ITEM WHERE transactionid=2607235515699971671 | 0 rows (bug confirmed) |
| 3 | TYPEOF of OrderLines grouped, 3 days | ARRAY=14,813 · XML=9,776 |
| 4 | card_type frequency from flat_sales_order, 7 days | visa 26,692 · PayPal 22,046 · mc 19,324 · amex 3,367 |
| 5 | ARDM_TENDER for the transaction | tendertype=99, amount 37.99 |
| 6 | ARDM_CUSTOMER for the transaction | 2 rows (Billing, Delivery) — by design |
| 7 | Raw XML for order 45103713 | 1 Line, CardType mc |

## 10. Attachments

Secure search showing 31 days of eComm orders with empty SKU, and the Order Number Search result with duplicate rows and Tender Type Unknown. [See Jira attachment]

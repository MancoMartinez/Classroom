---
ticket: RCS-28510
cliente: Wild Fork Foods / c354wff (legacy ardm_354)
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS
sintoma: los recibos de refund no muestran el bloque de la transaccion original
causa: la funcion GET_TRANSACTION_JSON del cliente 354 nunca construye la clave origorderinfo, se perdio en la migracion GP a Snowflake
fix: agregar el bloque siguiendo el patron del cliente 355, con la llave de join correcta
version: 1 (la ficha del 28 de agosto, con el fix ya aplicado, es RCS-28510-wild-fork-origorderinfo-v2.md)
relacionados: ENG-7594, ENG-3384, PR 51318
confluence_id: 478141775879
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478141775879
---

# RCS-28510 — Wild Fork Foods: Refund Transaction Receipts Not Showing Original Transaction

Prepared: 21 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28510 |
| Customer | Wild Fork Foods |
| Issue Type | Incident |
| Priority | High |
| Status | Work in Progress |
| Opened | 20 August 2026 |
| Reporter | Sean Parello (sean.parello@wildforkfoods.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28510 |

## 2. Problem Statement

Refund receipts no longer display the original-transaction information block at the bottom of the receipt. Example receipt: Store 9034, POS 2, Trans# 9034-02-AB06492, Event ID 2802323721399, RETURN, 4 items returned, total $-80.78.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c354wff (Wild Fork Foods) |
| Legacy system | Greenplum, schema ardm_354 — NOT migrated to SnowTime |
| ARDM version | Legacy pyardm (pre-SnowTime) |
| Snowflake | ARDM data replicated into ARDMPROD; receipt JSON served via a per-client Snowflake function |
| Active product | Receipt viewer (Secure) consuming GET_TRANSACTION_JSON |

## 4. Investigation

### 4.1 Identify transactionid from receipt

PASS. transactionid = 2608113429229397644, matches the receipt exactly.

### 4.2 Validate linked-order data

PASS. link_type = 'return', original_order_id = '2608116581900433013' — a real value, not 'UNKNOWN'.

### 4.3 Validate original transaction exists

PASS. Original transaction found: order_number 9034-03-AA27212, store 9034, POS 3, total $93.00, same trading day. Full data chain correct end-to-end in Greenplum.

### 4.4 Code review — Secure receipt JSON function

POINT OF FAILURE FOUND. The receipt viewer calls GET_TRANSACTION_JSON(TXN_ID), which assembles the entire receipt payload server-side. Client 354's function builds "linkedorder" but never builds "origorderinfo". Client 355's function contains this exact block (lines 51-62). Not carried over for client 354 during the GP-to-Snowflake migration (PR 51318, ENG-3384, May 2026).

### 4.5 Cross-client scope survey

ADDITIONAL FINDING. Per-client code gap, not isolated to Wild Fork.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | GET_TRANSACTION_JSON for client 354 never constructs the "origorderinfo" JSON key |
| Why | Each client has its own hand-authored copy of this function. During the migration, the original-transaction resolution logic — present (flag-disabled) in the legacy Greenplum function and fully ported for sibling clients — was not carried over for client 354 |
| Scope | Every refund/return receipt for client 354 since ~May 2026; same defect in 9 other clients |
| Business impact | Informational/cosmetic gap only — no data integrity issue |
| Evidence | The return resolves to a valid original_order_id and the original header exists with correct data; client 355's function contains the missing block, 354's does not |

## 6. Additional Findings

| Group | Client IDs |
| --- | --- |
| Full origorderinfo support | 113, 133, 135, 218, 248, 355, 356, 438, 439, 442 |
| linkedorder present, origorderinfo missing (same defect) | 123, 143, 352, 353, 354, 440, 46, 500, 505, 506 |
| No linkedorder key at all | 89 remaining clients (not a defect) |

## 7. Recommended Fix

### Option A — Patch client 354's Snowflake function (Recommended)

Add an "origorderinfo" block following the pattern used by client 355, with one adjustment: for client 354, ARDM_LINKEDORDER.ORIGINAL_ORDER_ID holds the original transaction's TRANSACTIONID, not ORDER_NUMBER — the join key must be different.

```
(SELECT ARRAY_AGG(OBJECT_CONSTRUCT_KEEP_NULL(
            'order_number',    oh.ORDER_NUMBER,
            'transactionid',   oh.TRANSACTIONID,
            'origstoreno',     oh.STORENO,
            'origposno',       oh.POSNO,
            'origcashierno',   oh.CASHIERNO,
            'origticketno',    oh.TICKETNO,
            'origtradingday',  oh.TRADINGDAY,
            'origtotalamount', oh.TOTAL_AMOUNT::VARCHAR))
   FROM (SELECT DISTINCT ORIGINAL_ORDER_ID FROM $(SnowflakeArdmSchemaName).ARDM_LINKEDORDER WHERE TRANSACTIONID = TXN_ID AND TRADINGDAY = TO_DATE(LEFT(TXN_ID::VARCHAR, 6), 'YYMMDD')) lo
   JOIN $(SnowflakeArdmSchemaName).ARDM_HEADER oh ON oh.TRANSACTIONID = TRY_TO_NUMBER(lo.ORIGINAL_ORDER_ID)
   HAVING COUNT(*) > 0) AS "origorderinfo"
```

Steps: add the block, deploy the function, validate against the sample transaction, confirm the receipt viewer renders it, and raise a follow-up for the other 9 clients.

## 8. Open Questions

* Fix not yet implemented at the time of this version — pending operator go-ahead.
* Should the 9 other affected clients be fixed in the same PR, or a separate systemic ENG ticket? (Recommendation: separate ticket.)

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | ardm_354.ardm_header WHERE order_number='9034-02-AB06492' | transactionid 2608113429229397644 |
| 2 | ardm_354.ardm_linkedorder WHERE order_id=... | original_order_id valid |
| 3 | ardm_354.ardm_header WHERE transactionid=2608116581900433013 | Found, $93.00 |
| 4 | Code comparison 354 vs 355 | 354 missing "origorderinfo" block |

## 10. Extras / Additional Screenshots

Receipt image (Store 9034, RETURN). [See Jira attachment / link in ticket]

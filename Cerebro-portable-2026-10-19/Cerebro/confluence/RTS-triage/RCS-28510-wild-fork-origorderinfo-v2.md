---
ticket: RCS-28510
cliente: Wild Fork Foods / c354wff (legacy ardm_354)
analista: Diego Buelvas
estado_ficha: Resolved
sintoma: los recibos de refund no muestran el bloque de la transaccion original
causa: la funcion GET_TRANSACTION_JSON del cliente 354 nunca construyo la clave origorderinfo, se perdio en la migracion GP a Snowflake
fix: agregar el bloque origorderinfo siguiendo el patron del cliente 355, con la llave de join correcta
alcance_sistemico: mismo hueco en 9 clientes mas, 123 143 352 353 440 46 500 505 506
relacionados: ENG-7594, ENG-3384, PR 51318
version: 2 (hay otra ficha del mismo ticket del 21 de agosto)
confluence_id: 478155472897
modificado: 2026-08-28
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478155472897
---

# RCS-28510 — Wild Fork Foods: Refund Transaction Receipts Not Showing Original Transaction

Prepared: 28 August 2026 | Analyst: Diego Buelvas | Status: Resolved

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28510 |
| Customer | Wild Fork Foods |
| Issue Type | Incident |
| Priority | High |
| Status | Completed (Resolved) |
| Opened | 20 August 2026 |
| Reporter | Sean Parello (sean.parello@wildforkfoods.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28510 |
| Related Engineering ticket | ENG-7594 |

## 2. Problem Statement

Refund receipts were not showing the original-transaction information block at the bottom of the receipt (store/POS/cashier/ticket/trading day/total of the sale being returned). Example receipt: Store 9034, POS 2, Trans# 9034-02-AB06492, RETURN, total $-80.78. The underlying transaction data was confirmed correct in the database — the issue was isolated to what the receipt-rendering function returned to the front end.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c354wff (Wild Fork Foods) |
| Legacy system | Greenplum, schema `ardm_354` — NOT migrated to SnowTime |
| ARDM version | Legacy pyardm (pre-SnowTime) |
| Snowflake | ARDM data also replicated into Snowflake (ARDMPROD); receipt JSON served via a per-client Snowflake function |
| Active product | Receipt viewer (Secure) consuming `GET_TRANSACTION_JSON` |

## 4. Investigation

### 4.1 Identify transactionid from receipt

PASS. Found `transactionid = 2608113429229397644`, matches receipt exactly (store 9034, POS 2, cashier LBLACKMA, total $-80.78).

### 4.2 Validate linked-order data

PASS. Row exists, `link_type = 'return'`, `original_order_id = '2608116581900433013'` — a real value, not `'UNKNOWN'`.

### 4.3 Validate original transaction exists

PASS. Original transaction found: order_number `9034-03-AA27212`, store 9034, POS 3, cashier LBLACKMA, total $93.00, same trading day. Full data chain correct end-to-end in Greenplum.

### 4.4 Code review — Secure receipt JSON function

POINT OF FAILURE FOUND. The receipt viewer does not query the database live at render time — it calls a single per-client Snowflake function, `GET_TRANSACTION_JSON(TXN_ID)`, which assembles the entire receipt payload server-side as one JSON/VARIANT. The front end only renders keys present in that JSON. Client 354's function builds `"linkedorder"` (raw link rows) but never builds `"origorderinfo"` (the resolved original-transaction object). Client 355's function contains this exact block. The block was not carried over for client 354 during the GP-to-Snowflake migration (PR 51318, ENG-3384, May 2026).

### 4.5 Cross-client scope survey

FINDING. Confirmed this is a per-client code gap, not isolated to Wild Fork — see Additional Findings.

### 4.6 Pre-change validation (read-only, ARDMPROD)

PASS. Confirmed (1) the join resolves to the correct original transaction, (2) the `origorderinfo` block in isolation produces the expected JSON, (3) a normal transaction without a linked order correctly returns NULL for the block (no regression, via `HAVING COUNT(*) > 0`).

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | The Snowflake function `GET_TRANSACTION_JSON` for client 354 never constructed the `"origorderinfo"` JSON key |
| Why | Each client has its own hand-authored copy of this function (no shared/framework code). During the GP-to-Snowflake migration (PR 51318, ENG-3384, May 2026), the original-transaction resolution logic — fully ported for sibling clients — was not carried over for client 354 |
| Scope | Every refund/return receipt for client 354 since the migration (~May 2026); same defect pattern confirmed in 9 other clients |
| Business impact | Informational/cosmetic gap only — no data integrity issue |
| Evidence | The return transaction resolves to a valid original_order_id, and the original header exists with correct data. Sibling client 355's function contains the missing block; client 354's did not |

## 6. Additional Findings

Cross-client survey (repo Secure, 109 `ClientSpecific/*/GetTransactionJson.sql` files):

| Group | Client IDs | Meaning |
| --- | --- | --- |
| Full `origorderinfo` support | 113, 133, 135, 218, 248, 355, 356, 438, 439, 442 | Migration ported the logic correctly |
| `linkedorder` present, `origorderinfo` missing (same defect) | 123, 143, 352, 353, 354 (Wild Fork), 440, 46, 500, 505, 506 | Same code gap as this ticket |
| No `linkedorder` key at all | 89 remaining clients | Feature not applicable — not a defect |

A CodeAnt AI code-review comment flagged a potential type mismatch, suggesting `oh.TRANSACTIONID` be cast to string in the new block. This was investigated and refuted: client 355, already live, emits `transactionid` as a native JSON number with the same pattern, and the pre-migration Greenplum function for 354 did too. No client-side type-matching logic exists anywhere in repo Secure. The cast suggestion was not applied.

## 7. Recommended Fix

### Option A — Patch client 354's Snowflake function (Applied)

Added an `"origorderinfo"` block to `ClientSpecific/354/ArdmDependent/Common/Functions/secure/GetTransactionJson.sql` (repo Secure), following the pattern used by client 355, with one required adjustment: for client 354, `ARDM_LINKEDORDER.ORIGINAL_ORDER_ID` holds the original transaction's TRANSACTIONID, not ORDER_NUMBER as in client 355 — the join key is different.

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

Steps taken: added the block, validated read-only against ARDMPROD.ARDM_354 before rollout, committed and deployed, customer confirmed the block now displays.

Follow-up: the same gap exists in 9 other clients (123, 143, 352, 353, 440, 46, 500, 505, 506) — recommended as a separate systemic ENG ticket. If a similar complaint is raised for any of those clients, this is the same root cause and does not need re-investigation.

## 8. Open Questions

No open questions — ticket resolved. Internal follow-up: branch naming convention pending rename; broader QA validation in staging pending since dev/lab environments don't hold real Wild Fork data; the 9-other-client rollout is not yet scheduled.

## 9. Queries Run

| # | Query | Purpose | Result |
| --- | --- | --- | --- |
| 1 | ardm_354.ardm_header WHERE order_number='9034-02-AB06492' | Identify transactionid from receipt | 2608113429229397644 |
| 2 | ardm_354.ardm_linkedorder WHERE order_id=... | Validate link to original transaction | original_order_id valid |
| 3 | ardm_354.ardm_header WHERE transactionid=2608116581900433013 | Validate original transaction exists | Found, $93.00 |
| 4 | Code comparison 354 vs 355 GetTransactionJson.sql | Identify root cause | 354 missing origorderinfo block |
| 5 | Repo-wide sweep of 109 files | Scope the gap | 10 clients affected |
| 6 | Read-only SELECT against ARDMPROD.ARDM_354 | Pre-change validation | Correct, no regression |

## 10. Extras / Additional Screenshots

Receipt image (Store 9034, Trans# 9034-02-AB06492, RETURN). [See Jira attachment / link in ticket]

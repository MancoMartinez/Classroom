---
ticket: RCS-28471
cliente: Kroger / client 026 (legacy ARDMPROD.ARDM_026)
analista: Diego Buelvas
estado_ficha: UNDER CUSTOMER REVIEW
sintoma: la busqueda Sale Followed by Return trae Tender Exchange en vez de Returns
causa: el ETL que llena NEXTTRANSTYPE y PREVIOUSTRANSTYPE escribe KROGERTRANSACTIONTYPE, el codigo nativo del POS, en vez del codigo estandar, y los codigos colisionan
fix: corregir el job para que lea TRANSACTIONTYPE/STDTRANSACTIONTYPE y reprocesar desde 2026-04-19
onset: regresion iniciada entre el 2026-04-18 y el 2026-04-19
colisiones_extra: Kroger 6 (Inquiry) se muestra como Post Void, Kroger 8 (Control) como Cash Management
confluence_id: 478143283201
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143283201
---

# RCS-28471 — Kroger: Possible Mapping Error

Prepared: 25 August 2026 | Analyst: Diego Buelvas | Status: UNDER CUSTOMER REVIEW

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28471 |
| Customer | Kroger |
| Issue Type | Incident |
| Priority | Medium |
| Status | Under Customer Review |
| Opened | 19 August 2026 |
| Reporter | Benjamin Axe (ben.axe@kroger.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28471 |

## 2. Problem Statement

When attempting to create the search "Sale Followed by Return - Cashier", results include "Tender Exchange" transactions instead of "Returns". The search is meant to surface transactions where an item is purchased and then immediately returned in the next transaction.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | 026 (Kroger) |
| Snowflake schema | `ARDMPROD.ARDM_026` |
| Pipeline | Legacy (pre-SnowTime) — no dbt project exists for client 026; has client-specific extension columns (KrogerTransactionType, KrogerStoreNo, KrogerDivisionNo, KrogerTransactionId) |
| Active product | Secure Store (EBR Search / Composer) |

## 4. Investigation

### 4.1 Reproduce reported symptom in header data

POINT OF FAILURE FOUND. Transaction 74 (Sale) had NEXTTRANSTYPE = 2. The real next transaction (75) is TRANSACTIONTYPE=26 / STDTRANSACTIONTYPE=5 (Tender Exchange), but its KROGERTRANSACTIONTYPE = 2. NEXTTRANSTYPE matched KROGERTRANSACTIONTYPE, not the standard type of the next row.

### 4.2 Confirm meaning of code "2" in the standard domain

PASS. STDTRANSACTIONTYPE = 2 is globally "Return" (23 rows that day, negative average amount). Confirms code 2 unambiguously means Return, system-wide.

### 4.3 Rule out a Secure/Composer decoding bug

PASS. The generated SQL joins secure_EnumerationReferenceData identically for TransactionType, NextTransType, and PreviousTransType. No KrogerTransactionType reference exists anywhere in the Secure repository. The defect is upstream.

### 4.4 Confirm pattern is systemic, not a single row

POINT OF FAILURE FOUND. LEAD() window comparison confirmed at client-wide scale — store 11339 (184 rows on 2026-08-17 and again on 2026-08-10) and store 11344 (245 rows) — not isolated to one cashier, store, or day.

### 4.5 Determine onset date (regression window)

POINT OF FAILURE FOUND. Near-zero occurrences through 2026-04-17; jumps to 170+/day from 2026-04-19 onward. Onset isolated to 2026-04-18/19 — consistent with a code regression from a deploy in that window.

### 4.6 Check for additional code collisions

POINT OF FAILURE FOUND. Two additional collisions: KrogerTransactionType=6 (real type: Inquiry) displays as "Post Void"; KrogerTransactionType=8 (real type: Control) displays as "Cash Management".

### 4.7 Confirm scope of impact

FAIL (broader impact than reported). Affects all users of the application, not just the one search reported — independently reproducible in at least two saved searches from two different users.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | ARDM_HEADER.NEXTTRANSTYPE and PREVIOUSTRANSTYPE for Kroger (client 026) |
| Why | The upstream ETL/batch job populating these two derived fields writes the value of KROGERTRANSACTIONTYPE (Kroger's native raw POS transaction-type code) into them instead of TRANSACTIONTYPE/STDTRANSACTIONTYPE. Any consumer decoding these fields against the standard dictionary renders the wrong label whenever the native code numerically collides with a different standard code. |
| Scope | Client-wide (client 026). Confirmed in 2 stores, multiple trading days, 184-245 affected header rows per store per day. Regression began 2026-04-18/19. |
| Business impact | Any search, report, or workflow referencing Next/Previous Trans Type returns mislabeled transaction data for Kroger. |
| Evidence | Ticket 74 shows NEXTTRANSTYPE=2 ("Return") while the real next transaction is StdType=5 (Tender Exchange) with KrogerType=2. No KrogerTransactionType reference in the Secure or SnowTime repositories — the defect lives in an external legacy ETL pipeline. |

## 6. Additional Findings

Two further code collisions identified, same root cause: KrogerTransactionType=6 (real: Inquiry) displays as "Post Void"; KrogerTransactionType=8 (real: Control) displays as "Cash Management". Engineering should fix all in the same pass.

## 7. Recommended Fix

### Option A — Correct ETL source column (Recommended)

Escalate to Engineering (not Delivery — this is a code/transformation defect). The job populating ARDM_HEADER.NEXTTRANSTYPE/PREVIOUSTRANSTYPE for client 026 must source from TRANSACTIONTYPE/STDTRANSACTIONTYPE instead of KROGERTRANSACTIONTYPE. Correlate against deploy history around 2026-04-18/19. After the fix, backfill/reprocess affected historical rows (2026-04-19 onward).

## 8. Open Questions

* Which deploy around 2026-04-18/19 introduced this regression?
* Does the same pattern affect any other client with a similar client-specific raw-code column?
* Full historical backfill scope/plan — pending Engineering fix.

## 9. Queries Run

Q1 detail pull of ARDM_HEADER for store 11339 on 2026-08-17 (confirms the mismatch on tickets 74/75). Q2 GROUP BY of the three type columns (confirms code 2 = Return by negative-amount profile). Q3 code search for KrogerTransactionType in the Secure repo (0 matches) plus review of the Composer SQL. Q4-Q6 LEAD() window checks across stores 11339 and 11344 and two trading days (184, 245, 184 affected rows). Q7-Q10 historical spot-checks narrowing onset to 2026-04-18/19. Q11 distinct type combinations cross-referenced against seed_std_transaction_type.csv, revealing the two extra collisions.

Canonical dictionary used: 1=Sale, 2=Return, 3=Order, 4=No Sale, 5=Control, 6=Post Void, 7=Inquiry, 8=Cash Management, 9=Account Payment, 10=Exchange, 11=Cancel, 12=Inventory, 13=Pre-Fulfillment, 14=Appeasement, 99=Unknown.

## 10. Extras / Additional Screenshots

Results table, journal/receipt viewer for transactions 74/75, and the Composer definition of the search. [See Jira attachment / link in ticket]

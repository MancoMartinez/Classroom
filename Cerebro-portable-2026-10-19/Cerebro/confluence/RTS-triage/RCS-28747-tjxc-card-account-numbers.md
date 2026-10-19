---
ticket: RCS-28747
cliente: TJX Canada (TJXC) / c070_tjc
analista: Diego Buelvas
estado_ficha: Under Customer Review
sintoma: el numero de tarjeta muestra letras donde el cliente espera digitos o asteriscos
causa: el POS Xstore envia MaskedCardNumber siempre como ############ y el pipeline cae a AuthorizationToken, un token opaco del procesador
fix: ninguno, comportamiento esperado del feed, se explica al cliente
relacionados: RCS-25655
confluence_id: 478178377729
modificado: 2026-09-04
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478178377729
---

# RCS-28747 — TJX Canada (TJXC): Incorrect Display of Debit/Credit Card Account Numbers

Prepared: 04 September 2026 | Analyst: Diego Buelvas | Status: Under Customer Review

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28747 |
| Customer | TJX Canada (TJXC) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Under Customer Review |
| Opened | 03 September 2026 |
| Reporter | Cindy Coreas (cindy_coreas@tjxcanada.ca) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28747 |

## 2. Problem Statement

Customer identified transactions where the debit/credit card account number displays letters in a segment where they expected either digits or masking asterisks. Two example receipts were provided showing inconsistent formatting of the "Card #" field on the same tender type (MasterCard/Visa, NFC entry).

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c070_tjc |
| Region | US (Snowflake account) |
| ARDM Version | V2 (snowtimeV2) |
| Snowflake Schemas | ARDM_PRODUCTION.C070_TJC (output) / ARDM_PRODUCTION.C070_TJC_SNOWTIME (working) |
| Feed | raw_pos — Xstore/DTV IXRetail POSLog (TJX Canada primary transaction feed) |

## 4. Investigation

### 4.1 Confirm masked-card field content in production

Query: pulled ARDM_TENDER for the store/pos/ticket of the "letters" example receipt (Store 40763, POS 2, Ticket 545).

POINT OF FAILURE FOUND. cardnumbermasked = "############" — a sentinel/redacted placeholder, not real asterisk masking.

### 4.2 Identify what the UI is actually displaying

POINT OF FAILURE FOUND. accountnumber = "559538JBIMQM2708" — matches exactly what the client saw as "Card #". Confirms the displayed field is accountnumber, not cardnumbermasked.

### 4.3 Cross-check the "correctly masked" example

PASS (confirms mechanism). For Store 40078 / POS 3 / Ticket 6254, accountnumber = "547183******9757" — same source field, different token shape from the payment processor. Proves both examples come from the identical code path, just different upstream data.

### 4.4 Confirm this is feed-wide behavior, not an isolated glitch

PASS. Every current FLAT_POS_LINEITEM row has tender_creditdebit_maskedcardnumber = "############" and authorizationtoken in the <6digits><6alphanumeric><4digits> shape — confirms this is the feed's normal behavior.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Nothing broke — no defect in the pipeline or in Secure's display logic. |
| Why | TJX Canada's Xstore POS always sends tjx:MaskedCardNumber as the literal redacted sentinel "############" (documented feed behavior, mirrored from legacy pyardm: ARDM_20_Tender.sql:87-89 NULLIFs the same sentinel). Both the legacy and current pipeline then fall back to tjx:AuthorizationToken — an opaque payment-processor token, not a real card number — to populate the "Card #" field. The processor's token format varies transaction to transaction. |
| Scope | Feed-wide (all c070_tjc POS transactions using card tender) — not limited to the two reported examples. |
| Business impact | Cosmetic/informational only — no PII exposure risk, since the value was never a real PAN; it is an opaque processor token. |
| Evidence | ARDM_TENDER.accountnumber matches the client's displayed values exactly for both examples; FLAT_POS_LINEITEM confirms maskedcardnumber is always "############" feed-wide. |

## 7. Recommended Fix

### Option A — No code fix; client communication (Recommended)

This is expected behavior of the TJX Canada Xstore feed, identical in root cause to a prior ticket (RCS-25655, Canadian Tire) where the same passthrough/fallback pattern was confirmed as raw-data behavior, not a bug. Response sent to client explaining the AuthorizationToken fallback and that the token format is controlled by TJX's payment processor, outside our pipeline. Offered to close unless the client wants to escalate with their payment processor.

## 8. Open Questions

Awaiting client confirmation/response (ticket currently "Under Customer Review"). No open technical questions — root cause fully confirmed.

## 9. Queries Run

| # | Query | Environment | Result |
| --- | --- | --- | --- |
| 1 | ARDM_HEADER + ARDM_TENDER for store 40763 / pos 2 / ticket 545 | ARDM_PRODUCTION.C070_TJC | cardnumbermasked = "############" |
| 2 | accountnumber for transactionid 2026090240763020545 | ARDM_PRODUCTION.C070_TJC | "559538JBIMQM2708" (matches client screenshot) |
| 3 | Same lookup for store 40078 / pos 3 / ticket 6254 | ARDM_PRODUCTION.C070_TJC | "547183******9757" (matches well-masked screenshot) |
| 4 | FLAT_POS_LINEITEM sample where authorizationtoken IS NOT NULL | C070_TJC_SNOWTIME | Every row: maskedcardnumber = "############" |

## 10. Extras / Additional Screenshots

Two receipt screenshots (well-masked and letters examples). [See Jira attachment / link in ticket]

---
ticket: RCS-28170
cliente: TJX / client 079
analista: Diego Buelvas
estado_ficha: RESOLVED
sintoma: no se poblaron Work Items el 5 de agosto
causa: las llaves de API de ingestion de TJX expiraron, HTTP 400, el feed paro y el volumen del dia quedo en 200,408 contra un minimo GNG de 1,700,000, se saltaron las 23 definiciones
fix: extender las llaves y reemplazarlas antes del vencimiento, mas correccion de una configuracion de busqueda del lado del cliente
nota_reutilizable: el chequeo GNG salta la generacion de Work Items cuando el conteo de transacciones del dia esta por debajo del minimo configurado
relacionados: RTS-205289
confluence_id: 478143479821
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143479821
---

# RCS-28170 — TJX: No Work Items Populated - 8/5/26

Prepared: 12 August 2026 | Analyst: Diego Buelvas | Status: RESOLVED

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28170 |
| Customer | TJX |
| Issue Type | Incident |
| Priority | Not Available |
| Status | Closed |
| Opened | 05 August 2026 |
| Reporter | Chris Moore (TJX) / Christine Harkness / Jason Bridge |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28170 |

## 2. Problem Statement

On the morning of 2026-08-05, TJX reported that no new Work Items had populated, even though spot-checking the underlying searches showed results were available. The customer asked Support to check whether the Work Item job had failed and, if so, to rerun it.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | TJX (client 079) |
| ARDM Version | Not Available |
| Application | EBR Instant Analytics / Work Items (WISC) |
| Active Products | Work Items — POSlog + TJX US Corporate Investigations definitions |

## 4. Investigation

### 4.1 GNG (Go/No-Go) threshold check

POINT OF FAILURE FOUND. All 23 WI definitions were skipped with the message: "The transaction count is below the expected minimum (1,700,000) for the following trading day(s): 04/08/2026 (200,408)."

### 4.2 Feed status investigation

FAIL — feed inactive. The postransactions trickle feed had stopped receiving new data; the last file was received on 2026-08-04 at 22:04 UTC. This explained the abnormally low transaction volume (200,408 vs. a typical 2.5M–3.6M/day).

### 4.3 Root cause of feed stoppage

POINT OF FAILURE FOUND. No changes were made on the Appriss side. TJX's ingestion API keys had expired, causing HTTP 400 authentication failures on every ingestion call.

### 4.4 Remediation and data catch-up

PASS. Engineering extended the API key expiration to 2026-09-02. TJX resumed sending files at 19:32 UTC on 2026-08-05. Trading day 2026-08-05 reached 2,691,137–2,428,043 transactions, and all Work Items completed successfully.

### 4.5 Client-reported residual "no Work Items" symptom

After the fix, the client continued to report that no Work Items were visible. The WI was re-run via the WISC Control Panel with a video recording confirming it ran successfully with results. Client-side cache was suspected; the ticket went quiet for several days.

### 4.6 Final closure

PASS — confirmed resolved on 2026-08-12. The residual symptom is attributed to a client-side search configuration issue, which was corrected. Resolution code: "Support Resolved - Fixed Configuration."

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | 23 Work Item definitions were skipped by the GNG check for trading day 2026-08-04; separately, the client continued to report Work Items as missing after the feed was restored |
| Why | TJX's ingestion API keys expired, causing HTTP 400 authentication failures that stopped the postransactions feed, so trading day 08-04 volume fell to 200,408 (below the 1,700,000 GNG minimum) and all dependent WI definitions were skipped. The residual report after the fix was caused by a client-side search configuration issue. |
| Scope | Trading days 2026-08-04 through 2026-08-06; 23 WI definitions initially affected |
| Business impact | High / customer-facing — client escalated directly |
| Evidence | 200,408 transactions vs. 1,700,000 minimum on 08-04; feed last received 2026-08-04 22:04 UTC; keys extended to 2026-09-02 |

## 6. Additional Findings

After the feed outage was resolved and WI re-ran successfully, the client continued to report empty Work Items for several more days. Traced to a client-side search configuration problem, separate from the ingestion/GNG root cause, fixed on 2026-08-12.

## 7. Recommended Fix

### Option A — API key extension and reissue (Applied)

Engineering extended the expiration of TJX's ingestion API keys to 2026-09-02. New replacement keys are to be generated and delivered ahead of that date to prevent recurrence.

### Option B — Search configuration correction (Applied)

Corrected the client-side search configuration responsible for the residual report; confirmed with the customer on 2026-08-12.

## 8. Open Questions

No open questions — ticket resolved.

## 9. Queries Run

No SQL queries on record — investigation was based on WI job run logs (GNG check messages), Application Insights feed activity, WISC Control Panel manual WI re-run, and a screen recording.

## 10. Extras / Additional Screenshots

GNG skip log screenshots, Teams thread in Retail Ops > Secure 5 Issues, screen recording confirming WI results. Related ticket: RTS-205289 (TJMAXX Postransactions Data Feed Inactive).

---
ticket: RCS-28732
cliente: Alo Yoga / Shopify client 505 (no es cliente SnowTime)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: no se puede reportar quien proceso los refunds de customer service
causa: la funcion ShopifyRefundToMDMOrder nunca incluyo staffMember en la consulta GraphQL de enriquecimiento
fix: extender el GraphQL en shopify_mapping, dueno Growth Engineering, no hay superficie editable en SnowTime ni Secure
relacionados: DO-6616
confluence_id: 478177296395
modificado: 2026-09-04
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478177296395
---

# RCS-28732 — Alo Yoga: Need to be able to view and report on the customer service transactions

Prepared: 04 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28732 |
| Customer | Alo Yoga |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 02 September 2026 |
| Reporter | krislyn.vara@aloyoga.com |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28732 |

## 2. Problem Statement

Alo Yoga requested that Appriss capture the staffMember field from the Shopify Refund GraphQL object (who processed a customer-service refund) so they can report on CS refund transactions. Alo confirmed with Shopify that the field is available and that the required read_users scope is already enabled for Appriss.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Alo Yoga |
| Shopify Client ID | 505 (NOT a SnowTime dbt client — no dbt/clients or pyardm project exists) |
| Pipeline | Dedicated Shopify ingestion pipeline (Shopify Tunnel to Event Hub to shopify_mapping Azure Function to Greenplum GP3 + Snowflake), owned by Growth Engineering / DataOps Platform |
| ARDM Version | v3 |
| Data store | Greenplum GP3, schema ardm_505 (dedicated, not the shared ardm_500 multi-tenant schema) |
| Active products | Secure Investigations / Engage |

## 4. Investigation

### 4.1 Client/pipeline identification

FAIL (expected) — No SnowTime/dbt client exists for Alo Yoga. Architecture docs in the Secure repo confirmed Alo Yoga (Shopify client_id 505) runs on a separate Shopify-to-ARDM pipeline owned by Growth Engineering, not SnowTime.

### 4.2 Data store / query engine identification

PASS — Confirmed engine is Greenplum/Postgres (plpythonu), dedicated schema ardm_505 — not Snowflake, not SQL Server. (Analyst initially validated against the wrong connection twice — T-SQL syntax errors — before confirming the correct GP3 target.)

### 4.3 Data validation — staffMember capture gap

POINT OF FAILURE FOUND — Over a 90-day window of return/exchange events, sales_person_id and manager_id are NULL in 100% of rows, and extra_fields contains only {"event_id": "..."}. cashier_number is populated in a small subset of rows only (in-store POS returns, not the Shopify-admin CS refunds the client is asking about). Confirms the Shopify staffMember field is never captured by the mapping pipeline.

### 4.4 Precedent check

FINDING — DO-6616 ("ALO - Cashier Profiles Not Configured", closed Not Needed, Feb 2026) requested different, unavailable StaffMember-object attributes (role, hire date, address); Shopify's API doesn't expose those. This ticket's ask (staffMember on the Refund object) is a distinct, standard, documented GraphQL field — not the same dead end.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | N/A — feature gap, not a regression. The Shopify mapping function (ShopifyRefundToMDMOrder) never included staffMember in its Refund GraphQL enrichment query. |
| Why | The GraphQL query used to enrich refund events was scoped without the staffMember{id,firstName,lastName,email} sub-selection, even though Shopify exposes it and Appriss already holds the read_users scope. |
| Scope | All Alo Yoga (client_id 505) Shopify-admin/CS refund and exchange events, historical and ongoing. |
| Business impact | Alo Yoga cannot report on which staff member processed customer-service refunds — a reporting gap, not data corruption or outage. |
| Evidence | 90-day sample of ardm_505.ardm_event (return/exchange types) — sales_person_id/manager_id NULL in 100% of rows; extra_fields carries only event_id. |

## 6. Additional Findings

cashier_number is populated for a small subset of return/exchange events — these correspond to in-store POS-originated returns, which already carry a cashier number through the standard POS feed. Unrelated to the CS/Shopify-admin refund flow requested in this ticket; requires no fix.

## 7. Recommended Fix

### Option A (Recommended)

Growth Engineering: extend the ShopifyRefundToMDMOrder function (repo DataOps Platform/shopify_mapping) GraphQL query to include staffMember { id firstName lastName email } on the Refund object, and map it to ARDM_EVENT.SALES_PERSON_ID (or EXTRA_FIELDS) for return/exchange type events. No client-side work required — scope already enabled.

No Option B — SnowTime/Secure have no editable surface for this pipeline.

## 8. Open Questions

* Should staffMember map to the existing SALES_PERSON_ID column or a new EXTRA_FIELDS field? (Growth Engineering decision.)
* File as a new ticket against shopify_mapping/DataOps Platform backlog, or handle via comment/escalation on RCS-28732?
* Confirm whether backfilling historical refund events is in scope, or only forward-looking capture.

## 9. Queries Run

| # | Query | Target | Result |
| --- | --- | --- | --- |
| 1 | `SELECT e.type, e.cashier_number, e.sales_person_id, e.manager_id, e.extra_fields, COUNT(*) FROM ardm_505.ardm_event e WHERE LOWER(e.type) IN ('return','exchange') AND e.date_time >= CURRENT_DATE - INTERVAL '90 days' GROUP BY 1,2,3,4,5` | Greenplum GP3, schema ardm_505 | sales_person_id/manager_id NULL 100%; extra_fields only event_id; cashier_number populated in under 10% of rows (POS-only) |

## 10. Extras / Additional Screenshots

CX.Refund.pptx and the email thread with Shopify staffMember GraphQL instructions. [See Jira attachment / link in ticket]

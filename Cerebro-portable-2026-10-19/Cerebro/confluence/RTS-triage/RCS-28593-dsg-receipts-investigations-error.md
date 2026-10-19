---
ticket: RCS-28593
cliente: Dick's Sporting Goods (DSG) / c095_dks
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: abrir un recibo dentro de una Investigation da error generico con tracking code
causa: el alias de conexion pos-data del cliente 095 sigue apuntando a Greenplum, el servicio ejecuta GET_ARDM_JSON, que es solo de Snowflake, contra Postgres
fix: repuntar el connection string en Azure App Service, fuera de arpfiles y de SnowTime
confluence_id: 478175100930
modificado: 2026-09-03
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478175100930
---

# RCS-28593 — Dick's Sporting Goods: Receipts in Investigations Throwing Errors

Prepared: 03 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28593 |
| Customer | Dick's Sporting Goods (DSG) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 26 August 2026 |
| Reporter | Ryan Wade (ryan.wade@dcsg.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28593 |

## 2. Problem Statement

When opening a receipt from within an Investigation (Work Item to Events to click a transaction), the UI shows a generic error ("Something went wrong while trying to get the information you requested.") with a tracking code. Reported independently by two users on the same account, reproducible.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID (dbt) | c095_dks |
| Client ID (Secure) | 095 |
| ARDM Version | v2 (snowtimeV2) |
| Snowflake Schema | ARP_PRODUCTION.C095_DKS |
| SnowTime Go-Live | 20 August 2026 (PR 56337) |

## 4. Investigation

### 4.1 Ticket screenshots analysis

POINT OF FAILURE FOUND. Grafana log shows: `Component: Core.ArdmJson.SnowtimeArdmJsonService`, `Sender: FetchTransactions`, message `System.Exception: Snowflake call to 'GET_ARDM_JSON' failed. ---> Npgsql.PostgresException: 42883: function get_ardm_json(transactionids := bigint[]) does not exist`. The call is labeled as a Snowflake call but the driver in the stack trace is `Npgsql` (Postgres/Greenplum), not the Snowflake .NET driver.

### 4.2 Secure code review — SnowtimeArdmJsonService

PASS (informational). Confirmed the 3-tier fetch: primary raw-SQL read against `ARDM_JSON` table (Snowflake), scalar fallback `GET_TRANSACTION_JSON`, and a Greenplum-only fallback `get_secure_json`. None of these default names/signatures match the error's `get_ardm_json(transactionids := bigint[])` — ruling out a simple code-level naming bug.

### 4.3 EventProviderFactory activation logic

Finding. When `Feature.SnowtimeArdmJson.EnableSnowtimeArdmJsonEventProvider=True` and the configured provider is `GenericEventProvider`, the factory swaps in `SnowTimeEventProvider` at runtime (EventProviderFactory.cs:162-170), which assumes the provider's configured `connectionName` resolves to Snowflake.

### 4.4 GetArdmJson.sql — Snowflake-only confirmation

PASS (informational). `GET_ARDM_JSON(TRANSACTIONIDS VARCHAR)` is a Snowflake-only function, standard replacement for `GET_TRANSACTION_JSON` for SnowTime-migrated clients. No Greenplum/Postgres counterpart exists or is expected.

### 4.5 arpfiles config comparison (095 vs. working client 166)

PASS (rules out app-config cause). Both clients have identical `EventProvider.store.connectionName: "pos-data"` and identical feature flag state. Both `database-manifest.usprod.json` files list only a `snowflake` connection entry — the "pos-data" alias is not defined in this repo, so it resolves at the infrastructure layer (Azure App Service / Function App), outside `arpfiles` and outside SnowTime's scope.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Receipt fetch for client 095 routes through `SnowTimeEventProvider` to `SnowtimeArdmJsonService`, which executed its Snowflake-shaped read against a Postgres/Greenplum connection instead of Snowflake. |
| Why | The client's connection alias "pos-data" is resolved at the Azure infrastructure level (App Service / Function App connection string), not in application config. For client 095, this alias likely still points to the legacy Greenplum database and was not repointed to Snowflake as part of the 20 August 2026 SnowTime go-live — unlike already-migrated clients (e.g. 166), where it works correctly. |
| Scope | All receipt/transaction-detail views under Investigations for client 095 since go-live (20 August 2026 onward). |
| Business impact | Analysts cannot view transaction receipts inside investigations for this client — a core investigation workflow is blocked. |
| Evidence | Error trace shows `Npgsql.PostgresException: 42883` under a component that expects a Snowflake call; `GET_ARDM_JSON` is confirmed Snowflake-only in the deployed DDL; app-level config for 095 is identical in shape to a working client (166). |

## 7. Recommended Fix

### Option A — Repoint the "pos-data" connection at infrastructure level (Recommended)

Escalate to Engineering/DevOps (Secure infra) to verify the "pos-data" connection string/alias configured on client 095's Azure App Service / Function App, and repoint it from the legacy Postgres/Greenplum database to the client's Snowflake connection (`ARP_PRODUCTION.C095_DKS`), matching the setup already in place for migrated clients such as 166. Not actionable from the SnowTime or `arpfiles` repos — requires Azure infra access.

## 8. Open Questions

Root cause is inferred from log evidence + code + config comparison, not yet confirmed directly against the Azure App Service connection-string configuration for client 095. Needs Engineering/DevOps confirmation before closing.

## 9. Queries Run

No SQL queries run — investigation was based on Jira ticket data, Secure source code, and arpfiles configuration comparison.

## 10. Extras / Additional Screenshots

Grafana error log with the full exception trace, and the UI error dialog with tracking code. [See Jira attachment / link in ticket]

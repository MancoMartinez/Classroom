---
ticket: RTS-205543
cliente: Lululemon (LLU / c056llu)
analista: Ayesha Mehar
estado_ficha: RESOLVED (CLOSED)
sintoma: GP Process Error en el pipeline load_ardm_ecom, no partition for partitioning key
causa: 8 filas historicas de 2023-01-07 a 2024-06-11 caen en un hueco de particiones entre la particion init y la primera semanal real
fix: dropear las particiones manuales y dejar que generate_order_partitions() reconstruya
advertencia: nunca agregar una DEFAULT partition a una tabla de Greenplum manejada por una funcion generate_*_partitions(), son incompatibles
confluence_id: 478141808643
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478141808643
---

# RTS-205543 — Lululemon: GP Process Error (Partition Gap) — Data Load Failure

Prepared: 25 August 2026 | Analyst: Ayesha Mehar | Status: RESOLVED (CLOSED)

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-205543 |
| Customer | Lululemon (LLU / c056llu) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Closed (Resolution: Resolved) |
| Opened | 09 August 2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Ayesha Mehar (amehar@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-205543 |

## 2. Problem Statement

Grafana alert fired for Lululemon (LLU/056): GP Process Error in the ecom load pipeline (`load_ardm_ecom`) on GP2, trading day 2026-08-07. Alert category: Dataload Alerts.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c056llu (Lululemon) |
| Framework | Legacy pyardm (`appriss_ardm`), Greenplum GP2 |
| Schema | `ardm_056` |
| Table affected | `ardm_056.order_tender` |
| ARDM version | N/A — legacy pyardm pipeline |

## 4. Investigation

### 4.1 Initial failure — partition key error

POINT OF FAILURE FOUND. `psycopg2.DataError: no partition for partitioning key`. 8 historical ecom rows (2023-01-07 to 2024-06-11) in `order_tender` fall into a partitioning gap between the `init` partition (1000-01-01 to 1000-01-02) and the first real weekly partition (2024-07-08).

### 4.2 First fix attempt — DEFAULT partition conflict

FAIL. Adding `t_historical` plus a DEFAULT partition unblocked the INSERT but introduced a new conflict: `Process in recovery mode, but recover semaphore is missing` — caused by a prior failed run leaving `recover_flg = 0` in `ardm_056.config_control` with status ERRORED.

### 4.3 Recovery semaphore fix

PASS. `UPDATE ardm_056.config_control SET recover_flg = 1::BIT(1) WHERE client_id = 'c056llu' AND is_production = 1::BIT(1) AND configuration_id = 'ardm'` cleared recovery mode.

### 4.4 Partition function conflict

POINT OF FAILURE FOUND. Rerun triggered `ardm_056.generate_order_partitions()`, which failed: `cannot add RANGE partition "t2023_01" to relation "order_tender" with DEFAULT partition "other"`.

### 4.5 Correct fix — drop manual partitions, let function rebuild

PASS. Dropping both manual partitions and rerunning the pipeline let `generate_order_partitions()` create all required weekly partitions from 2023 onward.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | `ardm_056.order_tender` partitioned table on Greenplum GP2 |
| Why | Partitioning gap for 8 historical ecom rows between the `init` partition and the first real weekly partition; the manual DEFAULT partition added as a workaround was incompatible with the table's `generate_order_partitions()` auto-partitioning function |
| Scope | c056llu ecom load, trading day 2026-08-07, 8 historical rows |
| Business impact | Ecom load pipeline blocked; L1 Grafana alert fired |
| Evidence | The error chain: no partition for partitioning key, DEFAULT partition workaround, recovery-mode lock, cannot add RANGE partition with DEFAULT partition, resolved by dropping both manual partitions |

## 7. Recommended Fix

### Option A — Drop manual partitions, let auto-generator rebuild (Applied)

```
ALTER TABLE ardm_056.order_tender DROP PARTITION other;
ALTER TABLE ardm_056.order_tender DROP PARTITION t_historical;
```

Rerun the pipeline — `generate_order_partitions()` creates all needed weekly RANGE partitions automatically. Never add a DEFAULT partition to a Greenplum table managed by a `generate_*_partitions()` function.

## 8. Open Questions

No open questions — ticket resolved.

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | ADD PARTITION t_historical + ADD DEFAULT PARTITION other | Unblocked INSERT, caused recovery-mode conflict |
| 2 | UPDATE ardm_056.config_control SET recover_flg = 1::BIT(1) ... | Cleared recovery-mode lock |
| 3 | DROP PARTITION other; DROP PARTITION t_historical | Resolved — generator rebuilt partitions automatically |

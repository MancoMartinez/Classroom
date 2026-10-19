# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

Production. Client 248, Chemist Warehouse, tenant chemistwarehouse.

### Chemist Warehouse (CWH), 2026-09-23

1. Sign in through the internal Control Panel, usprod.apprissretailcloud.com/control, table Customers in USPROD, Chemist Warehouse, Click logo to sign in.
2. Inside the tenant, open All Apps, Secure Store, Composer.
3. New search. Conditions, Store No, operator In, values 036,803.
4. Display Fields, add Store No, Channel, Order Number, Trading Day, POS No.
5. Run. Open the Query button to read the generated SQL.

Expected: POS No resolves the till name, for example TILLD04, per the mapping DO-9495 shipped.
Actual: POS No returns raw multi digit values, for example 147426 and 863485, on both stores 036 and 803. The generated SQL shows the field bound to T1.posno on ardm_Header. Result capped at 1000 rows, no trading day filter applied yet.

## 2. Findings

1. Verified. The Composer POS No field pulls T1.posno directly from ardm_Header for CWH, confirmed from the Query button output on 2026-09-23.
2. Verified. Same query returns raw numeric posno values on store 036 and on store 803. A store specific cut is ruled out.
3. Verified, from DO-9495, https://trebuco.atlassian.net/browse/DO-9495. Tomasz Sutkowski diagnosed the original defect as the field reading ardm_event_vw.pos_number instead of ardm_header_vw.machine_name. Bartosz Bereski closed it by reloading one raw file by hand, c248_rawdata_postransactions/2026/02/17/17/data_6_5_0.json.gz. FixVersions is empty.
4. Unverified hypothesis. The machine_name mapping from DO-9495 was never written into map_ardm_header.sql. New transactions since the manual reload keep resolving from the raw column, which matches what today's query shows.
5. Verified. The bad value on this ticket, 863485, has six digits. The bad value on DO-9495, 71, was a two digit register number. Whether both come from the same source column is not confirmed against the dbt repo.

## 3. Troubleshooting performed, and the limits of support access

1. Reviewed prior tickets on the same tenant and field. DO-9495, https://trebuco.atlassian.net/browse/DO-9495. DO-7534, https://trebuco.atlassian.net/browse/DO-7534, the original business requirement for an alphanumeric till value.
2. Reproduced live in Production on 2026-09-23 through Composer as described above and pulled the generated SQL with the Query button.
3. Ran the store 036 and 803 combined search. Did not yet run a trading day scoped query, the 1000 row cap was hit before that filter was applied.
4. Claude flagged this as the likely root cause. I checked the DO-9495 ticket text, ran the Composer query myself in Production, and pulled the generated SQL. Here is what I found. This is what I think is happening. Could someone else evaluate this and give me your thoughts?
5. No conversations about this ticket happened outside of Jira.
6. Support has no read access to the dbt repo for client 248 or to Azure DevOps PR history. I cannot confirm whether map_ardm_header.sql currently references machine_name.

## 4. Ruled out. Do not repeat

| Hypothesis | Refutation |
|---|---|
| Store specific mapping gap, store 036 against 803 | Both stores return raw numeric posno in the 2026-09-23 query |
| ENG-7898, Gold Layer IS_ECOM fix, https://trebuco.atlassian.net/browse/ENG-7898 | Affects IS_ECOM only, the ticket itself states it is not a new failure mode |
| ENG-7610, Snowflake Shares export addition, https://trebuco.atlassian.net/browse/ENG-7610 | Backlog, no code merged. Confirms the pipeline is cwh_ecom, is not itself the cause |
| RCS-28661, Wal-Mart POS 84 showing instead of register | Same symptom shape, different pipeline, BigQuery, no technical relation |

## 5. Still open

1. Does map_ardm_header.sql for client 248 currently map posno from machine_name, or still from the raw flat layer column that ardm_event_vw.pos_number used before DO-9495?
2. If the mapping is not in the model, can it be added there instead of relying on a manual file reload. Posno feeds get_transaction_id(), the 19 digit PK, so a remap changes transactionid for new transactions going forward and needs a stated cutover date.
3. Does DO-9495 cover ardm_Header.posno, or only ardm_event_vw.pos_number? Today's query reads T1.posno from ardm_Header, not from ardm_event_vw.

Related tickets. DO-9495, https://trebuco.atlassian.net/browse/DO-9495. DO-7534, https://trebuco.atlassian.net/browse/DO-7534. ENG-7610, https://trebuco.atlassian.net/browse/ENG-7610. Priority Medium, 29 days since the client reported it on 2026-08-25.

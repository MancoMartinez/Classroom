Hi Enrique, I took a look at RCS-29231. I think the link to RTS-208663 is the key, and it may not be stale data at all.

On 30 Sep the C044_URB dbt run failed on column X_RCPT_COUNT with the same error, Numeric value '' is not recognized. Sumeet said it came from an earlier PR. The pipeline was resumed and the alert closed. The rows already loaded with '' could still be in the table. The reprint receipt report likely compares X_RCPT_COUNT to a number, so Snowflake stops on the first ''.

Three quick checks to confirm:
1. QUERY_HISTORY for QueryId 01c77149-0109-d5e7-0120-d20111089fc7 to see the compiled SQL and the column it casts.
2. data_type of X_RCPT_COUNT in ARDM_PRODUCTION.C044_URB.
3. Count of rows where X_RCPT_COUNT = '' by load date. I would expect them to start on 29 or 30 Sep.

Running the report with a date range ending 28 Sep is also a fast test. If all of that lines up, the ask goes to SnowTime in Data Issues, referencing RTS-208663: fix the mapping to send NULL and backfill the affected rows. I may be missing something, happy to look at it together.

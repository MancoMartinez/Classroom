-- Read only. Run in sqldb-prd-wus2-arp-production-209-tbi-platform.
SELECT DB_NAME() AS SelectedDatabase, GETUTCDATE() AS CheckedAtUTC;

WITH TargetUsers AS (
    SELECT UserName
    FROM (VALUES
        ('Jacinta.Titus@kgstores.com'),
        ('Emeldia.Pryor@kgstores.com'),
        ('Christi.Winters@menswearhouse.com'),
        ('Rahim.Mehdiyev@menswearhouse.com'),
        ('Cheneria.Chevalier@josabank.com')
    ) AS Names(UserName)
)
SELECT
    t.UserName,
    CASE WHEN st.UserName IS NULL THEN 'Not found' ELSE 'Found' END AS TeamRowFound,
    st.TeamName,
    st.Persistent,
    st.InsertedDateTime AS TeamRowInsertedAt,
    st.UtcDateFrom,
    st.UtcDateTo
FROM TargetUsers AS t
LEFT JOIN sso.teams AS st ON st.UserName = t.UserName
ORDER BY t.UserName, st.Persistent DESC, st.InsertedDateTime DESC;

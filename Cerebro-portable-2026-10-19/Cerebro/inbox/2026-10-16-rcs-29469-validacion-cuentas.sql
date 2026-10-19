-- Step 1. Check the selected database before running the remaining SELECTs.
SELECT DB_NAME() AS SelectedDatabase, GETUTCDATE() AS CheckedAtUTC;

-- Step 2. Run in sqldb-prd-wus2-arp-production-209-tbi-platform.
-- Each SSO assignment is shown separately. Do not treat multiple rows as a defect yet.
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
    CASE WHEN u.UserName IS NULL THEN 'Not found' ELSE 'Found' END AS AccountFound,
    u.SecurityID AS AccountSecurityID,
    u.LastLoginDate,
    s.SecurityID AS SSORowSecurityID,
    s.Persistent,
    s.InsertedDateTime AS SSORowInsertedAt,
    s.UtcDateFrom,
    s.UtcDateTo
FROM TargetUsers AS t
LEFT JOIN membership.Users AS u ON u.UserName = t.UserName
LEFT JOIN sso.SecurityLevelAssignments AS s ON s.UserName = t.UserName
ORDER BY t.UserName, s.Persistent DESC, s.InsertedDateTime DESC;

-- Step 3. Inspect schema before querying the teams table by username.
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'sso' AND TABLE_NAME = 'teams'
ORDER BY ORDINAL_POSITION;

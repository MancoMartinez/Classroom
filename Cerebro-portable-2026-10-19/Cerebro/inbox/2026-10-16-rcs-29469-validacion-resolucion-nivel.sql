-- Read only. Select the TBI platform database in SSMS.
SELECT DB_NAME() AS SelectedDatabase, GETUTCDATE() AS CheckedAtUTC;

SELECT OBJECT_DEFINITION(
    OBJECT_ID(N'sso.GetUserSecurityLevel')
) AS GetUserSecurityLevelDefinition;

Sure Kiran. This is the query that fails, from the goodwillsacto nettrack Error log (case 10839, 10/06):

Error: LPSDAL.LPSDAL DAL.ReadDataTable: Incorrect syntax near the keyword 'Where'.
Query received: Where Shoplifting.ShopliftingID = 10839 And ( CaseType ='Critical Incident' )

It arrives as only the WHERE fragment, with no SELECT ... FROM before it. The legacy GoodwillSacto database still has the full Runquery for the same alert (Critical Incident):

Select 1 FROM MasterCase INNER JOIN Shoplifting ON Shoplifting.MasterCaseID = MasterCase.MasterCaseID INNER JOIN Suspect ON Suspect.SuspectID = Shoplifting.SuspectID INNER JOIN Store ON Store.StoreIdent = Shoplifting.StoreIdent LEFT JOIN Accident ON Accident.ShopliftingID = Shoplifting.ShopliftingID Where Shoplifting.ShopliftingID = @ShopliftingID And (CaseType ='Critical Incident')

If you meant the SELECT I ran to read the stored Runquery in the platform database, tell me and I send that too.

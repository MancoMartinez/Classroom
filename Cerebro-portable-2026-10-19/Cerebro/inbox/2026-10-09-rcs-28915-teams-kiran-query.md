Sure Kiran. This is what the engine runs and the error it gets, from the goodwillsacto nettrack Error log (case 10839, 10/06 02:58 UTC):

Error: LPSDAL.LPSDAL DAL.ReadDataTable: Incorrect syntax near the keyword 'Where'.
Query received: Where Shoplifting.ShopliftingID = 10839 And ( CaseType ='Critical Incident' )

It is only the WHERE fragment, there is no SELECT ... FROM before it. This is the full Runquery that the legacy GoodwillSacto database still has for the same alert (Critical Incident):

Select 1 FROM MasterCase INNER JOIN Shoplifting ON Shoplifting.MasterCaseID = MasterCase.MasterCaseID INNER JOIN Suspect ON Suspect.SuspectID = Shoplifting.SuspectID INNER JOIN Store ON Store.StoreIdent = Shoplifting.StoreIdent LEFT JOIN Accident ON Accident.ShopliftingID = Shoplifting.ShopliftingID Where Shoplifting.ShopliftingID = @ShopliftingID And (CaseType ='Critical Incident')

I can send the text for alerts 12, 13, 14 and 16 too.

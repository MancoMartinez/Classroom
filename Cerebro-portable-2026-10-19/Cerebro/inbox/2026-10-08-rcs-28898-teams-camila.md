Hi Camila, here is how store 1449 was confirmed on RCS-28898.

Diego queried the Urban database on September 15. Store 1449 maps to StoreIdent 503 in dbo.Store. The Shoplifting table is active, but the newest row for 503 is from December 6, 2025, so the Case for that investigation was never written. The incident schema also does not exist on that database. That is what confirms the Case record was never created.

For the cause, the Control Panel log from September 11 shows "Invalid object name incident.LPUser" on the Move to Case action. Matt called it the most likely cause and linked it to ENG-6976, and he said he had not validated that both tickets share the same issue. I did not find that validation afterwards. Nobody retested after the deploy either, because Tim could not reopen the investigation.

Diego's first write up pointed at the OrcInvestigation tables, and Matt corrected that the same day since Urban is not in unification mode.

The ticket closed on September 16 with a workaround, a new case related to 1-1449-23-External. Is there anything in the ticket I may be missing about a retest?

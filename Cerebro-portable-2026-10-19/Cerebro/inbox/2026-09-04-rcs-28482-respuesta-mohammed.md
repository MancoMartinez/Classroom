Hi Mohammed,

Confirmed on both reports. Rebuilding the Store join restored MISC and the full tab set.

PBI - Current Location Listing needed one join fixed, EmployeeID to Store.StoreManagerID, matching what you found.

Outlook Export had three broken joins, not one. Two matched a hierarchy pattern already in the report, EmployeeID to Store.RegionalManagerID and EmployeeID to Store.DistrictManagerID. The third compares Misc1 to Store, not EmployeeID. Setting it to Store.StoreManagerID, following the same hierarchy pattern as the other two, also unblocked all tabs.

I have not verified whether Misc1 to StoreManagerID is the intended mapping. It was not part of your original diagnosis. Can you confirm it is correct? If it is wrong, the tabs will still work, the report's data may not.

Saved both reports. Updating the client now that all tabs are available on both.

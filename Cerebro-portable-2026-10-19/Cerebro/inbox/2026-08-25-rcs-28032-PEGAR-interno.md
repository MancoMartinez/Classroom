**Client ID 433.** **Environment:** Production, `https://apps.apprissretail.com/vitaminshoppe/nettrack/`, build **6.26.8**.

Full history and current state. This ticket holds two separate problems. Only the second one goes to Engineering today.

## 1. Original report. Resolved

Brandon Bigelow hit a **Session Error** on 29 July after a forced password change. It cleared on its own within 24 hours. Joe Austin confirmed recovery on 31 July. His account is healthy. **Close that thread.**

## 2. Second problem. Raised 31 July

Joe reported that **Dayna Rivera** covers districts **501** and **504** and reaches only 504.

## 3. What Support changed on 4 August

I added both districts to her profile through **Control Panel, Hierarchies**. On 10 August Dayna reported the inverse result. She gained 501. She lost 504. That flip pointed us at multi-district assignment as the suspect.

## 4. What I ruled out between 4 and 11 August

| Checked | Result |
|---|---|
| Permission groups | She carries the same three groups as Journey Armstrong, Daniel Garza and Gisele Pohl |
| Account state | Locked, Disabled and Deleted all **false**. Last sign-in 10 August |
| Secure to Incident user mapping | All four users resolve to a valid active `LPUser` |
| Duplicate accounts from the platform update | No duplicate email addresses on this tenant |
| `EnableAdHocInitCaching` and `EnableAdHocPerRequestUserScope` | Both **True** on this database |
| District master data, `SupervisorFlag`, `SecurityID` | Not the driver |

None of them explains the behaviour.

## 5. Data model. Verified with SQL on 10 August

`structure.LocationHierarchyMaster` defines four levels on this tenant: **Company, Division, Region, District**. District sits at level 4.

All **884 rows** in `secure.LocationHierarchyUserAssignments` assign by `LocationId`. **Zero rows** use the district, region or division columns. District scope inherits from the store you assign.

## 6. Engineering contact that happened outside this ticket

**Kiran Vadday** reviewed the analysis above on 10 and 11 August. He asked for the exact page and URL where Dayna expects 501 and does not see it. Joe forwarded her screenshots to the ticket on **18 August**.

## 7. New SQL evidence from 25 August. This corrects item 3

`incident.Store` returns her three stores:

| StoreIdent | StoreNo | StoreName | Region | District | DistrictManagerID |
|---|---|---|---|---|---|
| 946 | 1016 | Federal Way WA Store | 3 | **501** | 10419 |
| 617 | 249 | Tanasbourne OR Store | 3 | **501** | 10419 |
| 466 | 500 | Everett WA Store | 3 | **501** | 10419 |

My 10 August note on this ticket recorded store 249 in district 504. **It returns 501 today.** All three of her stores sit in 501. She sees 501 because every store she holds sits in 501. She holds nothing in 504.

District **504** returns nine stores:

| StoreIdent | StoreNo | StoreName | District | DistrictManagerID |
|---|---|---|---|---|
| 377 | 541 | Puyallup WA Store | 504 | 49781 |
| 618 | 250 | Redmond WA Store | 504 | 80288 |
| 700 | 313 | Tukwila WA Store | 504 | 49781 |
| 764 | 393 | Issaquah WA Store | 504 | 49781 |
| 895 | 589 | Tacoma WA Store | 504 | 49781 |
| 938 | 1026 | South Lake Union WA Store | 504 | 80288 |
| **948** | **1018** | **Bremerton WA Store** | **504** | **10419** |
| 956 | 1023 | Clackamas OR Store | 504 | 49781 |
| 1292 | 1033 | Issaquah WA Store | 504 | 49781 |

**Store 948 carries `DistrictManagerID` 10419.** Her three stores carry the same value. That store sits in 504 and never made it into her LHUA scope.

Confirm 10419 maps to her:

```sql
SELECT UserID, FirstName, LastName, EmailAddr
FROM incident.LPUser
WHERE UserID = 10419;
```

District 504 spreads across **three district managers**: 49781 on six stores, 80288 on two, 10419 on one. Raise that with the customer as master data they need to review.

## 8. Next step on the district question. Do not escalate this part yet

Assign **store 948** to her in LHUA. Watch what happens. Three outcomes decide the case:

| Outcome | What it means |
|---|---|
| She gains **both** districts | She only lacked a store in 504. No defect |
| She swaps 501 **for** 504 | The platform ignores multi-district assignment. This part goes to Engineering |
| **Nothing** changes | The inheritance model in item 5 is wrong |

Book the window with Joe before you touch it. **A swap leaves her unable to work.**

## 9. Separate defect. Any user reproduces it. This is what needs Engineering

**New Audit cannot hold a selected location.** I reproduced it with full admin scope, so permissions play no part. **HAR attached.**

**Steps to reproduce**

1. Open `/vitaminshoppe/nettrack/Audit/NewAudit.aspx`
2. Type a store number into **Select Location**. The typeahead resolves. For `1016` the server returns `StoreNo 1016`, `StoreName Federal Way WA Store`, `StoreIdent 946`, `City Federal Way`, `State WA`, `OpsRegion 3`, `OpsDistrict 501`, `Zip 98003`, `Inactive 0`
3. Select the store. The browser posts the StoreIdent to `fld_storeident$cpStoreLookupCallbackPanel` as `c0:946`
4. **The server returns `hfStoreLookup` re-rendered with `value=""`.** Every later postback still carries `fld_storeident$fld_storeident` **0**, `fld_storeident$fld_storeno` **0**, `screentypecode` **0** and `clientid` **0**. Meanwhile the combo displays `1016 - Federal Way WA Store, Federal Way, WA, 3`
5. Click **Next**. **No HTTP request leaves the browser.** The console throws nothing. The button declares `autoPostBack: true` and `serverEvents: ['Click']`, then routes through `btnSave_Click`. That function validates against the empty hidden field and returns without rendering a message

**The form never holds a location.** That produces the *"Please select a location and try again"* message the customer reported on 11 August.

**Console output at page load.** Neither one fires on the click:

1. `[Violation] Permissions policy violation: unload is not allowed in this document`, thrown by `DXR.axd`
2. `Bootstrap doesn't allow more than one instance per element. Bound instance: bs.tooltip.`, thrown by `data.js:26`, stack `cpf.ui.js:8944`, `popover.js`, `base-component.js`, inside the jQuery ready handler

Check whether that second exception cuts DevExpress control initialisation short.

## 10. Screen Labels on the same page

The page renders **30 Screen Label fallbacks**. The list includes the store lookup's own column headers:

`Store_StoreNo`, `Store_StoreName`, `Store_City`, `Store_State`, `Store_OpsRegion`, `Store_OpsDistrict`, `Store_Address1`, `Store_Zip`, `Store_Country`

It also includes `btn_Next`, `sys_PleaseFindStore`, `title_storelookup`, `title_SelectAuditName`, `title_AuditName`, `LPUser_Language` and the `mnu_` navigation entries.

The store lookup runs with `dxpDisplayColumns: true` and `dxpValueField: 'StoreIdent'`. **Check whether it resolves the value column by name.** If it does, the missing labels break the mapping and explain item 9.

The React bundle loads as `allApps___v6.26.8_433en-GB`. **This tenant resolves culture as en-GB.** Check whether the label rows exist for en-US only. Dayna's 11 August screenshots show these same labels resolving correctly, so the failure tracks the session rather than the tenant.

## 11. Related tickets. Read these before you pick this up

**RCS-28005**, same client. Tyrone rebuilt the audit screens for 433 on 28 July to clear a 404 on `AuditSection_V268_S212.aspx`. Matt Kamminga then asked on the linked ENG to add validation confirming screens rebuild as part of the migration path. **That rebuild is a candidate for the missing label rows.**

**RCS-28321**, Boot Barn. `SystemSelect.aspx` returns 500 with `GetEncryptionKey: Record missing in Options Table` for slug `/bootbarn`, which breaks the cohesion-mode session handoff into Nettrack. Same exception class as RCS-27509 and ENG-6198. Kiran asked for reproduction steps there on 24 August. If the mechanism matches, **one missing config value per slug explains both the labels and the lost StoreIdent here.** Run a SELECT on the Options table for `/vitaminshoppe`.

## 12. What we need from Engineering

1. Explain why the server returns `hfStoreLookup` empty after it receives a valid StoreIdent
2. Confirm whether the store lookup resolves its value column by label name
3. Confirm whether the missing Screen Label rows come from a culture mismatch or from the 28 July screen rebuild

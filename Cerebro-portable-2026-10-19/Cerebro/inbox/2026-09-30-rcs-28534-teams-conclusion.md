# RCS-28534, conclusion para Teams con formato, ingles. Copiar desde el chat renderizado para conservar negritas

Hi Kiran, Diego and I reviewed Grafana for Stater Bros (clientId 423). Times in UTC.

**What we found**

**205148**
- 9/24 15:51: Discipline Request matched (6a Rows Returned=1)
- Went through 8, 8a, 11, 11d and **12b "Finding attachments"** at 15:52:04
- **No 13a, no End.** Every save from 15:57 to 20:43 shows Quit

**205157**
- 9/24 19:31: 6a returned 0 because DaysOffNotes was empty
- After Angie filled it, 19:32 returned 1 and the run **stopped at 12b** the same way. Quit at 19:36
- The filter uses **DaysOffNotes and CaseType, not case status**

**Before the fix**
- 17 HATR NettrackSmartAlertActivity **500 errors** on 9/28, the last one at 17:49

**After the fix**
- **189 of 189** runs that reached 12b also reached 13a within a second
- **99 of the last 100** emails at 13a reached 13b
- Only exception: "Stater Bros. Investigation 129" on 9/29 at 23:10, we will check it

**Quits since 9/28: 404 lines on 200 cases**
- 25 finished later
- 132 are a single Quit from an overlapping save
- 35 were already stuck before the fix
- 8 started showing Quits after it. We checked 205264: no run since 9/27, only Quits, so it was stuck before the fix

**Conclusion**
The 9/28 fix **also covers Stater Bros**. No new stuck runs appear after the deploy. The remaining Quits come from **cases stuck before the fix** that users keep saving.

**Next steps**
We will rerun **205148 and 205157 first**, then the cases Angie confirms HR still needs, **one at a time**:
1. Set InProcess = 0 in incident.Shoplifting
2. Open staterbros/nettrack/ProcessCaseAlert.aspx?ShopliftingID=<ID> from a System session
3. Check Grafana for 6a, 12b, 13a, 13b and End
4. Confirm the new row in SmartAlertProcess before moving to the next case

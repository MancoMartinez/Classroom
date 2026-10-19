# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment

Prod. VisualCron server QA-LPMS-VC-001, job `Refloader Prod Delhaize`, group Platform - Refloaders. Trigger runs Monday through Friday at 10:00 AM, active since 10 Jul 2025. 316 executions to date.

## 2. Field mapping confirmed

Read on 27 Aug 2026 from the format file the loader receives at runtime.

Source: `F:\Clients\Delhaize\RefLoader_Prod\fmt\employee.xml`, version 2025.07.09, created under RCS-21834.

| Item | Value |
|---|---|
| Feed file | `pii-pgp-DA_Employee_Info.dat` |
| Delimiter | comma |
| Text qualifier | double quote |
| Data starts at | row 2 |
| Target table | `incident.Employee` |
| Operation | upsert |
| Key | `EmployeeID`, position 19 |
| **Misc1** | **position 20** |
| `StoreNumber` | position 27 |

Loader binary: `F:\Clients\_CoreCode_Prod\RefLoader\ReferenceSupplementalLoad.exe`, invoked by `Custom_Load_ReferenceLPMS.cmd` with the customer config and the format file as arguments.

## 3. Findings

`Misc1` declares no `default` and no `rule` in the mapping. Compare against `Weight`, which carries `default="0"`, and against the date columns, which carry `rule="validdate"`. A blank position 20 loads as blank.

The operation is an upsert keyed only on `EmployeeID`. Any row ADUSA sends with position 20 blank overwrites the brand already stored for that employee. This is a hypothesis. It is not verified against the loader binary. A count of blank `Misc1` rows in `incident.Employee` measured against the current feed would settle it.

The mapping skips positions 5, 13, 21, 22 and 47. Positions 21 and 22 sit directly after `Misc1`, the usual place for Misc2 and Misc3. If ADUSA ever moved the brand into either one, the loader drops it without logging anything.

The EMPLOYEE block in the batch script sets `ANC_EXPECTEDDAILY=FALSE`. When the file does not arrive, the script writes one line to the job log and exits with code 0. No alert fires. Days without an employee feed are invisible in VisualCron.

## 4. Troubleshooting performed

Traced the chain from the VisualCron job variables to the FTP task output, then the batch script, then the format file. Task 1 output for the 27 Aug 10:00 run lists both downloaded files by full path. JobLog confirms the loader finds the file and returns code 0.

AI assisted. Claude was used to read the batch script and the XML mapping, and to draft this note. No SQL has been run against production for this yet.

Conversations outside the ticket: Matthew Kamminga on Teams, 26 and 27 Aug, pointed me to the Delhaize clients folder on the VisualCron machine and to the refloader job.

## 5. Ruled out. Do not repeat

| Hypothesis | Refutation |
|---|---|
| A separate employee import job exists | Filtering jobs on "employee" returns 6 results, none for Delhaize. The refloader carries store and employee in the same run |
| The batch never finds the file because of the `pii-` prefix | JobLog shows `Source file name: pii-pgp-DA_Employee_Info.dat` followed by return code 0 |
| The feed is an API integration | It is an SFTP pull from `lpms@files.lpguys.net:22`, folder `/uploads/DelhaizeFTP/imports` |

## 6. Still open

1. Jie Chen, confirm position 20 is the field your fix reads.
2. Run the blank `Misc1` count against `incident.Employee` to size the gap before ADUSA changes anything.
3. Decide whether `ANC_EXPECTEDDAILY` should flip to TRUE for the employee block, so a missing feed raises an alert.
4. Ask ADUSA for the file layout, to rule out that the brand moved into position 21 or 22.

Customer was asked on this ticket for position 20 to be populated for all employee records. Related: ENG-6744.

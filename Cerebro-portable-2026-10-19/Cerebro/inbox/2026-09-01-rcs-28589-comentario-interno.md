# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

This ticket was set to Completed with resolution Resolved on 27 August at 12:13. The load side was fixed. The symptom Ahold reported was not. Apostrophes still appear in the exported location listing, and that export feeds a downstream Ahold system. Automation for Jira reopened the ticket on 1 September at 10:29 against Jim Cosseboom's comment.

Ahold reads this as resolved in part. That reading is correct. Two layers live in one ticket and only one of them closed.

## 2. Environment and steps to reproduce

Environment: not recorded in this ticket. The 432 record correction ran against live location data and the export feeds a production Ahold system. Confirm PROD and write it here.

### Layer 1. Load. Closed. Ahold Delhaize (ADUSA), reported 26 August 2026

1. Take the store location file Ahold sends. The 26 August file carries examples.
2. Read the `EASFrequency` field, renamed to Longitude in the interface.

Expected: negative sign followed by the numeric value.
Actual: an apostrophe ahead of the negative sign. Screenshot `image-20260827-161228.png` attached 27 August 12:13.

### Layer 2. Export. Open. Ahold Delhaize (ADUSA), reopened 1 September 2026

1. Run the location listing export from LPMS. The exact screen and menu are not recorded in this ticket. Get them.
2. Open the exported file.
3. Read the Longitude column.

Expected: the value as stored, with no apostrophe.
Actual: an apostrophe ahead of the value. Screenshot `LPMS Apostrophes 09012026.png` attached 1 September 10:29.

Two items are missing and they decide the case. The file format produced by the export is not recorded. The application used to open the exported file is not recorded, and no one has asked.

## 3. Findings

The stored values carry no apostrophe. That was verified against the database on 1 September and evidenced in `image-20260901-153140.png`. The character therefore enters at export time or at render time.

Two causes remain live and they lead to different owners.

| Cause | Owner if true | Test that settles it |
|---|---|---|
| The export writes the character into the file | Engineering | Open the raw export in a plain text editor and look for the apostrophe |
| A spreadsheet application renders it on open | Ahold side, no platform defect | Same test. A spreadsheet shows a leading apostrophe on numbers held as text |

Nobody has run that test and nobody has asked Ahold which application opened the file. Ask before Engineering spends time on the export path.

The downstream system that consumes the export is not named anywhere in this ticket. Get the name. Whether that system rejects the values or only displays them differently changes the severity.

Scope is undefined. The load rule covers `EASFrequency` and `CCTVIPAddress`. No one has checked whether the export behaviour affects Latitude and `CCTVIPAddress` as well as Longitude.

## 4. Troubleshooting performed, and the limits of support access

27 August: apostrophes traced to the file Appriss receives, where the load accepted the data as sent. 432 affected records cleaned. A load rule added that ignores an apostrophe in `EASFrequency` and `CCTVIPAddress`.

1 September: database values checked after the reopen and confirmed clean, with a screenshot. Conclusion recorded that the export to file path needs an engineering review.

AI assistance: this note was drafted with AI assistance. Ticket state, transition timestamps, attachment names and quoted comments were read directly from Jira on 1 September 2026.

Conversations outside the ticket: the ADUSA escalation call on 1 September 2026 covered this ticket. Ahold described the behaviour there. The apostrophe does not appear in the store record for Food Lion Store 1. It does appear in column 8c of the CSV export of locations. It does not appear in the Izenda reports that feed their Power BI. Ron agreed on that call to tag Delivery and return the ticket to the list, so coordinate before moving state again or the two routes will cross.

## 5. Ruled out. Do not repeat

| Hypothesis | Why it is dead |
|---|---|
| The apostrophe sits in the stored data | Database values verified clean on 1 September, screenshot attached |
| The inbound file still carries it | The load rule added on 27 August strips it on ingest |
| The reports carry it | Ahold confirmed the Izenda reports feeding Power BI show no apostrophe |

## 6. Still open

1. Ask Ahold which application opened the exported listing, and get the raw export attached without saving it from a spreadsheet first. This is the single question that separates the two causes.
2. Record the exact screen and menu that runs the location listing export, and the file format it produces.
3. Name the downstream system that consumes the export, and confirm whether it rejects the values or only displays them differently.
4. Confirm whether the behaviour reaches Latitude and `CCTVIPAddress` as well as Longitude.
5. Confirm whether this needs to come back to planning as a platform bug, per the note on assignment.

Ticket opened 26 August 2026. Priority Medium. Reporter leighann.stubbs@adusa.com. Reopened by Jim Cosseboom. Currently Under Engineering Review with Matthew Kamminga as SRE.

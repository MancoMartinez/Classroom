# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction
This ticket was marked Completed and Resolved on 8/27 at 12:13, covering only the load side of the defect. Automation reopened it on 9/1 when Jim Cosseboom reported the apostrophes still appear on export. Closing it on 8/27 was premature. Only half the defect was fixed.

## 2. Environment and steps to reproduce
Environment: Production, AHL/DLZ tenant, store location listing export.

### AHL/DLZ, reopened 9/1

1. Run the export of the store location listing for the AHL/DLZ tenant.
2. Open the exported file without saving it from Excel first, to see the raw bytes.
3. Check the Longitude column, carried internally as EASFrequency.

Expected: the numeric value with no leading character, negative sign preserved where the value is negative.
Actual: two invalid characters appear before the numeric value. Ryan Barlow confirmed on 9/1 that the stored values in the database carry no apostrophe, so the character is introduced after the data leaves the database.

## 3. Findings
Two causes remain open and neither is ruled out. The export function could be inserting the character, or Excel could be displaying a leading apostrophe because the value is stored as text, which is standard Excel behavior for text formatted numbers. Ryan Barlow, 9/1, verbatim: "The actual values do not contain an apostrophe in the database. The apostrophes are either being added via excel, or through the export function. This ticket needs to go to engineering to review the export to file functionality."

## 4. Troubleshooting performed, and the limits of support access
Load side corrected on 8/27. Apostrophes stripped from 432 existing records and a rule added to ignore the character on load for EASFrequency and CCTVIPAddress. Support cannot inspect the export function's code path or confirm which export button ADUSA used, Manage Stores and Izenda are separate export paths and RCS-28161 already proved they behave differently. No AI assisted troubleshooting used beyond drafting this note.

## 5. Ruled out. Do not repeat
The database storing a corrupted value is ruled out. Ryan Barlow confirmed the stored values are clean.

## 6. Still open
1. Confirm ownership before this goes further. Ryan Barlow flagged this needs engineering review of the export function. Support has not yet confirmed with Delivery whether they already own this export path.
2. If Engineering owns it, please clone this into an ENG ticket and link it back here. Root cause has been narrowed since 9/1 with no defect ticket created yet.
3. Still requested from ADUSA, asked 9/1 and unanswered: confirm whether the exported file was opened in Excel, and attach the raw exported file as downloaded, without opening or saving it from Excel first.
4. Confirm which export button produced the file, Manage Stores or Izenda, since they are separate paths.

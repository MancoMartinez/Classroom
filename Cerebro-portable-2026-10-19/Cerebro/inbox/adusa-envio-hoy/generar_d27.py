#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el D27 (martes 29 sep 2026) a partir del D26. Verificado en Jira en vivo el 29 sep.

Cierres: RCS-28589 (Closed 9/25), RCS-29057 (Completed 9/25).
Pasan a Pending Ahold verification: RCS-29026, RCS-29042.
Estado corregido: RCS-28667 Work in progress (Juan), RCS-28683 Accepted into Development (Shandana),
RCS-29059 Work in progress (Vedant).
Nuevos: RCS-27077, RCS-29063, RCS-29108, RCS-29123, RCS-29131, RCS-29163, RCS-29164.
Fuera: RCS-29105 es interno de Appriss (S3), no va al cliente.
El resumen se recalcula desde el detalle.
"""
import sys, os, re, math, datetime
from copy import copy
import openpyxl
from openpyxl.styles import PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEN = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "Appriss ADUSA-Support-Tracker - 09222026 D26.xlsx")
DESTINO = os.path.join(AQUI, "Appriss ADUSA-Support-Tracker - 09302026 D27.xlsx")
FILL = {"Resolved": "FF7DE2DD", "Active with Appriss": "FFFBC521",
        "Awaiting Ahold input": "FF7C6BE8", "Pending Ahold verification": "FF528DF5"}
BLANCO, BANDA = "FFFFFFFF", "FFF4F6F9"
D = lambda m, d: datetime.datetime(2026, m, d)
WID = {8: 45, 9: 47, 10: 29, 2: 28}

wb = openpyxl.load_workbook(ORIGEN)
ws = wb["Support tracker"]

def need(k):
    for r in range(1, ws.max_row + 1):
        if str(ws.cell(row=r, column=1).value or "").strip() == k:
            return r
    sys.exit("No encontre " + k)

def categoria(r, cat):
    c = ws.cell(row=r, column=4); c.value = cat
    c.fill = PatternFill(fill_type="solid", fgColor=FILL[cat])

def anexa(r, *lineas):
    c = ws.cell(row=r, column=10)
    c.value = (c.value or "") + "".join("\n" + l for l in lineas)

def alto(r):
    n = 1
    for col, w in WID.items():
        t = str(ws.cell(row=r, column=col).value or "")
        k = sum(max(1, math.ceil(len(p) / (w * 1.05))) for p in t.split("\n"))
        n = max(n, k)
    ws.row_dimensions[r].height = min(409, 15 * n + 10)

def bloque(nombre):
    hdr = next((r for r in range(21, ws.max_row + 1)
                if str(ws.cell(row=r, column=1).value or "").strip() == nombre), None)
    if hdr is None: sys.exit("No encontre el bloque " + nombre)
    ultima = hdr
    for r in range(hdr + 1, ws.max_row + 2):
        v = ws.cell(row=r, column=1).value
        if v and str(v).startswith("RCS-"): ultima = r
        elif v: break
    return ultima

def nueva(tema, vals):
    plantilla = bloque(tema); dest = plantilla + 1
    guard = [str(m) for m in list(ws.merged_cells.ranges) if m.min_row >= dest]
    for s in guard: ws.unmerge_cells(s)
    alturas = {r: d.height for r, d in ws.row_dimensions.items() if d.height is not None and r >= dest}
    ws.insert_rows(dest, amount=1)
    for s in guard:
        m = re.match(r"([A-Z]+)(\d+):([A-Z]+)(\d+)", s)
        ws.merge_cells("%s%d:%s%d" % (m.group(1), int(m.group(2)) + 1, m.group(3), int(m.group(4)) + 1))
    for r in sorted(alturas, reverse=True):
        ws.row_dimensions[r + 1].height = alturas[r]
    for c in range(1, 11):
        ws.cell(row=dest, column=c)._style = copy(ws.cell(row=plantilla, column=c)._style)
    fg = ws.cell(row=plantilla, column=1).fill.fgColor
    banda = BLANCO if (fg.rgb if fg.type == "rgb" else BLANCO) == BANDA else BANDA
    for c in range(1, 11):
        ws.cell(row=dest, column=c).fill = PatternFill(fill_type="solid", fgColor=FILL[vals[3]] if c == 4 else banda)
    for i, v in enumerate(vals, start=1):
        ws.cell(row=dest, column=i).value = v
    alto(dest)

def upd(k, estado=None, cat=None, asig=None, fecha=None, issue=None, nxt=None, notas=()):
    r = need(k)
    if estado: ws.cell(row=r, column=3).value = estado
    if cat: categoria(r, cat)
    if asig: ws.cell(row=r, column=5).value = asig
    if fecha: ws.cell(row=r, column=7).value = fecha
    if issue: ws.cell(row=r, column=8).value = issue
    if nxt: ws.cell(row=r, column=9).value = nxt
    if notas: anexa(r, *notas)
    alto(r)

ws["A3"] = ("Cadence: weekly tracker email until the open issues are resolved, plus checkpoint calls "
            "Tuesdays 2:30 PM ET and Thursdays 3:30 PM ET.")
ws["A2"] = "Status as of Wednesday, September 30, 2026. Ticket states verified directly against Jira."

# ---------------- cierres ----------------
upd("RCS-28589", "Closed", "Resolved", "Aimee Wadsworth", D(9, 25), nxt=(
    "The loading side was corrected earlier, with the apostrophes removed from the 432 affected records and a rule "
    "that ignores an apostrophe in EASFrequency and CCTVIPAddress on load. The export fix went out with the release "
    "on 9/24. Leigh Ann exported the Asheville/Spartanburg area to CSV the same day and confirmed the extra "
    "characters no longer appear. Closed in Jira as resolved on 9/25."),
    notas=("9/24/2026 - Extracted the Asheville/Spartanburg area through the CSV export. The additional characters are no longer visible.",
           "9/25/2026 - Closed in Jira as resolved."))

upd("RCS-29057", "Completed", "Resolved", fecha=D(9, 25), nxt=(
    "Ahold sent case 2026-Ahold Delhaize USA Services LLC-9999-278 on 9/23. On Identification Request cases the "
    "text sat in Synopsis, which the workbench notes does not print on the document. Appriss added the narrative box "
    "at the top of Report Narrative for Identification Request on 9/24, so the narrative prints on new cases. For an "
    "existing case, copying the Synopsis text into that top box and saving brings it through. Leigh Ann confirmed on "
    "9/25 that this is expected behaviour and the ticket closed the same day."),
    notas=("9/23/2026 - Case 2026-Ahold Delhaize USA Services LLC-9999-278.",
           "9/25/2026 - That makes perfect sense. The workbench states that Synopsis will not print on the document.",
           "9/25/2026 - Closed in Jira as resolved."))

# ---------------- pendientes de verificacion ----------------
upd("RCS-29042", "Under Customer Review", "Pending Ahold verification", fecha=D(9, 28), nxt=(
    "A damaged attachment entry on that case was breaking the tab. Appriss removed it and resynced the case's "
    "attachment count on 9/23, so the case does not need to be deleted or redone. Appriss asked Leigh Ann on 9/24, "
    "and again on 9/28, to open the attachments on 2026-FOOD LION, LLC-1586-2 and confirm they load."),
    notas=("9/24/2026 - Appriss corrected the attachment entry on the case and asked Ahold to confirm the tab opens.",))

upd("RCS-29026", "Under Customer Review", "Pending Ahold verification", fecha=D(9, 28), nxt=(
    "Smart Alert History on case 0619-27 showed the 10:12 AM Defrauded Customer alert addressed to the full list, "
    "including Dawn Hendry, storepayments and the Asset Protection divisional group. The recipient who still appeared "
    "came in through the store manager setting for store 0619, not through the alert list. From 9/24 alerts stopped "
    "going out for all Ahold cases, which is tracked on RCS-29123. With that fixed on 9/28, both alerts from the "
    "original report are going out again. Appriss asked Leigh Ann on 9/28 to confirm on her side before closing."),
    notas=("9/25/2026 - No alerts appear to be going out now for the Impersonation/Social Engineering case type.",
           "9/25/2026 - The first case found without an alert was around 4:20 PM on 9/24.",
           "9/28/2026 - Appriss confirmed both alerts from the original report are going out again and asked Ahold to confirm."))

# ---------------- activos con estado corregido ----------------
upd("RCS-28667", "Work in progress", "Active with Appriss", "Juan Martinez", D(9, 24), nxt=(
    "Appriss confirmed on 9/24 that assigning a hierarchy to a new user is an administrator step today. The platform "
    "does not assign one when the account is created, and the steps from Settings > Users > Hierarchies were sent "
    "with screenshots. Leigh Ann explained that access is requested through Ahold IT, granted by Brand/Division, and "
    "that users only authenticate through single sign-on with Azure provisioning, so a manual step per user does not "
    "fit Ahold's flow. Appriss engineering is working on a change so that sign-in assigns the store hierarchy "
    "from the store and banner values Ahold already sends, which removes the manual step. Until that is released, "
    "assigning the hierarchy from the Hierarchies tab unblocks a new user."),
    notas=("9/24/2026 - Appriss confirmed hierarchy assignment is an administrator step and sent the steps with screenshots.",
           "9/24/2026 - Users are provisioned by Brand/Division, not a single location or district, with a 4 to 6 hour sync. This has not been an issue until now. There has to be a better way.",
           "9/24/2026 - Our IT department requires that users only authenticate through the SSO process, through Azure provisioning.",
           "9/24/2026 - Appriss asked who on the Ahold IT team manages the Azure setup, to include them on the call."))

upd("RCS-28683", "Accepted into Development", "Active with Appriss", "Shandana Khan", D(9, 24), nxt=(
    "Appriss reproduced the same 404 error the customer sees. The page the system tries to load after adding an "
    "associate does not exist on the server, which points to a platform defect rather than a data or account issue. "
    "Engineering accepted the fix into development. The case itself is created when the error appears and nothing "
    "entered is lost: select Return to Home, open the new case from the workbench and continue there. Leigh Ann linked "
    "this on 9/16 to the same error on the Elevator Entrapment case type. RCS-29164, raised 9/29 on Hannaford cases, "
    "describes the same steps and error, and Appriss is reviewing it against this ticket."),
    notas=("9/24/2026 - Appriss confirmed the fix was accepted into development and shared the Return to Home workaround.",))

upd("RCS-28693", fecha=D(9, 15))

upd("RCS-29059", "Work in progress", "Active with Appriss", "Vedant Shirude", D(9, 23), nxt=(
    "Appriss took ownership on 9/23 and is investigating why the indicator no longer marks transactions that sit in an "
    "investigation. Ahold's screenshot from last month showing the indicator working on the Ahold instance helps "
    "narrow down when it stopped."))

upd("RCS-28824", fecha=D(9, 25), nxt=(
    "Appriss corrected the store profile and Becky confirmed the Week, Month, Quarter and Year tabs now return charts. "
    "Two points stay open. The cashier profile page returns no charts, and the area map has no store coordinates to "
    "draw on. Ahold confirmed on 9/17 that it sends a store and location file and no employee file, and that what it "
    "needs on the cashier page is for the refund, void and coupon charts to populate. Because those charts populated "
    "on the previous platform, Appriss moved the question on 9/25 to the team that owns the profile configuration."),
    notas=("9/25/2026 - Appriss moved the cashier profile question to the team that owns the profile configuration.",))

upd("RCS-28281", fecha=D(9, 24), nxt=(
    "Jacquelyn sent a minute by minute breakdown for the flagged dates on 9/24 while Becky was out. It matches what "
    "Appriss sees for 8/12, where no transactions arrived between about 8:29 PM and 10:19 PM Eastern. 8/22 and 8/25 "
    "show no gaps, and 8/19 and 8/20 show dips of about three minutes each. Appriss asked on 9/24 for the 8/12 TLOG "
    "data covering 8:29 PM through 10:19 PM to be resent, and whether Ahold wants the 8/19 and 8/20 dips included in "
    "the same resend. Appriss will confirm the 8/12 counts once the resend lands."),
    notas=("9/23/2026 - Becky is out of the office this week and will return on Monday, September 28.",
           "9/24/2026 - Minute by minute breakouts attached. 8/12 abnormally low from 8:29 to 8:38 PM and 8:49 to 8:59 PM, all transactions missing from 9 PM, missing from 10 PM through 10:19 PM. 8/19 drop from 4:26 to 4:28 PM. 8/20 drop from 12:27 to 12:29 PM. 8/22 and 8/25 no obvious abnormalities.",
           "9/24/2026 - Appriss asked for the 8/12 data from 8:29 PM to 10:19 PM to be resent."))

# ---------------- nuevos ----------------
nueva("Case entry and assignment", ["RCS-29108", "Reassigned user not notified, repeated emails on one case",
    "Work in progress", "Active with Appriss", "Vedant Shirude", D(9, 24), D(9, 25),
    "Erica Sacre received several emails about case 2026-Food Lion, LLC-1565-7 after it was assigned to her. She then "
    "assigned it to Stephanie Jenkins, who received no notification. Ahold has not heard of other users seeing this. "
    "Raised 9/24 with a screenshot.",
    "Appriss took ownership on 9/25 and is reviewing the reassignment notice and the repeated emails on that case "
    "separately, since each email comes from a different part of the platform.",
    "Ticket opened 9/24/2026\n9/24/2026 - Erica Sacre received various emails on the same case after she was assigned. "
    "Stephanie Jenkins did not receive any notification when the case was assigned to her."])

nueva("Case entry and assignment", ["RCS-29131", "Users unable to add items to a case",
    "Under Customer Review", "Awaiting Ahold input", "Vedant Shirude", D(9, 25), D(9, 28),
    "Users report they cannot add items to a case. Leigh Ann could add them from the workbench and is checking why it "
    "does not work inside the case itself. She also notes the item wording on the entry page differs from Items "
    "Involved on the workbench. Raised 9/25 with a screenshot and a video.",
    "The wording difference between the entry page and the workbench comes from how fields are set up per case type. "
    "To reproduce the failure and read the logs for it, Appriss asked on 9/28 for the case type and one case number "
    "where adding an item does not work.",
    "Ticket opened 9/25/2026\n9/25/2026 - Users are having issues adding items to a case. Adding from the workbench "
    "works. There is a difference in terminology between the entry pages and Items Involved on the workbench.\n"
    "9/28/2026 - Appriss asked for the case type and a sample case number."])

nueva("Case entry and assignment", ["RCS-29163", "Add Merchandise button not responding on a shoplifting case",
    "Under Support Review", "Active with Appriss", "Unassigned", D(9, 29), D(9, 29),
    "Marcus Banks cannot add merchandise to shoplifting case 2026-THE STOP & SHOP SUPERMARKET COMPANY LLC-0851-88. "
    "The button does not respond when clicked. Raised 9/29.",
    "Open with Appriss. Raised on 9/29 and under support review. Appriss is reviewing it alongside RCS-29131, which "
    "also concerns adding items to a case.",
    "Ticket opened 9/29/2026\n9/29/2026 - Marcus Banks is unable to click the button to add merchandise. The button "
    "is not responding."])

nueva("Case entry and assignment", ["RCS-29164", "Error when adding an additional subject to a case",
    "Under Support Review", "Active with Appriss", "Unassigned", D(9, 29), D(9, 29),
    "Eric Hanson receives an error screen after completing a case on the workbench and clicking Add to enter an "
    "additional subject. He selects Return Home and edits the second entry page to add the suspect's information. "
    "Examples 2026-HANNAFORD BROS. CO., LLC 8377-136 and 8377-137. Raised 9/29.",
    "Open with Appriss. The steps and the error match RCS-28683, which engineering already accepted into development, "
    "and Appriss is reviewing it against that ticket. The Return Home workaround on RCS-28683 applies here as well.",
    "Ticket opened 9/29/2026\n9/29/2026 - Error when adding an additional subject after clicking Add on the workbench. "
    "The user returns home and edits the second entry page to add the suspect's information."])

nueva("Platform configuration and notifications", ["RCS-29123", "Smart Alerts not going out",
    "Under Customer Review", "Pending Ahold verification", "Juan Martinez", D(9, 25), D(9, 28),
    "Smart Alerts stopped going out for Ahold cases. Leigh Ann confirmed on 9/25 that Defrauded Customer and "
    "Shoplifting cases entered that day sent no alerts, and noted the risk of not notifying the right people if "
    "something major happened. Jim flagged it as a significant operational issue the same evening. Raised 9/25.",
    "Alert runs for Ahold stopped completing on 9/24 at about 7:06 AM Eastern. Appriss traced it to a recent code "
    "change that caused the alert process to lock up, and deployed a fix on 9/28. On 9/27 Appriss sent the alerts "
    "for nine affected cases by hand. Jim confirmed alerts arriving again from about 2:30 PM on 9/28. As Jim asked, the "
    "fix works going forward, so alerts missed between 9/24 and the fix are not resent. Appriss will close once Ahold "
    "confirms nothing else is missing.",
    "Ticket opened 9/25/2026\n9/25/2026 - Smart Alerts are not going out today. Defrauded Customer and Shoplifting "
    "incidents are not generating any alerts.\n9/25/2026 - Any updates? It is becoming a significant operational issue "
    "not having them working.\n9/27/2026 - Alerts for nine affected cases sent manually.\n9/28/2026 - Fix deployed. "
    "Alerts confirmed arriving from about 2:30 PM."])

nueva("Transaction, tender and POS data", ["RCS-27077", "New tender types for Delhaize",
    "Under Customer Review", "Pending Ahold verification", "Nikita Rathore", D(5, 26), D(9, 24),
    "Ahold requested new tender types to support new benefit card acceptance. On 9/23 the request was split by "
    "banner: the Delhaize tender types continue here and the Ahold ones moved to RCS-29063.",
    "Appriss added the two new Delhaize tender types and loaded the 9/17 files to the test environment for "
    "validation. The tender type change went to production on 9/24, and the 9/24 data was loaded to the test "
    "environment. Appriss asked Rodney to verify the Delhaize tender types on his side.",
    "9/23/2026 - We are checking the data. We assume no changes were needed to the data load process for the "
    "alphanumeric cashier ID.\n9/23/2026 - What fix was needed, how soon will it be in production, were there issues "
    "loading the data, and was it loaded for both Ahold and Delhaize?\n9/24/2026 - Were you able to load any Delhaize "
    "files sent after September 17?\n9/24/2026 - Appriss confirmed the tender types are in production and asked Ahold "
    "to verify."])

nueva("Transaction, tender and POS data", ["RCS-29063", "New tender types for Ahold",
    "Under Delivery Review", "Active with Appriss", "Andres Esteban", D(9, 23), D(9, 29),
    "Ahold needs two new tender types for new benefit card acceptance at brick and mortar stores: 97 for FIS "
    "transactions and 98 for Evermore transactions. Split from RCS-27077 on 9/23.",
    "Tender type 97 is ready to add. Code 98 is already used inside the Ahold data load for cash change records, so "
    "Appriss first moves those records to a new reserved code, 93, so they are not labelled as Evermore. That change "
    "and the 98 relabel go out together. Nothing is needed from Ahold at this point.",
    "Ticket opened 9/23/2026"])


# ---------------- movimientos del 30 sep ----------------
upd("RCS-29059", "Work in progress", "Pending Ahold verification", fecha=D(9, 30), nxt=(
    "The indicator depends on a setting that shows the Associated mark for every investigation, not only the ones "
    "the user owns or has been shared. That setting was found switched off, and Appriss turned it back on for both "
    "the Delhaize and Ahold instances on 9/30. Appriss asked the team to confirm the indicator now shows correctly, "
    "and is still looking into how the setting came to be switched off."),
    notas=("9/30/2026 - The Associated flag should show that a transaction was already identified by another user, even when that investigation was not shared.",
           "9/30/2026 - Appriss turned the setting back on for Delhaize and Ahold and asked the team to verify."))

upd("RCS-29063", "Waiting for Software Release", "Active with Appriss", fecha=D(9, 30), nxt=(
    "Code 98 was already used inside the Ahold data load for cash change records, so Appriss moved those records to a "
    "new reserved code, 93, before relabelling 98 as Evermore. Tender type 97 for FIS is added. Both new tender types "
    "are in the staging environment and are waiting for the software release, after which they will show on "
    "transactions. Nothing is needed from Ahold at this point."))

upd("RCS-28683", fecha=D(9, 30))

upd("RCS-28824", fecha=D(9, 30),
    notas=("9/30/2026 - Appriss is confirming with its data team whether the cashier profile charts depend on an employee file.",))

r = need("RCS-29163")
ws.cell(row=r, column=3).value = "Under Customer Review"; categoria(r, "Awaiting Ahold input")
ws.cell(row=r, column=5).value = "Diego Buelvas"; ws.cell(row=r, column=7).value = D(9, 30)
ws.cell(row=r, column=9).value = (
    "Appriss could not reproduce the button not responding on that case. On 9/30 Appriss asked for a screen recording "
    "or screenshots of the steps right before it stopped responding, including the browser window size and zoom, the "
    "browser Marcus uses, and whether he was adding a new item or editing an existing one.")
anexa(r, "9/30/2026 - Appriss asked for a recording of the steps, the browser and the window size used.")
alto(r)

r = need("RCS-29164")
ws.cell(row=r, column=3).value = "Work in progress"
ws.cell(row=r, column=5).value = "Edwin Garzon"
ws.cell(row=r, column=9).value = (
    "Jim confirmed on 9/29 the error was a 404, seen on 9/25 between 5:10 and 5:15 PM. That is the same error as "
    "RCS-28683, where the fix is in development, and Appriss is reviewing it against that ticket. The Return Home "
    "workaround on RCS-28683 applies here as well.")
anexa(r, "9/29/2026 - Error seen on 9/25 between 5:10 and 5:15 PM. Error Code 404.")
alto(r)


# ---------------- movimientos de la tarde del 30 sep ----------------
upd("RCS-28667", "Under Engineering Review", "Active with Appriss", "Shandana Khan", D(9, 30),
    notas=("9/30/2026 - Appriss confirmed engineering is working on a change so new users receive their store hierarchy when they sign in through Azure. No call needed for now. The Hierarchies tab remains the workaround.",))

nueva("Performance and timeouts", ["RCS-29202", "Systemwide slowness on the Delhaize instance",
    "Under Customer Review", "Pending Ahold verification", "Camila Cortes", D(9, 30), D(9, 30),
    "Becky reported intermittent slowness for all Delhaize users on 9/30.",
    "The platform had a temporary performance degradation on 9/30 that slowed page loading. Engineering addressed "
    "it the same day and Becky confirmed it seemed better. At her request the ticket stays open while both sides "
    "monitor, and Ahold will reply on the ticket if any user reports slowness again.",
    "Ticket opened 9/30/2026\n9/30/2026 - It does seem better now, but it was intermittent prior to opening the ticket. "
    "Let's leave this open for the day and continue to monitor."])

# ---------------- resumen recalculado ----------------
COLS = {"Resolved": 4, "Pending Ahold verification": 5, "Awaiting Ahold input": 6, "Active with Appriss": 7}
cuenta, tema = {}, None
for r in range(23, ws.max_row + 1):
    a = ws.cell(row=r, column=1).value
    if not a: continue
    if not str(a).startswith("RCS-"): tema = str(a).strip(); continue
    cuenta.setdefault(tema, {k: 0 for k in COLS})[ws.cell(row=r, column=4).value] += 1
for r in range(7, 18):
    t = ws.cell(row=r, column=1).value
    for k, c in COLS.items():
        ws.cell(row=r, column=c).value = cuenta.get(t, {}).get(k, 0)

wb.save(DESTINO)

# ---------------- verificacion ----------------
ws2 = openpyxl.load_workbook(DESTINO)["Support tracker"]
tot = [sum((ws2.cell(row=r, column=c).value or 0) for r in range(7, 18)) for c in (4, 5, 6, 7)]
print("Guardado:", os.path.basename(DESTINO))
print("resueltos %d | pend verif %d | esperando Ahold %d | activos %d | total %d" % (*tot, sum(tot)))
claves = []
for r in range(23, ws2.max_row + 1):
    k = ws2.cell(row=r, column=1).value
    if k and str(k).startswith("RCS-"):
        claves.append(k)
        if ws2.cell(row=r, column=4).value != "Resolved":
            print("  fila %-4d %-10s %-26s %-27s %s" % (r, k, ws2.cell(row=r, column=3).value,
                  ws2.cell(row=r, column=4).value, ws2.cell(row=r, column=5).value))
d = sorted({k for k in claves if claves.count(k) > 1})
print("Filas:", len(claves), "| Duplicados:", d or "ninguno")

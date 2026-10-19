#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el D28 (viernes 9 oct 2026) a partir del D27 del 30 sep.

Primer tracker de la cadencia semanal anunciada a Jim el 9/30.
Periodo cubierto: 30 sep al 9 oct.

Verificado en Jira en vivo el 9 oct:
  Cierres (5):  RCS-29042, RCS-29059, RCS-29123, RCS-29163, RCS-29202
  Cambian de columna (3): RCS-29026 y RCS-27077 de Pending Ahold verification a
                          Active with Appriss; RCS-29131 cambia estado, sigue en
                          Awaiting Ahold input
  Nuevos (9):   RCS-29228, RCS-29234, RCS-29282, RCS-29285, RCS-29300,
                RCS-29315, RCS-29335, RCS-29355, RCS-29376
  Fuera por decision de Juan: RCS-29347, abierto por Appriss y en flujo de delivery,
  no lo reporto el cliente.
"""

import sys, os, re, datetime
from copy import copy
import openpyxl
from openpyxl.styles import PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEN = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    AQUI, "Appriss ADUSA-Support-Tracker - 09302026 D27.xlsx")
DESTINO = os.path.join(AQUI, "Appriss ADUSA-Support-Tracker - 10092026 D28.xlsx")
if not os.path.exists(ORIGEN):
    sys.exit("No encuentro el D27 en:\n  %s" % ORIGEN)

FILL = {"Resolved": "FF7DE2DD", "Active with Appriss": "FFFBC521",
        "Awaiting Ahold input": "FF7C6BE8", "Pending Ahold verification": "FF528DF5"}
BLANCO, BANDA = "FFFFFFFF", "FFF4F6F9"
def D(d): return datetime.datetime(2026, 10, d)

wb = openpyxl.load_workbook(ORIGEN)
ws = wb["Support tracker"]


def need(clave):
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if v and str(v).strip() == clave:
            return r
    sys.exit("No encontre %s. Revisa que el archivo sea el D27." % clave)


def categoria(r, cat):
    c = ws.cell(row=r, column=4); c.value = cat
    v = c.fill
    c.fill = PatternFill(fill_type=v.fill_type, fgColor=FILL[cat], bgColor=v.bgColor)


def anexa(r, linea):
    c = ws.cell(row=r, column=10)
    c.value = (c.value or "") + "\n" + linea


def bloque(nombre):
    hdr = None
    for r in range(21, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if v and str(v).strip() == nombre:
            hdr = r; break
    if hdr is None:
        sys.exit("No encontre el bloque '%s'." % nombre)
    ultima = hdr
    for r in range(hdr + 1, ws.max_row + 2):
        v = ws.cell(row=r, column=1).value
        if v and str(v).strip().startswith("RCS-"):
            ultima = r
        elif v:
            break
    return ultima


def nueva(nombre_tema, vals, alto):
    plantilla = bloque(nombre_tema)
    dest = plantilla + 1
    guardadas = [str(m) for m in list(ws.merged_cells.ranges) if m.min_row >= dest]
    for s in guardadas:
        ws.unmerge_cells(s)
    alturas = {r: d.height for r, d in ws.row_dimensions.items()
               if d.height is not None and r >= dest}
    ws.insert_rows(dest, amount=1)
    for s in guardadas:
        m = re.match(r"([A-Z]+)(\d+):([A-Z]+)(\d+)", s)
        ws.merge_cells("%s%d:%s%d" % (m.group(1), int(m.group(2)) + 1,
                                      m.group(3), int(m.group(4)) + 1))
    for r in sorted(alturas, reverse=True):
        ws.row_dimensions[r + 1].height = alturas[r]
    ws.row_dimensions[dest].height = alto
    for c in range(1, 11):
        ws.cell(row=dest, column=c)._style = copy(ws.cell(row=plantilla, column=c)._style)
    fg = ws.cell(row=plantilla, column=1).fill.fgColor
    previa = fg.rgb if fg.type == "rgb" else BLANCO
    banda = BLANCO if previa == BANDA else BANDA
    for c in range(1, 11):
        ws.cell(row=dest, column=c).fill = PatternFill(
            fill_type="solid", fgColor=FILL[vals[3]] if c == 4 else banda)
    for i, v in enumerate(vals, start=1):
        ws.cell(row=dest, column=i).value = v
    for c in (6, 7):
        ws.cell(row=dest, column=c).number_format = \
            ws.cell(row=plantilla, column=c).number_format


ws["A2"] = ("Status as of Friday, October 9, 2026. "
            "Ticket states verified directly against Jira.")

# ===================== CIERRES =====================

r = need("RCS-29042")
ws.cell(row=r, column=3).value = "Closed"
categoria(r, "Resolved")
ws.cell(row=r, column=7).value = D(5)
ws.cell(row=r, column=9).value = (
    "Appriss corrected the record behind that case and Leigh Ann confirmed on 10/5 that every "
    "attachment type on it opens correctly. The ticket closed the same day.")
anexa(r, "10/5/2026 - I went to the case and I was able to open all the attachment types within "
         "this case. It appears that the issue with this case is resolved.")
ws.row_dimensions[r].height = 190

r = need("RCS-29059")
ws.cell(row=r, column=3).value = "Completed"
categoria(r, "Resolved")
ws.cell(row=r, column=7).value = D(5)
ws.cell(row=r, column=9).value = (
    "The Associated indicator now marks transactions that sit in an investigation. Ahold validated "
    "it on 10/2 and confirmed on 10/5 that it shows correctly, and the ticket closed the same day.")
anexa(r, "10/5/2026 - Confirmed the Associated tab is showing correctly again.")
ws.row_dimensions[r].height = 280

r = need("RCS-29123")
ws.cell(row=r, column=3).value = "Completed"
categoria(r, "Resolved")
ws.cell(row=r, column=7).value = D(7)
ws.cell(row=r, column=9).value = (
    "Smart Alerts are generating again after the correction was deployed. Leigh Ann confirmed on "
    "10/7 that an alert from the previous day reached her inbox, and the ticket closed the same "
    "day.")
anexa(r, "10/7/2026 - Alert from yesterday shows as distributed to my email account, so it appears "
         "to be working.")
ws.row_dimensions[r].height = 235

r = need("RCS-29163")
ws.cell(row=r, column=3).value = "Closed"
categoria(r, "Resolved")
ws.cell(row=r, column=7).value = D(1)
ws.cell(row=r, column=9).value = (
    "The user is able to add items to an incident report again. Ahold confirmed on 10/1 that "
    "everything works, and the ticket closed the same day.")
anexa(r, "10/1/2026 - User has confirmed that everything is great and he is able to add items.")
ws.row_dimensions[r].height = 145

r = need("RCS-29202")
ws.cell(row=r, column=3).value = "Closed"
categoria(r, "Resolved")
ws.cell(row=r, column=7).value = D(1)
ws.cell(row=r, column=9).value = (
    "The slowness traced to the web application servers. Appriss restarted the instances that were "
    "failing and Becky confirmed on 10/1 that the system was stable again. The ticket closed the "
    "same day.")
anexa(r, "10/1/2026 - Confirmed the system is stable again on our side.")
ws.row_dimensions[r].height = 120

# ===================== CAMBIOS DE COLUMNA =====================

r = need("RCS-29026")
ws.cell(row=r, column=3).value = "Work in progress"
categoria(r, "Active with Appriss")
ws.cell(row=r, column=7).value = D(9)
ws.cell(row=r, column=9).value = (
    "The alert for that case did not reach its recipients because one person appeared twice on the "
    "distribution, once on the alert's own email list and once through their store role, with the "
    "two addresses written differently. Appriss reviewed every alert sent this year for the same "
    "pattern and shared on 10/9 the other cases where it appears. Ahold explained how addresses "
    "are added to a distribution list, and both sides agree that keeping each person in one place "
    "only is the way to avoid it. Appriss is working through the remaining lists.")
anexa(r, "10/9/2026 - Appriss shared the other alerts where the same duplicate recipient pattern "
         "appears, and both sides agreed on keeping each person in a single place on the list.")
ws.row_dimensions[r].height = 355

r = need("RCS-27077")
ws.cell(row=r, column=3).value = "Work in progress"
categoria(r, "Active with Appriss")
ws.cell(row=r, column=7).value = D(9)
ws.cell(row=r, column=9).value = (
    "The Delhaize side of this request is resolved and deployed, and all September and October "
    "test files were loaded by 10/7. Ahold sent the Ahold data on 10/8 for the same change and "
    "Appriss is loading it. Appriss suggested on 10/9 tracking the Ahold requirements on a "
    "separate ticket so that side can move without holding this one.")
anexa(r, "10/8/2026 - Ahold data sent for testing, covering 8/29 through 10/8.")
anexa(r, "10/9/2026 - Appriss suggested tracking the Ahold requirements separately so each side "
         "can progress on its own.")
ws.row_dimensions[r].height = 250

r = need("RCS-29131")
ws.cell(row=r, column=3).value = "Work in progress"
ws.cell(row=r, column=7).value = D(8)
ws.cell(row=r, column=9).value = (
    "The same user can add items to a case from another computer and from a tablet using the same "
    "browser, which points to something on that one machine rather than to the account or the "
    "case. Appriss sent the steps to try on 10/8 and Ahold passed them to the user. Appriss is "
    "waiting on what the user reports back.")
anexa(r, "10/8/2026 - Information sent to the user to try the recommendations, and the user has "
         "been asked to report back.")
ws.row_dimensions[r].height = 175

# ===================== NUEVOS =====================

nueva("Login and access", [
    "RCS-29315", "User cannot get past the sign in screen",
    "Work in progress", "Active with Appriss", "Megha Rathi", D(7), D(9),
    "A Central Station operator reaches the sign in screen and cannot get any further. The page "
    "refreshes and stays where it is, with no error message, and the user does not appear as "
    "logged in. Raised 10/7.",
    "Appriss searched the user list by name and by email address and found no account. Appriss "
    "asked for the link used, the access level and the time of the attempt, and Ahold sent those "
    "on 10/9. Appriss is working from that detail.",
    "Ticket opened 10/7/2026\n10/7/2026 - She reaches the sign in screen and cannot get any "
    "further.\n10/9/2026 - Link and access level sent. She does not get an error message, the page "
    "refreshes and stays there.",
], 150)

nueva("Login and access", [
    "RCS-29376", "Reset Password option visible on the Admin users screen",
    "Under Engineering Review", "Active with Appriss", "Shandana Khan", D(9), D(9),
    "Reset Password appears as an option on the Admin users screen. Ahold authenticates through "
    "SSO and asks that the option not be available there, and wants to know whether it is visible "
    "anywhere else. Raised 10/9.",
    "Appriss took the ticket on 10/9 and passed it to engineering for review. Appriss will come "
    "back on where the option appears and what can be done about it.",
    "Ticket opened 10/9/2026\n10/9/2026 - Reset Password is an option on the Admin users screen. "
    "We authenticate by SSO, so this does not need to be there, and we do not want anyone able to "
    "change it wherever else it may be visible.",
], 150)

nueva("User accounts and duplicates", [
    "RCS-29282", "User with two hierarchies cannot create a case",
    "Closed", "Resolved", "Diego Buelvas", D(5), D(6),
    "A user with access to two hierarchies could not get past the select incident type screen when "
    "creating a report. Ahold confirmed the user should hold one profile only and asked whether "
    "other accounts are in the same state. Raised 10/5.",
    "Appriss corrected the account so the user holds a single hierarchy, and Ahold confirmed on "
    "10/6 that the user can create cases again. The ticket closed the same day.",
    "Ticket opened 10/5/2026\n10/5/2026 - The user cannot get past the select incident type screen. "
    "He should only have one profile.\n10/6/2026 - Confirmed resolved on our side.",
], 150)

nueva("Attachments and file handling", [
    "RCS-29335", "Forbidden message when attaching photos from one phone model",
    "Closed", "Resolved", "Diego Buelvas", D(7), D(8),
    "A user could not upload photos taken on one model of phone and received a forbidden message, "
    "while photos from other phones uploaded without trouble. Raised 10/7.",
    "Appriss came back with what was behind the message and what the user can do about it, and "
    "Ahold asked on 10/8 to close the ticket.",
    "Ticket opened 10/7/2026\n10/7/2026 - Anytime I try to upload pictures taken with this phone "
    "into LPMS it says forbidden. Pictures from a different phone upload without issue.\n"
    "10/8/2026 - Please close this ticket.",
], 150)

nueva("Reporting and exports", [
    "RCS-29285", "Bulk export appeared to return only one day of a date range",
    "Closed", "Resolved", "Diego Buelvas", D(5), D(5),
    "A bulk export of a saved search run over a four day range appeared to contain only the most "
    "recent day, while running the individual days returned data. Raised 10/5.",
    "Appriss reviewed the export and confirmed it carries the full range. The dates in the file "
    "are held as text, so filtering on that column in the spreadsheet does not list every value. "
    "Ahold confirmed the same day and the ticket closed.",
    "Ticket opened 10/5/2026\n10/5/2026 - A bulk export for 10/2 to 10/5 appears to include only "
    "10/4.\n10/5/2026 - Confirmed the export is correct. The end date is formatted as text, so the "
    "filter did not show all values.",
], 165)

nueva("Case entry and assignment", [
    "RCS-29234", "Cases not saving and entered data lost",
    "Accepted into Development", "Active with Appriss", "Shandana Khan", D(1), D(8),
    "After entering data into a case and clicking Save, the system stalled, returned to the case "
    "screen and lost everything entered. It affected many users across many case types. Raised "
    "10/1.",
    "The application was restored on 10/2 and no further reports have come in on the ticket since. "
    "Engineering accepted the case into development and confirmed on 10/8 that cases save without "
    "problems in the test environment. Appriss will update this ticket as that work progresses.",
    "Ticket opened 10/1/2026\n10/1/2026 - After entering data into a case, clicking Save stalls and "
    "returns to the case screen with all entered data deleted. Many users and many case types.\n"
    "10/6/2026 - Appriss confirmed the application was restored and no new reports had come in.",
], 165)

nueva("Transaction, tender and POS data", [
    "RCS-29228", "One tender type no longer appearing in reporting",
    "Closed", "Resolved", "Luis Hernandez", D(1), D(6),
    "Ahold saw a sharp decline in the use of one tender type in its reporting and asked Appriss to "
    "check the transaction data for a sample receipt to confirm whether that tender was present in "
    "what Ahold sends. Raised 10/1.",
    "Appriss reviewed the transaction data for the sample Ahold provided. Ahold's own POS team "
    "confirmed on 10/6 that the cause sits on their side and asked to close the ticket.",
    "Ticket opened 10/1/2026\n10/1/2026 - Sharp decline in usage of this tender type. Please review "
    "the transaction data for this receipt.\n10/6/2026 - Our POS team has confirmed the issue is on "
    "their end, so we can close this ticket.",
], 165)

nueva("Transaction, tender and POS data", [
    "RCS-29300", "Item order on receipts does not match the order items were scanned",
    "Under Customer Review", "Awaiting Ahold input", "Megha Rathi", D(6), D(9),
    "A user reported that the order of items on a receipt does not match the order on video. "
    "Sorting the transaction by item record date time lines up with the video, while the sequence "
    "on the receipt does not match either the audit tab or the item record sequence order. Raised "
    "10/6 with a sample transaction.",
    "Appriss checked the sample and then the source file for that trading day. The receipt follows "
    "the item sequence number and the audit tab follows scan time, and the two differ because the "
    "sequence numbers in the file arrive out of scan order. The same pattern appears on 392 "
    "tickets across 54 stores in that one file, so no further samples are needed. Appriss shared "
    "the findings on 10/9 for Ahold to review with the team that produces the file.",
    "Ticket opened 10/6/2026\n10/6/2026 - The item sequence on the receipt does not match the audit "
    "tab or the item record sequence order, while the date time sort matches the video.\n"
    "10/9/2026 - Appriss confirmed the sequence numbers arrive out of scan order in the source "
    "file, on 392 tickets across 54 stores for that day.",
], 190)

nueva("Transaction, tender and POS data", [
    "RCS-29355", "Data load requested for files with no regular delivery route",
    "Under Support Review", "Active with Appriss", "Edwin Garzon", D(8), D(9),
    "Ahold supplied two sets of files that have no standard delivery route to the intake server "
    "yet, and asked that they be loaded into the Delhaize instance. The transactions relate to "
    "receipts covered by data that already arrives on the normal route. Raised 10/8.",
    "Appriss took the ticket on 10/9 and is reviewing what is needed to load the supplied files. "
    "Appriss will come back with the outcome of that load.",
    "Ticket opened 10/8/2026\n10/8/2026 - These files do not currently have a standard data flow to "
    "the intake server, so they are being provided here until we do.",
], 150)

# ===================== RESUMEN =====================

def fres(nombre):
    for r in range(7, 18):
        if ws.cell(row=r, column=1).value == nombre:
            return r
    sys.exit("No encontre '%s' en el resumen." % nombre)

#                                           D   E   F   G
objetivo = {
 "Login and access":                        (4, 0, 0, 3),
 "User accounts and duplicates":            (6, 0, 0, 0),
 "Store and brand restrictions":            (8, 0, 0, 1),
 "Case entry and assignment":              (11, 0, 1, 5),
 "Attachments and file handling":           (5, 0, 0, 0),
 "Reporting and exports":                   (7, 0, 0, 2),
 "Performance and timeouts":                (5, 0, 0, 0),
 "Platform configuration and notifications":(4, 0, 0, 1),
 "Store file and location data":            (4, 0, 0, 0),
 "Transaction, tender and POS data":        (4, 0, 2, 3),
 "Change requests and scoping":             (1, 0, 0, 0),
}
for tema, (d, e, f, g) in objetivo.items():
    r = fres(tema)
    ws.cell(row=r, column=4).value = d
    ws.cell(row=r, column=5).value = e
    ws.cell(row=r, column=6).value = f
    ws.cell(row=r, column=7).value = g

wb.save(DESTINO)

# ===================== VERIFICACION =====================
ws2 = openpyxl.load_workbook(DESTINO)["Support tracker"]
print("\nGuardado:", os.path.basename(DESTINO)); print(ws2["A2"].value, "\n")
tot = [0, 0, 0, 0]
for r in range(7, 18):
    for i, c in enumerate((4, 5, 6, 7)):
        tot[i] += ws2.cell(row=r, column=c).value or 0
print("resueltos %d | pend verif %d | esperando Ahold %d | activos %d | total %d"
      % (tot[0], tot[1], tot[2], tot[3], sum(tot)))

esp = {
 "RCS-28693": ("Under Engineering Review",     "Active with Appriss"),
 "RCS-29315": ("Work in progress",             "Active with Appriss"),
 "RCS-29376": ("Under Engineering Review",     "Active with Appriss"),
 "RCS-28667": ("Under Engineering Review",     "Active with Appriss"),
 "RCS-28683": ("Accepted into Development",    "Active with Appriss"),
 "RCS-28849": ("Accepted into Development",    "Active with Appriss"),
 "RCS-29108": ("Work in progress",             "Active with Appriss"),
 "RCS-29131": ("Work in progress",             "Awaiting Ahold input"),
 "RCS-29164": ("Work in progress",             "Active with Appriss"),
 "RCS-29234": ("Accepted into Development",    "Active with Appriss"),
 "RCS-28824": ("Work in progress",             "Active with Appriss"),
 "RCS-29000": ("Accepted into Development",    "Active with Appriss"),
 "RCS-29026": ("Work in progress",             "Active with Appriss"),
 "RCS-28281": ("Under Customer Review",        "Awaiting Ahold input"),
 "RCS-27077": ("Work in progress",             "Active with Appriss"),
 "RCS-29063": ("Waiting for Software Release", "Active with Appriss"),
 "RCS-29300": ("Under Customer Review",        "Awaiting Ahold input"),
 "RCS-29355": ("Under Support Review",         "Active with Appriss"),
}
cerrados_hoy = ["RCS-29042", "RCS-29059", "RCS-29123", "RCS-29163", "RCS-29202",
                "RCS-29228", "RCS-29282", "RCS-29285", "RCS-29335"]
ok, vistos, claves = True, set(), []
print("\nAbiertos:")
for r in range(21, ws2.max_row + 1):
    k = ws2.cell(row=r, column=1).value
    if not (k and str(k).startswith("RCS-")):
        continue
    claves.append(k)
    cat = ws2.cell(row=r, column=4).value
    if cat == "Resolved":
        continue
    est = ws2.cell(row=r, column=3).value
    vistos.add(k)
    mal = k in esp and (est, cat) != esp[k]
    ok = ok and not mal
    print("  %s fila %-4d %-11s %-28s %-27s %s" % (
        "!!" if mal else "  ", r, k, est, cat, ws2.cell(row=r, column=5).value))
if set(esp) - vistos:
    ok = False; print("\nFaltan abiertos:", ", ".join(sorted(set(esp) - vistos)))
if vistos - set(esp):
    ok = False; print("\nAbiertos inesperados:", ", ".join(sorted(vistos - set(esp))))
print("\nCerrados en el periodo:")
for k in cerrados_hoy:
    for r in range(21, ws2.max_row + 1):
        if str(ws2.cell(row=r, column=1).value).strip() == k:
            c4 = ws2.cell(row=r, column=4)
            bien = c4.value == "Resolved" and c4.fill.fgColor.rgb == FILL["Resolved"]
            ok = ok and bien
            print("  %s fila %-4d %-11s %-11s %-9s fill=%s" % (
                "  " if bien else "!!", r, k, ws2.cell(row=r, column=3).value,
                c4.value, c4.fill.fgColor.rgb))
            break
    else:
        ok = False; print("  !! %s no esta en el documento" % k)
if sum(tot) != 77 or tot[0] != 59:
    ok = False; print("\nTotales mal, deberian ser 77 y 59 resueltos.")
d = sorted({k for k in claves if claves.count(k) > 1})
if d:
    ok = False; print("\nDuplicados:", ", ".join(d))
print("\ntickets en el documento: %d" % len(claves))
print("\n" + ("Todo cuadra." if ok else "Revisa lo marcado."))

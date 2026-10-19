#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el D26 (martes 22 sep 2026) a partir del D25.

D23 el jueves 17, D24 el viernes 18, D25 el lunes 21, D26 el martes 22.

Verificado en Jira en vivo:
  RCS-29042  nuevo, Leigh Ann Stubbs 9/22, bloque Attachments and file handling
  RCS-29057  nuevo, Leigh Ann Stubbs 9/22, bloque Reporting and exports, Awaiting Ahold input
  RCS-29059  nuevo, Teresa Coughenour 9/22, bloque Case entry and assignment
  RCS-29000  Under Engineering Review a Accepted into Development, 9/22 11:14
  RCS-28824  acuse de Appriss a Becky el 9/22 14:16, sin cambio de estado
  RCS-28281  seguimiento real de Juan el 9/22 20:29, sin cambio de estado
  RCS-29026  asignado a Juan Martinez el 9/21 20:51, sin comentario nuevo al cliente
  Los otros cuatro sin cambio.
"""

import sys, os, re, datetime
from copy import copy
import openpyxl
from openpyxl.styles import PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEN = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    AQUI, "Appriss ADUSA-Support-Tracker - 09212026 D25.xlsx")
DESTINO = os.path.join(AQUI, "Appriss ADUSA-Support-Tracker - 09222026 D26.xlsx")
if not os.path.exists(ORIGEN):
    sys.exit("No encuentro el D25 en:\n  %s" % ORIGEN)

FILL = {"Resolved": "FF7DE2DD", "Active with Appriss": "FFFBC521",
        "Awaiting Ahold input": "FF7C6BE8", "Pending Ahold verification": "FF528DF5"}
BLANCO, BANDA, HOY = "FFFFFFFF", "FFF4F6F9", datetime.datetime(2026, 9, 22)

wb = openpyxl.load_workbook(ORIGEN)
ws = wb["Support tracker"]


def need(clave):
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if v and str(v).strip() == clave:
            return r
    sys.exit("No encontre %s. Revisa que el archivo sea el D25." % clave)


def categoria(r, cat):
    c = ws.cell(row=r, column=4); c.value = cat
    v = c.fill
    c.fill = PatternFill(fill_type=v.fill_type, fgColor=FILL[cat], bgColor=v.bgColor)


def anexa(r, linea):
    c = ws.cell(row=r, column=10)
    c.value = (c.value or "") + "\n" + linea


def bloque(nombre):
    hdr = None
    for r in range(23, ws.max_row + 1):
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


ws["A2"] = ("Status as of Tuesday, September 22, 2026. "
            "Ticket states verified directly against Jira.")

# ---------- RCS-29000, ingenieria lo acepta para desarrollo ----------
r = need("RCS-29000")
ws.cell(row=r, column=3).value = "Accepted into Development"
ws.cell(row=r, column=7).value = HOY
ws.cell(row=r, column=9).value = (
    "Appriss reproduced the behaviour on the report. Running the same saved search without "
    "changing it returns one or two of the four calculated percent columns without the two decimal "
    "setting, and the column that behaves that way changes between runs. The values themselves are "
    "arithmetically correct, what varies is how they are presented, and the grid and the export "
    "behave the same way column for column. Engineering accepted the case into development on "
    "9/22. Appriss will update this ticket as that work progresses.")
anexa(r, "9/22/2026 - Engineering accepted the case into development.")
ws.row_dimensions[r].height = 175

# ---------- RCS-28824, acuse a Becky, sin avance de estado ----------
r = need("RCS-28824")
ws.cell(row=r, column=7).value = HOY
anexa(r, "9/22/2026 - Appriss confirmed it is still working through the cashier profile charts and "
         "the area map with its data team.")
ws.row_dimensions[r].height = 180

# ---------- RCS-28281, seguimiento real ----------
r = need("RCS-28281")
ws.cell(row=r, column=7).value = HOY
ws.cell(row=r, column=9).value = (
    "Appriss posted the full count per trading day on 8/27. Ahold reported on 8/31 that a good "
    "deal of recovery had occurred, with two gaps left on its view, the 9 PM to 10 PM hour on "
    "8/12 and a handful of trading days sitting 100,000 to 200,000 transactions below average. "
    "Appriss asked Rodney on 9/7 to have Becky run the same 10 minute check she used on 8/20 "
    "against 8/11, 8/12, 8/19, 8/20, 8/22 and 8/25, so Appriss can confirm which batches still "
    "need resubmission. Appriss checked back on 9/17 and again on 9/22 to ask whether that check "
    "has been run for those dates.")
anexa(r, "9/22/2026 - Checking back on the ten minute check. Could you confirm whether it was run "
         "for the other flagged dates, the eleventh, twelfth, nineteenth, twentieth, twenty second "
         "and twenty fifth?")
ws.row_dimensions[r].height = 125

# ---------- RCS-29026, Appriss toma el ticket ----------
r = need("RCS-29026")
ws.cell(row=r, column=5).value = "Juan Martinez"

# ---------- RCS-29042, nuevo ----------
nueva("Attachments and file handling", [
    "RCS-29042",
    "Attachments tab returns an error on one case",
    "Under Support Review", "Active with Appriss", "Vedant Shirude", HOY, HOY,
    "Opening the attachments tab on case 2026-FOOD LION, LLC-1586-2 returns an error. The same tab "
    "opens correctly on a different case, so the behaviour looks specific to that case rather than "
    "to the tab itself. Ahold asks what is happening with that case number and whether the case "
    "should be deleted and redone. Raised 9/22 with a screenshot.",
    "Open with Appriss. Raised on 9/22 and under support review. Appriss took ownership the same "
    "day and is reviewing that case before advising whether anything needs to be redone.",
    "Ticket opened 9/22/2026\n9/22/2026 - The attachments tab returns an error on this case. A "
    "different case opens its attachments without trouble. What is going on with that case number, "
    "and should it be deleted and the case redone?",
], 150)

# ---------- RCS-29057, nuevo, esperando el numero de caso ----------
nueva("Reporting and exports", [
    "RCS-29057",
    "Narrative missing from the LP External Doc",
    "Under Customer Review", "Awaiting Ahold input", "Juan Martinez", HOY, HOY,
    "The narrative is not appearing on the LP External Doc. Ahold notes the same behaviour was "
    "addressed under RCS-22886 last year and appears to have returned. The ticket does not name a "
    "specific case. Raised 9/22.",
    "Appriss generated the document on two test cases of different case types on 9/22 and the "
    "narrative came through correctly on both, so the behaviour does not appear on a freshly "
    "generated document. Appriss asked Ahold the same day for the case number where the narrative "
    "is missing, and the case type if it is to hand, so that exact case can be opened and checked.",
    "Ticket opened 9/22/2026\n9/22/2026 - Narrative is missing from the LP External Doc. This was "
    "addressed under RCS-22886 last year and appears to be an issue again.\n9/22/2026 - Appriss "
    "asked for the case number where the narrative is not showing, so that case can be pulled up "
    "directly.",
], 165)

# ---------- RCS-29059, nuevo ----------
nueva("Case entry and assignment", [
    "RCS-29059",
    "Associated indicator not showing on the quick receipt",
    "Under Support Review", "Active with Appriss", "Unassigned", HOY, HOY,
    "The Associated indicator on the quick receipt is not marking transactions that already sit in "
    "an investigation. Ahold raised it while reviewing work items that appear to duplicate because "
    "of the date range behind them. Ahold reports the same behaviour on the Ahold instance and has "
    "an earlier screenshot showing the indicator working there. Raised 9/22 with a video.",
    "Open with Appriss. Raised on 9/22 and under support review. Appriss is picking up ownership "
    "and will confirm the next step.",
    "Ticket opened 9/22/2026\n9/22/2026 - A transaction that sits in an investigation is not "
    "indicated as Associated on the quick receipt. The same behaviour shows on the Ahold instance, "
    "and an earlier screenshot shows the indicator working there.",
], 165)

# ---------- resumen ----------
def fres(nombre):
    for r in range(7, 18):
        if ws.cell(row=r, column=1).value == nombre:
            return r
    sys.exit("No encontre '%s' en el resumen." % nombre)

ws.cell(row=fres("Case entry and assignment"), column=7).value = 3
ws.cell(row=fres("Attachments and file handling"), column=7).value = 1
ws.cell(row=fres("Reporting and exports"), column=6).value = 1

wb.save(DESTINO)

# ---------- verificacion ----------
ws2 = openpyxl.load_workbook(DESTINO)["Support tracker"]
print("\nGuardado:", os.path.basename(DESTINO)); print(ws2["A2"].value, "\n")
tot = [0, 0, 0, 0]
for r in range(7, 18):
    for i, c in enumerate((4, 5, 6, 7)):
        tot[i] += ws2.cell(row=r, column=c).value or 0
print("resueltos %d | pend verif %d | esperando Ahold %d | activos %d | total %d"
      % (tot[0], tot[1], tot[2], tot[3], sum(tot)))
esp = {"RCS-28693": ("Under Engineering Review",  "Active with Appriss"),
       "RCS-28667": ("Under Engineering Review",  "Active with Appriss"),
       "RCS-28683": ("Under Engineering Review",  "Active with Appriss"),
       "RCS-28849": ("Accepted into Development", "Active with Appriss"),
       "RCS-29059": ("Under Support Review",      "Active with Appriss"),
       "RCS-28824": ("Work in progress",          "Active with Appriss"),
       "RCS-29000": ("Accepted into Development", "Active with Appriss"),
       "RCS-29057": ("Under Customer Review",     "Awaiting Ahold input"),
       "RCS-29042": ("Under Support Review",      "Active with Appriss"),
       "RCS-29026": ("Under Support Review",      "Active with Appriss"),
       "RCS-28589": ("Accepted into Development", "Active with Appriss"),
       "RCS-28281": ("Under Customer Review",     "Awaiting Ahold input")}
ok, vistos, claves = True, set(), []
print("\nAbiertos:")
for r in range(23, ws2.max_row + 1):
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
    print("  %s fila %-4d %-11s %-26s %-27s %s" % (
        "!!" if mal else "  ", r, k, est, cat, ws2.cell(row=r, column=5).value))
if set(esp) - vistos:
    ok = False; print("\nFaltan:", ", ".join(sorted(set(esp) - vistos)))
if vistos - set(esp):
    ok = False; print("\nAbiertos inesperados:", ", ".join(sorted(vistos - set(esp))))
if sum(tot) != 60 or tot[0] != 48:
    ok = False; print("\nTotales mal, deberian ser 60 y 48 resueltos.")
d = sorted({k for k in claves if claves.count(k) > 1})
if d:
    ok = False; print("\nDuplicados:", ", ".join(d))
print("\n" + ("Todo cuadra." if ok else "Revisa lo marcado."))

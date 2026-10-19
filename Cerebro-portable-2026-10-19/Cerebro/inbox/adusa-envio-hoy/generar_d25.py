#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el D25 (lunes 21 sep 2026) a partir del D24.

D21 el 14, D22 el 15, D23 el jueves 17, D24 el viernes 18, D25 el lunes 21.

Verificado en Jira en vivo:
  RCS-29000  Under Support Review a Under Engineering Review, de Sebastian Rueda a Shandana Khan
  RCS-29026  nuevo, abierto por Leigh Ann Stubbs el 9/21, bloque Platform configuration and notifications
  RCS-28589  solo comentario espejo del ticket interno de ingenieria sobre QA. No se toca.
  RCS-28281  solo aviso automatico de 14 dias sin respuesta del cliente. No se toca.
  Los otros cuatro sin cambio.
"""

import sys, os, re, datetime
from copy import copy
import openpyxl
from openpyxl.styles import PatternFill

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEN = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    AQUI, "Appriss ADUSA-Support-Tracker - 09182026 D24.xlsx")
DESTINO = os.path.join(AQUI, "Appriss ADUSA-Support-Tracker - 09212026 D25.xlsx")
if not os.path.exists(ORIGEN):
    sys.exit("No encuentro el D24 en:\n  %s" % ORIGEN)

FILL = {"Resolved": "FF7DE2DD", "Active with Appriss": "FFFBC521",
        "Awaiting Ahold input": "FF7C6BE8", "Pending Ahold verification": "FF528DF5"}
BLANCO, BANDA, HOY = "FFFFFFFF", "FFF4F6F9", datetime.datetime(2026, 9, 21)

wb = openpyxl.load_workbook(ORIGEN)
ws = wb["Support tracker"]


def need(clave):
    for r in range(1, ws.max_row + 1):
        v = ws.cell(row=r, column=1).value
        if v and str(v).strip() == clave:
            return r
    sys.exit("No encontre %s. Revisa que el archivo sea el D24." % clave)


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


ws["A2"] = ("Status as of Monday, September 21, 2026. "
            "Ticket states verified directly against Jira.")

# ---------- RCS-29000, pasa a revision de ingenieria ----------
r = need("RCS-29000")
ws.cell(row=r, column=3).value = "Under Engineering Review"
ws.cell(row=r, column=5).value = "Shandana Khan"
ws.cell(row=r, column=7).value = HOY
ws.cell(row=r, column=9).value = (
    "Appriss reproduced the behaviour on the report. Running the same saved search without "
    "changing it returns one or two of the four calculated percent columns without the two decimal "
    "setting, and the column that behaves that way changes between runs. The values themselves are "
    "arithmetically correct, what varies is how they are presented, and the grid and the export "
    "behave the same way column for column. Appriss passed the case to its engineering team on "
    "9/21 for review and will update this ticket as that review progresses.")
anexa(r, "9/21/2026 - Appriss reproduced the behaviour across repeated runs of the unchanged "
         "search and passed the case to engineering for review.")
ws.row_dimensions[r].height = 165

# ---------- RCS-29026, nuevo ----------
nueva("Platform configuration and notifications", [
    "RCS-29026",
    "Smart Alert did not reach its recipients on a case",
    "Under Support Review", "Active with Appriss", "Unassigned", HOY, HOY,
    "A Smart Alert configured for a case type did not reach Asset Protection for case "
    "2026-FOOD LION, LLC-0619-27, which was keyed in on 9/20. Store Payments confirmed the alert "
    "did not arrive on that side either, and a recipient who is no longer on the distribution list "
    "for that case type still appears on the alert. Ahold notes this case carried a large loss and "
    "asks whether other alerts were due to fire and did not. Raised 9/21.",
    "Open with Appriss. Raised on 9/21 and under support review. Appriss is picking up ownership "
    "and will come back with what it finds on this case and on the recipient list.",
    "Ticket opened 9/21/2026\n9/21/2026 - Asset Protection did not receive the Smart Alert for "
    "this case, and Store Payments confirmed it did not arrive on their side either. A recipient "
    "who is no longer on the distribution list for this case type still appears on the alert. "
    "Are there any more that were supposed to fire off and did not?",
], 165)

# ---------- resumen ----------
def fres(nombre):
    for r in range(7, 18):
        if ws.cell(row=r, column=1).value == nombre:
            return r
    sys.exit("No encontre '%s' en el resumen." % nombre)

ws.cell(row=fres("Platform configuration and notifications"), column=7).value = 1

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
       "RCS-28824": ("Work in progress",          "Active with Appriss"),
       "RCS-29000": ("Under Engineering Review",  "Active with Appriss"),
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
    print("  %s fila %-4d %-11s %-26s %s" % ("!!" if mal else "  ", r, k, est, cat))
if set(esp) - vistos:
    ok = False; print("\nFaltan:", ", ".join(sorted(set(esp) - vistos)))
if vistos - set(esp):
    ok = False; print("\nAbiertos inesperados:", ", ".join(sorted(vistos - set(esp))))
if sum(tot) != 57 or tot[0] != 48:
    ok = False; print("\nTotales mal, deberian ser 57 y 48 resueltos.")
d = sorted({k for k in claves if claves.count(k) > 1})
if d:
    ok = False; print("\nDuplicados:", ", ".join(d))
print("\n" + ("Todo cuadra." if ok else "Revisa lo marcado."))

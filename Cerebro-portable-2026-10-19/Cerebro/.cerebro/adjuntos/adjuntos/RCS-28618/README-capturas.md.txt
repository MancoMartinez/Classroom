# Adjunto README-capturas.md
Ruta: adjuntos/RCS-28618/README-capturas.md
Tipo: md
Ticket: RCS-28618
Modificado: 2026-09-08

# RCS-28618 — adjuntos y qué muestra cada captura

Los cuatro PNG los subió Steve Curry a Jira el 27 ago 2026 07:33 EDT. Juan los pasó al chat el
31 ago 2026. Los binarios siguen en Jira. Aquí queda la descripción textual, que es lo buscable.

| Archivo en Jira | ID adjunto | Contenido |
|---|---|---|
| image-20260827-113050.png | 1412276 | Reporte propio de Walmart, "Return Audits" |
| image-20260827-113134.png | 1412279 | Composer, parámetros del quick link Refund Audit - Expired |
| image-20260827-113306.png | 1412277 | Composer, resultado 0 filas |
| image-20260827-113328.png | 1412278 | Panel Quick Links, familia Refund Audit |

## Captura 1. Reporte interno de Walmart, "Return Audits"

Título de la tabla: "Store Return Completion % by WM Week". Columnas: Store, Success, Fail,
Expired, Total Audit, %, WM Week, Year. Todas las filas son WM Week 27, año 2026.

| Store | Success | Fail | Expired | Total Audit | % |
|---|---|---|---|---|---|
| 5693 | 41 | 0 | 0 | 41 | 100.00% |
| 3111 | 26 | 2 | 2 | 30 | 93.33% |
| 2839 | 39 | 0 | 3 | 42 | 92.86% |
| 5791 | 25 | 0 | 2 | 27 | 92.59% |
| 4057 | 14 | 2 | 3 | 19 | 84.21% |
| 4478 | 42 | 0 | 8 | 50 | 84.00% |
| 5692 | 37 | 1 | 9 | 47 | 80.85% |
| 3238 | 51 | 10 | 16 | 77 | 79.22% |
| 7127 | 48 | 8 | 15 | 71 | 78.87% |
| 7072 | 27 | 2 | 11 | 40 | 72.50% |
| 3062 | 19 | 3 | 22 | 44 | 50.00% |
| 4470 | 12 | 3 | 36 | 51 | 29.41% |

Fila de totales: 538 / 381 / 31 / 127 / 539 / 76.44% / WM Week 27 / 2026. Los totales no cuadran
con la suma de las 12 filas visibles, así que la tabla está recortada o el total abarca más tiendas.
Pie de la captura, cortado: "Please follow up to failed & expired audits".

Este reporte no sale de Secure. Es el sistema interno de Walmart. Es la fuente de la afirmación
"los datos existen".

## Captura 2. Composer, parámetros

Breadcrumb: Portal > Secure Store > Explorer > Composer. Título "Results". Nombre del search:
"Refund Audit - Expired". Descripción: "Review your refund audit expired results by store number
for a given time period."

Dos parámetros, los dos marcados REQ en verde:

    REQ  EXT_INKIRU_RVA   Store No       Equal to   3238
    REQ  HEADER           Trading Day    Between    January 01 2026  and  August 27 2026

El prefijo del primer parámetro nombra la tabla del dataset externo, ext_inkiru_rva. El segundo
viene de HEADER, o sea ardm_header. Son dos entidades distintas, unidas por join.

## Captura 3. Composer, resultado

Mismo search. Pestaña Tabular activa. Contador: "0 results". Columnas de salida: Store No,
Audit Result, Nbr of Expired Audits. Cuerpo: "No Results Found".

No hay mensaje de error. La query corrió y devolvió cero filas. La columna Audit Result en la
salida confirma que audit_result es una condición o un agrupador del search, no un parámetro
que el usuario haya tocado.

## Captura 4. Panel Quick Links

Pestañas: Quick Links | Store Quick Lookups | Refund Audit. La tercera está activa. Siete entradas:

    Refund Audit
    Refund Audit - Conducted Own Audit
    Refund Audit Cashier - Fail
    Refund Audit Cashier - Fail - Item Missing
    Refund Audit Supervisor - Fail
    Refund Audit Supervisor - Fail - Item Missing
    Refund Audit - Expired

Esta lista es la base de la matriz de prueba. Cada entrada aísla un valor distinto de
audit_result y de audit_fail_reason sobre la misma tabla.

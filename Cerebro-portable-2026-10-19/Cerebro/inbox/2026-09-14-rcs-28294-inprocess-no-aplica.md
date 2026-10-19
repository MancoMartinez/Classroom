# RCS-28294 — InProcess no aplica, avance del Paso 0

## Que pasa

RCS-28294 (Vallarta) sigue en Work in progress. El UPDATE de InProcess que Matt le paso a Luis no
aplica aqui. Se corrio el Paso 0 del plan de reproduccion contra produccion.

## Causa

CONFIRMADA que InProcess no aplica. H1, frontera de fecha UTC, gana evidencia. HIPOTESIS aun, falta
el audit log crudo.

## Evidencia

1. RCS-28294 es sobre `2026-ADUP-40-96`, caso HR, sin fila en `incident.Shoplifting`.
2. `SELECT ... FROM incident.ChangeHistory WHERE CaseNo = '2026-ADUP-40-96'` da "Invalid column
   name" en las seis columnas. La tabla existe, el nombre de columnas usado no. Sin documentar en
   el cerebro.
3. Vianney Valdez, vvaldez@vallartasupermarkets.com, TimeZone `America/Los_Angeles` real, no UTC.
   LastLoginDate 2026-09-11, CreateDate 2026-07-30. Fuera del bucket de 308 cuentas Vallarta con
   TimeZone=UTC. El desfase de ocho horas entre reporte y Change History no viene de su cuenta.

## Que hago hoy

1. Corre esto para sacar los nombres reales de columnas antes de reintentar el SELECT:

       SELECT COLUMN_NAME, DATA_TYPE
       FROM INFORMATION_SCHEMA.COLUMNS
       WHERE TABLE_SCHEMA = 'incident' AND TABLE_NAME = 'ChangeHistory'
       ORDER BY ORDINAL_POSITION;

2. Con los nombres reales, reescribe el SELECT del audit log crudo de `2026-ADUP-40-96` y compara
   contra el PDF.
3. No corras ningun UPDATE en este ticket.

## Precedentes

- RCS-28465 y RCS-28534, Stater Bros, InProcess atascado, ENG-2819 —
  `brain/markdown/26-adusa-estado-tickets-reuniones.md`
- ENG-2819, Done, Kiran Vadday, causa distinta — `tickets/ENG-2819.md`

## Compromisos

Ninguno nuevo con el cliente. Pendiente interno: correr INFORMATION_SCHEMA, reescribir el SELECT
del ChangeHistory, cerrar H1 contra H2.

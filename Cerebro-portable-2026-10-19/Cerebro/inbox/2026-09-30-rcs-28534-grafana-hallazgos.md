# RCS-28534 Stater Bros, lectura de Grafana, 30 sep. Horas en UTC, Bogota = UTC-5

## Que pasa
205148 y 205157 son atascos reales, no filtro. Corrigen la nota anterior: el filtro de Discipline Request no mira CaseStatus, mira SUSPECT.DAYSOFFNOTES y CaseType.

## Causa
HIPOTESIS con evidencia fuerte. Las dos corridas se cuelgan en 12b "Finding attachments", antes de 13a. No es la firma del mecanismo 8, que se cuelga despues de 13a. Coincide con la hipotesis 4.7 de Diego, descarga de adjuntos del blob.

## Evidencia
205148, 24 sep: 15:51:53 6a Rows=1, 8, 8a, 11, 11d 15:52:03, 12b 15:52:04, sin 13a ni End. Quit desde 15:57 hasta 20:43.
205157, 24 sep: 19:31 6a Rows=0, DaysOffNotes vacio. 19:32 6a Rows=1, 8, 8a, 11, 11d, 12b 19:32:30, sin 13a. Quit 19:36.
Post fix: 13a y 13b pareados 99 de 100 desde 29 sep 16:56. Unico 13a sin 13b: 29 sep 23:10:37, Stater Bros. Investigation 129, 0 adjuntos.
HATR NettrackSmartAlertActivity 500: 17 veces el 28 sep entre 05:11 y 17:49, ninguna despues del deploy.
Quit desde 28 sep: 404 lineas, 200 IDs. 25 terminaron despues, 132 son un Quit suelto sin prueba, 35 empezaron antes del fix, 8 empezaron despues: 205264, 205376, 205356, 205296, 205378, 205462, 205158, 205171.
205367 y 205395: Quit desde antes del 29 sep, su corrida colgada es anterior. 205211 y 202901 sin lineas en la ventana.

## Que hago hoy
1. Por cada uno de los 8 post fix, rango 2026-09-27 00:00 a now: ver la ultima corrida antes del primer Quit, en que paso muere y a que hora.
2. Finding attachments y Ready to send email desde 2026-09-28 13:30 Bogota: parear 12b contra 13a.
3. Investigation 129, 29 sep 17:00 a 19:00 Bogota.
4. Si algun post fix muere en 12b despues del deploy, esa es la prueba para Kiran.

## Precedentes
inbox/2026-09-28-smart-alerts-mecanismo-8-deadlock.md
inbox/2026-09-28-grafana-smart-alerts-lectura.md

## Compromisos
Revisar con Diego. Responder a Kiran con caso, pasos y lineas.

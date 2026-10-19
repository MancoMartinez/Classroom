# RCS-28294 — Defecto B confirmado, Defecto A con evidencia fuerte

## Que pasa

Corrida completa contra `sqldb-prd-wus2-arp-production-432-vsa-platform`. La tabla real de
auditoria es `incident.CaseChanges`, no `ChangeHistory` en ningun esquema. Cambio de tabla
verificado por conteo de filas, `incident.ChangeHistory` da cero.

## Causa

Defecto B, render del modal Change History. CONFIRMADA.
Defecto A, frontera de fecha UTC. HIPOTESIS, evidencia fuerte, falta el log de disparo de la alerta.

## Evidencia

1. Primer `SAVE.CASE` crudo: `2026-08-10 23:23:43.000` UTC. El modal de Vianney Valdez lo pinto
   como `8/11/2026 12:23 AM`. Diferencia exacta: +1 hora sobre el crudo. Una conversion real a
   Pacific resta 7 horas, no suma 1.
2. El crudo 23:23:43 UTC del 10 ago coincide con el reporte de David, 4:23pm Pacific el mismo dia
   (16:23 PT + 7h = 23:23 UTC). El dato en base esta correcto, el defecto es solo el render.
3. Ese guardado cae 37 minutos antes de medianoche UTC. Si la ventana de Smart Alert corta por dia
   calendario UTC, el guardado de la tarde Pacific queda al filo y puede disparar en el batch del
   dia siguiente. Coincide con "trigger until the following day" de Tatiana.

## Que hago hoy

1. Escala Defecto B a Engineering como confirmado: el modal suma 1 hora al crudo UTC en vez de
   convertir a Pacific.
2. Antes de escalar Defecto A, corre el Paso 11 de `inbox/2026-08-25-rcs-28294-sql-changehistory.sql`,
   busca tabla de log de envio (`%Alert%`, `%Notif%`, `%Email%`, `%Queue%`) en esta misma base.
   Sin el evento real de disparo, H1 sigue siendo guardado, no envio.
3. No mandes los dos defectos juntos a Engineering, ya quedo escrito que asi rebota.

## Precedentes

Ninguno nuevo. Sigue vigente `investigaciones/smart-alerts-familia-de-fallas.md` #6.

## Compromisos

Ninguno nuevo con el cliente. Pendiente interno: correr el Paso 11 antes de la proxima escalacion.

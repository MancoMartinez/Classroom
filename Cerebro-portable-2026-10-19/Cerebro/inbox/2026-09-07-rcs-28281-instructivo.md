# RCS-28281. Instructivo

Runbook para desatorar el ticket. Ejecuta en orden. El detalle del razonamiento está en el informe que acompaña este archivo.

Revisión del 7 de septiembre. La búsqueda de una fuente propia para el análisis de 10 minutos terminó en dos tablas que no sirven, ver Paso 1. Juan decidió no esperar la respuesta de Nikita ni de Viraj para mover el ticket. El orden queda así, reasignación y comunicación al cliente primero, escalación interna solo si eso no destraba nada.

## Paso 1. Buscar una fuente propia para el análisis de 10 minutos. Cerrado, sin resultado

Dónde se ejecuta: Azure Bastion, SSMS, Managed Instance sqlmi-prd-wus2-arp-001.
Lectura. Solo SELECT. Ya ejecutado.

Primer intento, listar tablas con nombre reconocible en la base de tenant de Ahold. El código corto real es dai, no adusa como decía la ficha en `brain/memoria/project_adusa_ficha_y_tickets.md`, que queda corregida en ese punto.

```
SELECT TOP 50 TABLE_NAME
FROM [sqldb-prd-wus2-arp-production-441-dai-platform].INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%trans%' OR TABLE_NAME LIKE '%tlog%';
```

Resultado: cuatro tablas, WireTransfer, Translation, TransmissionReport y Transactions.

Segundo intento, columnas de Transactions.

```
SELECT COLUMN_NAME, DATA_TYPE
FROM [sqldb-prd-wus2-arp-production-441-dai-platform].INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Transactions'
ORDER BY ORDINAL_POSITION;
```

Resultado: FtiID, TileID, EventID, CreatedDateTime, EventSummary, SourceApp. Tabla de eventos de aplicación, sin Store No ni Ticket No, no es transacción POS.

Tercer intento, columnas de TransmissionReport.

```
SELECT COLUMN_NAME, DATA_TYPE
FROM [sqldb-prd-wus2-arp-production-441-dai-platform].INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'TransmissionReport'
ORDER BY ORDINAL_POSITION;
```

Resultado: Division, Region, District, StoreDescription, TransmissionDate, TransmissionStatus, IncidentType, SuspectID, CaseNo, ShopliftingId, RestitutionTransmit, TotalStolen. Transmisión de casos de Incident, shoplifting y restitución, no transmisión de archivos TLOG.

Conclusión verificada con dos tablas distintas: la base de tenant sirve al módulo Incident, no a Secure 5.4. No hay más que probar ahí con Bastion y SSMS. Juan no tiene en esta sesión una fuente propia para el análisis de 10 minutos. No sigas buscando tablas nuevas en esta base.

## Paso 2. Reasignarse el ticket

Dónde se ejecuta: Jira, campo Assignee de RCS-28281.
Escritura. Autoriza Juan Martinez, lo ejecuta Juan Martinez.

Que hace este paso: pone el ticket a nombre de quien de hecho lo trabaja desde el 18 de agosto. No requiere acuerdo previo con Nikita, es un cambio de campo, no una decisión compartida.

Que se espera ver: Assignee cambia a Juan Martinez.

Si falla: si el flujo de Jira exige que Nikita libere el ticket primero, avísale por Teams que lo tomaste de vuelta, sin pedir permiso, como aviso.

## Paso 3. Actualizar al cliente con el pedido invertido

Dónde se ejecuta: Jira, comentario en RCS-28281.
Escritura. Autoriza Juan Martinez, lo pega Juan Martinez.

Que hace este paso: rompe el silencio de siete días sin repetir la promesa de conteos que ya falló el 19 y el 26 de agosto, y le devuelve el trabajo de campo a quien ya demostró tener el acceso que a Appriss le falta. Becky revisó a mano el bloque de 6 a 8 PM del 20 de agosto y encontró actividad de aproximadamente una transacción por minuto. Ese nivel de detalle no está disponible del lado de Appriss según el Paso 1. Pedirle a Becky que repita ese chequeo en las demás fechas marcadas es la vía más rápida que queda.

```
Hi Rodney,

Reassigning this to myself to keep it moving.

I reviewed our tenant database for a transaction level log that would let us break down the flagged dates into 10 minute blocks. It does not hold POS transaction data at that granularity on our side.

Becky's manual check on 8/20 between 6 and 8 PM already showed transaction activity at roughly one per minute in a window we had flagged as low. If Becky can run that same check for the other flagged dates, 8/11, 8/12, 8/19, 8/20, 8/22 and 8/25, that tells us directly which windows are real gaps versus counts that landed on a later trading day. Send us what she finds and we take it from there on batches that need resubmission.

Thank you.
```

Que se espera ver: el comentario se publica sin generar una nueva fecha comprometida de parte de Appriss, y devuelve la pelota a un dato que el cliente ya probó que puede producir.

Si falla: no aplica, este paso no depende de un sistema externo.

## Paso 4. Escalar a Viraj, solo si el paso 3 no mueve nada en dos días hábiles

Dónde se ejecuta: Jira, comentario interno en RCS-28281.
Escritura. Autoriza Juan Martinez, lo pega Juan Martinez.

Que hace este paso: pide al equipo de datos una fuente que Juan ya buscó y no encontró en la base de tenant. Este paso es la red por si Rodney y Becky no responden, no el primer movimiento.

```
Viraj, following up on Ayesha's note from 8/27 that never got a reply here.

I checked the tenant SQL database, sqldb-prd-wus2-arp-production-441-dai-platform, for a raw transaction table that would let us break the flagged dates into 10 minute blocks. The only tables there with transaction in the name, Transactions and TransmissionReport, belong to the Incident module, not to Secure 5.4 POS data.

Does your team have access to a transaction level log for Ahold Secure 5.4 that we could query for this. I already asked the client's team to run a manual check on their side in the meantime.
```

Que se espera ver: Viraj confirma si existe esa fuente y desde dónde se consulta.

Si falla: si no hay respuesta en dos días hábiles, escala por Teams al mismo hilo donde Peyman hizo la asignación original, referenciado en el comentario de Jira del 18 de agosto.

## Paso 5. Transicionar a Under Customer Review

Dónde se ejecuta: Jira, RCS-28281, transición 571 Under Customer Review.
Escritura. Autoriza Juan Martinez, lo ejecuta Juan Martinez. Verificada en vivo el 7 de septiembre como transición disponible para este ticket.

Que hace este paso: refleja que el ticket espera un dato que solo el cliente puede producir, el chequeo de Becky. Va después de pegar el comentario del Paso 3, no antes.

Que se espera ver: el estado cambia a Under Customer Review. Según `brain/memoria/reference_jira_rcs_workflow.md`, la automatización devuelve el ticket a Work in progress solo cuando el cliente comenta. No hace falta moverlo de regreso a mano.

Si falla: no aplica, es transición estándar del workflow, ya confirmada disponible.

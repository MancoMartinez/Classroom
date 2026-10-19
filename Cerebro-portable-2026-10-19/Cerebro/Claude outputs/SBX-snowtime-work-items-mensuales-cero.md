# SBX c166, work items mensuales en cero tras el cutover a SnowTime

Abierta 2026-09-30. Tickets RCS-29205, RCS-29206, RCS-29207. Mismo reporter, Manish Sethia, los tres
creados entre 17:11 y 17:25 EDT del 30 sep. Estado de la causa: HIPOTESIS.

## El dato que ordena todo

Tres definiciones mensuales distintas dan cero en el mismo periodo, 24 ago a 27 sep 2026. Las tres
dieron resultados en los dos periodos previos. SBX paso de pyardm legacy a SnowTime el 27 ago, dentro
de ese periodo. Sebastian Rueda lo verifico contra ARDM_PRODUCTION.C166_SBX en RCS-28873 el 10 sep y
Bryant McAnnally lo confirma en el mismo ticket el 14 sep.

Las tres dependen de campos propios de Starbucks en tablas _EXT: marcador de partner discount,
tarjeta SVC de partner, estrellas y MemberID. Esa es la variable comun. Talos y el analisis del 30
sep trataron cada ticket aislado y propusieron tres causas distintas.

## Correccion al corpus de Confluence

La ficha confluence/RTS-triage/RCS-28873-starbucks-searches-error-slowness.md dice en 4.2 que c166_sbx
no tiene cutover y lee ARDMPROD.ARDM_166. Es incorrecto. Sebastian lo corrigio en Jira el 10 sep a las
17:07. La primera nota de RCS-28848 arrastra el mismo error. La ficha sigue sin corregir en Confluence.

## Hipotesis, de mas a menos probable

H1. Las definiciones filtran por un campo _EXT cuyo mapeo en el catalogo apunta a una columna que en
SnowTime existe como placeholder X_ siempre NULL o con otro nombre. Resultado: cero filas sin error.
Precedentes: RTS-206268 Kinney, X_POS_ARTICLEID placeholder siempre NULL. RCS-28848, Gabor el 17 sep,
filtro memberid que debia ser x_memberid. RCS-28873, x_StoreManager contra x_storemanagername.

H2, solo RCS-29207. La definicion agrupa por MemberID y la deaggregacion falla por el binding numerico
sin comillas de DeaggregationEngine.cs. Abierto en RCS-28873 desde el 25 sep, ENG-9112 en Backlog.
Se distingue de H1 porque deja rastro de fallo en el run.

H3. Retencion por go/no-go, 2 dias 7 horas tras el cierre, o rollover del ano fiscal. Cae si otras
definiciones mensuales de SBX si produjeron items para el mismo periodo.

## Discriminadores, en orden de costo

1. En Secure, correr a mano la trigger search de cada definicion para 24 ago a 27 sep y para 27 jul a
   23 ago. Resultados en el periodo nuevo apuntan a generacion o retencion. Cero apunta a H1.
2. Platform DB, solo SELECT. Descubrir columnas antes de filtrar:

   SELECT name FROM sys.databases WHERE name LIKE '%166%';
   SELECT TABLE_NAME, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
   WHERE TABLE_SCHEMA = 'workview'
     AND TABLE_NAME IN ('Workview','WorkItemDefinitionGenerationRequest','WorkItemDeaggregationRequest')
   ORDER BY TABLE_NAME, ORDINAL_POSITION;

   Con los nombres reales, contar work items por Category y Period desde jul 2026, y leer Failed,
   DeaggregationRequestsCreated y SearchVersion de los runs de las tres definiciones.
3. Snowflake. Diferenciar columnas legacy contra SnowTime y medir nulos por semana:

   SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS
   WHERE TABLE_SCHEMA = 'C166_SBX'
     AND (COLUMN_NAME ILIKE '%PARTNER%' OR COLUMN_NAME ILIKE '%STAR%' OR COLUMN_NAME ILIKE '%SVC%'
          OR COLUMN_NAME ILIKE '%MEMBER%' OR COLUMN_NAME ILIKE '%DISC%')
   ORDER BY 1, 2;

   Repetir con ARDMPROD.INFORMATION_SCHEMA y TABLE_SCHEMA = 'ARDM_166'. Por cada columna que la
   definicion usa:

   SELECT DATE_TRUNC('week', TRADINGDAY) AS semana, COUNT(*) AS filas, COUNT(<columna>) AS no_nulos
   FROM ARDM_PRODUCTION.C166_SBX.<tabla>
   WHERE TRADINGDAY BETWEEN '2026-07-27' AND '2026-09-27'
   GROUP BY 1 ORDER BY 1;

   Un salto a cero no_nulos en la semana del 24 ago confirma H1 para esa columna.

## Reparacion, si H1 se confirma

Resync del catalogo por Delivery, igual que arpfiles PR 57459. En RCS-28671 el rerun de WISC no
reparo nada porque el dedup salto los work items que ya existian. Aqui el periodo esta en cero y no
hay duplicados, asi que el rerun despues del fix podria regenerarlo. Que lo decida quien haga el fix,
y dejarlo escrito en el ticket.

# SBX c166, paso a paso para RCS-29205, RCS-29206 y RCS-29207

Objetivo: separar tres causas posibles con evidencia propia. Solo lectura en todo el recorrido.
Anota cada resultado en la tabla del final. Con esa tabla se marca la causa CONFIRMADA o se descarta.

| Ticket | Definicion |
|---|---|
| RCS-29205 | Refunds - Refund to a Partners SVC or Credit Debit Card with no Partner Discount – fiscal period |
| RCS-29206 | Discounts - Partner Discount with controllable discounts on serve ware |
| RCS-29207 | SFE - Star Farming same day high volume |

Periodo que falla: 24 ago a 27 sep 2026. Periodo de control: 27 jul a 23 ago 2026.

No uses el rerun de WISC como diagnostico. En un periodo en cero no hay duplicados que saltar y el
rerun crearia work items reales en la cola de Starbucks. Eso es la reparacion, no la prueba.

---

## Parte A. Secure, dentro del tenant SBX

### Paso 1. Entrar al tenant
1. Abre `usprod.apprissretailcloud.com/control`.
2. Ve a Customers in USPROD.
3. Busca Starbucks, Client ID 166, codigo SBX.
4. Haz click en el logo de la primera columna, Click logo to sign in. Esa es la entrada de soporte.
   No uses `/sbx/signin`.

### Paso 2. Ver si ya aparecieron items del periodo
Esto descarta o confirma la espera de 2 dias 7 horas que propuso Talos. El umbral paso el 30 sep.
1. Abre Work View.
2. Filtra por categoria o por nombre de cada una de las tres definiciones.
3. Ordena por fecha de creacion, la mas reciente arriba.
4. ANOTA para cada definicion: hay items creados el 29 sep o despues con periodo 24 ago a 27 sep, si o no.
5. De paso, abre dos o tres definiciones mensuales que no esten en los tickets, por ejemplo cualquier
   otra de Refunds o Discounts. ANOTA si tienen items del mismo periodo.

Que leer:
- Las tres ya tienen items: la causa fue la espera de datos. Salta a la Parte D, fila H3.
- Otras mensuales tienen items y estas tres no: la espera queda descartada. Sigue al paso 3.
- Ninguna mensual tiene items del periodo: la generacion completa esta retenida o fallo. Sigue al paso 3
  y marca esto en la tabla. Cambia el escalamiento a Engineering.

### Paso 3. Correr a mano la busqueda origen de cada definicion
1. Abre el Work Item Composer y busca la definicion por nombre.
2. En el paso 1 del Composer, Titulo y busqueda origen, ANOTA la ruta de la busqueda origen.
   La ruta suele empezar con `/system/ebr/`.
3. Abre esa busqueda en Search Compose. El quick link crea una copia efimera bajo `unsaved searches`.
   Abre, corre, lee. No edites ni guardes nada.
4. Pon el rango 27 jul a 23 ago 2026. Pulsa Run. ANOTA el numero de filas.
5. Cambia el rango a 24 ago a 27 sep 2026. Pulsa Run. ANOTA el numero de filas y si sale error.
6. Si sale error, copia el tracking code completo.
7. Pulsa el boton Query, si esta disponible, y copia el SQL generado a un archivo de texto.
   Busca ahi columnas con prefijo `X_` y los nombres de las columnas de partner, SVC, discount,
   stars o memberid. Esos nombres son los que vas a medir en la Parte C.
8. Repite con las tres definiciones.

Que leer:
- Control con filas y periodo nuevo con cero, sin error: apunta a H1, campo vacio o renombrado.
- Periodo nuevo con filas: la busqueda esta bien. El fallo esta en la generacion. Sigue a la Parte B.
- Error con texto `Numeric value ... is not recognized`: H2, solo esperable en RCS-29207.
- Error `invalid identifier`: rename sin resync del catalogo, misma familia que RCS-28873.

---

## Parte B. Platform DB de SBX, solo SELECT

### Paso 4. Conectar
1. Entra por Azure Bastion a la VM y abre SSMS. Desde tu equipo el puerto 1433 esta cerrado.
2. Servidor `sqlmi-prd-wus2-arp-001`. Usa el login de lectura.
3. Corre:

```sql
SELECT name FROM sys.databases
WHERE state = 0 AND database_id > 4 AND name LIKE '%-166-%platform'
ORDER BY name;
```

4. Debe salir `sqldb-prd-wus2-arp-production-166-xxx-platform`. ANOTA el nombre exacto.
   Confirma el 166 en el selector Client de la pagina Cache del Control Panel. No elijas la base por
   parecido del nombre.
5. Seleccionala en el desplegable de bases. Sin eso las consultas van contra master.

### Paso 5. Ver las columnas reales antes de filtrar

```sql
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'workview'
  AND TABLE_NAME IN ('Workview','WorkItemDefinitionGenerationRequest','WorkItemDeaggregationRequest')
ORDER BY TABLE_NAME, ORDINAL_POSITION;
```

ANOTA en WorkItemDefinitionGenerationRequest la columna que guarda la ruta o el ID de la definicion
y la columna de fecha de creacion. En Workview ANOTA la columna de fecha.

### Paso 6. Los runs de cada definicion
Mira primero los 20 runs mas recientes sin filtro para ver el formato:

```sql
SELECT TOP 20 *
FROM workview.WorkItemDefinitionGenerationRequest WITH (NOLOCK)
ORDER BY <columna_fecha> DESC;
```

Luego filtra por definicion. Cambia los dos marcadores por lo que anotaste en el paso 5:

```sql
SELECT TOP 10 *
FROM workview.WorkItemDefinitionGenerationRequest WITH (NOLOCK)
WHERE <columna_ruta_definicion> LIKE '%serve ware%'
ORDER BY <columna_fecha> DESC;
```

Repite con `'%partners svc%'` y con `'%star farming%'`.

ANOTA por definicion y por periodo: Failed, DeaggregationRequestsCreated, SearchVersion y la fecha.

Que leer:
- No hay run del periodo 24 ago a 27 sep: nunca corrio. Escala a Engineering por generacion.
- Run con DeaggregationRequestsCreated = 0 y Failed = 0: corrio y la busqueda no encontro nada. H1.
- Run con Failed mayor que 0: fallo. Ve al paso 7.

### Paso 7. Solo si hubo Failed

```sql
SELECT TOP 20 *
FROM workview.WorkItemDeaggregationRequest WITH (NOLOCK)
WHERE <columna_id_del_run> = '<id del run del paso 6>'
ORDER BY 1 DESC;
```

ANOTA el mensaje de error si la tabla lo guarda. Si trae `Numeric value ... is not recognized`,
H2 queda confirmada para RCS-29207.

### Paso 8. Cuanto produjo cada definicion mensual del periodo
Sirve para el punto 5 del paso 2 con numeros. Cambia la columna de fecha:

```sql
SELECT Category, Period, COUNT(*) AS items
FROM workview.Workview WITH (NOLOCK)
WHERE <columna_fecha_workview> >= '2026-07-01'
GROUP BY Category, Period
ORDER BY Category, Period;
```

---

## Parte C. Snowflake, columnas legacy contra SnowTime

### Paso 9. Abrir Snowflake
1. Entra a Snowsight y abre un worksheet nuevo.
2. Usa un rol con lectura sobre `ARDM_PRODUCTION` y `ARDMPROD`.

### Paso 10. Columnas candidatas en SnowTime

```sql
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'C166_SBX'
  AND (COLUMN_NAME ILIKE '%PARTNER%' OR COLUMN_NAME ILIKE '%STAR%'
       OR COLUMN_NAME ILIKE '%SVC%'   OR COLUMN_NAME ILIKE '%MEMBER%'
       OR COLUMN_NAME ILIKE '%DISC%')
ORDER BY 1, 2;
```

### Paso 11. Las mismas columnas en legacy

```sql
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM ARDMPROD.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'ARDM_166'
  AND (COLUMN_NAME ILIKE '%PARTNER%' OR COLUMN_NAME ILIKE '%STAR%'
       OR COLUMN_NAME ILIKE '%SVC%'   OR COLUMN_NAME ILIKE '%MEMBER%'
       OR COLUMN_NAME ILIKE '%DISC%')
ORDER BY 1, 2;
```

Pon los dos resultados lado a lado. ANOTA cada columna que cambio de nombre, de tipo o que solo
existe en uno de los dos lados. Cruza con el SQL que copiaste en el paso 3.

### Paso 12. Nulos por semana en cada columna que usa la definicion
Una consulta por columna. Cambia tabla y columna:

```sql
SELECT DATE_TRUNC('week', TRADINGDAY) AS semana,
       COUNT(*)          AS filas,
       COUNT(<columna>)  AS no_nulos
FROM ARDM_PRODUCTION.C166_SBX.<tabla>
WHERE TRADINGDAY BETWEEN '2026-07-27' AND '2026-09-27'
GROUP BY 1
ORDER BY 1;
```

Que leer:
- no_nulos cae a cero desde la semana del 24 ago: H1 CONFIRMADA para esa columna. Es un placeholder
  vacio, como X_POS_ARTICLEID en Kinney.
- no_nulos estable toda la ventana: esa columna no es la causa. Pasa a la siguiente.
- filas cae a cero: no llego data para esa tabla. Eso es otro problema, de carga. Escala a SnowTime.

---

## Parte D. Decision y a quien va

| Resultado | Causa | Escala a | Que pegas |
|---|---|---|---|
| Items aparecieron el 30 sep | H3 espera de datos | Nadie | Respuesta al cliente con el hallazgo |
| Busqueda da cero, columna vacia en SnowTime | H1 catalogo | Delivery, resync como PR 57459 | Comentario interno con columna y consulta |
| Run con Failed y Numeric value | H2 binding MemberID | Engineering, sumar a RCS-28873 y ENG-9112 | Comentario interno enlazando |
| Busqueda da filas, no hay run | Generacion | Engineering | Comentario interno con el run faltante |
| Ninguna mensual produjo | Generacion general | Engineering, urgente | Comentario interno y aviso a Camila |

Si H1 se confirma, el arreglo del catalogo no repara el periodo ya corrido. Pide en el mismo comentario
quien regenera los work items del 24 ago a 27 sep. RCS-28671 mostro que WISC no lo hace cuando hay
duplicados. Aqui no los hay, asi que el rerun si podria servir despues del fix. Que lo decida quien
haga el fix.

---

## Tabla de resultados

| Paso | RCS-29205 | RCS-29206 | RCS-29207 |
|---|---|---|---|
| 2. Items del periodo hoy | | | |
| 2. Otras mensuales con items | | | |
| 3. Filas periodo control | | | |
| 3. Filas periodo que falla | | | |
| 3. Error y tracking code | | | |
| 3. Columnas X_ en el SQL | | | |
| 6. Run existe | | | |
| 6. Failed | | | |
| 6. DeaggregationRequestsCreated | | | |
| 11. Columnas que cambiaron | | | |
| 12. Columna que cae a cero | | | |
| Causa | | | |

Pega la tabla llena en el chat. Con eso redacto el comentario de cada ticket.

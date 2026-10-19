---
name: reference_ardm_playbook_peyman
description: "Procedimiento para arreglar un problema de datos en ARDM: rastrear el campo hasta su tabla de referencia, confirmar si la pantalla pega a Greenplum o Snowflake, respaldar y deduplicar"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-11T23:40:55.288Z
---

Aprendido en la llamada de 2h21 con Peyman Motlagh el 11 ago 2026, resolviendo RCS-28077. Documento completo: https://claude.ai/code/artifact/9cb0690a-4f40-4748-9747-48713f1c2e13

**Las tres tablas de referencia de ARDM** son `reference_product` (llave `article_id`, que es el SKU), `reference_location` (una fila por tienda, con la dirección) y `reference_employee`. Casi todo "un campo salió vacío o repetido" cae en una de ellas. Ojo: en DBeaver aparecen `ref_product` y `reference_product`; la buena es la larga.

**Rastrear un campo de la pantalla hasta su origen.** El prefijo de las columnas del resultado dice la tabla (`item` → tabla `item`). El script que la carga está en el repo del cliente en `SQL / load ARDM scripts / load_ardm_item`. Ctrl+F por el campo y se lee el join: `item_receipt_description` viene de `reference_product` unido por `article_id`. Si esa tabla tiene N filas por `article_id`, el detalle se multiplica por N. El nivel agregado no hace ese join, por eso el resumen sale bien y solo el drill down sale roto.

**Greenplum o Snowflake.** Un cliente puede ser mixto: unas pantallas leen de uno y otras del otro. Se distingue mirando la consulta que la aplicación manda: **Greenplum arma un CTE, Snowflake no**. Si corriges datos y la pantalla no cambia, la primera hipótesis no es el caché, es que corregiste el motor equivocado. El flujo es Greenplum primero y de ahí se copia a Snowflake, así que se corrigen los dos.

**Respaldar antes de tocar producción.** No hay barandas. En Greenplum: click derecho en la tabla → Generate SQL → DDL → pegar en un editor nuevo → renombrar a `BKUP_YYYYMMDD_<tabla>` → ejecutar → `INSERT INTO backup SELECT * FROM original` → contar las dos. Se hace por DDL y no con `CREATE TABLE AS` para conservar estructura y permisos. En Snowflake: click derecho → Clone. **Nunca nombrar el backup empezando por `reference_product`**: el job diario de Luke copia a Snowflake cualquier cosa que haga match con ese nombre.

**Deduplicar.** `SELECT DISTINCT *` no funciona porque las filas difieren en `inserted_datetime`. Lo que sirve es quedarse con la última por llave: `SELECT DISTINCT ON (article_id) * FROM ... ORDER BY article_id, inserted_datetime DESC`. La verificación que cuenta no es el conteo, es correr la búsqueda del cliente con el mismo filtro.

**Los archivos crudos** están en `p-ingest-<region>/<id>_<CODIGO>/Archive/Prod/<fecha>`. Ahí se ve lo que el cliente realmente mandó, que no es lo que el cliente cree que mandó.

Relacionado: [[reference_ardm_instancias_clientes]], [[project_rcs_28077_28003]], [[reference_peyman_motlagh]].

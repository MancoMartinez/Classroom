---
name: reference_acceso_sql_tenants
description: "Ruta de acceso a las bases de tenant por Bastion + SSMS, nomenclatura de las DB, mapa de Client IDs y el patrón de barrido cross-database"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-11T16:25:39.058Z
---

**Acceso.** Azure Bastion → SSMS → Managed Instance `sqlmi-prd-wus2-arp-001`. El login de Juan es `jmartinez@trebu.co`. Ver [[project_juan_accesos]].

**Nomenclatura.** Las bases de tenant se llaman `sqldb-prd-wus2-arp-production-NNN-xxx-platform`, donde NNN es el Client ID y xxx el código corto del cliente. Las bases ya no llevan nombre de compañía, por eso el Client ID es obligatorio en todo comentario interno.

| Client ID | Cliente | Código |
|---|---|---|
| 209 | Tailored Brands | tbi |
| 423 | Stater Bros | sbs |
| 433 | Vitamin Shoppe | vse |

**Barrido cross-database.** Para revisar la misma cosa en todos los tenants: `sys.databases` filtrando `state = 0 AND database_id > 4 AND name LIKE '%platform'`, construir SQL dinámico con `QUOTENAME(name)`, insertar en una tabla temporal, `EXEC sp_executesql`, y hacer el pivot al final.

**Gotcha que costó una sesión.** SQL Server compila el batch completo antes de ejecutarlo. Si la tabla temporal ya existe en la sesión con un esquema viejo, el SELECT final se resuelve contra el esquema viejo y sale `Msg 207 Invalid column name`, aunque el batch tenga un DROP arriba. La solución es usar un nombre nuevo de tabla temporal, no arreglar el DROP.

**Regla.** Todo lo que se corre en producción es de solo lectura. Diagnóstico sí, cambios nunca.

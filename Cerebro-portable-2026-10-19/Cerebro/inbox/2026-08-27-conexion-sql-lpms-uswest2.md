# Conexion SSMS al SQL de LPMS produccion US

Fecha: 2026-08-27. Contexto: Edwin Garzon pide correr un UPDATE en la base de Luxottica
sobre el servidor pd-lpms-uswest2-sqldb-001. SSMS falla al conectar.

## El error

Named Pipes Provider, error 40, "Could not open a connection to SQL Server", Microsoft SQL
Server Error 53, "The network path was not found".

Error 53 con Named Pipes significa que SSMS resolvio el nombre como una maquina de la red local.
No intento salir a Azure. El nombre del servidor entro sin sufijo de dominio.

## La causa

`pd-lpms-uswest2-sqldb-001` es el nombre del recurso en Azure, no el endpoint de conexion.
Aparece asi en la lista de accesos de MSSQL Prod de la solicitud de acceso del equipo, ver
brain/markdown/17-reuniones-prep.md linea 163.

El endpoint de un logical server de Azure SQL siempre lleva el sufijo `.database.windows.net`.

## Server Name correcto

```
pd-lpms-uswest2-sqldb-001.database.windows.net
```

Si sigue fallando, forzar puerto:

```
tcp:pd-lpms-uswest2-sqldb-001.database.windows.net,1433
```

Si el recurso resulta ser Managed Instance y no logical server, el endpoint lleva zona DNS
intermedia, patron `nombre.<zona>.database.windows.net`. La referencia conocida de ese patron es
el MI de Secure: `sqlmi-prd-wus2-arp-001-production.d4f7681860d3.database.windows.net`. La zona
se lee en el Overview del recurso en el portal de Azure.

## Los otros dos servidores de la misma familia

- Canada: `pc-lpms-canadacentral-sql-001.database.windows.net`
- Europa: `pe-lpms-northeurope-sql-001.database.windows.net`

## Resto de la ventana de conexion

- Authentication: Microsoft Entra MFA, correcto.
- User Name: jmartinez@trebu.co, correcto, es el login registrado en reference_acceso_sql_tenants.
- Database Name: poner el nombre real de la base en vez de `<default>`. Con Entra el default es
  master y la cuenta de soporte no siempre tiene lectura ahi. El nombre exacto de la base se
  confirma expandiendo Databases en Object Explorer. Edwin escribio "Luxotica", la marca es
  Luxottica.
- Trust Server Certificate marcado con Encrypt Mandatory, correcto.
- La sesion tiene que correr dentro de la VM de Bastion. Desde el equipo local el puerto 1433
  hacia Azure esta cerrado.

## Nota de alcance

La regla del cerebro es SELECT contra produccion. El UPDATE que pide Edwin
`UPDATE Suspect SET StoreIdent = 36247 WHERE StoreIdent = 45101;` lo ejecuta Juan bajo la
instruccion de Edwin, no Claude. Antes de correrlo conviene el conteo:
`SELECT COUNT(*) FROM Suspect WHERE StoreIdent = 45101;` y dejar el numero registrado en el
ticket, porque el UPDATE no trae WHERE adicional y toca todas las filas de esa tienda.

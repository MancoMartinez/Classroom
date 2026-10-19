---
name: reference_configuration_items_features
description: "Los feature flags viven en secure.ConfigurationItem y el valor efectivo puede ser CustomerEditedValue, no Value"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-12T00:15:36.214Z
---

Los items de configuración de features están en **`secure.ConfigurationItem`**, no en `incident.ConfigurationItem`, aunque el nombre del flag empiece por `Feature.Incident.`. Verificado el 10 ago 2026 en el tenant 433.

Columnas reales, verificadas contra `INFORMATION_SCHEMA.COLUMNS` el 11 ago 2026: `Name`, `ID`, `DataType`, `Value`, **`CustomerEditedValue`**, `CustomerEditedDateTimeUtc`, `IsVisible`. **No existe `ItemName`**, que es el nombre que uno tiende a escribir y devuelve `Msg 207`.

Consulta que funciona:

```sql
USE [sqldb-prd-wus2-arp-production-209-tbi-platform];
GO
SELECT Name, Value, CustomerEditedValue, CustomerEditedDateTimeUtc, IsVisible
FROM secure.ConfigurationItem
WHERE Name LIKE '%AdHoc%' OR Name LIKE '%BlobAppend%'
ORDER BY Name;
```

**El valor efectivo puede ser `CustomerEditedValue`**, no `Value`. Por eso Matt Kamminga insiste en verificarlos en la base y no en Control Panel: Control Panel puede mostrar una cosa y el sistema estar leyendo otra. Al consultar, usar siempre `ISNULL(CustomerEditedValue, Value)`.

**Flags conocidos**
- `Feature.Incident.EnableAdHocInitCaching`
- `Feature.Incident.EnableAdHocPerRequestUserScope`
- `Feature.Incident.EnableBlobAppendLogging`

Los dos primeros quedaron en false en 209-tbi después de un release del 6 ago 2026 porque faltaban en el historial de seed y el default es false. Ese es el patrón a buscar cuando un tenant se degrada justo después de un despliegue: no es que alguien los apagara, es que nunca se sembraron.

Relacionado: [[reference_acceso_sql_tenants]].

# RCS-28223, cuarta tanda

Dos correcciones y una pista nueva.

## Lo que el paso 15 descarta

    CREATED  2026-07-29  Audit           72
    CREATED  2026-07-29  Otros modulos   21
    NULL     2026-07-29  Otros modulos    1
    NULL     2026-02-11  Otros modulos    1
    NULL     NULL        Otros modulos   15

93 pantallas se construyeron el 29 de julio de 2026. Audit y otros modulos juntos. CREATED es el
estado de 93 de 110 pantallas del tenant.

`BuildStatus = CREATED` no es anomalo. No lo uses como evidencia. Lo que queda del paso 12 es solo
la fecha del rebuild, el 29 de julio, dos dias despues de la migracion.

## La pista que abrio el paso 14

`ScreenDetail` de las pantallas 83 y 88 devuelve 8 filas cada una, una por pregunta. Todas con
`ReadOnly` 0, `HiddenField` 0 y `FieldProtected` 0. No hay bloqueo de permisos. Eso confirma lo que
dijo David.

El LEFT JOIN contra `ScreenLabel` devolvio NULL en las 16 filas. `LPMSFieldName`, `NewFieldName`,
`Editable`, `ShowVisible` y `FieldClass` todas en NULL.

Dos lecturas posibles. Las filas de `ScreenLabel` existen y traen esas columnas vacias. O las filas
no existen y los `ScreenLabelID` 201141 a 201148 y 201186 a 201193 estan huerfanos.

**Si estan huerfanos, la causa raiz esta encontrada.** El cerebro ya tiene el precedente escrito en
`inbox/2026-08-25-rcs-28032-cierre-evidencia-y-escalacion.md`, sobre Vitamin Shoppe: el rebuild de
pantallas de Audit "es candidato a explicar por que hoy faltan 30 entradas en la tabla de Screen
Labels". Mismo modulo, misma migracion, misma tabla.

Corre la consulta 17 primero. Decide el caso.

---

## Consulta 17. Existen esas Screen Labels

```sql
SELECT  sd.ScreenMasterID,
        sm.PageName,
        sd.ScreenLabelID,
        COUNT(sl.PrimaryKeyID) AS FilasEnScreenLabel
FROM    incident.ScreenDetail sd
JOIN    incident.ScreenMaster sm ON sm.ScreenMasterID = sd.ScreenMasterID
LEFT JOIN incident.ScreenLabel sl ON sl.ScreenLabelID = sd.ScreenLabelID
WHERE   sd.ScreenMasterID IN (83, 88)
GROUP BY sd.ScreenMasterID, sm.PageName, sd.ScreenLabelID
ORDER BY sd.ScreenMasterID, sd.ScreenLabelID;
```

FilasEnScreenLabel en 0 significa huerfano. Con 1 o mas significa que la fila existe y las columnas
vienen vacias.

---

## Consulta 18. Cuantas Screen Labels faltan en todo el tenant

Mide el alcance. Separa Audit del resto.

```sql
SELECT  CASE WHEN sm.PageName LIKE 'AuditSection%' THEN 'Audit' ELSE 'Otros modulos' END AS Grupo,
        CASE WHEN sl.PrimaryKeyID IS NULL THEN 'Sin fila en ScreenLabel' ELSE 'Con fila' END AS Estado,
        COUNT(*) AS Campos
FROM    incident.ScreenDetail sd
JOIN    incident.ScreenMaster sm ON sm.ScreenMasterID = sd.ScreenMasterID
LEFT JOIN incident.ScreenLabel sl ON sl.ScreenLabelID = sd.ScreenLabelID
GROUP BY CASE WHEN sm.PageName LIKE 'AuditSection%' THEN 'Audit' ELSE 'Otros modulos' END,
         CASE WHEN sl.PrimaryKeyID IS NULL THEN 'Sin fila en ScreenLabel' ELSE 'Con fila' END
ORDER BY Grupo, Estado;
```

Si los campos de Audit salen sin fila y los de otros modulos con fila, la causa raiz esta cerrada
y el precedente de Vitamin Shoppe la respalda.

---

## Consulta 19. El rango de ScreenLabel

Contexto. Cuantas filas tiene la tabla y hasta que ID llega.

```sql
SELECT  COUNT(*) AS Filas,
        COUNT(DISTINCT sl.ScreenLabelID) AS IDsDistintos,
        MIN(sl.ScreenLabelID) AS IDMin,
        MAX(sl.ScreenLabelID) AS IDMax
FROM    incident.ScreenLabel sl;
```

---

## Consulta 20. Reemplaza la 16, que salio vacia

Version simple, sin CASE en el GROUP BY. Cuenta por mes en que columna cayo el texto.

```sql
SELECT  CONVERT(char(7), ams.AuditDate, 126) AS Mes,
        SUM(CASE WHEN amq.Comments LIKE ',,,,,,,,%' THEN 1 ELSE 0 END) AS SoloCOL9,
        SUM(CASE WHEN amq.Comments NOT LIKE ',,,,,,,,%'
                  AND amq.Comments LIKE '%,,,,,,,,%' THEN 1 ELSE 0 END) AS COL1yCOL9,
        SUM(CASE WHEN amq.Comments NOT LIKE '%,,,,,,,,%' THEN 1 ELSE 0 END) AS ConColumnasDelMedio,
        COUNT(*) AS Total
FROM    incident.AuditMasterQuestion amq
JOIN    incident.AuditMasterStore ams ON ams.AuditMasterStoreID = amq.AuditMasterStoreID
JOIN    incident.AuditConfigQuestion acq ON acq.AuditConfigQuestionID = amq.AuditConfigQuestionID
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID = 4
  AND   acq.GridCols IS NOT NULL
  AND   DATALENGTH(acq.GridCols) > 0
  AND   ams.AuditDate >= '2025-01-01'
  AND   amq.Comments IS NOT NULL
  AND   LEN(REPLACE(REPLACE(amq.Comments, ',', ''), '|', '')) > 0
GROUP BY CONVERT(char(7), ams.AuditDate, 126)
ORDER BY Mes;
```

Si la columna ConColumnasDelMedio cae a cero en julio o agosto de 2026 y antes traia numeros, ese
es el numero que va al comentario de Jira.

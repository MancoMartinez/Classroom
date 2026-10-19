# RCS-28223, tercera tanda

El paso 13 salio vacio porque quedo `ScreenMasterID = 0`. Los reales son 83 para Manager Week 1 y
88 para Crew Week 1.

Estas tres cierran la investigacion.

---

## Consulta 14. Los campos de las dos pantallas

Verifica ReadOnly, HiddenField y FieldProtected en las pantallas que reporta el cliente.

```sql
SELECT  sm.PageName,
        sm.ScreenDescription,
        sd.ScreenDetailID,
        sd.ScreenLabelID,
        sl.LPMSFieldName,
        sl.NewFieldName,
        sl.Editable,
        sl.ShowVisible,
        sl.FieldClass,
        sd.FieldOrder,
        sd.ReadOnly,
        sd.HiddenField,
        sd.FieldProtected,
        sd.ConditionToShow,
        sd.FieldsToDisplay
FROM    incident.ScreenDetail sd
JOIN    incident.ScreenMaster sm ON sm.ScreenMasterID = sd.ScreenMasterID
LEFT JOIN incident.ScreenLabel sl ON sl.ScreenLabelID = sd.ScreenLabelID
WHERE   sd.ScreenMasterID IN (83, 88)
ORDER BY sd.ScreenMasterID, sd.FieldOrder;
```

Si sale vacio, esas pantallas no tienen filas en ScreenDetail. Eso ya seria un hallazgo.

---

## Consulta 15. Es CREATED el estado normal

Las 74 pantallas de Audit se construyeron el 29 de julio de 2026 y quedaron en BuildStatus CREATED.
Esta consulta dice si el resto del tenant esta igual o si Audit es el caso raro.

Como leer el resultado. Si todas las pantallas del tenant estan en CREATED con la misma fecha,
el rebuild fue global y no distingue a Audit. Si las de Audit son las unicas en CREATED, o las
unicas construidas ese dia, el rebuild del 29 de julio es el sospechoso.

```sql
SELECT  sm.BuildStatus,
        CONVERT(char(10), sm.LastBuildDate, 126) AS DiaBuild,
        CASE WHEN sm.PageName LIKE 'AuditSection%' THEN 'Audit' ELSE 'Otros modulos' END AS Grupo,
        COUNT(*) AS Pantallas,
        MIN(sm.PageName) AS Ejemplo
FROM    incident.ScreenMaster sm
GROUP BY sm.BuildStatus,
         CONVERT(char(10), sm.LastBuildDate, 126),
         CASE WHEN sm.PageName LIKE 'AuditSection%' THEN 'Audit' ELSE 'Otros modulos' END
ORDER BY DiaBuild DESC, Grupo;
```

---

## Consulta 16. En que columna cae el contenido, antes y despues

Esta es la que convierte el sintoma en un numero. Clasifica cada respuesta de grilla segun donde
quedo el texto.

Ocho comas seguidas al inicio significa que COL1 quedo vacio y todo se fue a COL9.
Ocho comas seguidas en medio significa que COL1 y COL9 tienen dato y las siete columnas de accion
disciplinaria quedaron vacias.
Sin ocho comas seguidas significa que alguna columna del medio recibio contenido.

```sql
SELECT  CONVERT(char(7), ams.AuditDate, 126) AS Mes,
        CASE
            WHEN amq.Comments LIKE ',,,,,,,,%'  THEN '1. Solo COL9, sin nombre'
            WHEN amq.Comments LIKE '%,,,,,,,,%' THEN '2. COL1 y COL9, sin COL2 a COL8'
            ELSE                                     '3. Alguna columna del medio con dato'
        END AS Patron,
        COUNT(*) AS Respuestas
FROM    incident.AuditMasterQuestion amq
JOIN    incident.AuditMasterStore ams ON ams.AuditMasterStoreID = amq.AuditMasterStoreID
JOIN    incident.AuditConfigQuestion acq ON acq.AuditConfigQuestionID = amq.AuditConfigQuestionID
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID = 4
  AND   DATALENGTH(acq.GridCols) > 0
  AND   ams.AuditDate >= '2026-01-01'
  AND   NULLIF(REPLACE(REPLACE(ISNULL(amq.Comments, ''), ',', ''), '|', ''), '') IS NOT NULL
GROUP BY CONVERT(char(7), ams.AuditDate, 126),
         CASE
            WHEN amq.Comments LIKE ',,,,,,,,%'  THEN '1. Solo COL9, sin nombre'
            WHEN amq.Comments LIKE '%,,,,,,,,%' THEN '2. COL1 y COL9, sin COL2 a COL8'
            ELSE                                     '3. Alguna columna del medio con dato'
         END
ORDER BY Mes, Patron;
```

Si el patron 3 desaparece a partir de julio o agosto, queda probado que las columnas del medio
dejaron de aceptar entrada en esa fecha. Ese es el numero que va al comentario de Jira.

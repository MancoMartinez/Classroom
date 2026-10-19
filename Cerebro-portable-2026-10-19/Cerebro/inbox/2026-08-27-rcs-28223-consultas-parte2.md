# RCS-28223, segunda tanda

Los pasos 6 y 7 salieron vacios porque el join estaba mal.
`AuditMaster.DateCreated` no es la fecha de la auditoria. La fecha real y el numero de auditoria
viven en `AuditMasterStore`, que trae `AuditCaseNumber`, `AuditDate` y `StoreIdent`.

Estas cuatro consultas cierran el caso. Corre la 9 primero.

---

## Paso 9. La auditoria de Hugo, 959-30133

Confirma que existe, en que estado esta y cual es su AuditMasterStoreID.

```sql
SELECT  ams.AuditMasterStoreID,
        ams.AuditMasterID,
        ams.AuditCaseNumber,
        ams.StoreIdent,
        ams.AuditDate,
        ams.Status,
        ams.AuditCompleted,
        ams.AuditCompletionDate,
        ams.DateCreated,
        ams.LastEdited,
        ams.LastEditedBy,
        ams.EntrySource,
        ams.Version
FROM    incident.AuditMasterStore ams
WHERE   ams.AuditCaseNumber = '959-30133';
```

---

## Paso 10. La linea de tiempo real

Esta es la consulta que decide si el defecto arranca con la migracion del 27 de julio de 2026.
Cuenta, por mes, cuantas respuestas de preguntas con grilla llegaron con contenido.

Como leer el resultado. Si ConGrilla cae a cero a partir de julio o agosto de 2026 y antes venia
con numeros, la fecha de corte queda probada. Si viene en cero desde hace años, el defecto es
viejo y la migracion no tiene nada que ver.

```sql
SELECT  CONVERT(char(7), ams.AuditDate, 126) AS Mes,
        COUNT(*) AS RespuestasGrilla,
        SUM(CASE WHEN NULLIF(REPLACE(REPLACE(ISNULL(amq.Comments,''), ',', ''), '|', ''), '') IS NOT NULL
                 THEN 1 ELSE 0 END) AS ConGrillaLlena,
        SUM(CASE WHEN NULLIF(LTRIM(RTRIM(ISNULL(amq.Comments,''))), '') IS NOT NULL
                 THEN 1 ELSE 0 END) AS ConAlgoEnComments
FROM    incident.AuditMasterQuestion amq
JOIN    incident.AuditMasterStore ams ON ams.AuditMasterStoreID = amq.AuditMasterStoreID
JOIN    incident.AuditConfigQuestion acq ON acq.AuditConfigQuestionID = amq.AuditConfigQuestionID
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID = 4
  AND   acq.GridCols IS NOT NULL
  AND   DATALENGTH(acq.GridCols) > 0
  AND   ams.AuditDate >= '2023-01-01'
GROUP BY CONVERT(char(7), ams.AuditDate, 126)
ORDER BY Mes;
```

---

## Paso 11. Comparar la misma pregunta antes y despues

Trae las respuestas de las preguntas con grilla de 2026, para ver si llegan vacias o con basura.

```sql
SELECT TOP 100
        ams.AuditCaseNumber,
        ams.AuditDate,
        acs.SectionDescription,
        acq.AuditConfigQuestionID,
        acq.QuestionType,
        amq.Answer,
        DATALENGTH(amq.Comments) AS Comments_Bytes,
        amq.Comments,
        amq.LastEdited
FROM    incident.AuditMasterQuestion amq
JOIN    incident.AuditMasterStore ams ON ams.AuditMasterStoreID = amq.AuditMasterStoreID
JOIN    incident.AuditConfigQuestion acq ON acq.AuditConfigQuestionID = amq.AuditConfigQuestionID
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID = 4
  AND   DATALENGTH(acq.GridCols) > 0
  AND   ams.AuditDate >= '2026-06-01'
ORDER BY ams.AuditDate DESC, acq.AuditConfigQuestionID;
```

---

## Paso 12. Las pantallas. Cuando se construyeron por ultima vez

Precedente de Vitamin Shoppe, RCS-28032. Las pantallas de Audit se rompieron en la migracion y
Tyrone Whitney las reconstruyo. Matt Kamminga pidio entonces validar que las pantallas se
reconstruyan como parte de la ruta de migracion.

Si LastBuildDate es del 27 de julio de 2026 o posterior, y el control de grilla no sobrevivio ese
rebuild, la causa esta ahi y el precedente ya existe.

```sql
SELECT  sm.ScreenMasterID,
        sm.PageName,
        sm.PageTitle,
        sm.ScreenDescription,
        sm.ScreenType,
        sm.IsActive,
        sm.IsProtected,
        sm.LastBuildDate,
        sm.BuildStatus,
        sm.QEBuildStatus,
        sm.LastSavedDate,
        sm.LastSavedByID,
        sm.AppFolder
FROM    incident.ScreenMaster sm
WHERE   sm.PageName LIKE '%AuditSection%'
   OR   sm.PageTitle LIKE '%Audit%'
ORDER BY sm.LastBuildDate DESC;
```

---

## Paso 13. Solo si el paso 12 apunta a la pantalla

Los campos de la pantalla de la seccion 4. Verifica ReadOnly, HiddenField y FieldProtected.
Sustituye 0 por el ScreenMasterID que devuelva el paso 12 para AuditSection_V24_S4.

```sql
SELECT  sd.ScreenDetailID,
        sd.ScreenMasterID,
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
LEFT JOIN incident.ScreenLabel sl ON sl.ScreenLabelID = sd.ScreenLabelID
WHERE   sd.ScreenMasterID = 0
ORDER BY sd.FieldOrder;
```

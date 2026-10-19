-- RCS-28223 McDonald's Restaurant Cash Audit
-- Tenant mcdonalds, Client ID 402. Solo SELECT.
-- Cada bloque corre suelto. Sin variables. Selecciona un bloque y ejecuta.
--
-- CONFIRMADO EN EL PASO 1, 27 ago 2026:
--   AuditConfigID 4 = Restaurant Cash Audit,  Loss Prevention, v1.6,  NonScoredAudit 1
--   AuditConfigID 2 = Supervisor Cash Audit,  Loss Prevention, v1.14, NonScoredAudit 0
--
-- La 2 es el control. Misma clase, mismo tenant, otra configuracion. Si tiene preguntas
-- del mismo QuestionType y esas si funcionan, la comparacion aisla el defecto sin salir
-- de la base. Preguntarle al cliente si la Supervisor Cash Audit tambien falla.
--
-- Restaurant Cash Audit se edito por ultima vez el 2026-01-09. Antes de la migracion del
-- 27 de julio. Si la config no se toco desde enero y el sintoma arranca en agosto, la
-- configuracion no cambio sola. Eso apunta a codigo. Confirmalo con el paso 3.


-- ===========================================================================
-- PASO 2. Secciones de las dos auditorias.
-- Manager Week 1 y Crew Week 1 salen aca, con su AuditConfigSectionID.
-- ===========================================================================
SELECT  acs.AuditConfigID,
        ac.Description                AS AuditName,
        acs.AuditConfigSectionID,
        acs.SectionDescription,
        acs.SectionIdent,
        acs.SectionOrder,
        acs.DeleteFlag,
        acs.NASection,
        acs.HideSectionComments
FROM    incident.AuditConfigSection acs
JOIN    incident.AuditConfig ac ON ac.AuditConfigID = acs.AuditConfigID
WHERE   acs.AuditConfigID IN (2, 4)
ORDER BY acs.AuditConfigID, acs.SectionOrder;


-- ===========================================================================
-- PASO 3. LA CONSULTA QUE DECIDE A QUE EQUIPO VA EL TICKET.
-- Todas las preguntas de Restaurant Cash Audit con su tipo y su definicion de grilla.
-- ===========================================================================
SELECT  acs.SectionDescription,
        acq.AuditConfigQuestionID,
        acq.QuestionOrder,
        acq.Orderby,
        LEFT(acq.QuestionTextPlain, 130)          AS QuestionText,
        acq.QuestionType,
        acq.ParentQuestionID,
        acq.ParentQuestion,
        acq.TriggerAnswer,
        acq.GridCommentsYN,
        DATALENGTH(acq.GridCols)                  AS GridCols_Bytes,
        DATALENGTH(acq.GridConfig)                AS GridConfig_Bytes,
        acq.GridCols,
        acq.GridConfig,
        acq.Required,
        acq.HideComments,
        acq.DeleteFlag,
        acq.DoNotPrint
FROM    incident.AuditConfigQuestion acq
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID = 4
  AND   ISNULL(acq.DeleteFlag, 0) = 0
ORDER BY acs.SectionOrder, acq.QuestionOrder;

-- Como leer el resultado:
--   GridCols_Bytes NULL o 0 en las preguntas rotas y con valor en alguna que funcione
--     -> configuracion perdida. Va a Delivery. La conclusion de David cae.
--   GridCols_Bytes poblado e igual en todas
--     -> la config sobrevivio. El defecto es de codigo. La escalacion a Engineering se sostiene.


-- ===========================================================================
-- PASO 4. Resumen por tipo, las dos auditorias juntas para comparar.
-- ===========================================================================
SELECT  acs.AuditConfigID,
        acs.SectionDescription,
        acq.QuestionType,
        COUNT(*)                                                  AS Preguntas,
        SUM(CASE WHEN acq.GridCols   IS NULL THEN 1 ELSE 0 END)   AS SinGridCols,
        SUM(CASE WHEN acq.GridConfig IS NULL THEN 1 ELSE 0 END)   AS SinGridConfig,
        MIN(DATALENGTH(acq.GridCols))                             AS GridCols_Min,
        MAX(DATALENGTH(acq.GridCols))                             AS GridCols_Max
FROM    incident.AuditConfigQuestion acq
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID IN (2, 4)
  AND   ISNULL(acq.DeleteFlag, 0) = 0
GROUP BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType
ORDER BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType;


-- ===========================================================================
-- PASO 4b. El control. Preguntas de Supervisor Cash Audit del mismo tipo grilla.
-- Si esta si trae GridCols y la otra no, el caso queda cerrado en una pantalla.
-- ===========================================================================
SELECT  ac.Description                            AS AuditName,
        acs.SectionDescription,
        acq.AuditConfigQuestionID,
        LEFT(acq.QuestionTextPlain, 100)          AS QuestionText,
        acq.QuestionType,
        DATALENGTH(acq.GridCols)                  AS GridCols_Bytes,
        DATALENGTH(acq.GridConfig)                AS GridConfig_Bytes,
        acq.GridCols
FROM    incident.AuditConfigQuestion acq
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
JOIN    incident.AuditConfig ac         ON ac.AuditConfigID = acs.AuditConfigID
WHERE   acs.AuditConfigID IN (2, 4)
  AND   acq.GridCols IS NOT NULL
  AND   ISNULL(acq.DeleteFlag, 0) = 0
ORDER BY ac.Description, acs.SectionOrder, acq.QuestionOrder;


-- ===========================================================================
-- PASO 5. Como serializa una respuesta de grilla que si se guardo.
-- Vacio significa que el tipo grilla nunca guardo nada en este tenant.
-- ===========================================================================
SELECT TOP 30
        ac.Description                AS AuditName,
        acq.QuestionType,
        acq.AuditConfigQuestionID,
        amq.AuditMasterQuestionID,
        amq.AuditMasterID,
        amq.LastEdited,
        DATALENGTH(amq.Answer)        AS Answer_Bytes,
        LEFT(amq.Answer, 400)         AS Answer_Muestra,
        LEFT(amq.Comments, 200)       AS Comments_Muestra
FROM    incident.AuditMasterQuestion amq
JOIN    incident.AuditConfigQuestion acq ON acq.AuditConfigQuestionID = amq.AuditConfigQuestionID
JOIN    incident.AuditConfigSection acs  ON acs.AuditConfigSectionID  = acq.AuditConfigSectionID
JOIN    incident.AuditConfig ac          ON ac.AuditConfigID = acs.AuditConfigID
WHERE   acs.AuditConfigID IN (2, 4)
  AND   acq.GridCols IS NOT NULL
  AND   NULLIF(LTRIM(RTRIM(amq.Answer)), '') IS NOT NULL
ORDER BY amq.LastEdited DESC;


-- ===========================================================================
-- PASO 6. El discriminador temporal. Hugo dice que antes si funcionaba.
-- El tenant migro el 27 de julio de 2026.
-- ===========================================================================
SELECT  CAST(am.DateCreated AS date)                                       AS DiaAuditoria,
        acq.QuestionType,
        COUNT(*)                                                           AS Respuestas,
        SUM(CASE WHEN NULLIF(LTRIM(RTRIM(amq.Answer)), '') IS NOT NULL
                 THEN 1 ELSE 0 END)                                        AS ConAnswer,
        SUM(CASE WHEN NULLIF(LTRIM(RTRIM(amq.Comments)), '') IS NOT NULL
                 THEN 1 ELSE 0 END)                                        AS ConComments
FROM    incident.AuditMasterQuestion amq
JOIN    incident.AuditMaster am          ON am.AuditMasterID = amq.AuditMasterID
JOIN    incident.AuditConfigQuestion acq ON acq.AuditConfigQuestionID = amq.AuditConfigQuestionID
JOIN    incident.AuditConfigSection acs  ON acs.AuditConfigSectionID  = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID = 4
  AND   am.DateCreated >= '2026-05-01'
GROUP BY CAST(am.DateCreated AS date), acq.QuestionType
ORDER BY DiaAuditoria, acq.QuestionType;


-- ===========================================================================
-- PASO 7. Las auditorias de agosto. La de Hugo es la 959-30133 de Culver City.
-- ===========================================================================
SELECT  am.AuditMasterID, am.AuditMasterDescription, am.DateCreated,
        am.Status, am.Version, am.LastEdited, am.LastEditedBy
FROM    incident.AuditMaster am
WHERE   am.AuditConfigID = 4
  AND   am.DateCreated >= '2026-07-01'
ORDER BY am.DateCreated DESC;


-- ===========================================================================
-- PASO 0. Esquema de las tablas que faltan. Correr si hace falta llegar a
-- ScreenDetail por nombre de pantalla o a la auditoria por su numero.
-- ===========================================================================
SELECT  TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM    INFORMATION_SCHEMA.COLUMNS
WHERE   TABLE_SCHEMA = 'incident'
  AND   TABLE_NAME IN ('AuditMasterStore','AuditMasterSection','ScreenMaster','ScreenLabel')
ORDER BY TABLE_NAME, ORDINAL_POSITION;

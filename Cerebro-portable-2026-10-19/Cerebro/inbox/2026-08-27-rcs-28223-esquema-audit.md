# Esquema real del modulo Audit en Incident, tenant mcdonalds

Leido el 27 ago 2026 con INFORMATION_SCHEMA contra la base del tenant. Esto reemplaza cualquier
nombre de columna que se haya asumido antes.

## Lo que NO existe, y con que se reemplaza

    AuditConfig.Name                 no existe. El nombre vive en Description
    AuditConfig.Active               no existe
    AuditConfigSection.Name          no existe. Es SectionDescription, y hay SectionIdent
    AuditConfigQuestion.FieldType    no existe. El campo real es QuestionType
    AuditConfigQuestion.QuestionNumber  no existe
    AuditConfigQuestion.SortOrder    no existe. Es QuestionOrder real, y Orderby int
    AuditMaster.CreatedDate          no existe. Es DateCreated
    ScreenDetail.ScreenID            no existe. Es ScreenMasterID
    ScreenDetail.SortOrder           no existe. Es FieldOrder

David escribio "FieldType 35" y "FieldType 11" en el ticket. La columna se llama QuestionType.
El numero puede ser correcto. El nombre no. Corregirlo antes de que Engineering lo busque y no lo
encuentre.

## El hallazgo que cambia el diagnostico

`AuditConfigQuestion` trae tres columnas que definen la grilla:

    GridCols        nvarchar
    GridConfig      nvarchar
    GridCommentsYN  int

David concluyo el 24 ago: "This points to an application-level bug in the FieldType 35 render/save
path, not a data or configuration issue". Llego ahi mirando `ScreenDetail` y `AuditMasterQuestion`.
Nunca miro estas tres columnas. Son las que definen la grilla que no acepta entrada.

Si `GridCols` o `GridConfig` estan vacias para las preguntas rotas, el defecto es configuracion
perdida y el ticket va a Delivery, no a Engineering. Si estan pobladas, la conclusion de David se
sostiene y la escalacion sigue en pie. El paso 3 del SQL lo decide.

No escalar hasta correr esa consulta. Mandarlo a Engineering con la causa equivocada cuesta dias.

## Lo que explica la diferencia entre Manager y Crew

    ParentQuestionID  int
    ParentQuestion    int
    TriggerAnswer     nvarchar

En Manager, el disparador y la grilla van en una sola pregunta con Response Yes. En Crew van
separados y la segunda no tiene Response. Esas tres columnas modelan esa relacion. Confirma la
observacion que salio de las capturas.

## Lo que confirma a David

`AuditMasterQuestion` guarda `Answer` nvarchar y `Comments` nvarchar, una sola pareja de columnas
para toda pregunta sin importar su tipo. No hay deriva de esquema en el almacenamiento. Eso que
dijo David se sostiene.

Queda abierto como serializa una grilla de nueve columnas y dos filas dentro de un solo `Answer`
nvarchar. El paso 5 del SQL lo muestra si existe al menos una respuesta guardada.

## Columnas utiles que aparecieron

    AuditConfigQuestion.QuestionTextPlain    texto sin RTF, mejor para leer y comparar
    AuditConfigQuestion.DeleteFlag           filtrar borradas antes de contar
    AuditConfigQuestion.DoNotPrint           control de impresion
    AuditConfigQuestion.HideComments         relevante, el workaround del cliente es Comments
    AuditConfig.UseSectionLevelSecurity      seguridad por seccion, revisar si aparece permiso
    AuditConfig.QEEnabled                    bit NOT NULL, unico bit de la tabla
    AuditMasterQuestion.LockedByID           bloqueo de registro, descartar como causa

## Tablas cuyo esquema falta

`AuditMasterStore`, `AuditMasterSection`, `ScreenMaster` y `ScreenLabel`. Sin `ScreenMaster` no se
puede filtrar `ScreenDetail` por nombre de pantalla. Sin `AuditMasterStore` no se llega a la
auditoria 959-30133 por su numero. El paso 0 del SQL las vuelca.

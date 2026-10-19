RCS-28327 Instructivo

Cinco pasos. Los dos primeros cierran la validación que quedó abierta desde el 24 de agosto. El paso 3 se ejecuta con una de dos ramas según el resultado. El paso 4 es la transición. El paso 5 es independiente de todo lo anterior y ya está vencido por cadencia.

Paso 1. Confirmar en Composer a qué campo está atada la columna en blanco

Dónde se ejecuta: Secure 5.4 de Delhaize, UI. Lectura.

Qué hace: entra al perfil desde el que Becky vio el recibo, abre la búsqueda o vista donde aparece la columna Item Discount Description en blanco, ábrela en Composer, inspecciona la columna y anota el field ID literal al que está bindeada.

Qué se espera ver: el field ID coincide con el campo de tipo, el mismo que llama a Platform.GetExcelReferenceData. Si en cambio el field ID es code, la teoría de Edwin no aplica porque CODE ya trae loyalty discount en la base. Anota el resultado exacto antes de seguir al paso 2.

Si falla: si no ubicas la búsqueda exacta, pídele a Becky el nombre literal de la vista. No sigas al paso 3 sin este dato.

Paso 2. Confirmar si la enumeración de tipo de descuento existe en EnumerationReferenceData

Dónde se ejecuta: SQL contra el Platform DB del cliente 46. Solo SELECT.

El comando o la acción:

SELECT DISTINCT EnumerationType, [Key], Value FROM [46_Platform].[secure].[EnumerationReferenceData] WHERE EnumerationType LIKE '%Discount%';

Si el nombre de base no resuelve con el prefijo 46, verifica primero contra el Excel de client IDs cuál es el Platform DB que sirve la instancia 5.4 de Delhaize. No asumas que es el mismo 441 de ADUSA tenant, ese es otro identificador.

Qué se espera ver: filas con EnumerationType de descuento y sus pares Key, Value ya cargados, o cero filas.

Si falla: si no tienes acceso de lectura a ese Platform DB, pide el acceso puntual antes de escalar. No escales sin este dato, el documento del 24 de agosto ya advirtió que un ruteo a ciegas lo devuelve Peyman.

Paso 3. Pegar el comentario interno según el resultado del paso 2

Rama E, si el paso 2 devolvió filas para el tipo de descuento. La definición sigue llamando al xlsx muerto en vez de esta tabla. Pega este comentario, en inglés, sin editar:

Comment RCS-28327, version Engineering (pegar tal cual)

INTERNAL NOTE. NOT FOR CUSTOMER

Root cause investigation on this ticket, comment by Edwin Garzon on August 20, found that the reported symptom is not a data pipeline defect. Fifteen days passed since that finding with no action taken on it.

Environment. Production, Secure 5.4, client c046dhz, ARDMPROD.ARDM_046, Delhaize banner Food Lion.

Findings confirmed by Edwin Garzon on August 20. Transaction 2608025570789970641 carries CODE equal to loyalty discount in ARDM_ITEMDISCOUNT. The parser sets that value intentionally in pyardm/us/c046dhz/ardm/python/pd_pos_parser.py at lines 777 and 842 when it detects an AdvancedFrequentShopper or FrequentShopper POS event. The transaction data is correct.

Client 46 runs ARDM V3 with a text based itemdiscount schema. The definition itemdiscount.searchable resolves the displayed discount type text through Platform.GetExcelReferenceData pointed at /system/ebr/crdm/store/2_0/enumerations/crdm pos enumerations.xlsx. A SELECT against secure.Repo for that exact VirtualFilePath on client 46's Platform DB returned zero rows.

Validation completed today. Composer confirms the blank column is bound to the type field, the one that calls GetExcelReferenceData. A SELECT against EnumerationReferenceData for client 46 confirms the discount type enumeration already exists in that table.

Conclusion. The discount type enumeration for client 46 already exists in EnumerationReferenceData. The itemdiscount.searchable definition still calls the CRDM 2.0 xlsx path instead of that table. This definition was left behind in the V2 to V3 migration and it can affect every client migrated the same way, not only client 46.

Precedent. RCS-27761, same client 46, same reporter, Tender Check Amount blank on Payroll Check tender. Nikita Rathore found MediaNo 4 was missing because it originally mapped to paper Food Stamps. Engineering fixed it with a PR adding MediaNo 4. Same symptom family, an enumeration value missing at the platform level, resolved by Engineering.

Scope. Edwin states this is not isolated to loyalty discounts or to one store. It affects every item discount on this client where the type field renders through this same lookup.

Troubleshooting performed. Edwin Garzon queried ARDM_ITEMDISCOUNT and secure.Repo directly against production, read only, on August 20. I confirmed the Composer field binding and the EnumerationReferenceData content today, also read only. No AI assisted troubleshooting was used on the SQL or Composer steps recorded above. No conversation with Engineering happened outside this ticket before this comment.

What I need. Update itemdiscount.searchable to resolve the discount type description against EnumerationReferenceData instead of the CRDM 2.0 xlsx path for client 46. Confirm whether the same stale definition exists on other clients migrated from V2 to V3 and give a plan to check them.

Rama D, si el paso 2 devolvió cero filas en los dos lados. Pega este comentario en su lugar:

Comment RCS-28327, version Delivery (pegar tal cual)

INTERNAL NOTE. NOT FOR CUSTOMER

Root cause investigation on this ticket, comment by Edwin Garzon on August 20, found that the reported symptom is not a data pipeline defect. Fifteen days passed since that finding with no action taken on it.

Environment. Production, Secure 5.4, client c046dhz, ARDMPROD.ARDM_046, Delhaize banner Food Lion.

Findings confirmed by Edwin Garzon on August 20. Transaction 2608025570789970641 carries CODE equal to loyalty discount in ARDM_ITEMDISCOUNT. The parser sets that value intentionally in pyardm/us/c046dhz/ardm/python/pd_pos_parser.py at lines 777 and 842 when it detects an AdvancedFrequentShopper or FrequentShopper POS event. The transaction data is correct.

Client 46 runs ARDM V3 with a text based itemdiscount schema. The definition itemdiscount.searchable resolves the displayed discount type text through Platform.GetExcelReferenceData pointed at /system/ebr/crdm/store/2_0/enumerations/crdm pos enumerations.xlsx. A SELECT against secure.Repo for that exact VirtualFilePath on client 46's Platform DB returned zero rows.

Validation completed today. Composer confirms the blank column is bound to the type field, the one that calls GetExcelReferenceData. A SELECT against EnumerationReferenceData for client 46 confirms the discount type enumeration does not exist there either.

Conclusion. The discount type enumeration for client 46 does not exist in EnumerationReferenceData or in the CRDM 2.0 xlsx workbook. The lookup fails because the source content was never created for this client, not because the definition points to the wrong place.

Precedent. RCS-27761, same client 46, same reporter, Tender Check Amount blank on Payroll Check tender, was a missing enumeration value resolved by Engineering with a PR, not by Delivery. Confirm whether that precedent applies here before this stays with Delivery.

Scope. Edwin states this is not isolated to loyalty discounts or to one store. It affects every item discount on this client where the type field renders through this same lookup.

Troubleshooting performed. Edwin Garzon queried ARDM_ITEMDISCOUNT and secure.Repo directly against production, read only, on August 20. I confirmed the Composer field binding and the EnumerationReferenceData content today, also read only. No AI assisted troubleshooting was used on the SQL or Composer steps recorded above. No conversation with Engineering happened outside this ticket before this comment.

What I need. Create the missing enumeration content for client 46 with the correct type to description mappings for item discounts, either as the CRDM workbook or as EnumerationReferenceData rows. Confirm who owns Secure content setup for this client so the work gets assigned.

Paso 4. Transicionar según la rama usada en el paso 3

Rama E: transición a Under Engineering Review. El ENG se autocrea, no lo crees a mano. Asignación pasa a Shandana Khan según el procedimiento de Aimee Wadsworth.

Qué se espera ver: el ticket queda en Under Engineering Review, aparece el ENG vinculado, el assignee cambia a Shandana Khan.

Rama D: transición a Under Delivery Review. Asigna a Peyman Motlagh. Agrega el ticket al sprint RCS Support Team. Avísale a Peyman por Teams además de asignar, es la regla para Secure 5 en Delivery.

Qué se espera ver: el ticket queda en Under Delivery Review, assignee Peyman Motlagh, aparece en el sprint RCS Support Team.

Si falla: si Peyman devuelve el ticket, es porque el paso 2 se saltó o el resultado se leyó mal. Vuelve al paso 2 antes de reintentar la transición.

Paso 5. Actualizar a Becky, independiente de los pasos 1 a 4

Por qué: la cadencia exigida para Medium es semanal aun sin cambios. El último contacto fue el 27 de agosto, hoy son ocho días.

Pega este texto, en inglés, sin markdown:

Comment RCS-28327, respuesta a Becky (pegar tal cual)

Hi Becky,

Update on this one.

The investigation continues on our side. We are working through the platform configuration that controls how the discount description text displays for your account, and this needs review by another internal team before I can confirm anything.

I do not have a root cause confirmed yet. I will not share a cause until it is confirmed.

I need nothing further from you right now.

Thank you.

Qué se espera ver: comentario visible para el cliente en el ticket, sin cambio de estado asociado a este paso.

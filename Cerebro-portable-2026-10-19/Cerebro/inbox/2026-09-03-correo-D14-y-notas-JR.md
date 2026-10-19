# D14, 3 sep 2026. Correo, hallazgo y texto para el tracker de J.R.

Archivo: `adusa-envio-hoy/Appriss ADUSA-Support-Tracker - 09032026 D14.xlsx`. 49 tickets, 38 resueltos, 1 esperando información de Ahold, 10 activos con Appriss. Recalculado, cero errores, cero duplicados.

## RCS-28482, ya corregido

Tu resumen decía que RCS-28482 se transicionó a Under Engineering Review. La primera verificación en Jira mostró Work in progress. Hiciste la transición tú mismo después y confirmaste que había quedado en Under Engineering Review, reasignado a Shandana Khan. El D14 ya refleja ese estado, verificado en Jira en vivo por segunda vez.

## Correo de estado para Jim, con la sala en copia

Subject: ADUSA support tracker, 9/3 status

Jim, all,

Attached is today's tracker, verified directly against Jira.

RCS-28123 and RCS-28748 closed today.

Two new tickets opened today, RCS-28752 and RCS-28766.

Eleven tickets remain open: RCS-28093, RCS-28281, RCS-28482, RCS-28535, RCS-28589, RCS-28596, RCS-28667, RCS-28683, RCS-28693, RCS-28752 and RCS-28766.

Four of those are worth a look in the tracker. RCS-28482 and RCS-28683 both moved to engineering today after Appriss reproduced the errors directly. RCS-28667 has a full reproduction write-up. RCS-28693 connects to a broader store mapping fix Appriss is working on with the platform team.

Thank you.

## El link de SharePoint de Matt

Autorizaste por esta vez editar directamente el archivo de Matt. En lugar de texto en rojo se usaron comentarios nativos de Excel Online, uno por ticket, todos publicados hoy y todos con tu nombre como autor. Los ocho quedaron puestos y verificados uno por uno. Texto final de cada uno, tal como quedó en el documento:

**RCS-28535**, celda A45. 9/3: Pushed per J.R., not escalated. ENG-7181 advanced to Ready for Test on its own today.

**RCS-28482**, celda A61. 9/3: Reassigned to Shandana Khan. Reproduced directly in the tenant, found a working report that does show MISC. New theory: depends on the report's summary function, not report type. ENG clone still pending.

**RCS-28667**, celda A64. 9/3: Already in Under Engineering Review w/ Matthew Kamminga. Full reproduction steps documented today. ENG clone still pending, ticket is 5 days old.

**RCS-28123**, celda A65. 9/3: Closed as Completed. Field empty error confirmed resolved, duplicate of ENG 557 inside the unification work. Notification email symptom split off into RCS-28766.

**RCS-28693**, celda A66. 9/3: Not a support task, Vlad Bogus owns it. Waiting on Leigh Ann to confirm Harrison's test. No action needed from this side.

**RCS-28683**, celda A67. 9/3: ENG-8338 created and linked. RCS-28760 may be a duplicate of this same ticket, need to confirm before closing either one.

**RCS-28596**, celda A68. 9/3: Per the call, holding release past Friday given the long weekend. ENG-7904 still in Development Complete, in QA.

**RCS-28589**, celda A69. 9/3: Reopened, ticket carries no ENG key yet. Still working w/ Delivery to reproduce the export and confirm the storage path before escalating. Ajustado en el momento porque la nota existente en esa celda ya mostraba el ticket reabierto hoy, no en Under Engineering Review como decía tu resumen original.

# D16, 7 sep 2026. Verificación antes de generar el tracker

Revisé el borrador que quedó en la charla de RCS-28671 contra Jira en vivo. Tres cosas ahí estaban mal o incompletas. Esto es lo que hay que resolver antes de armar el archivo.

## Necesita que tú actúes en Jira

**RCS-28482.** Jim confirmó el 5 sep que los tabs ya funcionan y que reconstruye los reportes él mismo. No pidió nada. El ticket sigue en Work in progress en Jira, nadie lo transicionó. Si para ti está cerrado, ciérralo tú en Jira antes de que arme el D16, así el tracker sale correcto sin que yo tenga que inventar un estado que Jira no tiene.

## Necesita una respuesta a cliente, todavía no se ha mandado

**RCS-28784.** Cero respuesta humana en tres días, solo el acuse automático del viernes. Jim tuvo que avisarte que es un ticket de Secure y no de Incident porque nadie lo había tocado. Comentario listo para pegar, saludo a Becky LaPierre que es la reportera:

---

Hi Becky,

Thank you for the detail on this one.

This is a Secure ticket rather than Incident. Appriss has corrected the routing.

Appriss will check the transaction file for the store and transaction you supplied and confirm which price it carries for that item.

I need nothing from you on this one.

Thank you.

---

Compromiso que crea este texto: revisar el tlog y confirmar el precio. Anótalo.

## El borrador de correo tenía un problema de estilo

La respuesta a Jim sobre Cloudflare en RCS-28535 contaba el resultado de una prueba interna, un archivo de 5 MB que falló una vez y luego subió bien. Eso es un resultado de QA y no va al cliente, según cerebro-respuesta-cliente. Corregido, mismo hallazgo sin el detalle de la prueba:

"RCS-28535, on the Cloudflare question. Appriss made a change on that side related to attachment uploads. That change does not appear to explain what your Hannaford users are seeing on the longer files. Please have one of them retry an upload and send the file size and the time of the attempt, whether it succeeds or fails. That is the same information Appriss asked for on 8/26 and has not yet received."

## Un dato que corrijo del borrador viejo, no para el cliente

El D15 dijo que el fix de RCS-28596 ya estaba en QA. Verifiqué ENG-7904 en vivo y sigue en Development Complete, no pasó a QA. Corrijo la nota interna del tracker, no hay nada que decirle a Jim porque el comentario que le mandé el viernes no mencionó QA ni fecha.

## Verificado, sin acción necesaria, solo entra al tracker con su estado real

**RCS-28693.** Vlad le dio acceso a Harrison hoy a las 11:06 y le pidió a Leigh Ann que confirmara. Su respuesta de la 1:34 PM no confirma, vuelve sobre el caso de prueba de Paula y menciona una solicitud de acceso del jefe de Harrison que todavía no aprueba. Sigue esperando confirmación de Ahold.

**RCS-28752.** Vlad investigó a fondo hoy, encontró que el usuario solo tiene acceso a una de las dos tiendas duplicadas y lo pasó a ingeniería. Leigh Ann le hizo una pregunta directa a las 10:59 que Vlad no ha contestado todavía: "Is it because it's a duplicate store number but 2 different brands and picking up in alphabetical order?" Esto es de Vlad, no tuyo, lo dejo solo como aviso.

**RCS-28766.** Shandana se lo devolvió a Mohammed Mutahhar hoy a las 4:36 AM para que valide el análisis de causa raíz que Diego entregó el jueves. Diego ya le dijo a Leigh Ann el jueves que no hay ETA. Sin acción nueva de cliente pendiente.

**Sin cambios, verificados: RCS-28093, RCS-28281, RCS-28589, RCS-28667, RCS-28683.** Ninguno tuvo comentarios entre el 5 y hoy.

## Antes de que arme el archivo final

Dime si cierras RCS-28482 en Jira y si pegas el comentario de RCS-28784. El tracker y el correo van a reflejar lo que diga Jira en el momento que genere el archivo, así que el orden importa. Si prefieres que arme el D16 ya con el estado actual sin esperar esas dos acciones, también lo hago y quedan como pendientes del día.

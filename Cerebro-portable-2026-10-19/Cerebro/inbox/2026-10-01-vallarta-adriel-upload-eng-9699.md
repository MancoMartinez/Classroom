# Vallarta, Adriel Raygoza: acceso al portal y falla de subida de adjuntos (ENG-9699)

Fecha: 2026-10-01
Origen: Teams con J.R. Teagle 1:24 p.m., hilo Green Team de Nicolas Garcia 2:10 p.m., correo L1 de Shireesh R.

## Qué pasa
Adriel Raygoza (adriel.raygoza@vallartasupermarkets.com, +1 818-923-9217) no puede subir ningún adjunto a casos de Incident desde hoy. No está en el portal de soporte. J.R. pide aprobar acceso y averiguar qué pasa con Vallarta.

## Causa
Hipótesis. ENG-9699 reporta el mismo mensaje "The web server returned unexpected response." en demo7 PC, build de regresión 832307. Kiran lo reprodujo solo cuando Attachments vive en una página dinámica. Vallarta está en producción. Falta confirmar si ese build o ese cambio llegó a prod.

## Evidencia
Jira 1 oct 15:31 EDT: ENG-9699 Backlog, High, Unassigned, cero comentarios. Relacionados ENG-7181 (Reopened) y ENG-6910.
Teams 2:29 p.m. Kiran: "able to recreate it when the attachments is part of a dynamic page".
ENG-9252 "Remove clients: vallarta (PU)" Done 22 sep, sin descripción. Puede indicar migración de Vallarta a PC. Sin verificar.

## Qué hago hoy
1. Enviar el correo a Hector con Adriel en copia. Texto en 2026-10-01-vallarta-adriel-textos.md.
2. Responder a J.R. en Teams.
3. Preguntar en el hilo Green Team si el cambio aplica a prod.
4. Con la respuesta de Adriel, crear el RCS y enlazarlo a ENG-9699.
Regla del portal: si la aplicación estuviera caída por completo, se agrega primero y se valida después. Aquí falla una función, aplica la aprobación del admin.

## Precedentes
inbox/2026-08-31-correo-hector-acceso-noemi.md, mismo flujo con Noemi.
inbox/2026-08-31-vallarta-admins-portal.md, admins Hector Flores, Carlos Ardon, Noemi Casas.
NOTA-INTERNA-RCS-28022, santikos, ShowAttachments.aspx ausente tras migración.
RCS-28535, Hannaford, adjuntos y Cloudflare.

## Compromisos
Juan a J.R.: revisar el correo y arrancar el proceso hoy.

## Qué espero y qué hago con cada respuesta
Hector aprueba: agregar a Adriel en Customers, Organizations, Vallarta, Add Customer. Buscar antes por email.
Hector no responde hoy: escalar con J.R. para que lo empuje por su lado. La subida sigue en investigación igual.
Adriel manda datos: crear el RCS con caso, archivo, hora y captura. Enlazar a ENG-9699 y pegar los datos en el hilo Green Team.
Kiran confirma que aplica a prod: el RCS queda bloqueado por ENG-9699. Avisar a J.R.
Kiran dice que es solo staging: Vallarta es otro problema. Investigar el RCS por separado con los datos de Adriel.
Lo que más rápido destraba: los datos de Adriel. La respuesta de Kiran sin un caso de prod no confirma nada.

## Respuesta de Kiran, 1 oct tarde
Kiran: está investigando la subida intermitente y cree que es lo mismo que ve Vallarta. No reconoce "build 832307". Ese número sale de la descripción de Nicolas en ENG-9699, "Regression build 832307". Es la corrida de regresión, no un deploy.
Estado: RCS de Vallarta queda ligado a ENG-9699. Pendiente saber si retry sirve como workaround para el cliente.

## Kiran sube 56MB en Vallarta prod sin error, 1 oct 4:06 p.m.
Captura de Kiran: apps.apprissretail.com/vallarta, incident/432, Internal.aspx. Caso 2026-INT-52-8, Internal Merchandise Loss, tienda 52, CLOSED. Archivo .mp4 de 56MB listado en Attachments, Upload Date 10/1/2026 9:06 PM.
Lectura: la subida funciona en prod para Vallarta en esa pantalla. La falla de Adriel no es total. Depende de pantalla, tipo de caso, usuario, navegador o es intermitente. El dato de Adriel decide.
Pantalla probada por Kiran: Internal.aspx. ENG-9699 se reproduce en página dinámica, SinglePageExternal.aspx en demo7.

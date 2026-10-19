---
fecha: 2026-09-04
autor: Claude, siguiendo cerebro-ticket
tema: RCS-28709, pasos para avanzar hoy antes del fin de semana
---

# RCS-28709. Instructivo

Runbook. Ejecuta en este orden. Jira es de solo lectura, ningun paso de este instructivo lo escribe Claude en Jira.

## Paso 1. Decide cobertura del ticket para el fin de semana

Donde se ejecuta: decision de Juan, sin sistema.

Que hace este paso: Viraj Kansara sigue como assignee y sale por el fin de semana. El ticket es High y el sintoma acaba de repetirse en dos tiendas nuevas hoy. Decide si te quedas de guardia sobre este ticket hasta el lunes o si lo dejas en la rotacion normal de guardia.

Que se espera ver: una decision tomada antes de cerrar la sesion de hoy.

Si falla: si no hay nadie de guardia claro para un ticket High con perdida de datos activa, escalalo con tu lead antes de desconectarte.

## Paso 2. Lee el comentario interno de escalacion

Donde se ejecuta: lectura, archivo local.

Que hace este paso: abre `inbox/2026-09-04-rcs-28709-comentario-interno.md`. Es el texto completo listo para pegar en RCS-28709, en ingles, en markdown completo porque va a un comentario interno de Jira. Documenta la recurrencia de hoy en las tiendas 208 y 139, cierra los cuatro requisitos de Aimee y pide a Shandana que acepte el bug y cree el ENG vinculado.

Que se espera ver: el archivo contiene solo el texto pegable, sin encabezado en español.

## Paso 3. Pega el comentario interno en RCS-28709

Donde se ejecuta: Jira, escritura, autoriza Juan.

El comando o la accion: copia el contenido completo de `inbox/2026-09-04-rcs-28709-comentario-interno.md` y pegalo como comentario interno en RCS-28709.

Que se espera ver: el comentario visible en el historial del ticket, marcado como interno si el proyecto lo permite.

Si falla: si Jira no deja marcar el comentario como interno en este proyecto, revisa `brain/memoria/feedback_comentarios_reglas.md` antes de pegarlo como comentario publico.

## Paso 4. Manda el mensaje de Teams a Shandana Khan

Donde se ejecuta: Teams, escritura, autoriza Juan.

El comando o la accion: copia el contenido de `inbox/2026-09-04-rcs-28709-teams-shandana.md` y mandalo por Teams a Shandana Khan.

Que se espera ver: mensaje enviado. Este es el segundo ping sobre el mismo tema, el primero fue el 3 de septiembre y no tiene respuesta todavia.

Si falla: si Shandana no responde hoy, la decision de crear el ENG queda pendiente para el lunes. Deja esa constancia en el ticket antes de cerrar la sesion.

## Paso 5. Pega la respuesta a Angie Martinez en RCS-28709

Donde se ejecuta: Jira, escritura, autoriza Juan.

El comando o la accion: copia el contenido completo de `inbox/2026-09-04-rcs-28709-respuesta-angie.md` y pegalo como comentario dirigido a Angie en RCS-28709.

Que se espera ver: comentario visible para el cliente, sin fecha de arreglo, sin mencion de ingenieria ni de Screen Designer.

Si falla: no aplica, es un comentario, no hay condicion de fallo tecnico.

## Paso 6. Verifica la lista de Incident Types de Stater Bros

Donde se ejecuta: portal Admin del tenant Stater Bros, lectura.

Que hace este paso: entra a Admin del tenant y confirma que la lista de Incident Types sigue completa despues de las dos corridas de Build All Screens de esta semana. Esto responde al precedente de Santikos, RCS-28022.

Que se espera ver: el conteo de Incident Types coincide con el que tenia el tenant antes del 3 de septiembre.

Si falla: si la lista aparece vacia o incompleta, no ejecutes un tercer Build All Screens. Escala directo con Matthew Kamminga y Shandana Khan, y suma ese hallazgo al comentario interno del Paso 3 antes de pegarlo, o como comentario nuevo si ya se pego.

## Que sigue despues de estos cinco pasos

Registra lo trabajado hoy en la bitacora del ticket y deja que Claude recalcule la cola en la proxima sesion.

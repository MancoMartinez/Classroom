# Incidente ASDA — I1717_4_A2IPriceCast — 28 ago 2026

## Lo que llegó

Teams, Akshaya Purappanmane, 3:58 PM. Correo reenviado de ASDA porque el remitente no está en el portal. Cliente también llamó al Help Desk por el mismo tema y pidió unirse a un bridge call.

INC1838412 - AIS - Continuously receiving alerts for I1717_4_A2IPriceCast
Alertas continuas: "The request was canceled due to the configured HttpClient.Timeout of 100 seconds elapsing."
Aproximadamente 5000 mensajes acumulados en dead-letter queue.
OperationId: c3ffaa9dd3bca6a1fbc6ea40452293ca
Timestamp: 8/28/2026, 3:28 PM
Link de bridge call en el mensaje original de Teams.

## Verificado antes de escribir esto

- Jira (`trebuco.atlassian.net`, solo lectura): no existe ningún ticket RCS con "A2IPriceCast", "1838412" ni "ASDA"+"PriceCast". No hay ticket abierto todavía, ASDA no lo cargó al portal.
- Cerebro (`bin/buscar`): sin precedente de "A2IPriceCast", "I1717" ni "AIS" en conocimiento, tickets ni investigaciones. Es la primera vez que aparece este nombre de tarea.
- El patrón del nombre `I1717_4_A2IPriceCast` coincide con la convención de HATR (el runner de tareas programadas de Secure Platform): el lock distribuido se arma como `{ClientID:000}xTaskName`. Fuente: `brain/markdown/14-appriss-ingeniería-docs-fuente.md`, sección HATR. 1717 leería como ClientID, A2IPriceCast como el nombre de la tarea. Esto es lectura de Claude sobre la convención, no está confirmado contra el sistema real.
- Hora de verificación: 21:13 UTC del 28 ago. Con la tabla de on-call, esa hora cae en la ventana de SRE Americas (20:00-5:00 UTC pagina Americas, 5:00-20:00 UTC pagina Europe). Fuente: `brain/markdown/25-on-call-operación-escalación-jsm.md`.

## Por qué esto es P1 y no cola normal

Framework de triage del on-call guide (`brain/markdown/25-on-call-operación-escalación-jsm.md`): sistema no procesa, dato que no carga, cliente con llamada activa pidiendo bridge call. Encaja en P1 High/Critical, no en P2 ni P3. Un dead-letter queue creciendo es pérdida de datos en curso, no un problema estético.

## Pasos, en orden

1. Confirmar si ya existe un incidente JSM/Operations abierto para esta alerta antes de duplicar esfuerzo. El monitoreo debería haber generado su propio page, separado del correo que reenvió Akshaya.
2. Si no hay ticket RCS, crear uno ahora con prioridad Critical/High, Product Type = Incident (no Secure 5), resumen que incluya el OperationId y el timestamp exactos.
3. Escalar a Secure/Incident Engineering (Under Engineering Review, se autoasigna a Shandana Khan, se autocrea el ENG). Antes de mover el ticket dejar escrito: entorno, el texto completo de la alerta con OperationId y timestamp, y la lectura de que el patrón de nombre corresponde a HATR. Avisar al cliente que el ticket se está moviendo a ingeniería.
4. No entrar solo al bridge call. Traer a alguien de Secure/Incident Engineering, SRE Americas dado el horario UTC actual, antes de o al inicio de la llamada.
5. En la llamada: reconocer el impacto primero, ser transparente sobre que se está investigando, no prometer causa raíz todavía, dar update cada 30 minutos mientras el P1 siga activo.
6. Escribir nota de handoff completa en el ticket JSM si se escala fuera de tu equipo: qué investigaste, qué descartaste, qué necesita saber el siguiente owner.

## Actualización, segunda pasada con Jira y Confluence en vivo

Encontré el ticket real: **RTS-206675**, "INC1838412 - AIS - Continuously receiving alerts for I1717_4_A2IPriceCast". Se creó solo, por el correo entrante, a las 16:26:00 -0400 (20:26 UTC). El remitente original es Joy Koppully, Major Incident Management de ASDA, con copia a `AsdaTechMajorIncident@asda.uk` y a Simon Myatt. Los tres, fuera del portal.

El ticket ya está en **Closed, Resolution Resolved**. Eso no significa que el incidente esté resuelto. Léelo en los comentarios: Akshaya confirmó que ni Joy ni Simon están en el portal, reenvió el correo al equipo y cerró el RTS con la nota *"We have forwarded the Email to the respective team to have a check on this issue. As no further action is required we will close this ticket"*. Cerró su parte del intake, no el incidente. El primer comentario automático, de `svc rts`, dice *"CASD ticket created and assigned to TSOC support"*, la misma frase boilerplate que traen todos los tickets de monitoreo de RTS ese día (Grafana, PRTG, Report Server Monitor). No es una señal de que ya hay alguien de ingeniería trabajando el caso puntual, es el pipeline automático de intake de cualquier alerta.

Busqué "A2IPriceCast", "I1717", "AIS", "PriceCast" en Confluence completo. Cero resultados con match real. No hay runbook, no hay página de arquitectura, no hay precedente documentado en toda la wiki de Appriss para este nombre de tarea. Tampoco hay ningún ticket RCS, ENG ni DATASCI abierto sobre esto. **RTS-206675 es el único registro que existe del incidente, y está cerrado.**

Conclusión: nadie de Appriss tiene todavía un ticket vivo rastreando este incidente. El correo de Joy dice que el bridge call ya está en curso del lado de ASDA. Que el intake esté cerrado no cambia que el dead-letter queue sigue creciendo y que Major Incident Management de ASDA espera gente de Appriss en esa llamada.

## Qué hacer ahora, en orden

1. Reabrir o crear el ticket que rastree el incidente real. RTS-206675 se puede reabrir con una nota que aclare que el cierre fue solo el intake de L1, o crear uno nuevo en RCS/RTS con prioridad Critical y Product Type Incident, citando el OperationId `c3ffaa9dd3bca6a1fbc6ea40452293ca` y el timestamp 8/28 3:28 PM.
2. Camila ya está en copia por el reenvío de Akshaya, así que la escalación a tu líder ya ocurrió. No hace falta abrirla de nuevo, sí confirmarle que la viste.
3. Como no hay dueño de ingeniería identificado en ningún sistema para "A2IPriceCast" ni "AIS", entra a la llamada para levantar esa información en vivo. Pregúntale directamente a ASDA o a quien esté en el bridge qué equipo interno de Appriss owns ese pipeline, ya que ni cerebro ni Confluence lo tienen documentado.
4. No entres a prometer una causa raíz. Seguí el estándar del on-call guide: reconocer el impacto primero, ser transparente sobre que se investiga, dar update cada 30 minutos mientras el P1 siga activo.
5. Al salir de la llamada, con nombre de equipo y dueño en mano, deja la nota de handoff completa en el ticket que abriste en el paso 1: qué se investigó en la llamada, qué se descartó, quién quedó a cargo.

## Corrección con los adjuntos que mandó Juan

CLIENT_ID de ASDA es 105, no 1717. La teoría de que I1717 fuera el ClientID dentro de la convención de lock de HATR queda descartada, era lectura mía sin confirmar y la pantalla de cuenta la desmiente. Sigue sin identificarse qué es el 1717.

Ni Joy Koppully ni Simon Myatt existen como customers en la cuenta de ASDA. El auto-reply que salió a las 2:21 AM (`[RTS-206675] Re: ...`) es el canned de portal: agradece el contacto, dice que se reenvió al equipo correcto y pide que de ahora en adelante entren por `support.apprissretailcloud.com`. Fue systema/L1, no Juan ni Camila.

ASDA es cuenta High-Touch, CSM Shaun Callow.

## Proceso real para gente fuera del portal, con precedente

`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md`, sesión KT Kristin 15-jul, casos LULU (RCS-27843) y Samsung (RCS-27847), es el precedente exacto para este dilema. Regla destilada ahí: **el buzón existe para gente fuera del portal. Todo trabajo se formaliza como ticket venga por donde venga.** El ticket no es para que el cliente lo vea, no puede, es solo para que soporte lo trabaje. Se elige un reporter registrado para que las notificaciones fluyan, se apaga la notificación automática al cliente si alguien más lleva la comunicación, y se deja nota interna explicando que el enrutamiento es excepcional.

En el caso Samsung, Juan quedó como reporter porque no había nadie de la cuenta en el portal, y la comunicación con el contratista fue por correo directo, excepción a la regla general de comunicarse por el portal.

Aplicado a este incidente: el ticket y la respuesta al cliente no son alternativas, son dos cosas separadas que van en paralelo. El ticket registra el trabajo del lado de Appriss y dispara la escalación real a ingeniería. La respuesta a Joy es aparte, por correo directo, no el canned de portal que ya salió solo. Kristin responde desde su correo personal en estos casos para que el cliente tenga a quién volver a escribirle.

## Cómo crear el ticket, campo por campo

Verificado contra el schema real de RCS, proyecto id 19251, issue type Incident id 10102. Botón Create en Jira, arriba.

Project: Retail Customer Support (RCS).

Issue Type: Incident. Es el único tipo que trae esta metadata para RCS, la descripción del propio campo dice "Issue is related to a production outage."

Summary, pega esto tal cual:
```
ASDA - INC1838412 - AIS - Continuously receiving alerts for I1717_4_A2IPriceCast
```

Description, pega el texto literal del correo de Joy, nada resumido ni parafraseado:
```
From: Joy Koppully <Joy.Koppully@asda.uk>
Sent: Saturday, August 29, 2026 1:54:56 AM (UTC+05:30)
Subject: INC1838412 - AIS - Continuously receiving alerts for I1717_4_A2IPriceCast

Hello Appriss Retail

Please join the ongoing bridge call for the above-mentioned incident.

We are continuously receiving alerts for I1717_4_A2IPriceCast with "The request was canceled due to the configured HttpClient.Timeout of 100 seconds elapsing."

As a result of these failures, approximately 5,000 messages have accumulated in our dead-letter queue so far.

OperationId: c3ffaa9dd3bca6a1fbc6ea40452293ca
Timestamp 8/28/2026, 3:28 PM

Bridge call: https://teams.microsoft.com/meet/358067307824134?p=CAc7pui4YDyWwsApJz
```

Priority: Critical. El campo trae Critical, High, Medium, Low, Undefined. Con dead-letter queue creciendo y Major Incident Management de ASDA en llamada, no es High.

Reporter: déjalo en blanco. El campo trae default value, cae solo en el usuario que crea el ticket, que serías vos, igual que en el caso Samsung.

Product Type (cf 15196): Incident (f.k.a. LPMS). Es la familia que corresponde a Secure Incident, separada de Secure 5. Confírmalo en la llamada si en ingeniería te dicen que AIS vive en otro dominio, este campo se puede corregir después.

Problem (cf 15195): Performance Degradation. Mismo criterio que se usó en RCS-28075 para timeouts. Si en la llamada confirman que el pipeline está completamente caído y no solo lento, cámbialo a App Down.

Account Service Level (cf 18873): High-Touch. Coincide con lo que muestra la ficha de cuenta de ASDA.

Business Impact (cf 18384), campo libre, pega esto:
```
Approximately 5,000 messages accumulated in the dead-letter queue for I1717_4_A2IPriceCast and growing. ASDA Major Incident Management opened a bridge call.
```

Priority Justification (cf 18872), campo libre, pega esto:
```
Production data pipeline failing continuously with growing dead-letter queue. Customer escalated as Major Incident with an active bridge call.
```

Labels: opcional, podés agregar `FromEmail` para que quede la misma trazabilidad que traía RTS-206675.

Después de crear, primer comentario interno, no al cliente, explicando el enrutamiento excepcional:
```
Reporter is not a registered portal contact for ASDA. This came in via help@appriss, forwarded by L1 (Akshaya Purappemane) after confirming Joy Koppully and Simon Myatt are not in the portal. The automatic intake ticket RTS-206675 was closed by L1 as intake only, no engineering action was taken there. This ticket is the working record for the incident.
```

## Lo que no se hizo

No se unió al bridge call, no se reabrió ni comentó nada en Jira, no se confirmó contra el sistema real si 1717 es el ClientID de ASDA ni qué equipo interno es dueño de A2IPriceCast. Todo lo anterior queda para que Juan lo ejecute.

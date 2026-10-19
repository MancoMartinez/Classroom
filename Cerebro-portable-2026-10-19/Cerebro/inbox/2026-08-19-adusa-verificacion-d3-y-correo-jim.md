# ADUSA · verificación final antes del D3 · 19 ago 2026

## Verificación en vivo contra Jira (justo antes de generar el D3)

De los 7 comentarios sugeridos ayer, los 7 quedaron pegados tal cual en Jira. Confirmado.

Dos cosas de la lista de acción NO se aplicaron todavía, verificado ahora mismo:

RCS-28342 sigue en Under Customer Review en Jira en vivo. La transición a Work in progress
que quedó sugerida no se hizo. El D3 refleja esto literal (Under Customer Review), no lo que
se había recomendado, porque la columna de estado tiene que ser un espejo exacto de Jira.

RCS-28177 sigue Closed, pero el aviso de la automatización de Jira ("Needs Attention - Add
Resolution", segundo dropdown de Resolution Details vacío) sigue siendo el último comentario
del ticket, sin atender, desde las 12:11pm de hoy. Esto no bloquea el D3 porque de cara al
cliente el ticket está cerrado y Jim ya confirmó que funciona, pero alguien con permiso
(Viraj) debe entrar, transicionar a Completed y llenar el segundo dropdown para que
desaparezca esa bandera interna.

Ninguna otra cosa de la lista de ayer quedó pendiente.

## D3 generado

Archivo: Appriss ADUSA-Support-Tracker - 08192026 D3.xlsx, construido sobre la estructura del
D2 (mismo formato de 9 columnas por tema, sin Engineer/Cause/Priority). Cambios reales
aplicados, todos verificados en vivo:

RCS-28177: Under Customer Review to Closed. RCS-28342: estado se corrige a Under Customer
Review (el D2 tenía Work in progress por error, la transición real nunca se aplicó), categoría
pasa a Awaiting Ahold input porque ahora depende de que Jim diga qué cuenta usar. RCS-28093:
Work in progress to Accepted into Development. RCS-28378: categoría pasa a Pending Ahold
verification en vez de Resolved, porque Leigh Ann nunca confirmó. RCS-28413: Work in progress
to Completed, categoría a Resolved. RCS-28281: categoría pasa de Awaiting Ahold input a Active
with Appriss, con las cifras de backfill que diste (8/10 en 1,824,936; 8/16 en 1,864,852).
RCS-28292: categoría pasa de Awaiting Ahold input a Active with Appriss, con la confirmación de
SFTP de April. RCS-28365: corrección menor de Completed a Closed para calzar con Jira real.

Tabla resumen recalculada: total sigue en 35 tickets, Resolved 21, Pending Ahold verification 2,
Awaiting Ahold input 1, Active with Appriss 11.

## Correo para Jim

Formato JR, recortado a solo lo necesario (tres preguntas reales, nada repetido):

```
Hi Jim,

Thanks for the quick turnaround on testing and for looping in the team on the open items.
A few things I still need from you directly, separate from the tracker.

1. RCS-28342 - We found Janai's title sitting on a second, disabled account
(Janai.Harrison1@adusa.com) rather than her active one, and Stacie's and Melanie's active
accounts still show no title. Should the disabled account become the one in use for Janai,
or is there a different account we should treat as primary?

2. RCS-28196 - Leigh Ann asked if other incident entry pages have the same null default.
Do you or she already have specific pages in mind, or would you like us to check the other
entry pages directly?

3. RCS-28378 - Following up again, were you able to confirm with your team whether the
Save and Next buttons on the Hannaford case are working now?

Thanks,
```

No se incluyeron 28093, 28292, 28407 ni 28161 porque ya están cerrados de cara a Jim, ya
tienen respuesta, o el comentario en Jira ya cubre lo necesario sin requerir nada de vuelta.

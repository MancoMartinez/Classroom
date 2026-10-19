# TBI · Meeting with Matt and J.R. · October 16

Internal meeting guide / Guía para reunión interna

[ENGLISH](#english) · [ESPAÑOL](#español) · [EVIDENCE / EVIDENCIA](#evidence--evidencia)

Tickets: [RCS-29451 · Access investigation](https://trebuco.atlassian.net/browse/RCS-29451) · [ENG-10069 · Security ID defect](https://trebuco.atlassian.net/browse/ENG-10069) · [RCS-28256 · Original investigation](https://trebuco.atlassian.net/browse/RCS-28256)

## English

Opening: Matt, following our call with TBI, we need to decide whether an explicit Security ID would help, clarify the location model for SSU offices and DCs, and agree on owners and the next validation.

### 1. Explicit Security ID
J.R. asked whether TBI could send the Incident Security ID explicitly instead of deriving it from the teams file. Would that bypass the failure covered by [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069), or use the same assignment path? If viable, which file, field, values and precedence over team mappings and manual overrides would we support?

### 2. First sign in and returning users
Rachel had level 5 in SSO+ before account creation, but her first SSO sign in created a NULL SecurityID while assigning groups and a team. Christi has an older persistent level assignment and also had a blank account level. Does [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069) cover both paths, or does the returning user case need separate investigation?

### 3. Immediate recovery
TBI says some users sign in only once or twice a year. Can we reconcile existing blank Security IDs safely without waiting for another login? Who would own that work, how would we preserve intentional overrides, and what test would approve it?

### 4. SSU offices and DCs
Chris originally received 90002005; Colton confirmed 40002005 as his correct location. The customer showed SSU in the Brand column. Ryan said it appears we add the 9 but did not recommend replacing it with 4. What is the intended model: a distinct office/DC location or a mapping to an existing brand location? Where can we verify the current SnowTime rule?

### 5. Which source needs correction?
Which source defines valid locations, and which supplies user assignments? If a DC must be added or mapped, who owns each change and how does it reach both Secure and Incident? Chris's hierarchy was corrected manually; incident creation still needs confirmation.

### 6. Feed freshness
The October 15 investigation found security assignment timestamps still at October 13, although ReferenceDataBackLoad ran without reported errors. TBI showed a file named for October 14. What batch, receipt and processing evidence can confirm the latest data reached SSO+? Under SnowTime, are unchanged row timestamps expected?

### 7. Owners and next checkpoint
[ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069) is currently Backlog and unassigned. Who takes the security defect, who owns the SnowTime/location investigation, and should the latter have separate technical tracking under [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451)? What evidence and next update date can we agree before closing?

Close: Before we finish, can we confirm the chosen approach, the owner for each workstream, and the date of the next update?

## Español

Apertura: Matt, después de la llamada con TBI necesitamos decidir si ayudaría recibir el Security ID explícito, aclarar el modelo de ubicaciones para oficinas y DC con SSU y acordar responsables y la próxima validación.

### 1. Security ID explícito

¿Enviar el ID directamente evitaría el fallo de [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069) o pasaría por el mismo flujo? Si sirve, ¿qué archivo, campo y valores admite, y qué prioridad tiene frente a teams y ajustes manuales?

### 2. Alta y usuarios existentes. Rachel tenía nivel 5 en SSO+ antes de crearse la cuenta, pero quedó NULL mientras sí recibió grupos y team. Christi tenía una asignación persistente antigua y también apareció sin nivel

¿[ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069) cubre ambos casos o hay que investigar aparte el regreso de usuarios existentes?

### 3. Recuperación inmediata. Algunos usuarios entran una o dos veces al año

¿Podemos corregir las cuentas sin nivel sin esperar otro login? ¿Quién lo hace, cómo preserva ajustes intencionales y qué prueba autoriza la corrección?

### 4. Oficinas y DC con SSU. Chris recibió 90002005 y Colton confirmó 40002005 como ubicación correcta. Ryan indicó que aparentemente agregamos el 9, pero no recomendó sustituirlo por 4

¿El modelo exige una ubicación propia para oficinas/DC o mapearla a una marca existente? ¿Dónde comprobamos la regla actual de SnowTime?

### 5. Fuente y dueño de ubicaciones

¿Qué fuente define las ubicaciones válidas y cuál asigna usuarios? ¿Quién corrige cada una y cómo llega a Secure e Incident? Chris tiene jerarquía corregida manualmente; falta confirmar creación de incidentes.

### 6. Vigencia del feed. La investigación del 15 encontró fechas de asignación del 13, aunque la tarea terminó sin errores reportados. El cliente mostró un archivo con fecha 14 en el nombre

¿Qué evidencia de recepción, lote y procesamiento prueba qué datos llegaron? ¿Es normal que no cambien las fechas de filas sin modificaciones?

### 7. Dueños y próximo control. [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069) sigue Backlog y sin asignar, verificado hoy en Jira

¿Quién toma el defecto y quién la investigación SnowTime/ubicaciones? ¿Necesita seguimiento técnico separado bajo [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451)? Acordar evidencia pendiente y fecha del próximo update.

Cierre: Antes de terminar, confirmemos la opción elegida, el responsable de cada frente y la fecha del próximo update.

## Evidence / Evidencia

Open only if needed / Abrir solo si hace falta.

| Topic / Tema | Direct evidence / Evidencia directa |
| --- | --- |
| Rachel, first login and level 5 | [Internal escalation with timeline](https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050) · [Detailed log investigation](/Users/MancoMenStudio/Cerebro/inbox/2026-10-15-rcs-29451-logs-securityid.md) |
| Ryan: origin of 9, SnowTime and replication | [Ryan, first screenshot](/var/folders/8b/2nrxtyfs4vxbq0mxypj9x0n40000gp/T/codex-clipboard-4f97a524-93b0-432a-95be-6988e4760767.png) · [Ryan, follow-up screenshot](/var/folders/8b/2nrxtyfs4vxbq0mxypj9x0n40000gp/T/codex-clipboard-20517b57-1419-4a5f-a817-cf7a1ca6a581.png) |
| SSU in Brand column and customer file | [Customer screen and transcript](/var/folders/8b/2nrxtyfs4vxbq0mxypj9x0n40000gp/T/codex-clipboard-e7e8acb7-9829-42af-b101-936b7b589b5b.png) |
| Chris, location 40002005 | [Hierarchy screen and transcript](/var/folders/8b/2nrxtyfs4vxbq0mxypj9x0n40000gp/T/codex-clipboard-48e3bca6-c3e3-42d1-ab64-ebef27206a21.png) |
| Infrequent logins | [Mike's explanation and customer examples](/var/folders/8b/2nrxtyfs4vxbq0mxypj9x0n40000gp/T/codex-clipboard-11eb1590-dfd5-491a-84f0-ec500e49cdc4.png) |
| J.R.'s explicit field question | [J.R. transcript](/var/folders/8b/2nrxtyfs4vxbq0mxypj9x0n40000gp/T/codex-clipboard-d47dfa99-2de6-4ca2-a30d-8fe221db1170.png) |
| Full prior context | [Claude dossier](</Users/MancoMenStudio/.codex/attachments/5c3b1859-30e5-41bf-83be-fa51d9e8e4b4/Texto pegado.txt>) · [Full investigation](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-incident-id-analisis.md) |

Reading cautions / Precisiones:

Ryan said it appears we add the 9; the current SnowTime rule still needs verification. Do not assume a bulk replacement with 4 is correct. Successful task execution does not prove which file was processed. A second login is not a validated universal fix. The explicit Security ID approach is a question for Matt, not an approved workaround.

Ryan indicó que aparentemente agregamos el 9; falta comprobar la regla actual de SnowTime. No asumir que corresponde reemplazarlo masivamente por 4. Una tarea exitosa no prueba qué archivo se procesó. Un segundo login no es una solución universal validada. El campo Security ID explícito es una opción por evaluar con Matt.

Status checked live when preparing on October 16: RCS-29451 Accepted into Development, Shandana Khan; ENG-10069 Backlog, unassigned. These can change; use the ticket links above.

Este archivo unifica y sustituye los dos archivos de preguntas anteriores para uso en esta reunión. Las preguntas ya pasaron verificar_borrador interno sin bloqueantes; esta edición conserva el contenido y añade navegación, traducción y enlaces.

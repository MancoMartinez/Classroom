# Guía: cómo armar un RCA para un cliente (Appriss)

Consolidado el 18 ago 2026, verificado contra Confluence, Jira y el disco. Referencia
permanente, no se borra al cerrar el caso de Stater Bros.

## 1. Los dos documentos, nunca uno solo

| | Shorthand RCA | RCA Report |
|---|---|---|
| Qué es | 2-3 frases: qué pasó, impacto, causa si se conoce, resolución corto/largo plazo | Documento completo aparte |
| Dónde va | Pegado directo en el ticket o por correo | PDF adjunto |
| SLA (Critical/High) | 1 día desde la **resolución** | 10 días desde la **resolución** |
| SLA (Medium/Low) | 10 días desde la resolución | (no aplica / mismo shorthand) |
| Plantilla Confluence | RCA Ticket Template (474654900291) | RCA Report Template (474654965776) |

**El reloj corre desde que el incidente se resuelve, no desde que el cliente lo pide.**
Si el outage sigue activo, lo único que corresponde entregar es el Shorthand, y hay que
decírselo al cliente con esa razón, no quedarse callado.

## 2. Antes del RCA: el ticket OUTM

El "Outage Ticket Process" (Confluence RTS 478022696993) dice que todo outage genera un
ticket en el proyecto **OUTM** con: Description, Environment, RCS tickets vinculados,
Timeline (start/end), Classification (Issue Level, Availability %, Impact, Urgency),
Scope, Root Cause, Alerting. Ese ticket es la fuente del Timeline que después pide el
RCA Report. **Si no existe, hay que crearlo o pedir que se cree antes de escribir el RCA
a mano** — sin él, el Timeline se arma de memoria y eso es lo que después no cuadra.

## 3. Plantilla del RCA Report (RSI 474654965776)

```
<Título>
Date: <fecha del incidente>
Author: <autor>

Introducción / Summary
<resumen del incidente y el impacto>

Incident Details
  Timeline: tabla Date | Time (UTC) | Description
  Impact: sitios afectados, volumen de requests, ventana de tiempo
  Root Cause: descripción
  Resolution: cómo se resolvió
  Recurrence Preventative Measures: qué se hace para que no vuelva a pasar
```

## 4. Quién lo escribe (RSI 474840268801)

Cualquiera que estuvo involucrado, aunque sea de paso, tiene la responsabilidad de que
el RCA arranque. Una vez arrancado, la info clave se comparte con el Delivery Manager y
el Senior Implementation Consultant, que arman el documento final para el cliente.
Usar el comentario interno del ticket para todo lo sensible mientras se investiga.

## 5. Los tres Claude Skills que ya existen para esto

Documentados por Dean Korbakis, **ninguno instalado todavía en esta máquina**. Se instalan
desde Claude Code → Settings → Skills → Install from file. Los archivos `.skill` están
adjuntos a sus páginas de Confluence.

| Skill | Página | Qué hace |
|---|---|---|
| `appriss-rca-generator` (de Avi) | RTS 477550018564 | PDF interno con branding, base de los otros dos |
| `appriss-rca-generator-retro` | RTS 477856825345 | Antes del final: worksheet pre-llenado desde el ticket de Jira. Marca en verde lo que ya se sabe, deja en blanco lo que necesita respuesta de ingeniería (5-Whys, Root Cause, Business Impact) |
| `appriss-rca-generator-external` | RTS 477584359429 | Convierte eso en el PDF para el cliente: sin nombres, sin tickets de Jira, sin jerga interna, 13 secciones fijas, cadena de 5-Whys en lenguaje plano |

**Orden correcto: retro primero, external después.** El retro te dice con precisión qué
falta por preguntar; sin eso se termina preguntando cosas que ya estaban en el ticket.

Reglas duras de la versión externa (RTS 477584359429): nunca nombres de personas propias,
dueños de action items siempre por rol ("Appriss Retail Engineering Team", nunca "John
Smith"); nunca números de ticket Jira internos; nunca "Internal Use Only"; si la causa no
está confirmada, escribir "Under investigation", no especular; ante la duda, se deja por
fuera. Nombre de archivo: `RCA<YYYYMMDD>-<Cliente>-<TemaCamelCase>-External.pdf`.

## 6. Los dos precedentes reales, comparados

**RCS-20226 (marzo 2025, Secure EBR).** Informal: se prometió el PDF, se adjuntó una
semana después sin rastro de proceso en el ticket. Sirve solo para confirmar el
mecanismo de entrega (adjunto + "Support Resolved - Provided Requested Information"),
no como ejemplo de comportamiento.

**RCS-27009 (mayo-junio 2026, Sainsbury's, Dean Korbakis — mismo puesto que Juan).**
Este es el molde de comportamiento a seguir:
1. La causa técnica se investiga y confirma primero en Teams por quien la vivió, antes
   de prometerle nada al cliente.
2. Se anuncia una llamada interna con los ingenieros involucrados antes de escribir nada.
3. Si esa llamada no basta (gente de vacaciones), se avisa el retraso con la razón real,
   no en silencio.
4. El RCA solo se publica cuando la causa está confirmada por quien la investigó.
5. Ante una pregunta directa del cliente sobre responsabilidad, la respuesta es corta y
   honesta, sin sobre-explicar.

## 7. Checklist de arranque, en orden

1. Confirmar si el incidente está realmente resuelto. Si no, escribir solo el Shorthand
   y decir por qué el Report todavía no corresponde.
2. Verificar o pedir que se cree el ticket OUTM.
3. Reunir toda la evidencia ya disponible en Jira/Teams (esto lo hace Claude, no hay que
   pedirle a otra persona que la reúna si ya está escrita en un ticket o comentario).
4. Instalar los tres skills si no están instalados.
5. Correr `appriss-rca-generator-retro` con el ticket RCS/RTS correspondiente. Revisar
   qué quedó en verde (ya resuelto) y qué quedó en blanco (de verdad falta).
6. Conseguir solo lo que de verdad falta, directamente de quien lo sepa, con una pregunta
   concreta, no un pedido genérico de "reúne información".
7. Correr `appriss-rca-generator-external` para el PDF final.
8. Publicar como adjunto en el ticket, comentario "Provided RCA", esperar confirmación
   del cliente antes de cerrar. Cerrar es dos pasos: Resolve → Completed, después Close.

Ver también `2026-08-18-brief-reunion-adusa.md` para el caso Stater Bros específico que
disparó esta guía, y las memorias `project_rcs_...` relacionadas con RCS-28431/28058.

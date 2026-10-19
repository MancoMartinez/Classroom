RCA Smart Alerts, 29 septiembre 2026. Borrador interno local para retrospectiva.

Entregable: inbox/2026-09-29-smart-alerts-rca-internal.docx. Incluye la plantilla Internal RCA 474709983443, cronología, impacto, corrección, causa, acciones propuestas, hoja de reunión y fuentes. No publicado ni enviado.

Causa confirmada: ENG-9486 documenta que targetFramework="4.8", PR 57544, expuso un deadlock entre Await y GetAwaiter().GetResult(). El fix añade ConfigureAwait(False) a dos Await. Sustituye la explicación de serialización y exceso de tráfico del 28/9. Algunos correos llegaron antes del bloqueo y no registraron historia.
Fuente: https://trebuco.atlassian.net/browse/ENG-9486

Evidencia: revisados 20 comentarios de RCS-29026, 10 de RCS-29123 y confirmación pública de Joe en RCS-29145. Leídos 76 mensajes del hilo Teams Retail Ops > AALPS Issues > RCS-29123, del 27/9 al 29/9 10:23 Bogotá. Kiran confirmó EU/US desplegados y aclaró que no probó producción. Soporte publicó validación ADUSA; Joe confirmó Vitamin Shoppe el 28/9 16:42 EDT.

Estados vigentes: RCS-29026 y RCS-29123 Under Customer Review; RCS-29145 Completed; ENG-9486 Development Complete; ENG-9533 Done; ENG-9589 Backlog. Q4 en ENG-9589 es planificación automática, no compromiso.

Separar RCS-29026: la causa del caso 0619-27 del 20/9 sigue sin confirmar. Success no demuestra entrega. Duplicados, CRLF y tamaño son hallazgos aparte.

Hoy: Juan coordina retro con involucrados y Kara, verifica PBM, confirma alcance, horarios, causa sistémica y fechas. Solicitud J.R. 29/9 08:52 Bogotá; política exige programar en 48 horas. Objetivo final: cinco días hábiles desde confirmar causa. Plan conservador: 2/10, por solución registrada 27/9; validar hito y calendario. No hay reunión ni entrega comprometida por este documento.

Política: https://trebuco.atlassian.net/wiki/spaces/PBM/pages/478066671617
Flujo v8: https://trebuco.atlassian.net/wiki/spaces/PBM/pages/478038687749
El flujo pide etiqueta Problem Management para PBM. Juan hace cambios Jira. Aprobaciones externas: Support Manager, manager involucrado y Support VP.

Precedentes: consultar bin/buscar y el índice de sesión del 28/9. Las fuentes actuales corrigen la explicación técnica anterior. ADUSA pidió no reenviar pendientes; recuperación histórica requiere decisión aparte. Juan ingiere la nota desde su terminal con cerrar.

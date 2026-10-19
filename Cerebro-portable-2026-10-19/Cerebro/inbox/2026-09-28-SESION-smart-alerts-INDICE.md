# Sesion Smart Alerts 24 a 28 sep 2026: que ingerir y donde promover

## Vigentes, ingerir estos
Conocimiento
2026-09-28-smart-alerts-mecanismo-8-deadlock.md  causa, fix, reglas, pistas falsas, hallazgos colaterales
2026-09-28-grafana-smart-alerts-lectura.md  acceso, consultas, horas, pasos del log, trampas, SQL
2026-09-28-guia-disparar-smart-alert.md  procedimiento de Kiran v2, copia en flujos/smart-alert-disparo-manual.md
2026-09-28-smart-alerts-personas-y-lecciones.md
2026-09-28-rcs-29026-llamada-kiran-fix.md  transcripcion de la llamada del fix
2026-09-27-rcs-29026-proceso-prueba-smart-alert.md  procedimiento original del 9/27
2026-09-18-flujo-debug-smart-alerts-inprocess.md  metodo de Matt, RCS-28294
Fichas
2026-09-28-rcs-29026.md, 2026-09-28-rcs-29123.md, 2026-09-28-rcs-29145.md
Evidencia
2026-09-25-rcs-29026-grafana.md, 2026-09-25-rcs-29026-hallazgo-codigo.md, 2026-09-27-rcs-29026-logs-russ.md, 2026-09-28-rcs-29026-logs-russ-2.md, 2026-09-28-rcs-29145-grafana.md
Textos para pegar
2026-09-28-rcs-29026-cliente.md, 2026-09-28-rcs-29026-interno-final.md, 2026-09-28-rcs-29026-correo-jim-final.md, 2026-09-28-rcs-29123-cliente.md, 2026-09-28-rcs-29123-interno.md, 2026-09-28-rcs-29145-resolucion-interna.md, 2026-09-28-rcs-29145-respuesta-joe.md

## Obsoletos, no usar como fuente
2026-09-24-rcs-29026.md  ficha inicial con hipotesis de gateway
2026-09-25-rcs-29026-comentario-interno-eng.md  no se publico
2026-09-25-rcs-29026-incident-logs.md  hipotesis ThreadAbort descartada
2026-09-25-rcs-29026-prueba-test.md  URL de test inexistente
2026-09-28-rcs-29026-interno.md  reemplazado por interno-final; decia que Impersonation fallaba, corregido
2026-09-28-rcs-29026-correo-jim.md, -jim-2.md, -jim-3.md  reemplazados por correo-jim-final
2026-09-28-rcs-29026-plan-cierre.md  incluia ENG, descartado
2026-09-28-rcs-29026-reproceso-paso-a-paso.md  en pausa, ADUSA pidio solo hacia adelante
2026-09-28-rcs-29145-reproceso-casos.md  reemplazado por la guia v2

## Propuesta para investigaciones/INDICE.md, seccion Smart Alerts y notificaciones
| Mecanismo 8, deadlock en ProcessSmartAlert, sep 2026, ADUSA y Vitamin Shoppe, PR 58273 | investigaciones/smart-alerts-familia-de-fallas.md, desde 2026-09-28-smart-alerts-mecanismo-8-deadlock.md |
| Como leer Grafana para Smart Alerts: pasos 0 a 16, consultas, horas, trampas | desde 2026-09-28-grafana-smart-alerts-lectura.md |
| Success en SmartAlertProcess no prueba entrega, SmartAlert.vb | mecanismo 8, hallazgos colaterales |

## Propuesta para flujos/INDICE.md
| Disparar a mano una Smart Alert atascada, procedimiento de Kiran | flujos/smart-alert-disparo-manual.md |
| Destrabar InProcess y releer debug logs, metodo de Matt | 2026-09-18-flujo-debug-smart-alerts-inprocess.md |

## Discriminador de familia-de-fallas, pregunta nueva
Si varios tenants dejan de recibir todas las alertas desde la misma fecha y Grafana muestra 13a sin End, es el mecanismo 8.

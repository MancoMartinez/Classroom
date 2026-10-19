Apoyo en español para la reunión interna con Matt, 16 octubre

1. Security ID explícito. ¿Enviar el ID directamente evitaría el fallo de ENG-10069 o pasaría por el mismo flujo? Si sirve, ¿qué archivo, campo y valores admite, y qué prioridad tiene frente a teams y ajustes manuales?

2. Alta y usuarios existentes. Rachel tenía nivel 5 en SSO+ antes de crearse la cuenta, pero quedó NULL mientras sí recibió grupos y team. Christi tenía una asignación persistente antigua y también apareció sin nivel. ¿ENG-10069 cubre ambos casos o hay que investigar aparte el regreso de usuarios existentes?

3. Recuperación inmediata. Algunos usuarios entran una o dos veces al año. ¿Podemos corregir las cuentas sin nivel sin esperar otro login? ¿Quién lo hace, cómo preserva ajustes intencionales y qué prueba autoriza la corrección?

4. Oficinas y DC con SSU. Chris recibió 90002005 y Colton confirmó 40002005 como ubicación correcta. Ryan indicó que aparentemente agregamos el 9, pero no recomendó sustituirlo por 4. ¿El modelo exige una ubicación propia para oficinas/DC o mapearla a una marca existente? ¿Dónde comprobamos la regla actual de SnowTime?

5. Fuente y dueño de ubicaciones. ¿Qué fuente define las ubicaciones válidas y cuál asigna usuarios? ¿Quién corrige cada una y cómo llega a Secure e Incident? Chris tiene jerarquía corregida manualmente; falta confirmar creación de incidentes.

6. Vigencia del feed. La investigación del 15 encontró fechas de asignación del 13, aunque la tarea terminó sin errores reportados. El cliente mostró un archivo con fecha 14 en el nombre. ¿Qué evidencia de recepción, lote y procesamiento prueba qué datos llegaron? ¿Es normal que no cambien las fechas de filas sin modificaciones?

7. Dueños y próximo control. ENG-10069 sigue Backlog y sin asignar, verificado hoy en Jira. ¿Quién toma el defecto y quién la investigación SnowTime/ubicaciones? ¿Necesita seguimiento técnico separado bajo RCS-29451? Acordar evidencia pendiente y fecha del próximo update.

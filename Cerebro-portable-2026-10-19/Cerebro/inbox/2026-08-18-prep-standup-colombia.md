# Prep relámpago — reunión equipo Colombia, 18 ago

Barrido del tracker 10:30 (el más reciente) cruzado con lo que se dijo hoy en el chat de
End of July Unification. Colombia: tú, Diego Buelvas, Sebastian Rueda, Edwin Garzon,
Luis Hernandez, David Vargas.

## Tuyos

| Ticket | Estado tracker | Lo nuevo de hoy en Teams |
|---|---|---|
| RCS-28021 Izenda export | Work in progress | Matt: "looks to be working, however we need to get an actual report" — sigue pendiente de ti el nombre del reporte que falla |
| RCS-28123 Asignación de casos | Work in progress | Matt: "Fixed in Prod, we have not tested as it requires approving a record in a live system" — el bloqueo de permiso sigue en pie |
| **RCS-28124 Adjuntos** | Under Customer Review | **Contradicción a resolver hoy**: el tracker dice fix desplegado y probado el 14. Matt dijo a la 1:09 p.m. de ayer "in release just waiting for me to push to prod". Pregunta al equipo: ¿ya se empujó a prod o seguimos con el fix del 14 nada más? |
| RCS-28342 Anthony Lopez | Under Customer Review | Sin novedad nueva, esperando retest del cliente |
| RCS-28364 Brian Somsky | Under Customer Review | Sin novedad nueva, esperando retest del cliente |
| RCS-28353 502 al editar tienda | Work in progress | El fix grande de YARP/otelcol-swap (ENG-7270) se confirmó en prod para el cambio de ubicación de casos. Preguntar si aplica también a este ticket o es causa distinta |

## Del equipo

| Ticket | Dueño | Estado | Lo nuevo de hoy |
|---|---|---|---|
| RCS-28379 Case Owner/Creator en blanco | Diego Buelvas | Active with Appriss | Kiran: "Incident UserID <-> LoginID mapping is done... currently working on getting the missing User information on Incident tables like MasterCase and Shoplifting" — avanza, no está cerrado |
| **RCS-28093 Empleados no restringidos** | Edwin Garzon | Work in progress | **Punto de fricción real**: Matt dice "the true root cause of what this ticket was opened for is working as expected", pero avisa "Jim Cassebom may not agree, due to his interpretation of what should be happening here". Hay que decidir hoy cómo se lo explicamos al cliente antes de que Chris lo toque en la reunión |
| **RCS-28281 Carga de transacciones 10 ago** | Edwin Garzon | Under Support Review | **Vencido, 5 días sin comentario.** No hay update nuevo en Teams tampoco. Pregúntale a Edwin en la reunión directamente, es el único de los 21 así |
| RCS-28407 502 frecuente | Edwin Garzon | Under Support Review | Se está aislando moviendo Izenda a su propio app service (`web-prd-wus2-arp-izenda`), en dev/staging, no en prod. Sin ETA confirmado |
| RCS-28053 Link no-SAML | David Vargas | Completed | Cerrado, sin acción |

## Las tres preguntas que vale la pena hacer en la reunión

1. **28124**: ¿el segundo despliegue ya salió o seguimos con el del 14? Lo necesitas resuelto antes de armar el correo de hoy.
2. **28093**: si Matt considera que el comportamiento real es el esperado, ¿cerramos y explicamos, o esperamos a que Chris lo alinee con el cliente en la reunión de hoy?
3. **28281**: ¿alguien le puede pedir estado a Edwin ahora mismo, dado que es el único vencido?

## No es tuyo, pero afecta tu correo de hoy

**RCS-28196** (Vedant, no es Colombia) está confirmado resuelto en prod por Gabor, con el matiz de
Matt sobre los casos históricos con el valor por defecto. Tu versión del tracker todavía dice
"esperando release". Corrígelo antes de enviar.

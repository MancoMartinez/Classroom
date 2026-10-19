# Cola del 27 ago 2026, refresco de la mañana

Volcado Jira: 17 tickets abiertos asignados a Juan. Niveles 1=1, 2=1, 3=7, 4=8.
Comparación contra `cola/estado.anterior.json` del 26 ago 18:38.

## Aviso: el clasificador falla

`bin/eval_cola.py` da exactitud 9/13 = 69%. Baja de 100%, el orden de la cola no es confiable
sin revisión manual. Cuatro fallas:

| Ticket | Esperado | Dio | Lectura |
|---|---|---|---|
| RCS-27991 | 2 | 4 | Falla real. Shandana menciona a Juan directo y pregunta. Va a nivel 1. |
| RCS-28256 | 2 | 3 | Falla real. Juan prometió follow-up del login de Vincent Fortner. Va a nivel 2. |
| RCS-28289 | 1 | 4 | Etiqueta vieja. Juan ya contestó el 26 ago. Nivel 3 correcto. |
| RCS-27765 | 1 | 4 | Etiqueta vieja. Juan ya contestó. Nivel 3 correcto. |

Acción: actualizar `cola/EVAL-clasificador.json` para RCS-28289 y RCS-27765, y revisar el léxico
de promesas para que capture "I will follow up with you on that" y las menciones directas por nombre.

## Qué cambió desde ayer

- RCS-28482 subió de nivel 4 a nivel 1. Jim Cosseboom escribió anoche.
- RCS-28123 bajó de nivel 1 a nivel 2. Juan respondió y prometió update.
- RCS-28093 bajó de nivel 1 a nivel 4. Juan respondió.
- RCS-27991 recibió comentario de Shandana Khan con mención directa a Juan.
- RCS-28021 salió de la cola.
- Tickets nuevos: ninguno.

## Nivel 1, te toca responder

**RCS-28482** AHL/DLZ Greyed out fields in Izenda. Low, Work in progress, reporta Jim Cosseboom,
edad 7 días. Jim escribió y nadie de Appriss contestó.
Último, Jim Cosseboom: "Thank you. You are correct, the report is running correctly, it just isn't
editable."
Bitácora del 24 ago: Jim aclaró que necesita la pestaña MISC, no Data Sources. La disculpa y la
nueva ruta están redactadas y sin pegar.

**RCS-27991** Engage Analytics Not Populating Sections. High, Under Support Review, reporta Paul
Marderosian, edad 30 días. Elevado a mano desde nivel 4.
Alerta: Shandana Khan te mencionó directo.
Último, Shandana Khan: "@Juan Martinez given this was raised internally by Appriss CSM/not on behalf
of a specific customer, and given there's already an existing RCS from a customer raised on this
which we've accepted into the Engineering backlog, I'm not sure what the value in keeping this
ticket is."
Bitácora del 26 ago: escalación armada. RCS-28068 lululemon es el mismo defecto, Accepted into
Development desde el 18 ago. Precedente RCS-23643 Foot Locker, ADO 66220.

## Nivel 2, promesa sin cumplir

**RCS-28123** ADUSA Case assignment issues. Medium, Work in progress, reporta leighann.stubbs@adusa.com,
edad 24 días.
Último, Juan Martinez: "The missing confirmation and print option is a separate issue. I have logged
it, and engineering is reviewing it now. I will update you as soon as possible."

**RCS-28256** Appriss Incident Time Out(s) and Slow Load times. High, Under Customer Review, reporta
Colton Neal, edad 17 días. Elevado a mano desde nivel 3.
Último, Juan Martinez: "Vincent Fortner's login is a separate issue on our side. We are aware of it
and I will follow up with you on that. Fixes have been deployed for the save errors and for
reporting. Before I close either of these, I would prefer to get your confirmation."

## Nivel 3, esperando al cliente

- RCS-27676 RLC SFTP IP/Hostname Change. Low. 23 días de silencio. Toca perseguir.
- RCS-27959 PACSUN MasterData and Sales Posting, IP whitelist. Medium. 14 días de silencio. Toca perseguir.
- RCS-28122 Blain's no puede cambiar usuarios. Medium. 7 días de silencio. Toca perseguir.
- RCS-28496 PVH múltiples tiendas con problemas de login en desktop. Medium. 5 días.
- RCS-28282 Co-op bloqueo intermitente al seleccionar. Medium. 5 días.
- RCS-28223 McDonald's Restaurant Manager y Crew Cash Audit. Medium. 2 días.
- RCS-28289 Vitamin Shoppe Blocked Users. Medium. 1 día. Joe Austin espera a que Scott vuelva de vacaciones.
- RCS-27765 Winn-Dixie Data file check. Medium. 2 días. Hilo partido email/Jira, correo redactado en inbox del 24 ago.

## Nivel 4, en movimiento interno o trabajado sin pegar

- RCS-28153 BYF errores y cierre de sesión. High. 16 días sin oír a Appriss.
- RCS-28327 Delhaize Loyalty Discounts not Specified. Medium. 14 días sin oír a Appriss. Hay bitácora.
- RCS-28099 CWH HYP to RCS Item Discount Logic. Medium. 9 días sin oír a Appriss. Lo lleva David Vargas.
- RCS-28294 Vallarta Smart Alerts no disparan. Medium. 1 día. Hay bitácora.
- RCS-28093 Ahold empleados no restringidos por tienda. Low. 0 días.

## Recomendación

Empezar por RCS-28482. Es el único con el cliente esperando en frío, el texto ya está redactado
desde el 24 ago y solo falta pegarlo. Cierra en minutos y baja la deuda más visible.

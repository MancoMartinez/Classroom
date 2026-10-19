---
name: project_estado_abierto_2026_08_13
description: "Cola y pendientes de Juan al 13 ago 2026: lo que salió a PROD hoy, lo que le toca y las tres preguntas sin responder"
metadata: 
  node_type: memory
  type: project
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-13T18:27:23.968Z
---

Mesa de trabajo del día: https://claude.ai/code/artifact/41529835-12f4-4819-a814-b105c9819bba (17 abiertos, 4 High).

**Salió a producción hoy** (ver [[project_bucket_review_sesion2]]): adjuntos grandes y smart alerts. **Juan no tiene ningún ticket abierto en esos dos buckets** — su único de Attachments, RCS-28124, ya está Completed. Los que ese release destraba son RCS-28167 y RCS-28331 (Viraj) y RCS-28305 (Camila), en *Waiting for Software Release*. Lo que sí tiene es el pedido directo de Matt y la cadena escrita "Matt, then Support, then customer".

**Adjuntos: ya probado, pero incompleto.** Juan validó el 13 ago txt, pdf y video en Stater Bros y Sportsman's, lo más pesado 150 MB, todo sin error, y lo reportó en el chat de la Unificación. Diego Buelvas preguntó por archivos grandes y Matt Kamminga contó que su prueba en test fue de **5 GB**, pidiendo "as big as you have got". Falta repetir con ~1 GB y probar **descarga**, no solo subida. Detalle completo en [[project_uni_jul_26_attachments]].

**Dos preguntas que siguen sin responder:**
1. Si ya verificó los 240 minutos en `secure.ConfigurationItem` incluyendo `CustomerEditedValue`.
2. Si le responde a Matt ahora diciendo que arranca, o prueba primero y reporta resultado.

**Pendientes concretos:**
- **RCS-28256** — remedir con el protocolo de 6 fases; conseguir tenant de control; confirmar el valor esperado de `EnableBlobAppendLogging`; definir si ENG-7182 cubre el 524 de Izenda. Dueño de Izenda ya identificado: Jack. Ver [[project_rcs_28256_tailored_brands]].
- **RCS-28153 + RCS-28346** — Session Expiry ya son dos tickets, no uno. El 28346 entró el 13 a las 00:52, Stater Bros, escalado por JR, diciendo que la sesión sigue expirando antes de los 240 minutos, o sea que el arreglo del 28153 no está tomando. Juan está en copia de ese correo. Falta verificar que el 240 quedó en las dos columnas y escribir la nota interna que falta. Contraevidencia: BYF es Big Y Foods, aunque la página lo da como cliente sin identificar. RCS-28224 (Remember Me, del mismo correo de Angie) sigue sin enlazar.
- **RCS-28124** — Viraj lo resolvió el 11 a las 09:48 tras la reunión con Leigh Ann. Solo falta el segundo paso, el Close. La página de JR todavía dice que la dependencia por marca no tiene explicación, y eso dejó de ser cierto.
- **RCS-28033** — responder la pregunta de Kiran sobre cómo llegan los usuarios a `CaseEntry.aspx`; ahora aplica el SQL de desbloqueo.
- **RCS-27991** — escalación formal a Engage (Under Engineering Review, Ian Williams, mensaje de Teams obligatorio), después de avisarle a Paul. Diez días en silencio.
- **RCS-28342** — correr la comparación `incident.LPUser2` vs `membership.Users` para los user IDs 11139 y 1789032.
- **RCS-28327** — sacar la fila cruda de la transacción 2608025570789970641, leer primero RCS-28172, y rutear a Edwin Garzon.
- **RCS-28021** — corregir la línea de Edge/Chrome del tracker.
- **RCS-28214 / 28289 / 28282** — perseguir Ray IDs (Brandon Bigelow; Joe está de PTO hasta el 17 ago).
- Mandarle **RCS-28030** a David Vargas para el hilo de timezone en smart alerts.
- Confirmar con Russell Harmon si PacSun conservó sus IPs de producción anteriores.

- **RCS-28240** — United Supermarkets, SSO de test parado desde abril. Es de Camila, pero Juan preguntó el proceso. Ver [[project_rcs_28240_united_supermarkets]].
- **Vedant tiene cuatro tickets frenados** por no escribir las notas de triage: RCS-27971, RCS-28007, RCS-28010, RCS-28247. Aimee los marcó el 13 ago y Juan va en copia. El 28007 es el que más duele, la investigación ya existe y solo falta redactarla.

Ver [[project_estado_abierto_2026_08_11]], [[project_reparto_cola_2026_08_11]].

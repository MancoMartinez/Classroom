# Cosecha cola-proceso — 2026-08-28
Fuente: sesiones local_e3fd54bb-46fc-4e37-b348-de3ac2724e7f, local_2c86f407-b8b7-4cc0-b29b-eed21a678c7f y local_82b793ff-9432-4abd-93b2-93f1e7db5867

## Hallazgos verificados

El clasificador de la cola bajó del 100%. Dos corridas del día lo midieron por separado: una dio 67% y la otra dio 64%, esta última con 9 aciertos de 14 casos según `bin/eval_cola.py`.

La causa no es el léxico. `cola/EVAL-clasificador.json` se fijó el 24 de agosto y el estado real de los tickets avanzó después. Las fallas por etiqueta vencida se identificaron una por una: RCS-28327, RCS-28289, RCS-27765, RCS-28482 y RCS-28123. El clasificador leyó el estado correcto en los cinco. El set de referencia quedó atrás.

Existe una falla real de léxico. RCS-28256 lleva dos señales en el mismo comentario del 25 de agosto: pide confirmación al cliente y promete seguimiento. `cola.py` lo manda a nivel 3. La lectura humana lo pone en nivel 2.

Regla de reloj corregida. El plazo de 24 horas hacia el cliente corre solo cuando el cliente pregunta algo. Un acuse de recibo sin pregunta no abre plazo. El caso que lo estableció fue RCS-28482, donde Jim Cosseboom solo acusó recibo.

Escalación de RCS-28294. El changelog confirma que Juan sí transicionó a Under Engineering Review el 25 de agosto a las 20:02 con Shandana Khan como assignee. Shandana lo devolvió a Under Support Review el 26 a las 08:02 y pidió pasos exactos de reproducción en el mismo minuto. Devolver el ticket es su forma de pedir el dato, no una segunda decisión. Repitió el mismo patrón en RCS-27991.

El comentario del 25 cumplía uno de los cinco requisitos del checklist de Aimee Wadsworth. Le faltaban los pasos de reproducción. El comentario del 26 sí los trae, con precondiciones, ocho pasos numerados y query de verificación.

No existe ningún ENG auto creado el 25 ni el 26 para RCS-28294. El barrido del proyecto ENG lo confirma. J.R. quitó el enlace a ENG-6612 el 25.

ENG-7359, "Smart Alert not working with Quick Entry", Backlog, Matthew Kamminga, creado el 17 de agosto, describe el mecanismo del caso 48786. Texto literal del ticket: los usuarios en Quick Entry no reciben cookie cpf ni autentican al iniciar sesión, y la alerta no se crea ni se envía. Conecta con la medición de Juan de 308 cuentas con `LastLoginDate = NULL` sobre 419. Ryan Barlow reportó ahí el 18 de agosto que a Claire's le fallaron más de 140 smart alerts en un fin de semana en producción.

ENG-2819, "Smart Alert failing to run in Incident/Audit", Done, Kiran Vadday, aporta la firma de log a buscar: `LPSBO.SendHatrJob - Exception in HatrSmartAlert`.

## Decisiones y compromisos

Refijar `cola/EVAL-clasificador.json` contra el volcado de hoy. Mientras el set arrastre etiquetas del 24 de agosto, el porcentaje no mide nada.

Reclasificar RCS-28256 a nivel 2 a mano hasta que el léxico distinga la señal doble.

Escalar RCS-28294 de nuevo con el comentario corregido. Orden fijado: pegar el comentario interno, enlazar RCS-28131 de Sportman como relates to, transicionar a Under Engineering Review con Shandana, mandar el Teams, corregir a Tatiana. El ENG se auto crea con la transición.

No readjuntar el PDF del caso. Ya está en el ticket. El requisito de Aimee exige que los pasos vengan con capturas, no que se suban de nuevo.

ENG-7359 y ENG-2819 van nombrados como candidatos en la sección 6 del comentario, sin enlazar. Shandana hace el triage y decide si cierra contra ENG-7359, lo enlaza, o es aparte.

Juan quitó la declaración de uso de IA y la constancia de conversaciones externas del comentario. Son dos de los cuatro requisitos de Aimee. Ese es el motivo posible si el ticket rebota otra vez.

## Pendiente de verificar

Borrar `cola/estado.previo-run.json`. El sandbox no permitió eliminarlo. Ningún script lo lee.

Comparar `LastLoginDate` de la cuenta que creó el caso 48786 contra la que creó el 48575. Si la de 48786 está en NULL y la otra no, el mecanismo de ENG-7359 queda confirmado y RCS-28294 se cierra contra él.

El archivo de la cola quedó afirmando que Juan no hizo la transición de RCS-28294. Corregirlo.

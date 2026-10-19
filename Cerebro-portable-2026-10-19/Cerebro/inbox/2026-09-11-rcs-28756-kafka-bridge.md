# RCS-28756. Nike tiene razon. Existe un consumer Kafka de Appriss

## Que pasa

Nike respondio el 2026-09-11 via Akshaya que ellos no hacen push, que exponen un
stream Kafka y Appriss se conecta a consumirlo. Copiaron a un arquitecto suyo.
Piden logs o errores de conexion de nuestro lado.

Eso contradice la respuesta que Ayesha ya envio a Nike el 2026-09-10, donde le
dijimos que no hay consumer de Appriss, que no es Kafka y que ellos publican a
nuestra Ingestion API. Los puntos 1, 2 y 3 de esa respuesta estan mal.

## Causa

ENG-4235, en Backlog desde 2026-04-11, componente datacloud, documenta la pieza:

  App: Kafka Ingestion, archivo kafka_ingestion/nike.py
  Purpose: Bridges Nike Kafka topic to Azure Event Hub via background consumer thread
  Entornos: ops-datacloud-kafka-ingest-wus2 y prd-datacloud-kafka-ingest-wus2

Hay un consumer de Appriss entre el Kafka de Nike y el Event Hub. Nike describe
el flujo correctamente. El riesgo que quedo anotado el 2026-09-09, que existiera
un relay nuestro en medio, era esto.

Eso reencuadra la evidencia. Incoming Messages en cero desde 2026-08-27 19:02 UTC
no prueba que Nike dejo de enviar. Prueba que nuestro bridge dejo de publicar al
hub. El origen del corte se mueve de Nike hacia Appriss.

ENG-4235 tambien explica por que nadie se entero. El health check del App Service
pega a / y devuelve 200 con status online sin mirar stats.is_running. El /health
devuelve healthy siempre. Azure solo alerta si el contenedor entero cae, no si el
hilo consumidor murio. Coincide con el reporte inicial, no tenemos alertas para esto.

## Evidencia

- ENG-4235, descripcion completa, lineas 573, 541 y 457 de kafka_ingestion/nike.py
- Event Hub prd-datacloud-wus2-ehub-1, entidad c67_rawdata_order, Incoming y
  Captured en cero desde 2026-08-27 19:02 UTC
- Correo de Nike del 2026-09-11 en RCS-28756, arquitecto de Nike en copia

## Que hago hoy

1. Escribir a Nichols Turner, Data Engineering bajo Saddam Hussain. Sigue sin
   responder la pregunta del 2026-09-09. Ahora la pregunta cambia: no es si la
   API registro llamadas, es si prd-datacloud-kafka-ingest-wus2 sigue consumiendo.
   Texto en este archivo, abajo.
2. No responderle a Nike hasta que Nichols confirme. Cuando confirme, hay que
   corregirles los puntos 1, 2 y 3 de la respuesta del 10 de septiembre.
3. ENG-8368, GP11 NKE 67, es el contenedor de migracion SnowTime, creado el
   2026-09-04, despues del corte. No es causa. Descartado.

## Precedentes

- ENG-4235, mismo servicio, 2 fallas Sev0 de health check en prd, 8 y 10 de abril
- Peyman confirmo el 2026-09-09 que hay una API de Appriss entre Nike y el blob.
  Iba en la direccion correcta, la cadena tiene una pieza mas arriba
- AR Gateway normaliza ingesta por REST, Kafka o colas al formato de landing,
  brain/markdown/14-appriss-ingenieria-docs-fuente.md

## Compromisos

- Nichols: pendiente respuesta desde el 2026-09-09
- Ayesha y Akshaya: esperan texto para Nike, no sale hasta confirmar
- Nike: espera logs de conexion, y una correccion nuestra

## Mensaje para Nichols, Teams, listo para pegar

Hi Nichols, following up on the Nike feed question from Tuesday. I think I had it
backwards.

Nike says they do not push to us, they expose a Kafka stream and we consume it.
ENG-4235 seems to back them up: kafka_ingestion/nike.py, bridges Nike's Kafka topic
to Event Hub, running as prd-datacloud-kafka-ingest-wus2.

If that is the live path for 067, then the zeros on c67_rawdata_order since
2026-08-27 19:02 UTC mean our bridge stopped publishing, not that Nike stopped
sending.

Can you check what that app shows since then? Consumer thread state, logs, offsets
and lag, and any deploy or credential change near that date.

Also possible I am reading ENG-4235 wrong and Nike runs on something else. Let me
know either way, I have not replied to the client yet.

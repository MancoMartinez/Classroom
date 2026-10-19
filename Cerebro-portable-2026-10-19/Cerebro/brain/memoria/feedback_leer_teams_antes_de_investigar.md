---
name: feedback_leer_teams_antes_de_investigar
description: "Antes de proponer una consulta o una hipótesis, leer el hilo de Teams completo; el equipo suele haberlo hecho ya"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 254b4d73-4509-4741-99d1-56c88cb6d56c
  modified: 2026-08-12T00:15:50.548Z
---

Antes de mandar a Juan a correr una consulta, reproducir algo o escribir una hipótesis, **leer hasta el final el hilo de Teams del ticket**. Y cuando él pegue una transcripción, leerla entera antes de responder, incluidas las respuestas que ya contestan lo que se iba a preguntar.

**Why:** el 11 ago 2026, en RCS-28256, pasó dos veces en la misma hora. Primero mandé a correr la verificación de los tres feature flags en la base del 209, y Kiran ya la había corrido el 10 ago a petición de Matt y había publicado la captura: mismas tres filas, mismos valores, misma marca de milisegundo. Segundo, propuse como hipótesis que al tenant le faltaba el hotfix de RCS-28084, cuando Kiran ya le había contestado a Juan ese mismo día *"No. Once deployed, all the clients get the same code."* En los dos casos la información estaba en el chat que Juan había pegado. Le hizo perder tiempo y, peor, casi manda a Teams como hallazgo algo que el equipo ya sabía. Juan lo cortó con *"analiza nuevamente porque no estoy seguro de que tengas claras las cosas"*.

**How to apply:** el hilo de Teams es evidencia de primera clase, igual que el ticket. Antes de cada propuesta, preguntarse quién ya tocó esto y qué respondió. Si algo ya lo verificó otra persona, se cita a esa persona con fecha y no se vuelve a correr. Complementa [[feedback_borradores_al_final]] y [[feedback_agrupar_no_es_causa_raiz]].

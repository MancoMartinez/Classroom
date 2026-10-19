# RCS-28756. Saddam confirma investigacion activa, Nike descarta el whitelist

## Que paso hoy

Saddam Hussain respondio en Teams a la escalacion del 14 sep. A las 5:43am dijo que
esto se le habia perdido de vista desde agosto y que arrancan hoy. Juan pidio una
respuesta precisa para el cliente a las 9:12am. A las 9:15am Saddam mando captura de
un correo.

El correo es de Slade Jordan, sjordan@apprissretail.com, enviado hoy 15 sep 6:46am a
Rudraraju Pavan (Nike), Menon Narayan, Mohan Anant y Saddam Hussain en copia. Pregunta
si las IPs 20.83.208.237/32 y 20.51.107.212/32 siguen en whitelist del lado de Nike
para conectar a su "production stream". Dice que tienen problema de conexion.

Pavan de Nike respondio 14:55 confirmando que ambas IPs siguen en whitelist para el
production stream, y ofrece un bloque adicional 40.71.23.164/32 con acceso al test
stream.

Saddam cerro con: "I am debugging the issue. We sent out an email to the client to
check a couple of things. This is under investigation."

## Que confirma esto

Nike tenia razon desde el principio, es un modelo de consumo tipo stream, no push a
nuestra API. Appriss se conecta con IPs propias contra un production stream de Nike.
Esto es consistente con ENG-4235, Kafka Ingestion, kafka_ingestion/nike.py, el bridge
que consume el Kafka de Nike hacia el Event Hub.

Nike descarto el whitelist como causa, las IPs siguen habilitadas. Eso mueve la
sospecha hacia el conector mismo del lado Appriss. Slade Jordan es quien esta a cargo
de esa parte, no es Nichols Turner a quien se le habia escrito el 9 sep.

## Que hago hoy

1. Publicar update en RCS-28756 que refleje esto, para bajar la frecuencia de pings.
   Cuatro personas distintas pidieron update entre el 14 y el 15 sep sin que hubiera
   nada nuevo que contar hasta ahora.
2. Seguir sin contestarle a Nike. La instruccion que ya esta en el ticket sigue en pie.
3. No hay root cause confirmado ni fecha. Eso se dice tal cual, no se inventa plazo.

## Comentario para pegar en RCS-28756

Update. Saddam Hussain confirmed today that this is being actively worked. He is debugging on the Appriss side, and Slade Jordan already contacted Nike this morning to verify IP whitelisting for the production stream, 20.83.208.237/32 and 20.51.107.212/32. Nike confirmed both are still whitelisted and offered an additional block for the test stream.

That rules out the whitelist as the cause and points at the connector itself on our side, consistent with what I flagged from ENG-4235 on 2026-09-11. No root cause or fix confirmed yet. I do not have a timeline. Please hold on Nike until Data Engineering closes this out, I will update here as soon as there is a result.

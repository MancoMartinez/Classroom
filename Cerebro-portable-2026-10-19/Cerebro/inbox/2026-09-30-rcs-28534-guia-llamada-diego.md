# RCS-28534, guia de llamada con Diego, 30 sep. Horas en Bogota

## Conclusion en una frase
Stater se colgo antes del fix entre 12b y 13a, en la busqueda de adjuntos. Despues del deploy del 28 sep ninguna corrida se cuelga. Los Quit que siguen saliendo son casos atascados de antes, que el fix no libera.

## Por que estamos aqui
Angie escribio el 29 sep que HR no recibe alertas. Diego publico el RCA con 242 casos y la idea de un segundo gatillo propio de Stater. Kiran pidio Grafana antes de hablar de codigo y nos asigno revisarlo juntos.

## Pantalla 1. Jira RCS-28534
Comentario de Angie 29 sep, RCA de Diego, respuesta de Kiran 7:34 PM y 8:02 PM.

## Pantalla 2. 205148, rango 24 sep 10:00 a 16:00
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "205148"
10:51:53 6a Discipline Request Rows=1, 8, 8a, 11, 11d 10:52:03, 12b 10:52:04. Nunca 13a ni End. Quit desde 10:57 hasta 15:43.
Explicar: InProcess es un candado por caso. Se pone en 1 al entrar y vuelve a 0 al final. Si la corrida muere en medio, queda en 1 y cada guardado posterior sale con Quit.
El Quit de 10:51:54 cae en medio de la corrida viva. Un Quit suelto es un segundo guardado, no un atasco.

## Pantalla 3. 205157, rango 24 sep 14:25 a 14:40
14:31 6a Rows=0 con DaysOffNotes vacio. Angie lo llena. 14:32 6a Rows=1, muere en 12b 14:32:30.
El filtro de Discipline Request usa DAYSOFFNOTES y CaseType. No usa CaseStatus. Preguntar a Kiran que queria mostrar con el status.

## Pantalla 4. El fix, rango 28 sep 00:00 a 29 sep 00:00
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "NettrackSmartAlertActivity" |= "500"
17 errores 500 de HATR, el ultimo 12:49. Jim confirmo alertas desde 13:30.

## Pantalla 5. Despues del fix, rango 28 sep 00:07 a now
|= "Finding attachments" y luego |= "Ready to send email"
189 y 189 con la misma hora, menos de 1 segundo entre 12b y 13a. Ninguna corrida muere en 12b.
13a contra 13b desde 29 sep 11:56: 99 de 100 pareados. Excepcion: Stater Bros. Investigation 129, 29 sep 18:10.

## Pantalla 6. Los Quit de hoy, rango 28 sep 13:30 a now
|= "still on processing": 404 lineas, 200 IDs.
25 terminaron despues. 132 son un Quit suelto. 35 venian atascados de antes del fix. 8 empiezan despues.
Mostrar 205264 desde 27 sep: solo Quit desde 28 sep 17:24, ninguna corrida en la ventana. Se atasco antes.

## Lo que decidimos juntos
1. El fix cubre a Stater. El conteo de 98 creciendo son casos viejos que alguien vuelve a guardar.
2. Quedan casos con InProcess = 1 de antes del fix. Sacar la lista con SELECT ShopliftingID FROM incident.Shoplifting WHERE InProcess = 1.
3. Preguntar a Angie cuales casos necesita recibir. Disparar solo esos con la guia v2 de Kiran y su visto bueno.
4. ENG-8698 sigue siendo el arreglo de fondo. Un candado sin vencimiento vuelve a pasar con cualquier corte.
5. Diego actualiza el RCA con este alcance. Juan responde a Kiran con casos y lineas.
6. Revisar Investigation 129.

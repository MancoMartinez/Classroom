---
name: feedback_nada_solo_en_consola
description: Todo entregable se escribe a un archivo en el momento; Juan pierde respuestas buenas cuando se va a verificar algo y vuelve al scroll
metadata:
  type: feedback
---

Juan lo describió el 18 ago 2026: trabaja en la terminal, recibe una respuesta que sirve, pero antes de usarla necesita confirmar algo, se va a verificarlo, y al volver tiene que navegar el scroll de la consola para reencontrarla. Pasa todo el tiempo y se vuelve tedioso.

**Por qué:** la consola es un flujo, no un almacén. Un entregable que solo existe en el scroll ya está medio perdido: no se busca, no se comparte, no sobrevive a un `/clear` ni a cerrar la terminal.

**Cómo aplicarlo:** cualquier cosa que Juan vaya a usar, pegar o consultar después se escribe a `~/Desktop/Cerebro/inbox/AAAA-MM-DD-tema.md` **en el momento de producirla**, no al final del turno ni cuando lo pida. Comentarios de Jira, consultas SQL, guiones de llamada, análisis, planes. Luego se le dice la ruta en una línea. Si resulta que era conocimiento duradero, se mueve a la base con `guardar <carpeta> "título"`.

Corolario: no preguntar "¿quieres que lo guarde?". Guardarlo y decir dónde quedó.

Ver [[project_flujo_trabajo_cerebro]] y [[feedback_borradores_al_final]].

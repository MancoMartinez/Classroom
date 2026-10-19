# Bitacora por ticket

Un archivo por ticket, `RCS-XXXXX.md`, append only. Aca queda lo que Juan reporta haber trabajado
antes de que llegue a Jira, o lo que nunca llega a Jira porque es trabajo interno.

Jira sigue siendo la fuente de verdad del estado. La bitacora es la fuente de verdad de tu esfuerzo.

Se escribe de dos formas. Diciendomelo en el chat, y yo la escribo. O a mano:

```bash
bin/anotar RCS-28482 "pegue el comentario del MISC tab y lo pase a Work in progress"
bin/anotar RCS-28482 --ver
```

Cuando la ultima entrada de la bitacora es posterior al ultimo comentario del ticket en Jira, la
cola baja ese ticket y lo marca TRABAJADO, SIN PEGAR EN JIRA. Deja de quemar sin desaparecer.

Los adjuntos de cada ticket van en `adjuntos/RCS-XXXXX/`. El indexador los lista en la ficha.

# ENG-8008 Print Journal Stater Bros, dos PR en USdev

Consulta de Juan el 9 sep 2026: si tiene algo de esto asignado.

## Que pasa

No tienes nada de esto en tu cola. El ticket es RCS-28653, Stater Bro Print Journal not working,
lo trabaja Diego Buelvas y hoy esta asignado a Shandana Khan en Accepted into Development. Los
dos PR de ENG-8008 ya se probaron en USdev.

## Causa

CONFIRMADA como pertenencia, no como causa tecnica. Tu cola son 18 tickets abiertos y ninguno es
Print Journal ni Stater Bros. El unico Stater Bros del cerebro es RCS-28242, cerrado el 28 ago,
tambien de Diego.

## Evidencia

- Jira 9 sep: RCS-28653 assignee Shandana Khan, estado Accepted into Development, clona ENG-8008.
- ENG-8008 sigue en Backlog con Matthew Kamminga, actualizado el 4 sep. Los PR corren adelante
  del estado de Jira.
- `assignee = currentUser() AND statusCategory != Done` devuelve 18 tickets, ninguno de Stater
  Bros ni de impresion.

## Que hago hoy

1. Nada tuyo que ejecutar. Pasale los dos PR a Diego para que los guarde en RCS-28653.
2. Dile a Diego que no le anuncie el fix a Angie Martinez todavia. El ticket esta en Accepted
   into Development con assignee de Engineering. Se espera la transicion a Under Support Review.
   Anunciar antes repite el error de RCS-28161.
3. Cuando ENG-8008 salga de Backlog, pregunta por la fixVersion antes de que alguien prometa
   fecha. Los PR en USdev no son release a produccion.
4. Si quieres cerrar el hilo, ENG-7191 ya cubre journal notes que dan error al imprimir y esta
   Done. Confirma con Matt si ENG-8008 es el mismo defecto en la pantalla embebida de case entry
   o uno distinto. El titulo del PR dice embedded case-entry screen.

## Precedentes

- RCS-28242 Stater Bros, Unable to Print Journal Notes, cerrado el 28 ago contra ENG-7191.
- `tickets/ENG-7191.md`: cubre journal notes al imprimir, no cubre el panel post asignacion.
- Diego lleva tres updates seguidos sin ETA a Angie, 28 ago, 4 sep y 7 sep. El cuarto necesita
  contenido nuevo o el cliente lo va a leer como silencio.

## Compromisos

Ninguno tuyo. Los de RCS-28653 son de Diego y ninguno tiene fecha.

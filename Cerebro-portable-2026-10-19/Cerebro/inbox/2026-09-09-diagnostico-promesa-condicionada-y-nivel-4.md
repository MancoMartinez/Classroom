# Cola: promesa condicionada, lexico de promesa incompleto, y el nivel 4 como cajon

Fecha: 2026-09-09. Disparador: Juan reporto que RCS-28240 y RCS-28351 salian en nivel 2
estando en Under Customer Review con la pelota del cliente.

## Que pasa

El clasificador decidia entre pedido y promesa por posicion en el texto: `p_preg > p_prom`.
Juan cierra sus comentarios con cortesia, asi que la promesa queda siempre al final y gana.
Los dos tickets subian a PROMESA SIN CUMPLIR con el cliente debiendo datos.

## Causa, confirmada

Tres defectos, no uno.

1. La posicion no decide quien tiene la pelota. "I will follow up on this ticket once I hear
   back from your team" es una promesa condicionada a que el cliente responda primero. Cuenta
   como pelota del cliente, no como deuda de Appriss.
2. Lexico PREGUNTA sin las formas imperativas. Juan pide sin formula de cortesia:
   "I need your IT team to confirm", "I want you to verify", "Can Becky run the same check",
   "it's important that you send me screenshots". Ninguna matcheaba.
3. Lexico PROMESA sin "keep you updated". Tenia "keep you posted" y no la variante.
   RCS-28342 llevaba 4 dias en nivel 4 con una promesa de Juan sin cumplir encima.

## Evidencia

    RCS-28240  p_prom 542  p_preg -1   antes nivel 2, real 3
    RCS-28351  p_prom 308  p_preg -1   antes nivel 2, real 3
    RCS-28342  p_prom -1   p_preg -1   antes nivel 4, real 2
    niveles antes:   2=3 3=5 4=11      exactitud 13/13
    niveles despues: 2=1 3=8 4=10      exactitud 13/13

## Que se cambio en bin/cola.py

Lista CONDICIONADA nueva: `once (i|we) hear back`, `once you`, `when you`, `after you`,
`if you (are|do|still|see|continue)`, `once (that|this|it) is confirmed`, `upon (your|receipt)`,
`pending (your|the customer|the client)`, `as soon as you`.

Regla nueva: `if p_preg >= 0 and (p_preg > p_prom or p_cond >= 0)` cede a nivel 3.

PREGUNTA, once patrones imperativos. PROMESA, `keep you (updated|informed|in the loop)` y
las variantes de "I'll be working on".

Backup `bin/cola.py.bak-20260909`.

## Deuda que queda abierta

El nivel 4 no significa nada. Diez tickets, cinco situaciones distintas: peticion interna
dirigida a Juan, trabajo suyo en curso, cliente callado, hito de calendario vencido, y
ticket muerto. Tres de los diez son cosas que Juan debe.

El override de bitacora tapa el estado real. RCS-28294, RCS-28281 y RCS-27549 tienen la
pelota del cliente y la bitacora los baja a 4 con motivo "todavia no esta en Jira".

`bin/refrescar_eval.py` vigila los comentarios de Jira y no la bitacora. RCS-28753 cambio de
nivel a las 21:46 por una entrada de bitacora y el gold quedo vencido en quince minutos.

## Compromisos

Decidir con Juan si el nivel 4 se parte. Actualizar ESTADO.md.

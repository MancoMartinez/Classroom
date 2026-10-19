# Cosecha luxottica — 2026-08-28
Fuente: sesion local_acf1b969-2fc1-4284-a566-d094def0cf73, "Luxottica - Edwin"

Ticket: RCS-28601. Edwin es el assignee, Juan lo asesora.

## Hallazgos verificados

`appserver1.lpguys.net` no esta deprecada. La busqueda no encontro un solo ticket ni una sola
pagina que la depreciara. Es un forward especifico de Luxottica hacia CAMS que se rompe y se
repara.

Reincidencia documentada desde 2022. La ultima fue RCS-28037 del 29 de julio, con summary identico
caracter por caracter. David Vargas lo cerro en 27 minutos con "Our team has applied a fix" y el
cliente confirmo sin cambiar de URL.

Precedente decisivo, RCS-17591 de septiembre 2024. Jie Chen propuso el mismo cambio de URL que
propuso Edwin. Dean Korbakis lo rechazo: "They refused to change it due to the fact of their mass
scale across the globe has utilized the original URL." Jie arreglo el forward y cerro como Code
Fix Provided. La negativa de Michael Kahrig hoy repite una posicion que Appriss acepto hace dos
años.

Falla logica del argumento de Edwin. Los dos hosts son `lpguys.net`. Si la unificacion cerrara
lpguys.net, la URL que el ofrecio como reemplazo tambien moriria.

Causa probable, sin confirmar. DO-12224, upgrade de produccion a netTrack en LpGuys, completado el
25 de agosto por Ryan Barlow. El smoke testing no reporto hallazgos y el forward legacy quedo
fuera de alcance.

Corroboracion. RTS-206515, sintetico de Grafana LPMS, alerta desde el 25 de agosto a las 19:45 y
sigue abierto. Los seis anteriores cerraron con Active Alerts en 0.

Ruta de escalacion, sacada de las guias de Confluence y de las transiciones reales del ticket, no
de memoria. Canal de Teams `Retail Ops: AALPS Issues and Outages`, con `@channel`, el tag
`@Infra-all` y mencion directa a Ryan Barlow por haber ejecutado DO-12224. Sin acuse de recibo a
los 30 minutos, OpsGenie via label hacia AALPS DevOps.

Guias usadas: "How to Escalate Critical/High Priority Tickets", RTS `123301200564`, y "Customer
Escalation Handoffs, Secure Audit & Legacy", RTS `478022139957`.

Deuda estructural. Las repeticiones cerraron como "Restored Services". Nadie abrio nunca un item
para meter ese forward en el smoke testing de LpGuys. El proximo upgrade lo rompe otra vez.

## Decisiones

Edwin corrige hoy la respuesta al cliente. La afirmacion de deprecacion es incorrecta y se corrige
sin suavizar.

Se entrego un procedimiento de nueve pasos. Los tres primeros son los urgentes: tomar el ticket y
pasarlo a Work in progress, corregir el comentario al cliente, verificar si
`apps.lpguys.net/luxottica/nettrack/` carga. Ese ultimo dato define si la escalacion va como
forward roto o como tenant caido.

La clasificacion Sev1 queda a criterio de Juan. Mas de 4000 tiendas caidas encaja en Major
Incident Management. La guia no fija umbral por numero de tiendas.

## Pendiente de verificar

Si `apps.lpguys.net/luxottica/nettrack/` carga. Sin ese dato la escalacion no tiene forma.

El conteo exacto de reincidencias. La sesion dice cinco veces desde 2022 en un momento y seis
cierres como "Restored Services" en otro. Reconciliar contra Jira antes de citarlo.

La causa DO-12224 sigue como probable. Nadie de Infra la confirmo.

Abrir el item que meta el forward de Luxottica en el smoke testing de LpGuys.

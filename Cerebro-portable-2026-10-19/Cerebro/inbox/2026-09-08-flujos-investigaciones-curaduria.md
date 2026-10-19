# Curaduria de flujos e investigaciones, 8 sep 2026

Nota de sistema del Cerebro. No es la ficha de ningun ticket.

## Que pasa

`ESTADO.md` decia que `flujos/` tiene 3 archivos e `investigaciones/` tiene 1, y llamaba a eso la
deuda mas grande del sistema. La cifra es cierta y la lectura era incompleta. Los dos `INDICE.md`
no estan vacios: son mapas curados que enrutan a 50 memorias y a los espejos de markdown. Lo que
estaba desactualizado era la curaduria, del 24 de agosto, y lo aprendido en las dos semanas
siguientes no estaba enrutado en ninguna parte.

## Como se midio el hueco

Se conto, sobre las 443 fichas de ticket, cuantas tocan cada tema recurrente. Contar tickets dentro
de los chunks infla el numero, porque las fichas se citan entre si. Una ficha por ticket es la
medida honesta.

Escalacion a ENG toca 156 fichas, el 35%. Unificacion de julio 97, el 21%. Izenda 83 y SSO 82, el
18% cada uno. Timeout y 502, 56. Smart Alerts 46, el 10%.

De todos esos, Smart Alerts era el unico sin una sola entrada en ninguno de los dos indices. Los
demas ya tenian memoria propia enrutada. Escalacion a ENG resulto bien cubierto por
`reference_escalacion_l3_procedimiento.md`, que es fuerte y esta al dia, verificado contra
Confluence el 7 de septiembre. No se duplico.

## Que se escribio

`investigaciones/smart-alerts-familia-de-fallas.md`. El cliente siempre reporta lo mismo, que las
alertas no llegan, y debajo hay siete mecanismos que no comparten causa, ni arreglo, ni dueño. El
archivo abre con un discriminador de cuatro preguntas y despues detalla cada mecanismo con su
evidencia, su estado y quien lo lleva. Todo salio de material que ya estaba en la base y estaba
disperso en once chunks, cuatro memorias y siete fichas.

Los siete: la pagina de administracion que no regenera el SQL del filtro, el endpoint de envio
agotando el tiempo de peticion web, el adjunto ausente en el blob, las rutas rotas en modo Platform
Cohesion, Quick Entry sin cookie de autenticacion, la frontera de fecha UTC, y un PR que borro la
alerta de reasignacion. Mas dos casos abiertos sin mecanismo asignado.

Las rutas citadas se verificaron una por una contra el disco y contra la base antes de publicar.

## Que se enruto

En `investigaciones/INDICE.md` entro una seccion nueva de Smart Alerts con seis entradas, y se
enrutaron cinco memorias que estaban huerfanas desde la curaduria de agosto.

En `flujos/INDICE.md` entraron cinco procesos aprendidos entre el 27 de agosto y el 4 de septiembre,
una seccion nueva de familias de fallas con mapa propio, y tres entradas sobre como se trabaja el
propio cerebro en el Mac.

Ningun `INDICE.md` quedo con rutas rotas. Se verifico con un barrido sobre las dos tablas.

## Hueco de mantenimiento que aparecio de paso

`brain/markdown/` es el espejo de la base en texto plano, y existe para que el cerebro se pueda leer
sin SQLite. Nadie lo regeneraba. Los chunks escritos desde el 25 de agosto solo vivian en la base, y
el respaldo en texto plano estaba dos semanas atrasado.

Se agrego el comando `espejo` y se metio dentro de `cerrar`, que ahora encadena ingerir, indexar,
espejo y estado. El espejo se regenero y quedo al dia.

## Que sigue

Las familias con volumen alto y cobertura parcial son las siguientes candidatas a mapa propio.
Timeout y 502 con 56 fichas esta repartido entre tres memorias que no se citan entre si. SSO con 82
fichas tiene material nuevo del 4 de septiembre que no entro a la memoria existente.

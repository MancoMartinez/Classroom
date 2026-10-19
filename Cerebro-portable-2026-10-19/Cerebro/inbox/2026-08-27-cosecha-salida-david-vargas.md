# Cosecha: revisión de los tickets de David Vargas y reparto del 27 ago

Fecha: 2026-08-27. Sesión de origen: local_f945d5d5-c803-47bb-aefa-2fd6e68c66d5,
"David's tickets assignment review". Todo medido contra Jira en vivo.

## Números medidos

David tiene 6 tickets abiertos en total. Consulta directa por accountId sobre todos los proyectos,
no solo RCS. Coincide exacto con la captura que trajo Juan. Los tickets de quien sale del equipo
nunca aparecen en la cola sin asignar, hay que sacarlos por accountId.

RCS-28018 ya no es de David. Está con Peyman Motlagh.

Cola sin asignar: cero Urgent y cero High. El riesgo de SLA es edad, no prioridad. Cinco tickets
pasan de 7 días y los cinco son de David. RCS-27647, Ollie's, lleva 55 días.

Capacidad del equipo Colombia: cupo total del día 9 contra 29 huérfanos. Faltan 20. Esa es la cifra
que Juan lleva a J.R. Teagle y a Camila Cortes.

## Correcciones al supuesto de entrada

Diego Buelvas no está saturado. Lleva 13 abiertos de un techo de 16, margen 3.

Edwin Garzón es el que está en techo, 16 de 16. Tiene 6 tickets esperando a terceros. El desbloqueo
es cerrar lo que tiene en espera, no subirle el techo.

## Reparto propuesto, 7 tickets

| Persona | Cupo | Tickets |
|---|---|---|
| Diego Buelvas | 3 de 3 | RCS-28452 SpartanNash, RCS-28300 Nordstrom, RCS-28596 Ahold-Delhaize |
| Sebastián Rueda | 2 de 2 | RCS-28270 Nordstrom, RCS-28223 McDonald's |
| Luis Hernández | 1 de 2 | RCS-28574 Lux, condicionado |
| Sebastián Garcés | 1 de 2 | RCS-28582 MYER, condicionado |
| Edwin Garzón | 0 | nada, sin cupo |

Las dos filas de los nuevos quedaron condicionadas. La carpeta Cerebro no estaba montada en esa
sesión, así que no se pudo correr `bin/buscar` y no hay precedente verificado que citarles. Un nuevo
sin precedente no recibe ticket.

## Lo que queda fuera y por qué

RCS-27647, Ollie's, 55 días. Dueño natural Edwin Garzón, ya lleva dos tickets de Ollie's. Sin cupo.
Decisión pendiente de Juan: esperar el cierre de lo que tiene en Under Customer Review, o forzarlo.

RCS-28595, Stater Bros., cambiar el email de username. Fuera del reparto. Apunta a las tres tablas
de identidad de la Unificación de julio 2026, `membership.Users`, `LPUser` y `LPUser2`. Verificar en
`investigaciones/INDICE.md` antes de dárselo a alguien.

## Procedimiento que funcionó

Para sacar los tickets de alguien que sale del equipo, consulta por accountId con
`statusCategory != Done` sobre todos los proyectos. El filtro guardado 29803 y la cola de sin
asignar no los muestran.

## Desviación registrada

El reparto propuso RCS-28452 para Diego Buelvas. Juan lo asignó a Sebastián Rueda. Queda anotado
para el paso de cierre de ciclo del día siguiente.

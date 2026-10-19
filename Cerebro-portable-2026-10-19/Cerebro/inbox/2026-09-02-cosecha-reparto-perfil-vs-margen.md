---
fecha: 2026-09-02
origen: sesion local_43069ff0, "Cerebro asignacion diaria", segunda corrida del 1 sep 2026
tipo: correccion de proceso, clasificador de reparto
estado: sin aprobar para la base
---

# Reparto por perfil da 5 de 6. Reparto por margen da 0 de 4.

## Lo medido el 1 y el 2 de septiembre

Dos corridas el mismo dia, sobre la misma cola, con las mismas cinco personas. Verificado contra
Jira en vivo el 2 de septiembre.

Primera corrida, `asignaciones/2026-09-01.md`, reparto por margen. Puso cuatro tickets en Diego
Buelvas porque era el unico con cupo. Acierto 0 de 4.

Segunda corrida, sesion `local_43069ff0`, reparto por perfil y por quien ya lleva el cliente y el
subsistema, incluso encima del techo. Acierto 5 de 6.

| Ticket | Propuesto | Dueno real | Acierto |
|---|---|---|---|
| RCS-28704 | Luis Hernandez | Luis Hernandez | si |
| RCS-28699 | Luis Hernandez | Luis Hernandez | si |
| RCS-28701 | Sebastian Garces | Sebastian Garces | si |
| RCS-28702 | Edwin Garzon | Edwin Garzon | si |
| RCS-28697 | Edwin Garzon | Edwin Garzon | si |
| RCS-28694 | Edwin Garzon | Shandana Khan | no |

## La regla que sale de ahi

El orden es perfil primero, techo despues. El techo dice cuanto aguanta una persona. No dice quien es
el dueno del ticket. El margen sirve para frenar, no para elegir.

Corolario medido: tres personas terminaron por encima del techo porque tenian el perfil. Luis subio
a 7 contra un techo de 5. Garces a 7 contra 5. Edwin a 18 contra 16. Seis puntos de exceso en total,
y los seis son asignaciones correctas por perfil.

## La unica desviacion, y por que

RCS-28694 se propuso a Edwin como probable duplicado de su RCS-28485, mismo cliente y mismo
subsistema. Quedo con Shandana Khan en Under Engineering Review. El diagnostico de duplicado se
sostuvo. El ticket salio a ingenieria en vez de quedarse en soporte.

Regla nueva: cuando el ticket propuesto es probable duplicado de uno que ya esta en investigacion, la
salida esperada es ingenieria, no la cola del dueno del original.

## Precedentes de tenant que quedaron establecidos

Big5: tenant `big5sportinggoods.com`, ACA, GP11, GP1, staging 147. Fuente: directorio de clientes.

Permission Groups: matriz en Confluence 474657783971.

Guia de Kristine seccion 11: instrucciones de acceso al Support Portal, mas el workaround para el
reporter que todavia no esta en el portal.

## Aviso vivo sobre el lexico

La palabra `permission` es la que confunde al clasificador de dificultad. Marca basico y muchas veces
es identidad de la Unificacion de julio 2026. RCS-28701 esta con Sebastian Garces con ese aviso: si
al abrirlo aparece claim de SSO o las tablas de identidad, sale de la cola de un nuevo.

## Trabajo tipo SOW

RCS-28692 se propuso a Diego por bucket de reportes y quedo con Peyman Motlagh en Under Delivery
Review. El trabajo de tipo SOW sale de la cola de soporte hacia Delivery. Aplicado el 2 de
septiembre a RCS-28713, Pac Sun y Eddie Bauer, tambien issuetype SOW.

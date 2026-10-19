# Tickets con identificador dudoso

Curado a mano. `bin/indexar_tickets.py` no pisa este archivo.

El indexador crea una ficha para cualquier identificador que aparezca escrito en el cerebro. Escribir
un número no lo convierte en un ticket real. Estos cuatro quedaron registrados y después se
desmintieron.

## Desmentidos contra Jira en vivo el 19 ago 2026

RCS-28433, RCS-28445, RCS-28456 y RCS-28472.

La verificación del 19 de agosto corrió `project = RCS AND created >= -3d` contra Jira y no encontró
ninguno de los cuatro. La conclusión escrita ese día fue textual: "esos números no corresponden a
ADUSA, esa lista viene de otra sesión que se equivocó".

Hay una contradicción sin resolver. El archivo `adusa-envio-hoy/0-LEEME-PRIMERO.md` del 18 de agosto
describe RCS-28433 como usuarios sin acceso a LPMS del 17, completado, y RCS-28456 como Price Checked
Items, abierto y sin dueño. Un día después la consulta en vivo no los devolvió. La ventana de tres
días de esa JQL no alcanza a cubrir un ticket creado el 17, así que la consulta pudo no haberlos
podido ver nunca.

Antes de usar cualquiera de estos cuatro números, ábrelo en Jira. No lo cites desde su ficha.

Fuentes: `inbox/2026-08-19-adusa-acciones-antes-del-d3.md` § 3, y
`adusa-envio-hoy/0-LEEME-PRIMERO.md`.

## Qué hacer cuando aparezca otro

Agrégalo aquí con la fecha y la evidencia del desmentido. La ficha generada se queda, este archivo es
el que manda.

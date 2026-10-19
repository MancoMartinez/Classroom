# Tecnica: revelar frames ocultos de APIS con devtools

Fuente: Matt Kamminga, comunicacion directa con Juan, 22 sep 2026, con captura de nexcom-prep,
Template editor AT1000000055, Safety Audit Navy Lodge.

APIS usa frameset clasico en toda la plataforma, no una SPA. La ventana principal reparte el
espacio en filas de frames, y varias quedan con altura casi cero a proposito, por ejemplo
`10,10,10,10,10` en vez de un porcentaje visible. Ahi cargan spinner_work_area, data_area,
status_area, reload_work_area. Si el servidor devuelve un error dentro de uno de esos frames en
vez del contenido esperado, el error existe en el DOM, comprimido a un pixel, invisible.

Como revelarlo: abrir devtools, pestaña Elements, ubicar el `<frameset rows="...">` de mas arriba,
editar ese atributo a mano dandole altura real a las filas ocultas, por ejemplo
`50%,10,10,10,10,10%`. El valor exacto depende de cuantos frames se quieran ver. Con eso, lo que
este cargado en esos frames se vuelve visible en pantalla, incluido un error de servidor si lo
hay.

Aplica a cualquier pantalla de APIS que quede en blanco o se cuelgue sin error visible, no es
especifico de un template ni de un tenant.

Usado por primera vez en RCS-28881, NEXCOM, para intentar capturar en vivo si el hang de 8 a 10
minutos del formulario 576 trae un error de servidor ligado a los labels AUDIT.STATUS.1 y
AUDIT.STATUS.3 ausentes. Pendiente correr la prueba.

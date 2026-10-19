# Cosecha cerebro-persistencia — 2026-08-28
Fuente: sesion local_a166a9b0-f99e-4837-b2a5-623d5f29618c, "Cerebro knowledge organization"

## Hallazgos verificados

Cuatro capas de persistencia, con alcances distintos:

| Capa | Viaja sola a otros chats |
|---|---|
| Skills: cerebro-cola, cerebro-ticket, cerebro-asignacion, cerebro-comentario, cerebro-respuesta-cliente | Si, a todos los chats de todos los proyectos |
| Conocimiento del proyecto Cerebro Daily | Si, a los chats de ese proyecto |
| Carpeta conectada Cerebro-2026-08-18 | No. Se conecta en cada chat |
| Historial del chat | No |

El proyecto Cerebro Daily esta vacio. Cero documentos, cero archivos, sin memoria. Solo tiene
nombre y la descripcion "Update". Los chats nuevos no heredan nada de el.

El conocimiento del proyecto esta montado como `Read-only file system`. Ningun chat escribe ahi.
La idea de que los chats alimenten el conocimiento del proyecto queda descartada por prueba, no
por opinion.

Tamaños medidos de la carpeta Cerebro: 129 MB en total, base SQLite de 32 MB, texto plano de
6.9 MB en 478 archivos. Un proyecto no puede consultar la base SQLite.

Cowork lee y escribe la carpeta completa. En la sesion se consulto la base SQLite, se corrio una
busqueda FTS5 sobre 1648 fragmentos y se abrio una de las 67 memorias. Claude Code no hace falta
para el trabajo diario.

Cowork y Claude Code solo se separan en dos puntos. Claude Code no exige conectar la carpeta
porque arranca dentro de ella. Torch no cabe en el sandbox de Cowork, asi que los embeddings
locales solo corren en el Mac.

Prueba de verificacion despues de abrir un chat: pide "mi cola". Si contesta con los cuatro
niveles y los nombres de los tickets, la carpeta esta conectada. Si la pide, falto conectarla.

## Decisiones

Descartada la copia de Cerebro dentro del conocimiento del proyecto. Dos copias producen dos
verdades que se contradicen y la base SQLite no se puede consultar desde ahi.

Se escribio `CONTRATO-PROYECTO.md` con lo que no caduca: quien es Juan, las ocho reglas que no se
negocian, el estilo de escritura completo, los cuatro niveles de la cola, donde vive cada cosa y
que es fuente de verdad.

Se parcharon cerebro-cola, cerebro-ticket y cerebro-comentario con un paso cero que verifica la
carpeta y se detiene si falta, en lugar de entregar un resultado parcial con aviso.

El flujo de arranque de cada chat queda en dos pasos: asignar el chat al proyecto Cerebro Daily y
conectar la carpeta Cerebro-2026-08-18. El proyecto no arrastra la carpeta.

## Pendiente de verificar

cerebro-asignacion no guardo el parche por un error de conexion. cerebro-respuesta-cliente no
recibio el parche. Las dos ya piden la carpeta, les falta detenerse.

Juan tiene que subir `CONTRATO-PROYECTO.md` al conocimiento del proyecto Cerebro Daily.

Si la app recuerda la carpeta conectada y la sugiere de primera en el chat siguiente. Ese
comportamiento se ve en pantalla, no desde la sesion.

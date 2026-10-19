# 17 sep 2026, dos ajustes mas al clasificador y cola de la tarde

## Bug encontrado y corregido: firma corporativa completa

RCS-27791. Juan pregunto en tono de cierre si todo quedo funcionando. Stephanie Benedetti
contesto "Yes, thank you" seguido de firma completa: cargo, telefono, fax, correo y dos lineas
de hotline con un "?" adentro ("Suspicion of theft? Contact the LP Hotline..."). Ese "?" disparaba
CLIENTE_PIDE y el ticket se leia como si el cliente estuviera preguntando algo, dandolo nivel 1,
cuando el mensaje real es un cierre puro.

Cambios en cliente_devuelve_pelota() (bin/cola.py):
1. La firma se corta ANTES de cualquier chequeo, no solo antes de medir sustancia. Si se conoce
   el autor del comentario, se corta desde su propio nombre en adelante (cargo y contacto
   incluidos). Si no, se corta en el primer dato de contacto (office/phone/tel/mobile/cell/fax,
   mailto, hotline).
2. La funcion ahora devuelve (cede, tipo) en vez de un booleano. tipo es "compromiso" cuando el
   cliente promete volver, o "acuse" cuando solo agradece sin dejar nada pendiente. Antes los dos
   casos caian igual en nivel 3 con el motivo "se comprometio a volver", que es falso para un
   acuse puro. Un acuse puro ahora baja a nivel 4, sin nada pendiente de cara al cliente.

Eval en 100%, 7 de 7 casos vigentes.

## Cola de la tarde (18:14), comparada con la corrida de esta manana (12:07)

Niveles: 1=2, 2=1, 3=5, 4=7.

Nivel 1: RCS-28256 (Appriss Incident Time Out, High, Colton Neal escribio y nadie contesto) y
RCS-28756 (Nike ECOM, Sanath Acharya te menciono directo pidiendo update).

Nivel 2: RCS-28223 (McDonald's, prometiste un update hace 3 dias).

Cambio real: RCS-28281 paso de nivel 4 a nivel 3, esperando al cliente.

Salieron de la cola, cerrados o reasignados: RCS-28294, RCS-28342, RCS-28558.

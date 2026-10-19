# Desbloquear una cuenta bloqueada

Escrito el 11 sep 2026 despues de ejecutarlo en GUESS, RCS-28389. Aplica a cualquier tenant.

## Lo primero: la UI no sirve para esto

La casilla Locked de Control Panel esta ahi y no escribe. No es permiso del admin del cliente,
tampoco responde firmando como el tenant desde el lado Appriss. ENG-7177 se titula "locked
accounts stay locked until Appriss updates the database" y quedo Declined. La base es la unica
ruta. No pierdas media hora probando la casilla.

## Lo segundo: desbloquear no es el arreglo completo

La cuenta cayo por intentos fallidos, o sea que quien la usa no sabe la contraseña. Si la
devuelves abierta sin resetear, teclea la misma contraseña mala y se vuelve a bloquear.

Desbloqueo **mas** reset de contraseña. Asi cerro RCS-28166 en Stater Bros, Kiran desbloqueo y
J.R. mando a los usuarios a Forgot password el mismo dia.

## Paso 0. Armar la lista de cuentas. Aqui se pierde el tiempo, no en el SQL

El cliente casi nunca manda una lista limpia, y ninguna de las que manda es la verdad.

**Junta todas las fuentes del ticket, no solo la ultima.** En RCS-28389 vinieron dos, una tabla
pegada en un comentario el 4 sep y una captura el 11 sep. Solo cinco cuentas estaban en las dos.
Si te quedas con la captura mas reciente pierdes cuatro que el cliente ya habia reportado.

**Une y deja que la base decida.** Consultar trece cuentas cuesta lo mismo que consultar nueve.
Asumir cual sigue bloqueada sale caro. El paso 2 separa estado real de historia, ese es su
trabajo.

**Saca los identificadores de donde ya estan.** Las tablas que el cliente pega desde la UI traen
los links con el GUID adentro, `#edit/<guid>`. Eso te ahorra buscarlos uno por uno. Una captura
de pantalla no trae nada, solo correos, y ahi si toca sacar el GUID del link de cada fila.

**Saca tu propia foto.** En el tenant, Settings, Users, ordenar por Locked descendente. Eso es lo
que ves tu, no lo que el cliente cree ver. Si no coinciden, la base manda.

**Lee el ticket completo antes de armar la lista.** Puede haber cuentas que otro analista ya
desbloqueo. En RCS-28389 Viraj habia confirmado 03263 desbloqueada el 24 ago, esa no entra a la
lista aunque aparezca en el titulo del ticket.

**Verifica que el cliente lo haya pedido.** J.R. en RCS-28166: *"we can unlock them once the
customer gives us permission"*. No desbloquees cuentas por iniciativa propia.

**Mira por que se bloquearon antes de abrirlas.** `LastLockDate` contra `LastLoginDate` es el
chequeo barato. Si la cuenta lleva meses sin login exitoso y se bloqueo la semana pasada, alguien
la esta intentando con la contraseña equivocada y nunca entra. Si no cuadra con un usuario
legitimo, para y preguntale a Juan antes de escribir.

**El diff entre dos fotos es informacion, no ruido.** Las que salieron y las que entraron entre
una fecha y otra te dan la rotacion. En GUESS fueron cuatro y cuatro en una semana, el total
clavado en nueve. Eso es lo que prueba que el problema de fondo no es el desbloqueo.

Y antes de todo esto, `bin/buscar` con el sintoma. Casi siempre ya hay algo escrito.

## Paso 1. Ubicar la base del tenant

Azure Bastion, SSMS, instancia `sqlmi-prd-wus2-arp-001`.

```sql
SELECT name FROM sys.databases
WHERE  state = 0              -- solo bases en linea, descarta las caidas
AND    database_id > 4        -- salta master, tempdb, model y msdb
AND    name LIKE '%platform'  -- las bases de tenant terminan en platform
ORDER BY name;
```

El nombre sale `sqldb-prd-wus2-arp-production-NNN-xxx-platform`, donde NNN es el Client ID. El
Client ID lo sacas del selector Client de la pagina Cache del Control Panel, que lo imprime al
lado del nombre. GUESS es 41. **Nunca elijas la base por parecido del nombre.**

## Paso 2. Mirar antes de escribir

```sql
SELECT UserID,                -- GUID, es la llave con la que vas a escribir despues
       UserName,
       Email,
       Locked,                -- 1 bloqueado, 0 abierto
       InvalidLogonAttempts,  -- contador de fallos consecutivos
       LastLockDate           -- cuando se bloqueo, en UTC
FROM   membership.Users
WHERE  Email IN ('cuenta1@cliente.com', 'cuenta2@cliente.com')
ORDER BY Locked DESC, Email;
```

Dos cosas salen de aca y las dos importan.

**Cuantas filas traen `Locked = 1`.** Ese numero es tu control del paso 3. La lista que manda el
cliente casi siempre esta vencida, trae cuentas que ya se desbloquearon. En GUESS el cliente
pidio trece y la base dijo nueve.

**Los GUID.** A partir de aqui trabajas con `UserID`, no con el correo. El GUID ya quedo
verificado contra la fila real y no depende de como este escrito el email.

Si vuelven menos filas de las que pediste, hay correos que no existen con esa escritura. Buscalos
por `UserName` antes de seguir. No los ignores.

## Paso 3. Escribir, acotado y contado

```sql
BEGIN TRAN;                          -- abre transaccion, nada es definitivo todavia

UPDATE membership.Users
SET    Locked = 0,                   -- abre la cuenta
       InvalidLogonAttempts = 0      -- resetea el contador, ver nota abajo
WHERE  UserID IN (
  'GUID-1',
  'GUID-2'
)
AND    Locked = 1;                   -- guarda: solo toca las que estan bloqueadas

SELECT @@ROWCOUNT AS FilasAfectadas; -- va pegado al UPDATE, cualquier otra sentencia lo pisa

-- Coincide con el conteo del paso 2:  COMMIT TRAN;
-- No coincide:                        ROLLBACK TRAN;
```

Por que cada pieza:

`BEGIN TRAN` te deja salida. Si el numero no cuadra, `ROLLBACK` y no paso nada.

`AND Locked = 1` es la guarda. Sin ella tocas filas que ya estaban bien y el rowcount deja de
significar algo. Con ella, el rowcount es exactamente cuantas cuentas abriste.

`InvalidLogonAttempts = 0` va porque no sabemos si la app lee el flag `Locked` o lo recalcula
desde el contador contra un umbral. Resetear los dos cubre los dos casos y no rompe nada.

`LastLockDate` **no se toca**. Es historia de auditoria, sirve para medir cada cuanto se
rebloquean. En GUESS eso revelo que los bloqueos son goteo continuo, uno cada 2.8 dias, no un
evento de migracion.

**No dejes la transaccion abierta.** Mientras no hagas commit o rollback, esas filas tienen lock
exclusivo en produccion y cualquier login contra ellas se queda esperando.

## Paso 4. Purgar el cache del tenant

El UPDATE se salta la aplicacion, asi que la app puede seguir sirviendo el usuario cacheado como
bloqueado. Control Panel, seccion Engineering, pagina Cache. Eliges el cliente en el selector y
le das **Clear Client Cache**.

Los otros botones no. `Purge Search Cache` solo bota resultados de busqueda. `Clear System Cache`
es capa de plataforma. **`Nuke Cache` borra el cache de todos los tenants, nunca para esto.**

Una purga alcanza toda la granja, la propagacion entre nodos va por Redis pub/sub. No la repitas.

## Paso 5. Verificar y cerrar

Repite el SELECT del paso 2 y confirma todas en cero. Despues abre la lista de usuarios del
tenant y confirma que salen Locked False, porque el purge no siempre pega a la primera.

Al cliente le mandas los cuatro pasos, textuales de J.R.: Sign in, escribir el correo, Forgot
password, abrir el correo y poner contraseña nueva, volver a Sign in con el correo y la nueva.

Registra hora y cuentas en `bitacora/RCS-XXXXX.md`.

## Lo que este flujo no arregla

El umbral de intentos fallidos sobre logins de tienda compartidos. Mientras varias personas usen
la misma cuenta, la lista se vuelve a armar sola. Eso es producto y va por Pendo.

Ver `investigaciones/INDICE.md` para la Unificacion y `brain/memoria/reference_control_panel_admin.md`
para el resto de Control Panel.

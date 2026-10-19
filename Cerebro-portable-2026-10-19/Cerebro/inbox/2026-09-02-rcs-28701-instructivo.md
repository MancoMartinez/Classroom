# Instructivo, RCS-28701, confirmar client ID de DHL Global Mail

No hay comentario de Jira ni transición sugerida en este instructivo. Esto es investigación interna de identificación de cliente, no una acción sobre el ticket.

## Paso 1. Buscar el cliente por nombre en Control Panel

Dónde se ejecuta: Control Panel, lectura.

Acción: entra a Control Panel del ambiente correspondiente, USPROD si el tenant es de Norteamérica. Usa el buscador de clientes y escribe DHL. Revisa todos los resultados que devuelva, no solo el primero.

Qué se espera ver: uno o más clientes con DHL en el nombre, cada uno con su client ID numérico visible en la lista o en el detalle.

Si falla: si DHL no devuelve nada, repite la búsqueda con Global Mail. Si tampoco aparece, pasa al Paso 3.

## Paso 2. Confirmar cuál resultado corresponde a RCS-28701

Dónde se ejecuta: Control Panel, lectura.

Acción: si el Paso 1 devuelve más de un cliente con DHL en el nombre, abre el detalle de cada uno y compara contra el contexto del ticket. El reporter es Stephanie Kudla, dominio dhl.com, y el caso es Illegal Goods con IGEntryPage e IGIncidentReport bajo el módulo Incident, no Secure Audit.

Qué se espera ver: un client ID único que coincide con ese contexto. Anota el client ID y, si el detalle lo muestra, el slug de tenant en la URL.

Si falla: si dos clientes parecen igual de válidos, no elijas. Anota ambos client IDs y pasa al Paso 3 para desambiguar contra el tracker.

## Paso 3. Cruzar contra el tracker de migración, si el Paso 1 o el Paso 2 dejan duda

Dónde se ejecuta: archivo local, lectura.

Acción: abre el archivo en tu Mac, ruta ~/Downloads/Investigacion migracion e unificacion/Incident Migration 2026.xlsx. Busca la fila de DHL Global Mail y lee las columnas de número de cliente y ABV.

Qué se espera ver: el número de cliente y el ABV oficiales, que deben coincidir con lo encontrado en Control Panel.

Si falla: si el tracker tampoco trae DHL Global Mail, el dato no está confirmado en ninguna fuente interna disponible. Usa el client ID que confirmaste directamente en Control Panel en el Paso 1 o el Paso 2, ese es la fuente de verdad más alta disponible.

## Paso 4. Registrar el hallazgo para que quede buscable

Dónde se ejecuta: Cerebro, escritura, autoriza Juan.

Acción, en una nota nueva a guardar en la carpeta 16, RCS Soluciones:

Client ID confirmado de DHL Global Mail (organizacion JSD 72): [completar tras Paso 1 o 2]. Slug de tenant: [completar]. Fuente: Control Panel, [ambiente], [fecha]. Contraste contra Incident Migration 2026.xlsx: [coincide / no coincide / tracker sin esta fila].

Qué se espera ver: la nota queda indexada y la próxima vez que aparezca DHL Global Mail, bin/buscar la encuentra.

Si falla: no aplica, este paso no tiene condición de fallo técnico, solo depende de que Juan lo autorice y lo pegue.

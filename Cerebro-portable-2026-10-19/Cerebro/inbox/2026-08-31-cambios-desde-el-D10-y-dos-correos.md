# Cambios desde el D10, y los dos correos

Fecha: lunes 31 ago 2026, 13:15 ET. Verificada con `date`.
Baseline: Appriss ADUSA-Support-Tracker - 08282026 D10.xlsx, estado del 28 ago 19:00.
Barrido: los 42 del D10, más búsqueda de tickets nuevos por los cuatro reporters de ADUSA y por asunto.

El documento de hoy es el D11. La numeración D cuenta días hábiles. Lun 24 fue D6, vie 28 fue D10, hoy lunes es
D11.

## Cambios en Jira. Dos, y las dos son higiene

RCS-28378 pasó de Completed a Closed hoy 10:34.
RCS-28356 pasó de Completed a Closed hoy 10:30.

Las dos ya contaban como Resolved en el tracker. Nada cambia para el cliente.

Ningún otro de los 42 se movió en todo el fin de semana.

## Ticket nuevo. RCS-28667

Reporter Leigh Ann Stubbs, creado el 29 de agosto a las 13:02. Work in progress. Assignee Megha Rathi, no tú.

Lo que dice. Usuarios nuevos entran a la plataforma sin jerarquía asignada, y por eso no pueden seleccionar una
tienda para abrir un caso. Leigh Ann entra al perfil, agrega una ubicación de jerarquía, y el usuario ya puede
crear casos. Ejemplo confirmado por el propio usuario, Gabriel Quist: "I am able to select locations now and
create cases."

Y hace una pregunta de proceso, que es lo que de verdad hay que contestar: eso de armar la jerarquía de cada
usuario nuevo es función de administración del cliente, o debería quedar resuelto en la configuración de
provisioning.

**Esto no es un ticket nuevo, es el tercer brote del mismo tema.** RCS-28415, dos usuarios nuevos de Stop & Shop
sin poder crear casos, cerrado el 19. RCS-28519, Deborah Jean y Sammy Rivera, cerrado el 26. Los dos se
arreglaron a mano en el dato. La nota de cierre de RCS-28415 decía que Appriss estaba verificando si la
ubicación viaja en el claim de SSO para las cuentas futuras. Esa verificación nunca concluyó, y ahora el
síntoma vuelve para cada usuario nuevo.

Ese es el punto que hay que poner en la fila del tracker. No es un caso aislado, es una brecha de provisioning
que el cliente está tapando a mano.

## Correo de Jim sobre RCS-28093

Jim dice que April confirmó que la posición 20 de DA_Employee_Info.dat viene poblada para todos los registros,
y pregunta si tienes ejemplos donde no.

Sí lo tienes, y ya lo entregaste. El 21 de agosto a las 13:21 escribiste en el ticket: en la tienda 0001, el
empleado 5701349746 tiene MISC1 vacío mientras los demás traen FOOD LION ,LLC o The Stop & Shop Supermarket
Company LLC.

**No lo reenvíes sin verificar.** Ese ejemplo tiene diez días y April pudo haber corregido el feed en el medio.
Si mandas un ID que ya está poblado, Appriss queda reportando un problema que el cliente ya resolvió.

Verifica primero el estado de hoy del empleado 5701349746 en la tienda 0001, y de paso un muestreo del resto de
esa tienda. Dos escenarios y cada uno lleva a un lado distinto.

Si la posición 20 ya viene poblada en todos, el feed está corregido y lo que toca es volver a probar la búsqueda
de empleado, porque el arreglo del filtro de marca dependía de ese dato. Ahí el ticket pasa a validación
técnica de Appriss.

Si sigue vacía en algunos, le devuelves los IDs concretos y la pelota vuelve a ADUSA.

En los dos casos RCS-28093 deja de ser Awaiting Ahold input. ADUSA contestó. La categoría pasa a Active with
Appriss porque lo que falta lo debe Appriss.

Nota de método: la confirmación de April llegó por correo y no está en el ticket. Cuando respondas, deja la
confirmación escrita en Jira, o el tracker de mañana vuelve a mostrar un estado que el ticket no respalda.

## Conteos que mostraría el D11

Total 43, contra 42 en el D10. Resueltos 36. Pending Ahold verification 0. Awaiting Ahold input 0.
Active with Appriss 7.

Los siete activos: RCS-28093, RCS-28123, RCS-28281, RCS-28482, RCS-28535, RCS-28596, RCS-28667.

RCS-28667 entra en Store and brand restrictions, junto a RCS-28415 y RCS-28519 que son el mismo síntoma. Ese
tema pasa a 8 tickets, 5 resueltos y 3 activos.

## Lo que hay que resolver antes de generar el D11

1. Verificar la posición 20 del empleado 5701349746 en la tienda 0001. Decide el contenido de la fila de
   RCS-28093 y la respuesta a Jim.
2. Definir quién contesta RCS-28667. Está asignado a Megha Rathi y Leigh Ann te escribió a ti. Si contestas tú
   sin coordinar, quedan dos voces en el mismo ticket.
3. Sigue abierto de la semana pasada: confirmar que el ítem de RCS-28123 que le mencionaste a Jim el 26 existe
   en Jira. La búsqueda no lo encuentra.

Dime cómo sale la verificación de la posición 20 y genero el D11 con el correo.

# RCS-28671 THD Searches Producing only Errors

Fecha: 2026-08-31. Assignee: Juan Martinez. Estado en Jira: Escalated. Prioridad: High.
Reporter: Corey Wood (corey_wood@homedepot.com).

## Que se te pidio, exactamente

Simon Smith, 31 ago 12:26 EDT, en el ticket:

> "I've fixed the search in question and around 149 others. **Could someone in support retest?**
> I'm focusing on the public folder first, where there was 50 remaining ones to investigate, and
> then I'll look to fix user searches."

Tu tarea es correr la busqueda y reportar si pasa o falla. Nada mas. La causa raiz ya la tiene
Simon y la esta trabajando en DO-12041.

---

# El retest

## Antes de empezar: no edites nada

Abrir, correr, leer. No toques Composer. Simon esta reparando en este momento y en el caso
equivalente de Kinney Drugs, editar el campo por Composer empeoro el conteo de fallos de 3 de 30 a
11 de 30. Si tu editas mientras el repara, ninguno de los dos puede interpretar el resultado.

## Paso 1. Entrar a Explorer

Ya tienes sesion de tenant abierta desde Control Panel. El host de THD es
`https://apps.apprissretail.com/homedepot/`, no el patron `.apprissretailcloud.com`.

Estas en `platform/portal`. Explorer es otra aplicacion:

    https://apps.apprissretail.com/homedepot/platform/explorer

O la cuadricula de nueve puntos en la esquina superior izquierda. Es routing por hash, si cambias
solo lo que va despues del `#` la SPA no recarga. F5.

## Paso 2. Abrir la busqueda

**Path real, leido de la URL del Composer el 31 ago 12:49:**

    /public/internal investigation lookups/line item void/line item void - general search.search

Simon escribio bien el path. El arbol de Explorer muestra la carpeta como **Investigation Lookups**
porque ese es el display name. El file path es `internal investigation lookups`. El file path no
cambia aunque el cliente renombre, el display name si. No confundir uno con otro al comentar.

Busqueda del ticket: **Line Item Void - General Search**, owner Melissa Somer, "All line item voids
by a selected parameters".

## Paso 2b. Lo que dice la columna Last Changed

Simon reparo parte de esta carpeta hoy en la mañana y dejo el resto sin tocar. Lo dice la propia
lista, sin consultar nada:

| Busqueda | Last Changed | Estado |
|---|---|---|
| Line Item Void - SKU and Product Hiearchy | 08/31/26 11:03:49 | reparada hoy |
| **Line Item Void - General Search** | **08/31/26 11:04:47** | **reparada hoy, es la del ticket** |
| Line Item Void by Location Hierarchy V2 | 08/31/26 11:06:11 | reparada hoy |
| Line Item Void by Location Hierarchy | 08/31/26 11:17:55 | reparada hoy |
| Line Item Void by SKU and Store | 08/31/26 11:18:10 | reparada hoy |
| Account Acquisition Followed by LIV | 05/27/26 13:31:30 | sin tocar |
| Line Item Void by Department-Class-Subclass | 07/16/26 14:27:51 | sin tocar |
| Line Item Void by Cashier | 09/02/25 09:15:52 | sin tocar |
| Line Item Void by Location Hierarchy V3 | 01/12/23 08:37:26 | sin tocar |

La del ticket tiene fecha de hoy, asi que tu corrida si mide el trabajo de Simon.

## Paso 3. Poner los parametros de Corey

Exactamente estos, ni uno mas. Salen de su captura:

| Toggle | Seccion | Parametro | Operador | Valor |
|---|---|---|---|---|
| ON, REQ | HEADER | Transaction Date | Between | June 01 2026 y August 31 2026 |
| ON, REQ | HEADER | Store Number | Equal to | 2605 |
| ON | HEADER | Cashier LDAP | Equal to | UBMKVT7 |
| OFF | HEADER | Transaction Total | | |
| OFF | HEADER | Total Line Item Void Amount | | |
| OFF | TENDER | Account Number XREF | | |
| OFF | ITEM | SKU | | |
| OFF | TENDER | Tender Type Group | | |

**Tender Type Group va apagado.** En la captura de Corey esta apagado y la query igual incluia el
join que rompia, porque ese join vive en la definicion y no en el parametro. Si lo enciendes cambias
el caso y el resultado deja de ser comparable con lo que reporto el cliente.

## Paso 4. Run

Pestaña **Tabular**.

Anota:

- Hora de la corrida.
- **Si falla**: el tracking code que sale en pantalla. Es lo que permite cruzarlo con el log.
  Los dos previos son `7f39278d-ebfd-5af1-9a85-131fc3dff2cb` y
  `b7441dab-23a8-5798-b875-e5d63e194565`.
- **Si pasa**: numero de filas.
- Captura de pantalla en los dos casos.

## Paso 5. La segunda corrida, de control

**Line Item Void by Cashier** no sirve como control del defecto. Verificado en su Composer el 31 ago
12:50: sus condiciones son Transaction Date, Store Number, Cashier LDAP, Total Line Item Void Count
y Transaction Type. No tiene Tender Type Group, ni en Conditions ni en Display Fields. Sin ese
campo no se genera el join que rompia, asi que esa busqueda no estaba rota y correrla no prueba
nada sobre la reparacion.

Sirve para otra cosa, y por eso vale correrla igual: confirma que el tenant y el data area
responden. Sus tres parametros son REQ: Transaction Date, Store Number In, Cashier LDAP In.

**El control que si prueba el defecto** es una busqueda sin tocar que si tenga Tender Type Group.
Las tres candidatas, todas de la misma carpeta:

| Busqueda | Last Changed |
|---|---|
| Account Acquisition Followed by LIV | 05/27/26 13:31:30 |
| Line Item Void by Department-Class-Subclass | 07/16/26 14:27:51 |
| Line Item Void by Location Hierarchy V3 | 01/12/23 08:37:26 |

Abrelas en Composer y mira si **Tender Type Group** aparece en Conditions o en Display Fields. La
primera que lo tenga es el control. No edites, solo mira.

Lectura de resultados:

- **General Search pasa**: la reparacion resolvio el caso del cliente.
- **General Search pasa y el control con Tender Type Group falla**: quedan busquedas rotas por el
  mismo defecto en la carpeta que Simon ya reviso. Ese es el hallazgo que evita cerrar temprano.
- **General Search falla**: la reparacion no resolvio el caso. Manda el tracking code.

## Paso 6. Comentar el resultado

Ahi termina tu parte. El texto se redacta con `cerebro-comentario` cuando tengas el resultado,
dirigido a Simon, con: que busqueda corriste, con que parametros, PASS o FAIL, y el tracking code
si fallo.

---

# Resultado del retest

| Busqueda | Parametros | Resultado | Evidencia | Hora |
|---|---|---|---|---|
| Line Item Void - General Search | Store 2605, Cashier UBMKVT7, 01 jun a 31 ago 2026 | **PASS** | 216 results | 31 ago 12:57 EDT |
| Segunda, de control | | pendiente | | |

**La columna Tender Type devuelve valores.** En pantalla salen Charge y Debit. Esa columna es la que
producia el join que rompia, `T6.KeyAsInt = T3.TenderTypeGroup` contra
`secure_EnumerationReferenceData`. Que resuelva y traiga valores es evidencia directa de que la
reparacion corrigio el defecto, no solo de que la query dejo de fallar.

Datos de la corrida: store 2605, cashier UBMKVT7, transacciones del 02 jun 2026, register 20,
Trans ID 6646 y 6652, empleado BROCK DESTREMPS.

Observacion aparte, no bloquea nada. Las filas se repiten: Trans ID 6646 sale tres veces y 6652 sale
seis, todas con Total Line Item Void Count igual a 1 y el mismo monto. La definicion tiene LEFT JOIN
a `ardm_Item` y a `ardm_Tender` sin agregacion, asi que multiplicar filas por item o por tender es
consistente con eso. No lo reportes como defecto sin medirlo. Si el cliente se queja de conteos
inflados, el precedente es RCS-28077 de Ahold Delhaize, donde las busquedas de refunds devolvian
cada articulo seis veces por un join a tablas `reference_`.

---

# Lo que conviene preguntarle a Simon en el mismo comentario

Dos preguntas, no queries. El tiene los datos.

1. **Alcance de las busquedas de usuario.** El dijo que arranca por la carpeta publica y despues ve
   las de usuario. Corey reporta impacto en field y office users a nivel enterprise. Si respondes al
   cliente cuando la carpeta publica quede verde, vuelve manana con una busqueda de su carpeta
   personal.
2. **Cuantas quedan.** El dijo 50 pendientes en la publica. Preguntale el numero de las de usuario y
   en que plazo.

Esto es lo que impide que el ticket se cierre temprano, y no te cuesta ninguna consulta a base de
datos.

---

# Contexto, por si te lo preguntan

No necesitas esto para el retest. Sirve si Peyman o el cliente preguntan que paso.

El error es de Snowflake, `invalid identifier 'T3.TENDERTYPEGROUP'`, VendorCode 904. La definicion
guardada pide la columna `TenderTypeGroup` sobre `ardm_Tender` y esa columna ya no existe con ese
nombre.

Existe porque THD es cliente 85 y esta en migracion SnowTime en curso:
`DO-12041 SnowTime - C085_THD - Testing & Verification`, assignee Simon Smith, estado
**In Development**. Su descripcion dice textual "Verify searches still work". La migracion cambio el
esquema fisico y las definiciones guardadas quedaron apuntando al nombre viejo.

Es la misma clase de defecto que **RCS-28543** (Kinney Drugs), donde la causa quedo escrita asi:
"Secure's Instant Analytics field metadata was never resynced" tras la migracion. Ese ticket sigue
Under Engineering Review.

## Transicion

Ninguna hoy. Comenta y deja el estado quieto.

Verificado por API el 31 ago: desde Escalated si esta disponible Under Customer Review, id 571, sin
pantalla. Tecnicamente se puede. La razon para no hacerlo es otra. El motivo por el que Corey escalo
sigue vivo, porque quedan 50 busquedas publicas sin investigar y ninguna de usuario. Under Customer
Review pausa los SLA y arranca el reloj de auto cierre a 28 dias, y saca el ticket del Kanban de
escalados que se revisa en el SCRUM.

Mueve a Under Customer Review cuando lo unico pendiente sea la confirmacion de Corey y Simon haya
cerrado el alcance.

Detalle completo y medido en `flujos/estado-escalated.md`.

## Dato para el cerebro

El host del tenant de THD es `https://apps.apprissretail.com/homedepot/`. El cerebro decia que la
convencion era `[abrev].apprissretailcloud.com`, con nota de que Kroger y Academy usan
`apps.apprissretail.com/[cliente]/`. THD va en ese segundo grupo. Agregarlo cuando se cierre el
ticket.

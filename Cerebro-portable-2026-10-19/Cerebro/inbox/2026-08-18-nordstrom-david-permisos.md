# David sin permisos en dashboards de Nordstrom — RCS-28219

18 ago 2026. Juan ayudando a David Vargas. Error: `Permission Required` en
`usprod.apprissretailcloud.com/platform/cpf/errorhandler/nopermission`, con branding de
Nordstrom. David tampoco puede usar Impersonate User. Trey no maneja permisos dentro de apps.

## Qué dijo Kiran y qué significa

Kiran pidió *"the Prod url for Nordstrom"*. Juan le mandó enlaces profundos a dashboards.
Ella corrigió: *"I meant the signing url"* — quería la URL de **inicio de sesión**, con la
que identifica plataforma y tenant. Un `#/dashboard/...` no se lo dice.

Y el dato de fondo: *"usprod is not PU yet"*, *"app.apprissretail.com is pu"*.
**PU = Platform Unification.** El host que le pasaron es de la plataforma **clásica**, no de
la unificada, que es donde ella administra.

## La consecuencia práctica

David está entrando por **usprod**, o sea plataforma clásica. Sus permisos **no** se
administran del lado de Kiran, se administran en **Control Panel USPROD**, donde Juan ya
tiene acceso con `SupportL2` + `Engineers`. No hace falta escalar.

Ruta:
1. `usprod.apprissretailcloud.com/control`
2. En *Customers in USPROD*, **clic en el logo de Nordstrom** para entrar al tenant.
   No usar `/<slug>/signin`, que redirige al SSO del cliente donde el usuario de Appriss
   no existe.
3. All apps → Settings → Users → buscar a David
4. User details → Permission groups → agregar los que falten y **guardar**
5. Verificar la base de tres que llevan todos: `ApprissCase Search Users`,
   `ApprissCase Users`, `Basic Users`. Como el error es de dashboards, buscar además el
   grupo específico de dashboards o reporting.

## Duda abierta

Juan le dijo a David que entrara por `nordstrom.apprissretailcloud.com` y terminó en
`usprod`. Puede ser un redirect o que entrara por otra ruta. Confirmar con David la URL
exacta de login: si Nordstrom estuviera en PU, el sitio sería `app.apprissretail.com` y
entonces sí sería caso de Kiran.

RCS-28219 no se pudo abrir, el conector de Jira lleva caído toda la tarde (HTTP 404).

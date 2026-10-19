# RCS-28153 · El fix salió a producción hoy

Verificado en Jira y en el PR de Azure DevOps el 27 ago 2026.
Corrige lo que escribí esta tarde. Yo dije que no había evidencia de release a producción. Sí la hay,
y es de hoy.

## Lo que confirma la captura del PR

PR **56323**, estado **Completed**. Vedant Shirude lo mergeó a **main** el 20 ago a las 9:24 AM,
commit `d534d7fe`, rama `vedant-eng-7184-bug-incident-session-timeout-fix`.
Los cinco checks requeridos pasaron, sin conflictos. Aprobado por Chris Rippingale, Gina Pilato y
Matt Gladden. Kiran Vadday y Matt Kamminga figuran como opcionales sin revisar.

El work item es **ENG-7184**, no el número que yo venía manejando.

## Lo que confirma Jira sobre ENG-7184

| Campo | Valor |
|---|---|
| Título | Platform Session: cookie expires at the platform default and discards in-progress case entry |
| Status | **Done** |
| Resolution | **Resolved** |
| Fix version | **Secure August 2026 Release 2/2**, `released: true`, fecha **27 ago 2026** |
| Labels | `lpguys-deployed-prod`, `lpguys-deployed-test`, `Unification_Jul_26`, `2026` |
| Reporter | J.R. Teagle |
| Assignee | Vedant Shirude |
| Última actualización | 27 ago 2026, 08:20 |

`lpguys-deployed-prod` y el release marcado como liberado hoy son la evidencia que faltaba.

## Causa raíz, de la descripción del PR

`TryRefreshPlatformCohesionCookie`, el refresh de ventana deslizante del `CPFCookie` que corre en cada
carga de página de Nettrack, leía el timeout de sesión desde
`System.Configuration.ConfigurationManager.AppSettings("CPF.Core.LogOnTimeoutMinutes")`.
Esa clave de `web.config` **nunca se cableó**. El refresh caía siempre al default hardcodeado de 60
minutos e ignoraba el timeout configurado del tenant. Los usuarios que trabajaban solo dentro de
Nettrack quedaban deslogueados en el momento equivocado respecto de la sesión de la plataforma Secure.

Solución: leer el valor desde `secure.ConfigurationItem`, reusando
`LPSBO.Common.ReadEffectiveConfigurationValue(Name, PlatformID)`, que se amplió de `Private Shared` a
`Public Shared` porque ya la usaba el flag de screen label de ENG-7168. Resuelve
`COALESCE(NULLIF(CustomerEditedValue,''), Value)` para el ClientID del request, la misma precedencia
de override que espera el Control Panel. El decrypt de la cookie se movió más arriba en el método
para que `info.ClientID` esté disponible.

Eso también explica el comentario de Vedant del 19 ago sobre probar con `CustomerEditedValue` en 1.

## Hallazgo de alcance: hay dos tickets RCS más que este fix resuelve

ENG-7184 tiene seis tickets RCS enlazados. Estado verificado hoy:

| Ticket | Resumen | Estado |
|---|---|---|
| RCS-28036 | Big Y - Case deleted | Closed |
| RCS-28603 | Stater Bros. Holdings - System Times Out Quickly | Closed |
| **RCS-28153** | BYF - Errors and logging users out | Under Customer Review, tuyo |
| **RCS-28181** | Big Y Foods - ERMS Platform Issues | **Work in progress**, abierto |
| **RCS-28346** | Stater Bros - Angie Martinez - Locked user accounts | **Under Customer Review**, abierto |

RCS-28181 y RCS-28346 no están en tu cola, así que los lleva otra persona. Los dos siguen abiertos
contra un defecto que se resolvió hoy. Avisa a quien los tenga.

## Matiz antes de prometerle a Ashley que todo quedó resuelto

ENG-7184 tiene link `relates to` con **ENG-6220, Sign Out Behaviours**, Bug, High, status **In
Testing**. Ese no está liberado.

ENG-7184 arregla que el refresh de la cookie respete el timeout configurado del tenant. No cubre todo
el comportamiento de cierre de sesión. Escríbele a Ashley sobre los logouts prematuros y nada más.
No le digas que el comportamiento de sesión quedó completo.

## Los tres pasos

**Paso 1. Confirmar la versión en el tenant de Big Y.**
El release quedó marcado como liberado hoy. Confirma que BYF ya corre esa versión antes de pedirle a
Ashley que valide. Si le pides validar sobre una versión que todavía no le llegó, va a decir que
sigue fallando y el ticket retrocede.

**Paso 2. Escribir a Ashley.** Corre hoy. El reloj de cierre automático arrancó el 25 ago y ella
lleva 16 días sin oír nada sobre un ticket High. Este comentario también reinicia ese reloj.

```
Hi Ashley,

Update on this one.

We traced the errors and the unexpected logouts to a session timeout issue rather than to the attachments themselves. The session refresh was falling back to a default timeout instead of reading the one configured for your environment, which logged users out earlier than expected while they were working.

A fix has been developed, tested and released.

Could you and your users work normally over the next few days and let me know whether the errors and the early logouts have stopped? Once you confirm, I will close this out.

Thank you.
```

**Paso 3. Cerrar solo con la confirmación de Ashley.** La secuencia es la del workflow. Comentario al
cliente confirmando el cierre, comentario interno con lo que se arregló que alimenta el Resolution
Details, después Resolve, transición 111, a `Completed`, y después Close, transición 91. Nada pasa
solo de Completed a Closed.

Sugerencia de Resolution Details cuando llegue el momento: `Engineer Resolved`, segundo nivel
`Bug - Resolved w/ Release`, citando ENG-7184 y Secure August 2026 Release 2/2.

## Comentario interno para dejar la trazabilidad en el ticket

```
Root cause and fix confirmed against ENG-7184.

TryRefreshPlatformCohesionCookie, the sliding-window refresh of CPFCookie that runs on every Nettrack page load, was reading the session timeout from the web.config key CPF.Core.LogOnTimeoutMinutes. That key was never wired up, so the refresh always fell back to the hardcoded 60 minute default and ignored the timeout configured for the tenant. Users working only inside Nettrack were logged out at the wrong time relative to the Secure platform session.

Fixed by reading the value from secure.ConfigurationItem through LPSBO.Common.ReadEffectiveConfigurationValue, which resolves COALESCE(NULLIF(CustomerEditedValue,''), Value) for the request ClientID, the same override precedence the Control Panel expects.

PR 56323, merged to main on 20 August, commit d534d7fe. ENG-7184 is Done and Resolved against fix version Secure August 2026 Release 2/2, released 27 August, labelled lpguys-deployed-prod.

Awaiting customer confirmation before closing.

Note on scope. ENG-7184 covers the cookie refresh reading the tenant timeout. ENG-6220, Sign Out Behaviours, is a separate High bug still In Testing. RCS-28181 and RCS-28346 are also linked to ENG-7184 and are still open with other assignees.
```

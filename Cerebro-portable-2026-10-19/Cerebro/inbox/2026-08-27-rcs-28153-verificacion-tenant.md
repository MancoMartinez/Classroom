# RCS-28153 · Cómo verificar antes de escribirle a Ashley

27 ago 2026. Dos capas ya las verifiqué yo. Quedan dos que solo puedes hacer tú.
El procedimiento general quedó en `flujos/verificar-fix-en-produccion.md`.

## Ya verificado, no lo repitas

**Capa 1, el ticket ENG.** ENG-7184 en `Done`, resolution `Resolved`, fixVersion
`Secure August 2026 Release 2/2` con `released: true` y fecha 27 ago. Labels `lpguys-deployed-prod`
y `lpguys-deployed-test`.

**Capa 2, las Release Notes.** Página `Secure August 2026 Release 2/2 Release Notes`, espacio ARPDT,
id 478150459393, autora Shandana Khan, estado Released, fecha 8/27/2026.
https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/478150459393

ENG-7184 aparece en la sección **`Completed issues by product area`**, la de trabajo entregado. La
línea literal:

> ENG-7184 — Platform session cookie expiry discards in-progress case entry

No está en `Open and follow-up items`, no lleva salvedad y no está duplicado. Cuenta como entregado.

**Dato que importa.** De los 118 issues del fixVersion solo 81 están en Done. Un fixVersion liberado
no implica que todo lo que viaja en él esté listo. ENG-7184 sí lo está.

**Confirmado además:** ENG-6220, Sign Out Behaviours, **no aparece en este release**. La cadena "Sign
Out" no está en la página. Eso ratifica el matiz: escríbele a Ashley solo sobre los logouts
prematuros por timeout.

## Capa 3, la ventana de despliegue. Dos minutos

Abre el calendario en vivo, no la memoria:
https://docs.apprissretail.com/products/product-docs/general/release-calendar

Dos señales convergen y por eso esta capa es casi trámite. La fixVersion dice released el 27 ago.
El cerebro registra que **US PROD se despliega el último jueves del mes a las 9am BST**. Hoy es
jueves 27 y es el último jueves de agosto. 9am BST son las 3am hora Colombia, así que la ventana ya
pasó cuando empezaste el día.

Advertencia: el cerebro tiene dos versiones de la cadencia sin reconciliar. Una dice último jueves
del mes, otra dice semanas 2 y 4, miércoles y jueves. Por eso miras el calendario en vivo y no
la nota.

## Capa 4, la prueba en el tenant. Es la que importa

**Aquí hay un riesgo que ninguna de las capas anteriores detecta, y puede tumbarte el mensaje.**

Lo que ENG-7184 cambió es de dónde se lee el timeout. Antes salía de
`CPF.Core.LogOnTimeoutMinutes` en `web.config`, una clave nunca cableada, y siempre caía al default
de 60 minutos. Ahora lo lee de `secure.ConfigurationItem` resolviendo
`COALESCE(NULLIF(CustomerEditedValue,''), Value)` para el ClientID del request.

Léelo así: **el fix solo cambia el comportamiento si Big Y tiene configurado un valor distinto de 60.**
Si el valor efectivo del cliente 362 es 60, o está vacío, el comportamiento después del fix es
idéntico al de antes y Ashley te va a decir que sigue igual.

Ese es el escenario que hay que descartar antes de pedirle nada.

### Cómo leerlo. Solo lectura, no toques el valor

**Big Y Foods es el cliente 362.** Cliente nuevo, nació en la plataforma nueva, sin instancia de
Greenplum.

Por Control Panel:

1. Entra a `usprod.apprissretailcloud.com/control`, entorno USPROD. Tienes los roles `SupportL2` y
   `Engineers`, que es lo que hace falta.
2. Verifica arriba que estás en US production. La barra roja significa producción.
3. Menú **Engineering**, sección **Config Items**.
4. Filtra por el cliente 362, Big Y Foods, y busca `CPF.Core.LogOnTimeoutMinutes`.
5. Anota las dos columnas: el valor por defecto y el valor editado por el cliente. Lo que manda es
   el editado si no está vacío.

Si prefieres SQL, la base del tenant sigue el patrón
`sqldb-prd-wus2-arp-production-362-<código>-platform`. Confirma el código corto en el Product
Delivery Client Matrix antes de conectarte. Solo SELECT sobre `secure.ConfigurationItem` filtrando
por `Name` igual a `CPF.Core.LogOnTimeoutMinutes`.

### Qué significa cada resultado

| Valor efectivo para el cliente 362 | Lectura | Qué hacer |
|---|---|---|
| Distinto de 60 minutos | El fix cambia el comportamiento. Antes la sesión moría a los 60, ahora respeta este valor. | Escribe a Ashley el comentario del archivo anterior. |
| Igual a 60, o vacío | El fix no cambia nada observable para Big Y. | Frena. No le escribas todavía. Pregunta primero. |
| No existe el config item para este cliente | Igual que el anterior, cae al default. | Frena y pregunta. |

**Si cae en las dos últimas filas**, el problema de Ashley puede no ser el que arregla ENG-7184, o
Big Y necesita además que alguien le configure el timeout. Eso es una pregunta para Vedant Shirude
antes de prometer nada.

### Prueba de comportamiento, si quieres cerrarlo del todo

Con el valor configurado en la mano, firma como Big Y desde la tabla *Customers in USPROD*, columna
*Click logo to sign in*, entra a Nettrack y déjalo abierto navegando. La sesión debe sobrevivir hasta
el valor configurado, no morir a los 60 minutos. Es una prueba de reloj, así que déjala corriendo
mientras trabajas otra cosa.

## Capa 5, preguntar. Dos minutos y resuelve la ambigüedad

Si la capa 4 deja dudas, escríbele a Vedant Shirude por Teams. Es el assignee de ENG-7184 y quien
mergeó el PR. J.R. Teagle es el reporter.

```
Hi Vedant, quick one on ENG-7184. It is Done against Secure August 2026 Release 2/2 and shows lpguys-deployed-prod. Can you confirm it is live for Big Y Foods, client 362, before I ask the customer to validate on RCS-28153. Also, does the fix only change behaviour where the tenant has a configured value other than the 60 minute default? Thanks.
```

Aprovecha y pregúntale qué garantizan exactamente los labels `lpguys-deployed-prod` y
`lpguys-deployed-test`. El cerebro no lo tiene documentado y va a volver a hacer falta.

## Recordatorio de alcance

RCS-28181, Big Y Foods ERMS Platform Issues, en Work in progress, y RCS-28346, Stater Bros Angie
Martinez Locked user accounts, en Under Customer Review, están enlazados al mismo ENG-7184 y siguen
abiertos con otros assignees. Stater Bros es el cliente 423. Lo que descubras en la capa 4 les sirve
igual.

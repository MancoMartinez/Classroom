# Verificar que un fix llegó a producción antes de decírselo al cliente

Escrito el 27 ago 2026 a partir del caso RCS-28153 y ENG-7184.
El cerebro no tenía este procedimiento. Lo busqué en `brain/markdown/`, `brain/memoria/`,
`flujos/` e `investigaciones/` y no existe nada sobre cómo leer la versión que corre un tenant.
Este archivo llena ese hueco con lo que sí está documentado más lo verificado en vivo.

## Por qué el paso importa

Si le pides al cliente que valide sobre una versión que todavía no le llegó, va a responder que
sigue fallando. El ticket retrocede, pierdes la confianza y el reloj vuelve a cero.

## Las cinco capas, de la más barata a la más cara

Sube de capa solo mientras la anterior no alcance. Las capas 1 y 2 se hacen desde el escritorio en
cinco minutos. La 4 es la única que prueba el comportamiento real.

---

### Capa 1. El ticket ENG en Jira

Abre el ticket de ingeniería y mira tres campos.

| Campo | Qué buscar |
|---|---|
| Status | `Done` |
| Resolution | `Resolved` |
| Fix version | Que exista, y que diga `released: true` con fecha |

Los labels `lpguys-deployed-prod` y `lpguys-deployed-test` son señal fuerte. Advertencia: el cerebro
no documenta quién los pone ni qué garantizan exactamente. Trátalos como indicio, no como prueba.
Si alguien confirma su semántica, guárdalo aquí.

### Capa 2. Las Release Notes en Confluence

Espacio **ARPDT**. Patrón de título: `Secure <Mes> <Año> Release N/2 Release Notes`.

Busca el ticket ENG en la página y fíjate **en qué sección cae**. La distinción decide si puedes
hablar o no:

- `Completed issues by product area` significa entregado.
- `Open and follow-up items` significa que viajó en el mismo fixVersion sin estar en Done.
  La página lo dice literal: *"These may represent post-release validation, partially delivered
  scope, or items carried in the same fixVersion for tracking."*

Un fixVersion marcado como released no implica que todos sus issues estén listos. En el release del
27 ago, de 118 issues solo 81 estaban en Done. Hay tickets que aparecen en las dos secciones a la
vez. Verifica el estado en Jira, no te quedes con la página.

### Capa 3. El calendario y la ventana de despliegue

Calendario oficial: https://docs.apprissretail.com/products/product-docs/general/release-calendar

El cerebro tiene dos versiones de la cadencia y no están reconciliadas:

- `brain/markdown/13-appriss-onboarding-base-de-conocimiento.md:636`: *"EU PROD se despliega el
  último miércoles del mes a las 6pm BST; y US PROD el último jueves del mes a las 9am BST."*
- `brain/markdown/21-kt-kristin-sign-off-procesos-rts.md:1285` y
  `brain/markdown/24-appriss-dev-workflow-code-change.md:93`: releases en semanas 2 y 4, Secure sale
  miércoles y jueves.

Usa el calendario en vivo, no la memoria. 9am BST son las 3am hora Colombia, así que un release de
US prod ya corrió cuando empieza tu jornada.

### Capa 4. La prueba funcional en el tenant

Esta es la única que prueba comportamiento, y es la que hay que diseñar caso por caso a partir de lo
que el fix cambió. Lee la descripción del PR en Azure DevOps, sección Solution, y deriva de ahí un
efecto observable.

No existe en la base ninguna pantalla, endpoint ni tabla que diga qué build corre un tenant. Control
Panel muestra la ficha del cliente con client ID, cluster de Greenplum y versión de ARDM. Versión de
ARDM, no build de la aplicación. Si algún día aparece esa vista, documéntala aquí.

Herramientas para la prueba funcional:

- **Control Panel**, `usprod.apprissretailcloud.com/control`, entorno USPROD, roles `SupportL2` y
  `Engineers`. Bajo Engineering: Config Items, Global Config, Feature Flags, Enumerations, Arp Files.
- **Firmar como el cliente** desde la tabla *Customers in USPROD*, columna *Click logo to sign in*.
  Esa es la vía de soporte, no `/<slug>/signin`.
- **Base del tenant**, solo SELECT: `sqldb-prd-wus2-arp-production-NNN-xxx-platform`, donde NNN es el
  Client ID y xxx el código corto.
- **Ops Overview** para el estado en vivo por cliente.

### Capa 5. Preguntar a quien lo liberó

El assignee del ticket ENG y el reporter. Un mensaje de Teams resuelve en minutos lo que las capas
anteriores dejan ambiguo. Cuando lo hagas, trae la respuesta aquí.

---

## El error que este procedimiento evita

Antes de mirar el ticket ENG correcto, di por hecho que un PR mergeado más una prueba de QA en
`demo7` no eran evidencia de producción. Era cierto para esos dos artefactos. La evidencia estaba en
otro campo, el fixVersion, y en la página de release notes. Conclusión que vale para cualquier caso:
un PR y un QA verde no prueban producción, y su ausencia tampoco prueba lo contrario. El fixVersion
liberado más la sección de la release notes sí.

Segundo error del mismo día: leí una bitácora que decía "falta pegar el comentario" y lo reporté como
pendiente sin cruzarlo con Jira, donde ya estaba publicado. **Jira es la fuente de verdad del estado.
La bitácora dice lo que Juan reportó, no lo que está.**

## Precedentes en el cerebro

- RCS-28123 ADUSA, asignación de casos: *"El fix llegó a producción el 17. Está en verificación, pero
  para verificarlo hay que aprobar un registro real en producción y eso necesita permiso de ADUSA."*
  `brain/markdown/26-adusa-estado-tickets-reuniones.md:1744`
- RCS-28124 ADUSA, adjuntos: *"Pasa a staging hoy, con dos despliegues porque el release branch trae
  cosas extra. No lo cierres hasta que salga el segundo."* Mismo archivo, línea 1748.
- Formulación segura hacia el cliente mientras se verifica: *"An update was deployed to production on
  the evening of 17 August and is being verified now. We will confirm on this ticket as soon as
  verification completes."* Mismo archivo, línea 1980.

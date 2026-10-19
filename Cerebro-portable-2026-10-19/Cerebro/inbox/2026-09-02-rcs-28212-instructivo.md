# RCS-28212 — Instructivo

Runbook ejecutable. No requiere leer el informe.
Cliente 7-Eleven, tenant `7eleven` en PROD, `7-eleven-prep` en Prep. Producto APIS, legacy.

Caso malo de referencia: `CA-44541-COR-2026-0001`
Segundo caso malo: `CA-44377-COR-2026-0001`
Caso bueno de referencia: `CA-43895-CORP-2026-0001`
Incidente origen del caso malo: `IN-44541-COR-2026-0001`
Reporte afectado: `Corp_Internal_Theft_Fraud`, ID 5165

Antes de empezar, dos advertencias.
No compartas pantalla en admin → Users → Edit. APIS muestra las contraseñas en texto plano ahí.
Contra producción solo SELECT. Ninguna escritura en base de datos la ejecutas tú.

---

## Paso 1. Entrar a APIS PROD del tenant de 7-Eleven

**Lectura.**

Dónde: navegador, portal APIS PROD.
Acción: entra con la cuenta de Julie Barber. Las credenciales están en tu nota segura, guardadas
tras el sign-off con Kristin del 2 jul 2026. Selecciona el tenant `7eleven`.

Qué se espera ver: la home de APIS con el tenant de 7-Eleven cargado. Confirma si la instancia está
en vista 270 o 275 antes de seguir. Las dos muestran la misma data con UI distinta y los menús no
están en el mismo lugar.

Si falla: si el primer login rebota, puede ser bloqueo de Cloudflare. Repórtalo a IT. Si la cuenta
de Julie Barber ya no entra, escríbele a Matthew Kamminga pidiendo aprovisionamiento de cuenta PROD
propia. Él es el application owner de APIS.

---

## Paso 2. Abrir el caso malo y capturar el estado exacto de los cuatro campos

**Lectura.**

Dónde: APIS, búsqueda de casos.
Acción: abre `CA-44541-COR-2026-0001`. Anota el valor exacto, con asterisco y espacios, de estos
cuatro campos:

    Case Type
    Case Sub Type
    Event Alpha Code
    Case Description

Qué se espera ver: `Case Type` en `* COR`, `Case Sub Type` en `* CORPORATE EMPLOYEE`,
`Event Alpha Code` vacío y en rojo, `Case Description` en `Horizon Investigation`. En el bloque
Additional Information debe aparecer `IN-44541-COR-2026-0001 (Elevated)`.

Si falla: si `Event Alpha Code` no está vacío, alguien ya lo editó. Registra la fecha del último
cambio antes de continuar, porque cambia el diagnóstico.

---

## Paso 3. Abrir el dropdown de Case Type y clasificar el valor COR

**Lectura.** Este paso decide la causa raíz. No lo saltes.

Dónde: APIS, mismo caso `CA-44541-COR-2026-0001`, campo Case Type.
Acción: despliega el dropdown sin seleccionar nada y responde tres preguntas.

    1. Aparece COR en la lista, si o no
    2. Aparece Corporate en la lista, si o no
    3. El valor * COR figura dentro de la lista o solo en la casilla cerrada

Qué se espera ver: `Corporate` presente y `COR` ausente de la lista. Ese resultado confirma la
hipótesis. El valor almacenado no pertenece a la lista de casos y la UI lo inyecta con asterisco.

Si falla: si `COR` sí aparece en la lista como valor activo, la hipótesis cae. En ese escenario el
problema es que el cliente tiene dos tipos coexistiendo y el reporte solo filtra uno. Eso es
configuración del tenant y se cierra con el cliente, no con ingeniería.

---

## Paso 4. Abrir el caso bueno y confirmar que no vino de una elevación

**Lectura.** Este es el control del experimento.

Dónde: APIS, búsqueda de casos.
Acción: abre `CA-43895-CORP-2026-0001`. Revisa los mismos cuatro campos del Paso 2, y mira el bloque
Additional Information.

Qué se espera ver: `Case Type` en `Corporate` sin asterisco, `Event Alpha Code` poblado, y el campo
`Related incident` vacío o sin la marca `(Elevated)`.

Si falla: si el caso bueno también trae `(Elevated)`, la elevación no es la variable que separa los
dos grupos. Detente y avísame antes de escribir nada en el ticket. Habría que buscar otra variable,
probablemente el usuario que elevó o la fecha del renombre del tipo.

---

## Paso 5. Abrir el incidente origen y ver qué valor tenía antes de elevarse

**Lectura.**

Dónde: APIS, búsqueda de incidentes.
Acción: abre `IN-44541-COR-2026-0001`. Anota el valor exacto de su campo de tipo y de subtipo, y el
nombre de la etiqueta que APIS le pone en pantalla.

Qué se espera ver: el incidente con `COR` como valor válido y sin asterisco. Ese contraste cierra el
argumento. El valor es legítimo del lado incidente e ilegítimo del lado caso.

Si falla: si el incidente también muestra asterisco, el valor huérfano nació antes de la elevación y
el problema está en la creación del incidente, no en el paso a caso.

Advertencia de nomenclatura. Kamminga dejó escrito en RCS-1508, el 15 dic 2021, que en 7-Eleven el
campo rotulado `Event Type` en pantalla es en realidad `event_sub_type` en los filtros. No asumas
que la etiqueta y la columna coinciden. Anota las dos.

---

## Paso 6. Contar cuántos casos están afectados

**Lectura.**

Dónde: APIS, Ad Hoc Query Builder.
Acción: construye un reporte nuevo, no toques el 5165. Campos seleccionados mínimos:

    case.Case ID
    case.Case Type
    case.Case Sub Type
    case.Issue Date
    case.Owner ID

Filtro único, sin más condiciones:

    Selected Column: case.event_type
    Comparison Operator: IN
    Operand: COR
    User Input Type: Fixed

Rango de fechas: todo 2026.

Qué se espera ver: el conteo de casos con el tipo huérfano. Ese número es lo que Kamminga necesita
para dimensionar la corrección de datos. Guarda la exportación.

Si falla: si el operador `IN` no acepta el valor escrito a mano en ese campo, usa el operador `=`
con `COR`. Si el dropdown de operando no ofrece `COR` porque no está en la lista activa, ese fallo
en sí mismo es evidencia adicional de que el valor es huérfano. Regístralo y sigue al Paso 7.

Sin spinner en la UI. Si no pasa nada al dar Preview, el reporte ya está corriendo. No vuelvas a
hacer clic.

---

## Paso 7. Probar el workaround sobre una copia del reporte 5165

**Lectura y escritura de configuración.** Autoriza: Juan Martínez, sobre una copia. No modifiques el
reporte 5165 original del cliente sin autorización de Matthew Kamminga.

Dónde: APIS, Ad Hoc Query Builder.
Acción: duplica el reporte `Corp_Internal_Theft_Fraud`. Nómbralo:

    Corp_Internal_Theft_Fraud_TEST_RCS28212

En la copia, cambia la primera línea de filtro. De esto:

    case.event_type  =  Corporate  (Fixed)

A esto:

    case.event_type  IN  Corporate,COR  (Fixed)

El pie de la pantalla lo permite: "Use comma delimiter with IN". Deja las demás líneas de filtro
idénticas al original.

Qué se espera ver: `CA-44541-COR-2026-0001` y `CA-44377-COR-2026-0001` aparecen en el resultado,
junto con los casos que ya salían antes. Ese es el workaround entregable al cliente.

Si falla: si al cambiar el operador a `IN` el operando se vuelve una lista múltiple sin `COR`
disponible, prueba el operador `LIKE` con `COR%`. Si tampoco, el workaround de reporte no existe y
la única salida es la corrección de datos del Paso 8. Anótalo y pasa.

---

## Paso 8. Entregarle el diagnóstico cerrado a Matthew Kamminga

**Escritura en Jira.** Autoriza: Juan Martínez. El texto lo pegas tú, no lo escribe Claude.

Dónde: RCS-28212, comentario **interno**, no visible al cliente.
Acción: pega el bloque de abajo después de rellenar los cinco huecos marcados con `<>` con lo que
salga de los pasos 3, 4, 5, 6 y 7.

```
Internal note. Support-side investigation completed. Handing the diagnosis over, the data
correction is yours to decide.

Finding. Cases created by elevating an incident carry the incident type code into the case
Case Type field instead of the case-side value. CA-44541-COR-2026-0001 stores COR. The case
dropdown renders it as * COR because COR is <PASO 3: not present / present> in the active case
type list for tenant 7eleven. Case Sub Type shows the same symptom, * CORPORATE EMPLOYEE. The
required field Event Alpha Code is empty on the elevated case.

Control. CA-43895-CORP-2026-0001 stores Corporate, has Event Alpha Code populated, and
<PASO 4: has no Related incident marked Elevated / other>. The elevation path is the variable
that separates the two groups.

Source incident. IN-44541-COR-2026-0001 stores <PASO 5: valor exacto> with no orphan marker on
the incident side. The value is valid in the incident list and invalid in the case list.

Customer impact. AdHoc report Corp_Internal_Theft_Fraud, ID 5165, filters case.event_type with
operator = against the literal Corporate. Every elevated case is excluded by that filter.

Scope. <PASO 6: N> cases in tenant 7eleven carry event_type COR for calendar year 2026. Export
attached.

Workaround tested. A copy of report 5165 with the first filter changed to
case.event_type IN Corporate,COR returns <PASO 7: both cases / result>. This unblocks the
customer reporting without any data change. I have not touched the customer report 5165.

Two decisions are yours. First, whether to correct event_type and event_sub_type on the affected
cases. The case ID string is frozen at creation and will keep COR either way. Second, whether the
elevation mapping affects other APIS tenants that elevate incidents to cases.

Note on timing. 7-Eleven is scheduled to migrate to Incident around September or October 2026.

Happy to run any SELECT you want against the tenant, or to walk the customer through the report
workaround once you confirm.
```

Qué se espera ver: Kamminga responde con la decisión sobre la corrección de datos.

Si falla: si Kamminga no responde en tres días hábiles, escala a Aimee Wadsworth. Viraj ya la puso
en copia en el hilo el 18 de agosto.

---

## Paso 9. Transición del ticket

**Escritura en Jira.** Autoriza: Matthew Kamminga o Aimee Wadsworth. **Tú no la ejecutas todavía.**

Estado actual: `Under Engineering Review`, assignee Matthew Kamminga.
Transición sugerida: ninguna por ahora. El ticket se queda donde está mientras Engineering decide la
corrección de datos.

Cuándo mover a `Under Support Review`: cuando Kamminga confirme que no habrá cambio de código y
autorice entregar el workaround. Ahí el ticket vuelve a soporte y tú tomas el assignee.

No le comentes al cliente sobre el fondo del defecto mientras el ticket siga en
`Under Engineering Review` con assignee de Engineering. Ese es el error de RCS-28161.

---

## Paso 10. Comentario al cliente, solo cuando el Paso 9 lo habilite

**Escritura en Jira.** Autoriza: Juan Martínez, después de la confirmación de Kamminga.

Dónde: RCS-28212, comentario público al reporter Vinh Luong.
Acción: pega este bloque. Sin hallazgos de investigación, sin fechas futuras, sin causa raíz.

```
Hello Vinh,

Thank you for the detail and the screenshots, they made this straightforward to reproduce.

Confirmed. Cases that were elevated from an incident store a different Case Type value than cases
created directly, and report 5165 filters Case Type with an exact match, so the elevated cases fall
outside the result set.

There is a reporting change on your side that brings them back in. In the Ad Hoc Query Builder, open
Corp_Internal_Theft_Fraud, and on the first filter line change the Comparison Operator from = to IN,
then set the Operand to include both values, comma delimited. The builder accepts comma delimited
values with the IN operator.

We suggest testing this on a copy of the report first, then applying it to 5165 once you are happy
with the result.

The underlying difference in how the Case Type value is stored on elevated cases is with our
engineering team. We will come back to you on that separately.

Please let us know how the report behaves after the change.

Kind regards,
Juan Martinez
Appriss Retail Support
```

Qué se espera ver: Vinh confirma que el reporte ya trae los casos elevados.

Si falla: si el cliente responde que el operador `IN` no le funciona en su vista, confirma primero
en qué versión está su instancia, 270 o 275. La ubicación del control cambia entre las dos.

---

## Paso 11. Cerrar en Cerebro

**Escritura local.** Autoriza: Juan Martínez.

Dónde: terminal, raíz de la carpeta Cerebro.

```
bin/anotar RCS-28212 "Investigacion APIS case type en casos elevados. Confirmado filtro exacto en reporte 5165 y valor huerfano COR en el caso. Diagnostico entregado a Kamminga, workaround IN probado."
```

Si el hallazgo se confirma en los pasos 3 a 7, guárdalo en la base como conocimiento reutilizable:

```
bin/guardar --carpetas
cat inbox/2026-09-02-rcs-28212-informe.md | bin/guardar 16 "APIS elevacion incidente a caso rompe el case type y saca los casos de los reportes AdHoc con filtro exacto"
python3 bin/indexar_tickets.py
```

Carpeta 16 es RCS Soluciones.

---

## Paso 12. Documentar en Confluence lo que hoy no existe

**Escritura en Confluence.** Autoriza: Juan Martínez, con Kristin Krogman como reviewer si todavía
está.

El espacio AALPS tiene dos páginas con APIS en el título. La página índice 273453096 apunta al
manual de administración alojado en el OneDrive personal de una cuenta desactivada. No hay ninguna
página que documente los case types de APIS ni el comportamiento de la elevación.

Esta investigación es la primera pieza escrita de la APIS Survival Guide que quedó acordada en el
sign-off con Kristin. Súbela como subpágina de AALPS cuando el diagnóstico esté cerrado.

Título sugerido:

```
APIS: case types, incident to case elevation, and AdHoc report filtering
```

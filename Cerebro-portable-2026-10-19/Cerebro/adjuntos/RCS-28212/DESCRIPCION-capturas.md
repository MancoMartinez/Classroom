# RCS-28212 — descripción de las capturas

Las dos imágenes las subió Vinh Luong a Jira el 2026-08-06. Juan las pegó al chat el 2026-09-02.
Los PNG originales todavía no están en esta carpeta. Arrástralos aquí con estos nombres:

    image-20260806-133803.png
    image-20260806-134110.png

El texto de abajo es lo que queda buscable en Cerebro. La imagen no.

---

## image-20260806-133803.png — Ad Hoc Query Builder, configuración del reporte

Pantalla: "Ad Hoc Query Builder: Configure filters". Enlaces arriba a la derecha:
Report designer, Enable Translate. Botones de paso: Finish, Previous, Next Step.

Enter Report Title: `Corp_Internal_Theft_Fraud`

Available Fields visibles: case.Owner ID, case.Initiated By, case.Issue Date,
hierarchy_location.Store #, hierarchy_level.Market, case.Status, case.Case ID,
case.Case Description, case.SEI $ Amount, case.Total Value US, additional_info. [IN],
additional_info.48A's [CA]

Selected Fields: case.Case Type, case.Case Sub Type, case.Status, case.Issue Date,
hierarchy_level.Market, case.Owner ID, case.Initiated By

Tabla de filtros, columnas Logical Operator, Selected Column, Report.default label,
Report.name of filter, Comparison Operator, Operand, User Input Type:

| Lógico | Columna | Etiqueta | Nombre del filtro | Operador | Operando | Input |
|---|---|---|---|---|---|---|
| AND | case.event_type | Case Type | case.event_type | = | Corporate | Fixed |
| AND | case.event_sub_type | Case Sub Type | case.event_sub_type | IN | lista: CDC Chargebacks, Critical Incident, Expense Fraud AP, Fraud | Fixed |
| AND | case.status | Status [?] | case.status | IN | lista: Closed, New, Pending, To Market | Allow User Input |
| AND | case.issue_date | Issue Date | case.issue_date | BETWEEN | vacío, con selector Fiscal period | Allow User Input |
| AND | hierarchy_level.level2 | Market | hierarchy_level.level2 | = | vacío | Allow User Input |
| AND | case.iice_owner_id | Owner ID | case.iice_owner_id | = | vacío | Allow User Input |
| AND | case.agent_id | Initiated By | case.agent_id | = | vacío | Allow User Input |

Nota al pie de la pantalla: "Use comma delimiter with IN . Use mm/dd/yyyy for a date column."
Botones: Add Self-Defined Fields, Update Fields, Add documentation, Preview.

Resaltado en amarillo por el cliente: el nombre del filtro `case.event_type` y el operando
`Corporate`. Es lo que el cliente señala como el punto del problema.

**Dato clave.** El operador es `=` contra el literal `Corporate`, con User Input Type en Fixed. Un
caso con `event_type` igual a `COR` queda fuera del resultado por construcción del filtro.

**Segundo dato clave.** El campo `case.event_sub_type` de la fila siguiente sí usa el operador `IN`.
El constructor soporta `IN` en estos campos, y el pie confirma la sintaxis con coma.

---

## image-20260806-134110.png — ficha del caso CA-44541-COR-2026-0001

Aviso en rojo arriba: "All Fields in Red are Required Fields and Must be completed prior to
submitting for Approval."

Columna izquierda:

    Case ID:            CA-44541-COR-2026-0001
    Location:           44541 - 20011 Eureka Road
    Zone:               772299
    Market:             702264
    Alpha Code:         vacío
    Address:            vacío
    City:               Taylor
    State:              MI
    ZIP:                48180
    570 Balance:        vacío
    Corp GP %:          vacío
    Fran GP %:          vacío
    VIP %:              vacío

Bloque Additional location info: Employee directory (Click to View), NEARBY LOCATIONS
(Click to View).

Bloque AP Employee Information:

    Owner ID:           JCOOLBAUGH1
    Initiated By:       Jarred Coolbaugh
    Supervisor:         vacío
    Date of Incident:   1/14/2026

Columna derecha, dropdowns:

    * Case Type:        * COR                      <- resaltado en amarillo por el cliente
    * Event Alpha Code: vacío, etiqueta en ROJO    <- campo requerido sin poblar
    * Case Sub Type:    * CORPORATE EMPLOYEE
    * Case Description: Horizon Investigation
    Case Source:        vacío
    Takeback Status:    vacío
    BSC Secure Case:    vacío
    Is this a FIW case?         Yes / No, ninguno marcado
    * Is this a Barometer Case? [?]   No marcado
    Franchisee mediation requested or lawsuit filed?   ninguno marcado
    Is this an LON/Breach Case?       vacío

Bloque Additional Information:

    Related case:          Create | Attach
    Related investigation: Create | Attach
    Related incident:      Create | Attach
                           IN-44541-COR-2026-0001 (Elevated)  [X] +

Bloque Event Value ($1,930.32 - 1 Items), columnas Reason for the Adjustment/Correction, Cause of
Loss, PSA Category [?], Date [?], Description, Qty, Unit Retail Price/Adjustment/Correction Amounts,
Total Price/Adjustment, Disposition, Save/Discard:

    Reason: CASH THEFT | Qty: 1 | Unit: 1,930.32 | Total: 1,930.32

---

## Los cuatro datos que sostienen el diagnóstico

1. El asterisco aparece en **dos** campos, `* COR` y `* CORPORATE EMPLOYEE`. Un usuario no escribe
   el asterisco. La aplicación lo pinta cuando el valor almacenado no existe en la lista activa del
   dropdown. Dos campos a la vez descarta el error de digitación.

2. `Event Alpha Code` es requerido y está vacío. La elevación creó el caso sin completar el juego de
   campos de tipificación.

3. `Related incident: IN-44541-COR-2026-0001 (Elevated)`. El caso nació de una elevación y el
   incidente origen ya traía `COR` en su número. El caso heredó el código del incidente.

4. El número de caso congela el código. `CA-44541-COR-...` contra el caso correcto
   `CA-43895-CORP-...`. Corregir el dropdown después no reescribe el número del caso.

## Lo que las capturas no muestran

No muestran si `COR` existe o no dentro de la lista desplegable de Case Type del tenant. El dropdown
sale cerrado. Ese es el paso 3 del instructivo y es el que convierte la hipótesis en causa raíz.

No muestran la ficha del caso correcto `CA-43895-CORP-2026-0001`, así que no se puede confirmar por
imagen que los casos buenos carezcan de la marca `(Elevated)`. Ese es el paso 4.

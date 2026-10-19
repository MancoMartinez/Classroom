# RCS-28327 · Cerrar la validación pendiente de Edwin

Fecha: 2026-08-24
Ticket: https://trebuco.atlassian.net/browse/RCS-28327
Estado en Jira al momento de escribir: Work in progress, Medium, asignado a Juan Martinez, reporta Becky LaPierre, creado 12 ago, última actividad 20 ago (nota interna de Edwin Garzon).

Juan ejecuta. Claude redacta. Nada se escribe en Jira desde acá.

---

## 1. Qué está verificado y qué no

**Verificado por Edwin (nota interna del 20 ago, comentario 3301391):**

- La investigación previa se corrió contra el esquema equivocado. `ARDM_112` es Giant Food / Stop & Shop. La store 2667 y la TID 2608025570789970641 nunca existieron ahí. Cita textual: *"The earlier investigation was run against the wrong client schema (ARDM_112 = Giant Food / Stop & Shop, a different Ahold Delhaize banner)"*.
- Cliente correcto: `c046dhz` = `ARDMPROD.ARDM_046`, banner "FOOD LION".
- En `ARDMPROD.ARDM_046.ARDM_ITEMDISCOUNT` para la TID 2608025570789970641 la fila de descuento tiene `CODE = 'loyalty discount'`, `TYPE = 'other'`, `REASON = null`. Lo setea el parser a propósito en `pyardm/us/c046dhz/ardm/python/pd_pos_parser.py:777,842` cuando detecta un evento POS `AdvancedFrequentShopper` o `FrequentShopper`.
- Conclusión de Edwin sobre el pipeline: *"this is not a mapping/pipeline bug"*.
- Cliente 46 corre ARDM V3, esquema itemdiscount de texto: type, code, classification, reason, method.
- La definición `itemdiscount.searchable` resuelve el texto mostrado del campo de tipo de descuento vía:
  `Platform.GetExcelReferenceData(type, "/system/ebr/crdm/store/2_0/enumerations/crdm pos enumerations.xlsx", "ItemDiscountType")`
- Consultando esa VirtualFilePath exacta en `secure.Repo` del Platform DB del cliente 46: 0 filas.

**No verificado, y es lo que bloquea todo lo demás.** Palabras de Edwin: *"haven't yet 100% confirm[ed] [that] type is literally what renders as the 'Item Discount Description' column the customer sees (vs. a differently named field)"*.

**No verificado y Edwin no lo menciona:** si la falta del workbook es un hueco de contenido (falta subir el archivo) o si la definición `itemdiscount.searchable` quedó apuntando a una ruta muerta tras la migración a V3. Son dos causas distintas con dos dueños distintos. Ver paso D.

---

## 2. Paso A. Composer, confirmar a qué campo está atada la columna

Objetivo: probar que la columna en blanco que ve Becky está atada al campo `type` y no a `code`, `classification`, `reason` o `method`.

Esto importa porque `CODE` sí trae `'loyalty discount'`. Si la columna estuviera atada a `code`, la teoría del workbook faltante no explica nada y el problema es otro.

1. Entrá al Secure 5.4 de Delhaize con el mismo perfil desde el que Becky sacó la captura.
2. Abrí la búsqueda guardada o la vista de recibo donde aparece la columna "Item Discount Description" en blanco. Pedile a Becky el nombre exacto de la búsqueda si no la ubicás, es un dato que no cuesta y evita comparar vistas distintas.
3. Abrí esa misma búsqueda en Composer.
4. Inspeccioná la columna y anotá el field ID al que está bindeada, literal.
5. Anotá también el resto de campos de itemdiscount disponibles en esa definición y cuál de ellos sí está poblado en pantalla.

**Qué significa cada resultado:**

| Field ID de la columna | Lectura |
|---|---|
| Es el campo de tipo, el que llama a `GetExcelReferenceData(type, ...)` | La teoría de Edwin se sostiene. Seguí al paso B. |
| Es `code` u otro campo de texto directo | La teoría de Edwin no aplica. El valor está en la base y no se muestra igual, hay que investigar de cero. Frená y avisá. |
| Es un campo compuesto o calculado | Hay que abrir su definición antes de concluir nada. |

---

## 3. Paso B. Reproducir el 0 filas vos mismo

Antes de correr esto, resolvé una ambigüedad que hay en el material: la ficha de ADUSA en el cerebro dice **Client ID 441**, base `sqldb-prd-wus2-arp-production-441-adusa-platform`. Edwin habla del **"client 46's Platform DB"**. 46 es el ID del cliente ARDM de Delhaize, 441 es el tenant ADUSA. No asumas cuál es. Confirmá contra el Excel de client IDs cuál es el Platform DB que sirve la instancia 5.4 de Delhaize antes de consultar.

Con el Platform DB correcto identificado, solo SELECT:

```sql
SELECT *
FROM secure.Repo
WHERE VirtualFilePath = '/system/ebr/crdm/store/2_0/enumerations/crdm pos enumerations.xlsx';
```

Y en paralelo, un barrido más ancho para ver si el archivo está en otra ruta:

```sql
SELECT VirtualFilePath
FROM secure.Repo
WHERE VirtualFilePath LIKE '%enumeration%'
   OR VirtualFilePath LIKE '%.xlsx';
```

**Qué significa cada resultado:**

- 0 filas en la primera y el archivo no aparece en la segunda: el workbook no está para este cliente. Confirma a Edwin.
- 0 filas en la primera pero el archivo aparece en otra ruta en la segunda: no falta el archivo, falta que la definición apunte a la ruta correcta. Eso es un defecto de contenido, no un hueco de delivery. Cambia el ruteo.
- Devuelve filas: la teoría cae. La lookup no falla por ausencia y hay que mirar el contenido de la hoja `ItemDiscountType`.

---

## 4. Paso C. Probar que en otro cliente sí existe

Este paso es el que convierte "creo que falta" en "falta, y acá está la prueba". Sin esto, rutear a Delivery es una hipótesis.

Corré la primera consulta del paso B, misma VirtualFilePath, contra el Platform DB de otro cliente legacy que muestre bien la descripción de descuento.

- Si en el otro cliente devuelve filas y en el 46 no, el hueco está probado y es específico del cliente 46.
- Si en ningún cliente devuelve filas, la ruta de la definición está mal en todos lados y esto es sistémico, no un problema de ADUSA.

Anotá qué cliente usaste de comparación. Va en el comentario interno.

---

## 5. Paso D. Separar hueco de contenido de definición muerta

Cliente 46 corre ARDM V3. La ruta que llama la definición es `crdm/store/2_0`, o sea CRDM 2.0, el predecesor del ARDM. El cerebro tiene una advertencia sobre esto: *"El CRDM (Common Retail Data Model) es el predecesor del ARDM... Aparece en páginas viejas de Confluence y en código de la versión 5.x. No extiendas nada que sea CRDM."*

En Secure moderno las enumeraciones viven en `EnumerationReferenceData`, no en un xlsx del repo. Chequeá si el tipo de descuento ya existe ahí:

```sql
SELECT DISTINCT EnumerationType, [Key], Value
FROM [<CID>_Platform].[secure].[EnumerationReferenceData]
WHERE EnumerationType LIKE '%Discount%';
```

También podés mirarlo por UI en Control Panel USPROD, sección Engineering, Enumerations. Ya tenés el rol Engineers.

**Por qué importa y a quién le toca según el resultado:**

- La enumeración de tipo de descuento **existe** en `EnumerationReferenceData` pero la definición sigue llamando al xlsx CRDM: la definición quedó atrás en la migración V2 a V3. Es un defecto de contenido de la plataforma, y probablemente afecta a todos los clientes migrados. Esto va a Engineering, no a Delivery.
- La enumeración **no existe** en ninguno de los dos lados: es un hueco de setup del cliente. Eso es Delivery. La regla de Kristin Krogman es literal: *"Anything having to do with the initial setup and configuration of the product... anything having to do with the data mapping... That's going to be delivery. Whereas anything that is more of a bug is something that's more broken. If you're more broken, that's going to be engineering."*

No decidas el ruteo antes de tener este resultado. Si lo mandás a Delivery y era defecto de plataforma, Peyman lo devuelve y perdés otra semana en una cuenta que está en escalación ejecutiva.

---

## 6. Contexto que conviene tener a mano

**RCS-28172, el que había que leer primero.** Resultó ser otra cosa: el trickle feed de 5.4 de Delhaize parado el 4 y 5 de agosto. Edwin re-ejecutó el proceso el 6 de agosto, Becky validó el mismo día, cerrado como Support Resolved - Fixed Configuration. Lo que aporta es el patrón de reporte de Becky: siempre compara la instancia legacy 3.5 contra la 5.4 y reporta la diferencia. Acá hizo exactamente lo mismo, *"This same transaction in the legacy version pre-upgrade (3.5) shows this was a loyalty discount on the receipt"*. También aporta que Edwin es quien viene trabajando el pipeline de Delhaize 5.4.

**RCS-27761, precedente casi idéntico.** Mismo cliente 46, misma reportante. Becky no veía el Tender Check Amount de Payroll Check. Nikita Rathore encontró que había dos media numbers para el mismo tender y que el 4 no estaba incluido porque originalmente refería a Food Stamps en papel. Cita: *"The Four was not included... That's why it was not mapping."* Se resolvió con PR de código incluyendo el MediaNo 4. Es la misma familia de síntoma, valor de enumeración ausente y campo en blanco en pantalla, y se resolvió por Engineering, no por Delivery. Tenelo a mano si Peyman rebota el ticket.

**Alcance real del síntoma.** Edwin dice que no es exclusivo de loyalty ni de una tienda, *"it affects every item discount"*. Si el paso B lo confirma, decidí si le decís a Becky que el alcance es más ancho de lo que ella reportó. Eso amplía el ticket y en una cuenta en escalación puede ser mejor decirlo vos antes de que lo descubran ellos.

**Si el ruteo termina siendo Delivery:** Secure 5 en Under Delivery Review va por Peyman primero, y hay que avisarle por Teams además de asignar. Client ID va en el comentario interno, siempre.

---

## 7. Lo que queda pendiente de decisión

**El comentario al cliente no depende de nada de lo anterior.** Becky lleva 12 días sin respuesta y el último comentario tuyo es el acuse del 12 de agosto donde prometiste un update. Un comentario de estado no afirma causa raíz y no hay que retirarlo después. Decime y lo redacto.

**El comentario interno y el ruteo sí dependen** de los pasos A a D. No los redacto hasta que tengas esos resultados.

**Compromiso de la cuenta:** avisar por correo a Leigh Ann Stubbs y a Tom Blackburn cada vez que algo se libere, no solo en el ticket. Pedido explícito del 14 de agosto porque Leigh Ann no vive en la aplicación. Aplica cuando esto se resuelva, no ahora.

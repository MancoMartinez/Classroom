# Cosecha 4 sep 2026 — RCS-28753 Nike, precedente de campo de descuento manual

Sesión fuente: "RCS-28753 ticket" (local_499e196c), transcripción del 3 sep 2026.

## Hallazgo verificado

Precedente clave: RCS-21540, mismo cliente Nike, cerrado el año pasado. Peyman Motlagh de Ingeniería definió ocho campos de descuento con su columna fuente en ese ticket. El más cercano a "Manual Discount Amount" es "Total Discount Modify Amount", descrito por Peyman como "the monetary value of the sum of all manual overrides... the price was manually entered by the cashier".

Función PostgreSQL real que calcula esa familia de montos durante la ingesta: `SalePriceModifyAmount` y `SalePriceOverrideAmount`, filtradas por `manual_price_flag = 1`. Es la única fórmula concreta de un campo de descuento manual encontrada en la búsqueda completa.

Ruta de respaldo si Peyman confirma que es un campo distinto: `GetTransactionJson.sql`, override de Nike, cliente 67.

## Estado al cierre de la sesión

Comentario interno quedó pegado en RCS-28753 dirigido a Peyman Motlagh, preguntando si Manual Discount Amount es el mismo campo que él ya definió con otro nombre, con link a RCS-21540. Sin fecha de respuesta.

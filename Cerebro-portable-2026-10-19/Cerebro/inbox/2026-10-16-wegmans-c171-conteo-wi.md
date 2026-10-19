# Wegmans C171_WEG, conteo de work items sep y oct 2026

## Qué pasa
Dan Endersby pidió el conteo de work items de C171_WEG de septiembre y octubre, la comparación y las anomalías. Le preocupa el pico de duplicados. Cifras cerradas el 16 oct con SELECT contra la base Platform de Wegmans. La tabla de Shireesh Ramdas coincide con la base en sus 23 días.

## Evidencia
1. Septiembre, 30 días: 129 resultados, 57 generados, 72 duplicados, 0 fallos, 0 skipped. Duplicados 56%. Mensuales: 2 runs en ago y 2 en sep, 0 fallos. Sep generó 1 work item y 0 duplicados. No existe run mensual de octubre al 16 oct.
2. Octubre 1 a 15: 76 resultados, 35 generados, 41 duplicados, 0 fallos. Duplicados 54%.
3. Por día, sep contra oct: resultados 4.3 y 5.1, generados 1.9 y 2.3, duplicados 2.4 y 2.7. La tasa de duplicados no sube entre meses.
4. Dos bolsillos. 13 a 20 sep: 4.5 resultados por día, duplicados 75%, generados 1.1 por día. 11 a 15 oct: 9.0 resultados por día contra 3.1 del 1 al 10, 28 duplicados en 5 días, máximo de 9 el 15 oct.
5. gift cards purchased with lower trans amount.fti aporta 96 de los 113 duplicados, 85%. De sus 112 resultados, 96 son duplicados. Le siguen 8020 coupons with trans less than 5 by cc con 9 de 10 y coupons cashed overnight gt 3 dollars con 8 de 9. Las otras 8 definiciones tienen 0 duplicados.

## Causa
Confirmada en el SQL de la definición. DefinitionNativeCommand del run del 15 oct filtra TradingDay del 6 al 15 oct, 10 días hacia atrás. Cada run vuelve a evaluar esos 10 días y devuelve como duplicado todo ticket que ya generó work item, hasta que sale de la ventana. El 15 oct esta definición dio 9 resultados, 1 generado y 8 duplicados: 5 son los work items creados el 14 oct y 3 son anteriores. El noveno duplicado del día es 8020 coupons with trans less than 5 by cc, 1 por día. La subida refleja una ráfaga de 5 work items nuevos el 14 oct, sin defecto. Septiembre 13 a 20 no se verificó con este método.

## Qué hago hoy
Envía el mensaje de Teams v2, inbox/2026-10-16-wegmans-c171-teams-dan-v2.md. El v1 queda obsoleto.

## Precedentes
workview.IsDuplicateWorkItem, en la documentación de generación de work items en Cerebro. bitacora/RCS-28671.md línea 50 para la mecánica de wisc2. Es otro cliente.

## Compromisos
Juan responde a Shireesh y Dan con estas cifras. Sin fecha.

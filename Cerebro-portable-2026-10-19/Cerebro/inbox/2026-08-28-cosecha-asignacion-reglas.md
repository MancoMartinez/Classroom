# Cosecha asignacion-reglas — 2026-08-28
Fuente: sesión local_659260da-3f2b-4ed2-9e99-7ad7ddd931ce

## Hallazgos verificados

La skill de asignación ordenaba por fecha de creación y no por vencimiento de SLA. La consulta no traía el campo Target Assignment Time. Ese error hizo aparecer RCS-28571 como el más viejo en lugar del más vencido.

Medición del techo de tickets por persona:

| Palanca | Cupo del día | Abiertos del equipo |
|---|---|---|
| Techo 16, sin cambio | 8 | 46 |
| Techo 18 | 12 | 46 |
| Techo 20 | 13 | 46 |
| Cerrar los 17 en Under Customer Review | 13 | 29 |

Subir a 20 y hacer el barrido dan el mismo cupo del día, 13, porque el incremento diario topa en 3 y 2 por persona. El techo reparte los 46. El barrido los baja a 29.

Tasa de aplicación de las propuestas: 11 de 20, 55%. Los cuatro desviados son exactamente los cuatro huérfanos de David. Ninguna de las once propuestas de la cola normal se movió de sitio.

Luis Hernandez lleva 1 ticket abierto de 5 posibles. Se le propusieron dos el 25 de agosto con cita textual de precedente y no se aplicó ninguno. Su perfil en el clasificador dice React y .NET, y la cola no trae frontend puro. Son 4 slots vacíos hace tres días.

Sebastián Garcés tiene 3 abiertos de 5 y los tres están en Under Customer Review. Tiene cero trabajo activo.

Los seis huérfanos de David quedaron colocados y David tiene 0 abiertos. Dos terminaron con Juan, RCS-28099 y RCS-28223.

RCS-28595 Stater Bros no estaba en la cola sin asignar. Está con Ryan Barlow en Under Delivery Review. La lista que mandó Aimee traía cinco tickets y solo cuatro eran válidos.

De los 17 sin asignar al final del día, 16 son Medium y 1 es Low. No hay High ni Critical. El criterio que queda es antigüedad.

No existe procedimiento escrito para correr la carga de archivos de empleados. Se buscó tres veces en la base y no está.

Advertencia registrada para las cargas de archivo, del RCS-28085 de Ollie's: el IT del cliente confirmó que el archivo traía el rol correcto y el sistema igual resolvió mal el rol. No prometer al cliente que la carga arregla el síntoma.

Decisión en mesa, item 241: devolver los archivos de empleados incompletos al cliente para que los corrija. Los errores en la data de empleados producen discrepancias en reportes.

## Decisiones y compromisos

Juan ejecutó cuatro asignaciones: RCS-28593 DSG y RCS-28599 Lululemon y RCS-28606 Williams Sonoma para Diego, RCS-28590 Floor & Decor para Rueda.

Recomendación fijada: subir el techo a 18, no a 20. Da 12 slots, destraba a Edwin y a Rueda, y no quita el argumento del barrido de Under Customer Review.

Corregir la skill de asignación para que traiga Target Assignment Time y ordene por vencimiento de SLA.

Regla de alcance aclarada: un cliente un dueño aplica cuando coinciden cliente y subsistema. TG Jones con Edwin en RCS-28274 no bloquea RCS-28627 para Luis, porque RCS-28274 es mapeo de Original Transaction Amount a nivel de header.

Candidatos para Luis con precedente verificado: RCS-28611 Appriss Internal, gráfico tipo Gauge, apoyado en que el Chart Wizard documenta Area, Bar, Bubble, Column, Line, Pie y Scatter sin incluir Gauge. Y RCS-28627 TG Jones, con procedimiento de diagnóstico en la guía de Kristine sección 13.1.

Candidatos para Garcés: RCS-28621 APP y RCS-28634 DHL, los dos imports de empleados. Lo dejan en 5 de 5. El costo es una sesión de veinte minutos de Edwin o de Rueda para correr el primero con él mirando. La salida es tres tickets y un procedimiento que hoy no existe en la base.

Tickets descartados con motivo: RCS-28626 ASDA SAML tiene precedente en contra, el análisis de RCS-28442 Torrid desmonta la premisa del certificado. RCS-28624 Lux CAMS upload choca con Edwin en RCS-28574. RCS-28629 Big 5 no tiene precedente ni alcance claro. RCS-28625 Shell ya está en Under Engineering Review.

Las tres transcripciones cosechadas quedaron en inbox. No se corrió `bin/guardar`, espera aprobación de Juan.

## Pendiente de verificar

RCS-28606 Williams Sonoma volvió a la cola sin asignar, ahora en Under Delivery Review, después de que Juan lo asignara a Diego. Revisar quién lo movió a Delivery y le quitó el dueño.

RCS-28571 Winn-Dixie venció hace 27 horas y su dueño natural, Rueda, está en 16 de 16. Sigue sin colocar mientras el techo no suba.

Los 3 tickets de Garcés en Under Customer Review son su desbloqueo real. Perseguirlos libera techo sin subirle carga.

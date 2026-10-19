# RCS-28223, lo que el PDF de Hugo resuelve

Fecha: 2026-08-27. Fuente: `adjuntos/RCS-28223/McDonald's Manager and Crew Cash Audit.pdf`,
subido por Hugo Cortez el 13 ago 2026. Dos capturas con la URL visible.

## Datos duros que nadie habia extraido

    Client ID          402
    Tenant slug        mcdonalds
    Base de la ruta    /mcdonalds/nettrack/Audit/screens/incident/402/audit/screens/
    Manager Week 1     AuditSection_V24_S4.aspx
    Crew Week 1        AuditSection_V24_S9.aspx
    Audit Name         Restaurant Cash Audit
    Audit Number       959-30133
    Store              959 CULVER CITY, CA
    Audit Date         2026-08-06 11:55 AM
    Status             In Progress
    Owner              Hugo Cortez

El Client ID 402 no estaba en el cerebro. Anotarlo en `reference_acceso_sql_tenants.md`.

## Respuesta a la primera pregunta de Kamminga

Si. Todas las preguntas rotas renderizan una grilla. Las dos secciones muestran la misma tabla de
nueve columnas, dos filas: Employee Name, Coaching, 1st Verbal, 2nd Verbal, 1st Written,
2nd Written, First and Final, Termination, Comments. FieldType 35 es esa grilla.

## Tres cosas que David no vio

1. Le dio a Matt una sola pantalla. El defecto vive en dos. Manager es S4, Crew es S9. Matt
   reproduciendo solo en S4 cubre la mitad del reporte.

2. En la captura las celdas de la grilla aparecen vacias y sin control de entrada visible. La tabla
   se pinta con encabezados y bordes de fila. Eso apunta al render del control, no al guardado.
   David le pidio a Engineering revisar "the save/validation logic". La evidencia visual apunta al
   otro lado. Es observacion sobre una captura, no prueba. Un textbox sin borde se ve igual que una
   celda vacia. Confirmarlo en Test con el inspector antes de afirmarlo.

3. La grilla no tiene columna de monto. Las dos preguntas piden "dollar amount" en el enunciado.
   Las nueve columnas van de Employee Name a Comments sin ninguna de dinero. Puede ser una grilla
   generica reusada. Vale preguntarlo, no bloquea el defecto principal.

## Diferencia estructural entre las dos secciones

Manager Q2 junta el disparador y la grilla en una sola pregunta, y trae control Response con valor
Yes y marca "(0 of 0 pts) (Failed)".

Crew separa las dos cosas. Q1 es el disparador con su Response. Q2 es solo "If so, identify the top
two (2) crew members, dollar amount, and what action was taken." y no trae control Response ni
puntaje, solo la grilla.

O sea la numeracion de Hugo no mapea igual en las dos auditorias. El mapeo de David, Manager Q2 a
Q57, Q4 a Q60, Q6 a Q61, no se puede extrapolar a Crew. Hay que sacarlo del SELECT.

## Estado del cliente

Hugo escribio dentro del campo Comments de la auditoria, no en el ticket:
"TEST. For questions #2, #4 & #6, managers were able to input their results in the comments section
and add names." y "The same goes for questions #2, #4, #5, #7 & #8".

Confirma el workaround que David le ofrecio el 24 ago. Confirma tambien que Hugo estaba probando
sobre la auditoria real 959-30133 de la tienda de Culver City, en estado In Progress.

## Lo que sigue

El SELECT de `inbox/2026-08-27-rcs-28223-plan-repro.sql` ya se puede correr con Client ID 402.
Sirve para numerar las preguntas de Crew y confirmar su FieldType.

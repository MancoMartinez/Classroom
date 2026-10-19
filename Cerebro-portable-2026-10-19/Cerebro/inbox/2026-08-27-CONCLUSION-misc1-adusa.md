# RCS-28093. MISC1 resuelto: es la columna 20 del feed de empleados

Fecha: 27 ago 2026
Fuente: `F:\Clients\Delhaize\RefLoader_Prod\fmt\employee.xml`, version 2025.07.09, creada por RPB
bajo RCS-21834.

## La respuesta

```
Archivo    pii-pgp-DA_Employee_Info.dat
Separador  coma
Calificador comillas dobles
Datos      empiezan en la linea 2, la 1 es encabezado
Destino    incident.Employee
Operacion  upsert
Llave      EmployeeID, columna 19
MISC1      columna 20
```

El campo que alimenta `incident.Employee.Misc1` es la posicion 20 del archivo plano, la que sigue
inmediatamente a EmployeeID. `StoreNumber` es la posicion 27.

## Por que la marca llega intermitente

El mapeo de Misc1 no declara `default` ni `rule`. Comparar con `Weight`, que tiene `default="0"`,
y con las columnas de fecha, que tienen `rule="validdate"`. Una posicion 20 vacia entra tal cual.

La operacion es `upsert` con `EmployeeID` como unica llave. Cuando ADUSA envia una fila con la
columna 20 vacia para un empleado que ya existe, el upsert escribe el vacio encima del valor
anterior. La marca no se pierde en transito. La borra la propia carga.

Esto es inferencia sobre el comportamiento del motor, no esta verificado contra
`ReferenceSupplementalLoad.exe`. La query de conteo en la base lo confirma o lo descarta.

## Columnas del feed que el mapeo descarta

Posiciones ausentes: 5, 13, 21, 22, 47. Las 21 y 22 caen justo despues de Misc1, patron tipico de
Misc2 y Misc3. Si ADUSA envia la marca en alguna de esas, el loader la esta ignorando.
Vale pedirle al cliente el layout del archivo para descartarlo.

## Texto para Matt, Teams

Ver bloque en la conversacion.

## Para el comentario del ticket

Pendiente de redactar con la skill cerebro-comentario. Los datos duros ya estan aqui.

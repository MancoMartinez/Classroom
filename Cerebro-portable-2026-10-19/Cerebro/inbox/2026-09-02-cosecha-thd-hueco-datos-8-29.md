---
fecha: 2026-09-02
origen: sesion local_90848306, "Investigacion con desglose tecnico"
tipo: causa raiz, investigacion abierta
estado: sin aprobar para la base
---

# THD, hueco de detalle de transaccion del 29 de agosto

## Lo verificado

Seis archivos suman 878.922 transacciones con discrepancia el 29 de agosto. Es la mitad del volumen
de un archivo horario de THD.

Prueba puntual del hueco: recibo de la tienda 6568 con Subtotal 2.074,00 y Total Item Sale Amount
0,00.

## Cuatro episodios, no uno

El panel de horas lista cuatro:

| Episodio | Duracion abierto |
|---|---|
| 8/29 hora 16 | 61 horas |
| 8/30 hora 20 | 1 hora |
| 8/28 hora 04 | 7 horas |
| 1 al 2 de abril | 37 horas |

Tres se recuperaron solos. El del 8/29 no. La pregunta para ingenieria deja de ser por que se perdio
el detalle. Pasa a ser por que este lote no entro en el reproceso automatico que rescato a los otros
tres.

## Son dos incidentes en el mismo ticket

El archivo de la hora 04 del 8/28 afecto los trading days 8/27 y 8/28 con 51.842 transacciones. Ya
cerro. Los seis del 8/29 son otro lote. La queja original de Matthew apunta al primero. Hay que
definir si el reprocesamiento cubre uno o los dos.

## El sintoma original sigue abierto

La transaccion 1123 de AJAX del 8/27 renderiza el recibo completo en una vista y devuelve "This
transaction cannot be found. It may be out of data retention" en otra. Una transaccion de cinco dias
no esta fuera de retencion. Diego le dijo al cliente el 28 que quedaba corregido. No lo confirmes
cerrado.

## Hipotesis principal: el cambio de formato del 23 al 24 de agosto

Los archivos pasaron de llegar planos y sin cifrar a llegar con path `Archive/Prod/` y extension
`.pgp`. Los cuatro episodios de agosto caen despues de ese cambio.

Matthew lo descarto probando que archivos de los dos formatos cargan bien. Esa prueba no mide que
pasa con un lote de seis archivos simultaneos. DO-10275 dice textual que `files.py` "use special
file path and file name and combine them for copying".

## REBUILD_RANGE: no dispararlo todavia

REBUILD_RANGE no existe en el cerebro. Nadie lo documento. Antes de correrlo hacen falta tres
respuestas por escrito:

1. Quien tiene el rol admin.
2. Si borra y reconstruye el rango o inserta encima.
3. Que rango consume.

El tercero no es trivial. El lote tiene tres relojes distintos: nombre logico 16:01, deposito 20:15,
panel del cliente 18:00. Si el procedimiento inserta encima, 878.922 transacciones duplicadas
convierten un ticket escalado en un incidente mayor.

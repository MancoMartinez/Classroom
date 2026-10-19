---
fecha: 2026-09-02
origen: sesion local_957fbfa6, "Ahold y J.R transcripciones analisis"
tipo: proceso, regla de entrega
estado: sin aprobar para la base
---

# Que columna del tracker sale al cliente y que columna nunca sale

## La regla de J.R.

`Issue summary` y `Next steps` son columnas de cara al cliente. En esas dos no van nombres de
ingenieros, no van numeros de ENG, y no va mencion de otro cliente. Se escriben en tercera persona
Appriss.

`Appriss Notes` nunca sale. Ahi van los nombres, los ENG y los precedentes de otros clientes.

El error concreto que se corrigio: se habia metido una mencion a Lux, que es otro cliente, en una
columna de cara al cliente.

## Formato de titulo en la columna B

Sin prefijo de cliente y sin guion. Las filas 23 a 59 del documento ya lo hacen asi.

J.R. tenia `AHL/DLZ - Greyed out fields in Izenda`. Queda `Greyed out fields in Izenda`.

## Guiones que se dejan a proposito

Tres excepciones a la regla de no usar guiones:

1. Los prefijos de fecha con formato `8/26/2026 - texto`, porque las otras 37 filas del documento los
   usan. Romperlo en nueve filas se ve peor que mantenerlo.
2. Las citas textuales del reporter, con su `however` y sus parentesis. Son sus palabras.
3. Los valores literales de resolucion de Jira.

## Regla de entrega de comentarios

Un archivo no puede llevar el marco en espanol y los bloques en ingles al mismo tiempo. Van
separados. Un archivo por comentario con solo el texto pegable, y el plan aparte.

Todo comentario lleva los cuatro requisitos de Aimee, incluida la declaracion de uso de IA y las
conversaciones que ocurrieron fuera del ticket.

Donde falta un dato, el comentario dice que falta. No se inventa.

## Conteos del reporte diario ADUSA, D12 contra D11

| Metrica | D12 | D11 |
|---|---|---|
| Tickets | 45 | 43 |
| Resueltos | 35 | 36 |
| Activos | 10 | 7 |

Los tres cambios: RCS-28683 y RCS-28693 nacen. RCS-28589 se reabrio a las 10:29 despues de haber
salido como resuelto en el D11.

## Lo que no puede salir al cliente

Cuatro cosas que se dijeron en la llamada y no van al documento:

1. La ruta comentada en codigo de RCS-28123.
2. El caso de control de acceso de RCS-28693.
3. La causa en el left join de RCS-28596.
4. La hipotesis de Excel de RCS-28589.

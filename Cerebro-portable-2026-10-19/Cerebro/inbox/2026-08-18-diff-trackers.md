# Diff de los tres trackers — 18 ago 2026

| Archivo | Hora | Qué es |
|---|---|---|
| `Appriss ADUSA-Support-Tracker.xlsx` | 09:26 | Interno. 35 tickets, 14 columnas, 1 hoja |
| `Appriss ADUSA-Support-Tracker.xlsx` | 10:30 | El mismo, con un solo cambio |
| `Appriss ADUSA-Support-Tracker - 08182026.xlsx` | 09:56 | El de J.R. para el cliente. 35 tickets, 10 columnas, 2 hojas |

## 09:26 → 10:30: un único cambio

**RCS-28415 quedó resuelto.** Alguien firmando GP añadió:

  "GP: RESOVLED - Goes to non-unique stores issue for 1 user (store 0722 exists in Food Lion too).
   Removed location and added correct division for one; added location to hierarchy for the other.
   RCS ticket updated"

Confirma el diagnóstico: es el problema de números de tienda no únicos entre marcas, el mismo de
RCS-28043. La 0722 existe también en Food Lion. A un usuario le quitaron la ubicación y le pusieron
la división correcta, al otro le añadieron la ubicación en la jerarquía.

Nada más cambió entre esas dos versiones.

## Interno → versión de J.R.: reescritura completa

Mismos 35 tickets, pero cada celda reescrita. Estas son las reglas que aplicó, y son el patrón
que tienes que repetir esta tarde.

### 1. Quitó cuatro columnas enteras

`Engineer assigned` (Matt, Kiran, Ripp, Gabor), `Cause` (hipótesis técnicas nuestras),
la columna de notas de trabajo, y `Priority`. Más la bandera de "Updated today".

El cliente no necesita saber quién es el ingeniero interno, ni nuestras hipótesis sin confirmar,
ni nuestra etiqueta de prioridad, que además contradice el marco de P1 que maneja Chris.

### 2. Borró todo lo que nos deja mal

Esto es literalmente lo que J.R. pidió, "not show our company in too bad of a light". Ejemplos que
estaban dentro y desaparecieron:

- "Comma-filename cases from 8/4 testing were not specifically retested"
- "A written root cause was still owed to ADUSA"
- "Other screen types were not individually re-verified"
- "Jira shows Work in progress, reverted from the prior Resolution Suggested state; recommend
   confirming current investigation status with Juan Martinez"
- "Jira shows Under Support Review, a step back from the prior Accepted into Development state"

### 3. Borró las instrucciones escritas a colegas

- "MATT. IN prod. Testing. Tell Support as soon as tested"
- "Ripp multi perf PRs in Prod. Retest. Gina: unable to reproduce in test demo7"
- "Just need to run Lunar against the DB in prod"

### 4. Cada celda de próximos pasos termina en un compromiso o una petición concreta

No deja frases muertas. Añadió cosas que no existían, como en RCS-28030, ya cerrado:
"If anyone still sees a four hour offset, have them sign out and back in first, then send the
case number." Un ticket cerrado sigue diciéndole al cliente qué hacer si reaparece.

### 5. Reescribió los títulos desde el síntoma del cliente, no desde nuestra jerga

| Interno | J.R. |
|---|---|
| System latency | Users are experiencing sluggishness of the system |
| Unable to edit location data | Error 502 when updating store information |
| When searching by some users, older cases are not appearing | Brian Somsky unable to see his old cases |
| Case tier - abbreviated on Central Station Master page | Case tier abbreviated on Central Station Master page |

### 6. Metió los 10 nuevos dentro de su tema y arregló la aritmética

Esta es la respuesta directa a tu duda de ayer. En el interno los temas sumaban **25** mientras el
total decía **35**, porque los nuevos vivían en un bloque aparte al final y no se contaban.

J.R. los repartió: User accounts 3→5, Store and brand 3→5, Case entry 4→6, Reporting 2→3,
Performance 1→4. Ahora los temas suman 35 y el bloque de "New Issues" desapareció.

**Los tickets nuevos van dentro de su tema. El bloque de nuevos es andamio, no forma final.**

### 7. Añadió una segunda hoja y la cadencia

Hoja `Cases missing owners` con 34 casos de ejemplo para RCS-28379, y en la fila 3:
"Agreed cadence: daily summary email, plus checkpoint calls Tuesdays 2:30 PM ET and Thursdays
3:30 PM ET."

## Lo que ya está vencido en la versión de J.R.

La armó a las 09:56. Dos cosas pasaron después y no las tiene:

**RCS-28415.** J.R. escribió "Appriss is assigning an owner, correcting the brand level hierarchy".
Ya está **resuelto** desde las 10:30, con la causa identificada. Hay que reescribir la fila y
mover el conteo: Store and brand pasa de 3 resueltos a 4, y de 2 activos a 1.

**RCS-28196.** J.R. escribió "A change is built and is waiting on a release. No release date is
confirmed yet". Gabor dijo a las 10:34 en el chat de Unification que está **resuelto y probado en
staging y producción**, fix solo para ADUSA. Con el matiz de Matt sobre los casos históricos.
Case entry pasa de 2 resueltos a 3, y de 2 activos a 1.

Con esos dos, el total pasa de **16 resueltos / 13 activos** a **18 resueltos / 11 activos**.

Es el mejor titular que puedes llevar a una reunión con un cliente que amenaza con irse.

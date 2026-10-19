# RCS-28872, vista AMQComment de Guess

## Que pasa

Guess reporta en RCS-28872 que la vista AMQComment y los dos reportes de Izenda que la usan,
Test Reports Audit Tabular Grid Comments e Inventory Reports Area 999, desaparecieron tras la
migracion del tenant a la nueva URL apps.apprissretail.com/guess/signin. Piden reponerlos.
Ticket Incident, prioridad Low, asignado a Enrique Jimenez desde el 11 sep 2026.

## Causa

Hipotesis, no confirmada contra la base de Guess. La vista no es un objeto estandar de la
plataforma. Se creo a mano en 2024 sobre RCS-15815, fuera del modelo base de Incident o Secure.
Una migracion reconstruye el esquema estandar. No reconstruye un objeto que nunca perteneceio a
ese esquema. Confirmar contra Guess US y Guess EU antes de escalar con esta causa como cerrada.

## Evidencia

RCS-15815, Guess Inc, SOW Estimation, cerrado el 5 ago 2024. Louis Marchand y Ryan Barlow,
ambos Engineering, escriben y prueban el script en dos iteraciones. La version final la corre
Louis Marchand en produccion Guess US el 24 jul 2024 y en produccion GuessEU el 26 jul 2024. Se
factura como SOW, 15 horas. El script que trae Juan es identico caracter por caracter a esa
version final, copiada del comentario de Ryan Barlow del 26 jul 2024.

## Que hago hoy

No correr el script. Es DROP VIEW mas CREATE VIEW, DDL. La regla del proyecto es SQL solo
SELECT contra produccion, sin excepcion para Support. En el precedente lo escribio y lo desplego
Engineering, nunca Support. Escalar RCS-28872 a Engineering, mismo dueno logico del precedente,
Ryan Barlow o su equipo actual. Pedir que redepliegue la vista AMQComment y los dos reportes de
Izenda en Guess US, y que confirme si Guess EU tambien migro a la nueva URL y necesita el mismo
redeploy. No hay permisos de Support para crear vistas en produccion, ni en este ticket ni en
ninguno.

## Precedentes

RCS-15815, ruta completa del script y del despliegue, resuelto el 5 ago 2024.

## Compromisos

Ninguno con el cliente todavia. El ticket es de Enrique Jimenez, no de Juan. Confirmar con el si
Juan participa en la escalacion o si esto fue solo consulta de contexto.

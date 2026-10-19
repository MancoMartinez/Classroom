# Cola del 10 sep 2026, con diff contra el 9 sep

19 tickets abiertos, los mismos 19 de ayer. Niveles 1=0, 2=1, 3=8, 4=10.
Clasificador en 13/13, cero etiquetas vencidas.

## Cambios desde ayer

Cero comentarios nuevos en los 19. Dos cambios de estado, sin comentario que los explique:

    RCS-28756  Under Customer Review -> Under Support Review
    RCS-27549  Under Customer Review -> Resolution Suggested

Ningun ticket nuevo, ninguno cerrado. La cola no se movio en 24 horas.

## Lo que quema hoy

RCS-28342 Ahold-Delhaize. Nivel 2. Prometiste update el 4 sep, cinco dias sin cumplir.
Unico ticket donde Appriss debe algo por escrito.

RCS-27676 RLC. 36 dias sin que el cliente oiga nada de Appriss. El mas expuesto de la cola.
RCS-28122 Blain's 21 dias. RCS-28282 Co-op 19. RCS-28496 PVH 19. RCS-28289 Vitamin Shoppe 15.

RCS-27765 Winn-Dixie. Hito vencido. El cliente dijo que reenviaba el archivo el miercoles
9/9 a las 10 AM. No hay comentario que confirme que llego. Verificar en el servidor.

RCS-28756 Nike ECOM. Madhuraj Gujaran te pregunto directo el 9 sep y paso a Under Support
Review. Es tuyo y no tiene nivel propio en el clasificador, solo la alerta de mencion.

RCS-28099 CWH. 22 dias sin movimiento, ultimo comentario del 18 ago. Muerto.

## Nota de medicion

El diff de hoy salio de comparar cola/estado-2026-09-09.json con cola/estado.json. El
snapshot se guarda a mano antes de refrescar. Sin ese paso no hay comparacion posible entre
dias, porque cola.py sobreescribe estado.json.

## Compromisos

Decidir si cola.py archiva el snapshot solo, con fecha, cada vez que corre.
Sigue abierta la decision sobre partir el nivel 4 y sobre el override de bitacora.

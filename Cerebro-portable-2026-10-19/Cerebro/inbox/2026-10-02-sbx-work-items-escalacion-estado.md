# SBX work items, estado tras escalar, 2 oct 2026 13:07 ET

RCS-29205 y RCS-29207 en Under Delivery Review desde 13:07, assignee Juan Martinez. Team ownership y Sprint vacios.
Nota de escalacion y respuesta a Manish pegadas en ambos. RCS-29206 sigue en Under Customer Review.

Delivery Secure 5 no auto crea ticket. Solo Engineering (ENG), Infrastructure (RTAILIT) y Security (INFOSEC) lo hacen.
El RCS es el ticket que trabaja Delivery.

Peyman Motlagh existe y esta activo en Jira (pmotlagh, RCS-28751 a su nombre con Team ownership Support (Delivery Dep.)
y Sprint RCS Support team). Peyman fuera el 2 oct. No se le asigna mientras no este.

Precedente RCS-29104: Juan lo dejo en Under Delivery Review a su nombre el 24 sep. Ryan DeVries lo reasigno a
Damodaran Chandrababu el 1 oct. Siete dias en cola. Delivery Secure 5 hoy reparte entre Adarsh Kumar, Hao T Nguyen,
David Parraga, Damodaran Chandrababu, Carl Costelow, Zackary Graas.

RCS-28873, mismo cutover SBX, esta en Under Delivery Review sin assignee.

Accion: llenar Team ownership y Sprint, dejar a nombre de Juan, mensaje de Teams a Ryan DeVries pidiendo quien cubre mientras Peyman no esta.

## Correccion de ruta, 2 oct tarde

Ryan DeVries, Teams: "Hmm so support doesn't have a backup for Peyman? Peyman is not a part of delivery".
Cuadra con el doc de Aimee "Support Data Team Ticket Triage" (Confluence RTS 477555982355): el Support Data Team,
solo Secure 5, es de Support. Peyman lo lidera, monitorea la cola y reasigna. La ruta usa Under Delivery Review y
Team Ownership "Support (Delivery dep.)" aunque el equipo no es Delivery. El nombre del campo confunde.
Delivery propiamente dicho para Secure 3/4/5 es Tomasz Mikunda o Carl Costelow.

Asignados con label Support_Data_Team en los ultimos 30 dias: Peyman Motlagh, David Beck, Matthew Everett,
Sebastian Rueda, Nikita Rathore, Vlad Bogus, Zackary Graas.

Accion: label Support_Data_Team en RCS-29205 y RCS-29207, respuesta corta a Ryan, preguntar a Camila quien cubre la
cola de Peyman mientras no esta.

## Segunda respuesta de Ryan y arreglo, 2 oct tarde

Ryan: "where do you see the escalation document?" y "in general delivery doesn't really do much for work items".
Origen del error: la fila "Delivery, Secure 5, Peyman Motlagh" del doc de Aimee 478006902856. Esa fila describe la
ruta del Support Data Team (Support), no de Delivery. Corregir en brain/memoria/reference_escalacion_l3_procedimiento.md.

Que se necesita de verdad. Nada de GP ni PGP: SBX ya no carga por Greenplum desde el 27 ago y los refunds si llegan
(204,745 tras el cutover). RCS-29205: mapeo de x_partnerownedtoken en el dbt de SnowTime de c166_sbx
(precedente Myer, dbt/clients/us/c109_myr/models/mapping/map_ardm_tender.sql, Matthew Everett), recarga desde el
27 ago y rerun del periodo. RCS-29207: tipo de MemberID en la condicion de la definicion (familia arpfiles PR 57459,
Sebastian Rueda) y rerun del periodo. Ambos son trabajo del Support Data Team. Juan no tiene acceso a esos repos.

Accion: disculpa a Ryan con link al doc, corregir primer parrafo de las dos notas de escalacion, preguntar a Camila
si Matthew (29205) y Sebastian (29207) cubren mientras Peyman no esta.

Ryan agrego: "they both seem like not problems with the work items but mapping issues?". Respuesta: si, y se le pregunta si el mapeo cae en Delivery o en el Support Data Team. Camila espera hasta que Ryan conteste.

## Resolucion de ruta, 2 oct tarde

Ryan DeVries: Delivery esta disponible mientras los nuevos equipos de soporte se ponen al dia. El mapeo puede ir a
Delivery o al Support Data Team. Delivery no sabe de work items, pero los problemas de mapeo si los resuelven
facil. Ryan se ofrecio a verlo el 2 oct.
Decision: RCS-29205 y RCS-29207 asignados a Ryan DeVries, Under Delivery Review. Las notas de escalacion quedan
como estan, "Escalating to Delivery" ahora es correcto. No se manda el mensaje a Camila ni la correccion de notas.
Leccion: mapeo post cutover SnowTime puede ir a Delivery (Ryan DeVries) o al Support Data Team. Work items puros no van a Delivery.

Mensaje final a Ryan: gracias, pregunta si Juan asigna o Ryan los toma, y si puede ensenarle el proceso de mapeo para que Soporte lo cubra sin escalar.

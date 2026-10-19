# Mapa de criticidad de clientes. Borrador para completar con Juan. 5 oct 2026

Fuentes: tickets/INDICE.md (generado 24 sep, 656 tickets), inbox/2026-09-28-smart-alerts-personas-y-lecciones.md, inbox/2026-09-08-cola-manana.md, db:knowledge_chunks/1553 (escalación ADUSA 14 ago), inbox/2026-08-25-rcs-27941-plan-verificacion-escalamiento.md, investigaciones/excel-urban-root-cause-2026-09-17.md, transcripción del 2 oct.

Jira manda sobre este borrador. Ningún estado de abajo está verificado en Jira hoy. La columna Criticidad marca "confirmada" solo donde un directivo o el historial lo respalda por escrito. El resto queda "por confirmar" para que Juan lo fije.

Los conteos salen de las fichas del cerebro. 222 de 656 fichas no tienen cliente. Cuentan menciones, no tickets abiertos.

| Cliente | Contacto que escala | Historial que el equipo debe conocer | Criticidad | Qué hacer al recibir un ticket |
|---|---|---|---|---|
| ADUSA (Ahold Delhaize USA: 36 fichas ADUSA, 158 Ahold, 26 Delhaize) | Jim Cosseboom, Director AP, escribe por correo. Leigh Ann Stubbs, reporter de varios tickets | Escalación ejecutiva del 14 ago: un ejecutivo rechazó una hoja de cálculo como update y pidió hechos, acciones y fechas para brand presidents y CTO. Dos errores 502 en vivo durante la llamada. Smart Alerts con deadlock, fix PR 58273 en producción desde el 28 sep. Jim reportó un segundo problema tras una corrección en RCS-28482 | Confirmada. JR dijo el 2 oct que Jim escala rápido y puede llegar a conversación de CEO | Asigna con senior o con Juan de respaldo. Comentario al cliente el mismo día. Nunca des ETA al cliente. Consulta la lección 8 de inbox/2026-09-28-smart-alerts-personas-y-lecciones.md |
| Stater Bros (14 fichas) | Por confirmar | Smart Alerts: flag incident.Shoplifting.InProcess atascado en 1, precedente ENG-2819 cerrado por Kiran Vadday | Por confirmar | Revisa el precedente antes de investigar. Escala directo a Kiran Vadday, no a Shandana genérica |
| Vitamin Shoppe (4 fichas) | Joe Austin | RCS-28289 bloqueó usuarios, el cliente trabaja con su IT. RCS-29145 abierto. Luis Hernandez ya usa la guía de disparo manual de Smart Alerts | Por confirmar | Verifica quién tiene la pelota antes de tratarlo como deuda tuya |
| Tailored Brands (7 fichas) | Colton Neal | RCS-27941 SSO y permisos. Puntero colgante en incident.LPUser2, el fix es un script en producción que ejecuta Kiran Vadday | Por confirmar | Escala con la tabla de evidencia de tres filas |
| Urban Outfitters (cliente 44) | Por confirmar | Exportación Excel, tres tickets cerrados según Jira al 17 sep. Camila los mencionó el 2 oct entre los clientes molestos, la transcripción es dudosa en ese tramo | Por confirmar con Camila | Pide a Camila el estado actual antes de asignar |
| Vallarta | Tatiana Barcenas | RCS-28294 Smart Alerts no disparan, escalado a Ingeniería desde el 27 ago | Por confirmar | Da seguimiento a la escalación, no al cliente |
| McDonald's | Hugo Cortez | RCS-28223 abierto 56 días al 2 oct, Hugo escribió y nadie contestó | Por confirmar | Revisa la cola de Juan, nivel 1 |
| SpartanNash, Sportsman's | Jason Mann (SpartanNash) | RCS-28452 con follow up pendiente desde el 19 ago. RCS-28131 de Sportsman's tras migración de base de datos | Por confirmar | Revisa con investigaciones/smart-alerts-familia-de-fallas.md |

## Lo que Juan completa

1. Marca la criticidad de cada fila como alta, media o baja, con una razón de una línea.
2. Nombra quién del equipo conoce al cliente. El cerebro no lo registra y yo no lo infiero.
3. Agrega los clientes que faltan: Nordstrom (13 fichas), TJX (12), Walmart (10), Torrid (9), CWH (7), Nike (5), AutoZone (4).
4. Define cada cuánto se revisa este mapa. Propuesta: cada lunes con la cola.

## Cómo usarlo

Pega la fila del cliente en el mensaje de asignación a Teams, en inglés y sin formato. Si el ticket tiene a un líder en el hilo, súbelo a prioridad sin discusión, como definió Camila.

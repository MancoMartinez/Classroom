# Charla de emergencia 9 sep 2026: que toca a Juan y al equipo Colombia

Revision de los tickets citados en el resumen de estado que circulo hoy. Fuente: comentarios de Jira leidos el 9 sep.

## Toca al equipo y la charla no lo dice

RCS-28838 y RCS-28834, ICA, los trabajo Diego Buelvas, no Gabor Remenyi. Diego tomo ownership de ambos hoy, publico dos RCA completos con queries y punto de falla, y pidio routing a Shandana Khan. Assignee actual de los dos: Shandana Khan. El resumen atribuye la investigacion a Gabor y nombra a Anushka como owner. Diego no aparece.

RTS-206683 esta asignado a Diego Buelvas. Se cerro con el hallazgo de Jon Morgan, el WI TEST corrio bien y quedo deshabilitado. Sin accion pendiente.

## Dos contradicciones tecnicas abiertas

RCS-28834. Diego concluyo que los tender EPS 186 y 187 legitimamente no generan fila en ARDM_HEADER, que ambas busquedas estan construidas FROM ardm_header LEFT JOIN ardm_tender, y que el arreglo es reconstruirlas tender-driven en Composer sin tocar dbt. Gabor y Jon Morgan concluyeron lo contrario, data load, headers faltantes, va a SnowTime. Si SnowTime arranca a crear headers para operaciones de banco persigue un fantasma. Resuelve el desacuerdo antes de que Anushka gaste el dia.

RCS-28838. Peter Just escribio a las 13:10 "Please review my comment before doing any more work on this". Su hipotesis es doble mapeo de Points a Loyalty_Points y LoyaltyExt_Points desde los dos feeds POS. Diego ya habia cerrado causa raiz en otro lado, el XMLGET de flat_receipt_loyalty.sql salta el nodo intermedio VRArtsPoslogExt:LoyaltyAccount y deja card_number NULL. Dos causas raiz distintas para el mismo sintoma, ninguna descartada.

## Toca a Juan

RCS-27549, ICA performance, es de Juan. J.R. Teagle le pidio hoy 11:51 verificar y avisar al cliente. Juan respondio 13:18 confirmando que probo receipts en WI e Investigation. Queda Under Customer Review esperando a Marie.

## No toca a nadie del equipo

RCS-28517 Bunnings y RCS-28828 ICA weekly reports. Sin gente de Colombia en los comentarios. RCS-28517 si figura como precedente en bitacora/RCS-28671.md por la clase de falla de work items contra Snowflake, con Blue team y Jon Morgan.

## Compromisos

Preguntar a Diego si vio el comentario de Peter Just. Llevar el desacuerdo de RCS-28834 a Gabor y Jon antes del handoff a SnowTime.

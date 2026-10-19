# SBX work items, estado 9 oct 2026, verificado en Jira

RCS-29205: Work in progress, Juan. Ultimo comentario 8 oct 11:21 (avance al cliente). Sin nota interna sobre el branch de Ryan. Falta avance diario 9 oct.
RCS-29206: Under Customer Review. Juan publico seguimiento generico 9 oct 13:31. Automation aviso 7 dias sin respuesta el 8 oct.
RCS-29207: Completed desde 6 oct, falta Closed.
Pendiente confirmar si se enviaron los Teams del 8 oct a Ryan (cierre) y a Anushka/Adarsh (branch).

Teams del 8 oct a Ryan y a Anushka/Adarsh: enviados.
Anushka, 8 oct 11:00: el branch de Ryan ayuda; enrich_ardm_tender requiere cambios de mapeo; ella sube el PR; el rebuild necesita rol admin que ella no tiene, pedira a alguien tras el deploy.
Anushka, 9 oct 12:35: PR 58962 (achaudhary/c166_rcs29205_token_paidinout) con paid in/out, arreglos al acumulador de Ryan (column_spec, fuente prod, NULL en vez de FALSE, aproximacion x_refundtoown) y RCS-29205_fix_summary.md. Pide revision de Juan antes de deploy y rebuild.
Juan, 9 oct 12:42: preguntas antes de aprobar: validacion en lab, tokens ligados despues de la transaccion (seed hasta 26 ago, rebuild desde 22 ago, chunks diarios), paid in/out desde 26 ago cubre eventos desde 25 ago, aproximacion x_refundtoown acordada con dueno, quien hace seed, rebuild y regeneracion.
Nota interna del 9 oct reescrita con el PR.

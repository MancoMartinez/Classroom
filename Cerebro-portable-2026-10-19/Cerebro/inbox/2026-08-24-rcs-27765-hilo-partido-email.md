# RCS-27765 · Winn-Dixie · Data file check · 24 ago 2026

## Estado real en Jira, verificado hoy

Status: Work in progress. Assignee: Juan Martinez. Priority: Medium.
Labels: EB&F_scheduled, Support_Data_Team. Reporter: Heaven Poirot.
Ultimo update: 2026-08-24 08:23.

## Que pasó realmente

No hay problema técnico nuevo. El hilo se partió en dos canales.

Matthew Laney (IT de Winn-Dixie) escribió por correo a support@apprissretail.com.
Shireesh Ramdas pegó ese correo dentro del ticket el 22 jul a las 12:00.
Juan respondió el 27 jul a las 17:21 dentro del ticket, nunca en el hilo de correo.
Matthew nunca vio esa respuesta. Heaven lo confirma hoy, 24 ago 08:23:

> "I did not realize you all were only responding on the ticket. We have an email
> thread with reference to this ticket, that I.T had been waiting on a response to."

Camila Cortes hizo follow-up el 5 ago dentro del ticket. Mismo canal equivocado.
Resultado: 28 días perdidos esperando cada lado al otro.

## Evidencia técnica ya establecida, no hay que repetirla

Tienda 358, conteo de transacciones en producción:

| Fecha | Transacciones |
|---|---|
| 24/06/2026 | 2,323 |
| 25/06/2026 | 773 |
| 26/06/2026 | 2,421 |

Faltan aproximadamente 1,600 transacciones del 25/06. Confirma el incidente interno
que describió Matthew.

La primera investigación de Shireesh miró `\\p-ingest-fsla4\121_SEG\Archive`, el archivo
SFTP. Los datos entraron por Ingestion API. Por eso se reportó "no recibido" al inicio.

## El paso siguiente

Uno solo: mover la respuesta del 27 jul al hilo de correo, con reply all sobre el correo
original de Matthew, para que IT la vea. No abras investigación nueva. No pidas datos nuevos.

Después, un comentario corto en Jira que cierre el hueco de canal.

Dato a vigilar: el 25/06 tiene 60 días al momento de este reenvío. Si el reenvío por
Ingestion API se rechaza por antigüedad de la transacción, ese es un hallazgo distinto y
se documenta aparte. No lo afirmes antes de que ocurra.

## Bloque 1, correo a IT (reply all al hilo de Matthew, asunto con RCS-27765)

Hi Matthew and Heaven,

Apologies for the delay on this thread. Our reply went into the Jira ticket on July 27 and did not make it back onto this email chain. That is on us. Here is that response in full so you have it in one place.

We verified store 358 directly in our production data and confirmed the discrepancy. For 06/25/2026 we received 773 transactions for store 358. Surrounding days show a normal daily volume of roughly 2,300 to 2,600 transactions. 06/24 came in at 2,323 and 06/26 at 2,421. Roughly 1,600 transactions from 06/25 never reached production, which matches the internal issue Matthew described.

One correction to our first answer on this ticket. Our initial check looked at the SFTP archive. That data was transmitted through the Ingestion API, so the SFTP archive was the wrong place to confirm receipt. That is why we first reported the file as not received.

Please go ahead and rebuild and resend the 06/25/2026 TLOG data for store 358 through the Ingestion API. Send us the date and the time window when you trigger the resend, in Eastern Time, so we can watch the ingestion in real time on our side.

Once the resend lands, we will recount transactions for store 358 on 06/25/2026 and confirm the volume is consistent with a normal day.

Going forward, please keep RCS-27765 in the subject line and copy l1retailcustomersupport@apprissretail.com and l2retailcustomersupport@apprissretail.com. Every reply on this chain will then land on the ticket and both channels stay in sync.

Kind regards,
Juan Martinez
Appriss Retail Support

## Bloque 2, comentario en Jira

Hi Heaven,

Thank you for flagging that. You are right, our response stayed inside the ticket and never reached the email chain your IT team was watching. I have replied on that thread directly to Matthew and copied you, so IT now has our full answer.

The short version. We confirmed the gap in our production data for store 358 on 06/25/2026. We received 773 transactions that day against roughly 2,300 to 2,600 on the surrounding days. 06/24 was 2,323 and 06/26 was 2,421. The next action sits with your IT team: rebuild and resend the 06/25/2026 TLOG data for store 358 through the Ingestion API, and tell us the date and time window of the resend in Eastern Time so we can monitor ingestion live and verify the counts afterward.

To keep both channels aligned, please send email replies to support@apprissretail.com with RCS-27765 in the subject line, copying l1retailcustomersupport@apprissretail.com and l2retailcustomersupport@apprissretail.com. Anything sent that way lands on this ticket automatically.

Kind regards,
Appriss Retail Support

## Transición sugerida

Work in progress a Under Customer Review, una vez enviado el correo. La pelota queda en
IT de Winn-Dixie hasta que confirmen fecha y hora del reenvío.

## Lección de proceso, sirve más allá de este ticket

Cuando L1 pega un correo del cliente dentro del ticket, la respuesta no vuelve sola al
correo. Si el hilo nació en support@apprissretail.com y hay un tercero que no está en Jira,
responde en el correo y refleja en Jira. Nunca al revés.

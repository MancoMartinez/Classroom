# RCS-28756, respuesta DM Teams a Peyman Motlagh

Version ordenada con negritas y separada por punto, para pegar en Teams.
Responde las 4 preguntas de Peyman en su orden. Basado en la lectura completa
de los 34 comentarios y adjuntos del ticket, verificada el 2026-09-30.

## Texto listo para pegar (ingles, DM Teams a Peyman)

Hi Peyman, going point by point.

**Root cause.** Confirmed, it was the connector on our side, not Nike. Saddam fixed it around 9/15, current days have been flowing fine since.

**What I need from Bikash or Delivery.** Confirm everything after 9/17 loaded clean, and reach out to Nike to request a resend for 8/28 through 9/17.

**Have they sent all the backlog files.** No. Bikash checked the raw archive directly and found nothing for 8/28 to 9/17, wider than the 8/28 to 9/10 you asked him to reload. Those files were never received, nothing to reload on our end, Nike has to send them.

**How we identify backlog files.** Check the archive path directly against the expected daily files for the range, missing dates mean never received. That is how Bikash found this gap.

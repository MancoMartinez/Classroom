# Correo final para Jim — versión post verificación de Jira

Adjuntar: `~/Downloads/Appriss ADUSA-Support-Tracker - 08182026 PM.xlsx`

```
Jim,

Thank you for the detailed answers this morning and for the time on the call.  I've updated
the tracker on our side with everything that came out of both and it's attached.  Five items
closed today, which takes us from sixteen resolved to twenty-one.

A few things I need from you directly, separate from the tracker, because these are the ones
that move fastest with an answer from your side.

Your server migration, RCS-28292.  This one is time critical so I've put it first.  The
address we were given, 10.37.1.162, is a private internal address, so we can't tell from it
whether an allow list change is needed on our side.  Could you confirm the public IP address
the new server will present, before the window opens Thursday night?  April Valerio is noted
as the contact and we have your validation of the store file on the morning of the 21st.

Performance, RCS-28356 and RCS-28407.  You saw latency but no 502s this morning, and Leigh
Ann logged one with detail.  The read we still don't have is from the Hannaford team who
reported the longest page open times.  Have they seen a difference since Monday evening?

Attachments, RCS-28124.  A user reported the forbidden message again this morning, and the
upload fix went into the release later the same morning, so we're treating that report as
predating the fix until it's retested.  Could someone try a video upload and tell us either
way?  Separately, .txt was the only format that didn't behave in our testing.  Is that a
format your teams actually use?

The Central Division report, RCS-28413.  We have the name and the expected count now, thank
you.  Before we send a correction out, who received the 66 case version, and do you want us
to reissue to that list or send you the file to distribute?

Scheduled reports.  You offered to look at which ones run during business hours.  If you send
us the list and the time you need each report by, we'll move them and confirm.

RCS-28196, the two Shoplifting fields.  Thank you for validating this afternoon.  The one
open question for your side is whether cases entered between cutover and the fix need
reviewing for those two fields.  If so we can pull the list.

Assigning locations in the new application.  Matt offered to walk your team through it, since
that screen differs from the one they were trained on.  It would prevent the hierarchy issue
we saw on the two new accounts.  Is that useful, and who should be on it?

On the Secure side, RCS-28281.  Understood that it sits outside this workstream, and we'll
take it up with Lauren Linsenbach and Jacquelyn Wunders directly.  The original question
still stands for them: do you need the missing volume backfilled, or is a corrected figure
for that date enough?

Four to close: RCS-28177, RCS-28364, RCS-28378 and RCS-28415.  All show resolved on both
sides.  Confirm and we'll close them in Jira.

Job titles, RCS-28342.  Your examples confirmed the problem was wider than the individual
records we had corrected, and that the title is present in your own directory.  After the
call we updated the single sign-on mapping so the title field is handled.  Could one of the
affected users, Janai Harrison or Stacie Whetzel for example, sign out, sign back in and tell
us whether the title now appears?  Once that's confirmed we'll check the rest against the
same mapping.


Thanks,
```

---

## Nueve ítems, y por qué cada uno

| Pedido | Justificación |
|---|---|
| **IP pública, RCS-28292** | **Nuevo y urgente.** Gulshan preguntó hoy 05:24 que la dirección dada (10.37.1.162) es privada y no sirve para saber si hay que tocar la lista blanca. El status pasó a "Under Customer Review", o sea espera respuesta de ellos. La ventana abre el jueves por la noche. Si no llega, el archivo de tiendas puede romperse el viernes. |
| Lectura de Hannaford | J.R. la pidió ayer y nadie la contestó. |
| Prueba de video + .txt, RCS-28124 | Leigh Ann reportó el error otra vez hoy 08:36 y el fix salió después. Hay que cerrar el ciclo con una prueba de ellos. |
| Distribución del reporte, RCS-28413 | Falta saber a quién le llegó la versión mala para poder reemitir. |
| Lista de reportes programados | Jim se ofreció él mismo al cerrar la llamada. |
| Casos desde el cutover, RCS-28196 | Solo ellos pueden decidirlo. Ya validaron el fix hoy 15:04, así que solo queda esa decisión. |
| Llamada de acompañamiento | Matt la ofreció y nadie la agendó. Sin ella se repite con cada usuario nuevo. |
| Backfill, RCS-28281 | Pregunta original de J.R. sin responder. Cambia de destinatario, no se cae. |
| Cuatro para cerrar | Jira los tiene abiertos y sin resolución pese al visto bueno verbal. Sin el sí por escrito no se cierran. |

# Comentarios para el barrido — 18 ago 2026

Texto plano, en inglés, sin markdown, listos para pegar. Cada uno cierra con tu nombre.
Yo no escribo nada en Jira: tú los pegas.

Orden sugerido: primero los tuyos, luego los que no tienen dueño, y de último el vencido.

---

## RCS-28021 — Izenda, exportación

Update for 18 August.

The scheduled reports were rerun on 14 August against current data, and we confirmed on the
morning of 18 August that the Izenda scheduler is running and delivering on time.

The export problem is still open. We have not been able to reproduce it from a general
description, so we need one report by name that fails to export. With that we can trace the
export path end to end on that specific report.

We are also aware that the date range on a report does not always hold, which can return older
records without indicating it. The records themselves are present.

Juan Martinez
Appriss Retail Support

---

## RCS-28123 — Asignación de casos

Update for 18 August.

An update was deployed to production on the evening of 17 August and is being verified now. We
will confirm on this ticket as soon as verification completes.

To finish verifying we need to approve a record in production. We have asked ADUSA for permission
to do that on a nominated case rather than on live work.

Separately, we owe an answer on the point raised on 14 August, that a case PDF can no longer be
printed from the confirmation screen and has to be reached from the workbench. That is being
looked at alongside this.

Juan Martinez
Appriss Retail Support

---

## RCS-28124 — Adjuntos

Update for 18 August.

A further fix was deployed and tested on 14 August. A second deployment is going to staging today
because the release branch carries additional changes, so the full fix reaches production in two
steps rather than one.

This ticket stays open until ADUSA confirms. Could a Hannaford user retry a video upload and tell
us either way. If any attempt still fails, the case number is enough for us to trace it.

We are not closing this on our own testing again.

Juan Martinez
Appriss Retail Support

---

## RCS-28342 — Anthony Lopez

Update for 18 August.

The record was corrected on 14 August and the job title now displays on both entries. The cause
was multiple email addresses on the account, which matched the wrong user identifier, so the
profile and title did not follow through.

Please have Anthony sign out, sign back in and confirm. We will close as soon as you tell us it
is good.

Juan Martinez
Appriss Retail Support

---

## RCS-28364 — Brian Somsky

Update for 18 August.

His record was updated on 14 August to match the identifier from the previous system. Please have
him sign out, sign back in and confirm the historical cases appear.

We will come back separately on Anthony Powell, reported on 14 August with the same symptom.

Juan Martinez
Appriss Retail Support

---

## RCS-28353 — Error 502 al actualizar tienda

Update for 18 August.

This is being worked together with RCS-28356 and RCS-28407, because the 502 responses and the
general slowness appear to share an underlying cause.

A set of fixes reached production on the evening of 17 August. Early checks on our side are
positive but not yet proven across a full working day.

Please retry a store profile update and tell us whether the 502 still occurs. If it does, we will
take up the screen share ADUSA offered so we can capture a browser trace.

Juan Martinez
Appriss Retail Support

---

## RCS-28378 — Botones Save y Next, Hannaford

Update for 18 August.

We are assigning an owner to this today.

To move it forward we need the additional detail offered on 14 August: which page, which users,
and a screenshot if one is available. There is a possible match to a defect already under
investigation and we are checking this symptom against it rather than assuming they are the same.

Juan Martinez
Appriss Retail Support

---

## RCS-28413 — Reporte de Central Division

Update for 18 August.

We are assigning an owner to this today.

We will verify the true case count for Central Division against what the report returned, so it
is clear whether this is a reporting fault or genuinely missing cases. Nothing so far indicates
case data has been lost.

Two questions for ADUSA. Do the managers who received the 66 case version need a corrected report
sent out, and can you tell us what the count should be.

Juan Martinez
Appriss Retail Support

---

## RCS-28415 — Usuarios nuevos de Stop & Shop

Update for 18 August.

We are assigning an owner to this today.

Neither user had a location assigned. We are correcting the brand level hierarchy so both users
see Stop & Shop, and reviewing the store 0722 entry that was added, which produced Food Lion
access rather than the Stop & Shop access these users need.

We are reviewing this against RCS-28365 to confirm whether they share a cause.

Juan Martinez
Appriss Retail Support

---

## RCS-28281 — Carga de transacciones del 10 ago (VENCIDO, 5 días)

Este es el único de los 21 abiertos sin tocar desde el 13 de agosto. Es de Edwin, así que primero
pídele el estado. Si no responde antes de la reunión, pega esto para que no llegue en blanco:

Update for 18 August.

All files received have been loaded. Duplicate files in the delivery accounted for a material
share of the volume received, which reduced the usable total for the day. Loaded volume was
approximately 1.07 million transactions across 726 stores, against roughly 2.1 to 2.3 million on
each of 7, 8 and 9 August.

Why the day's data stops in the early afternoon is still being established. We will confirm the
cause and whether the shortfall can be backfilled.

Juan Martinez
Appriss Retail Support

---

## RCS-28196 — CORRECCIÓN IMPORTANTE ANTES DE ENVIAR LA HOJA

La hoja de J.R. dice "Waiting for Software Release, no release date confirmed yet". **Eso ya está
desactualizado.** En el chat de End of July Unification, Gabor Remenyi a las 10:34 a.m.:

  "RCS-28196 is resolved, tested both in staging and prod (fix for adusa only, other clients
   would still need lunar deployment)"

Y Matt Kamminga añadió el matiz que hay que decirle al cliente:

  "the historical cases that were created between go live and now. All future ones will be fine
   however other ones will still have the default value. If we respond we need to be specific
   on that part."

Gabor preguntó cómo distinguir un No elegido de un No por defecto, y Matt respondió que habría
que comparar contra la tabla `casechanges`: si el usuario lo puso a mano hay una fila ahí. Va a
intentar armar la consulta.

Actualiza la fila en la hoja y usa este comentario:

Update for 18 August.

This is resolved. The fix was tested in staging and in production and is in place for ADUSA.

One point to be specific about. Cases created from go live until now still hold the default
value on these two fields. Only cases created from this fix onward will open blank as expected.

We are working on a way to identify which of the existing cases were genuinely answered by a user
and which carry the default, so ADUSA can decide whether those need reviewing. We will come back
with what we find.

Juan Martinez
Appriss Retail Support

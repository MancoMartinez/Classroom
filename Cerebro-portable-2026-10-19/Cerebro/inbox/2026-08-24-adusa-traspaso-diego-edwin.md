# ADUSA · traspaso de los tres tickets sin dueño · 24 ago 2026

Los tres llevan entre tres y cuatro días en Under Support Review, sin dueño y sin una sola respuesta de Appriss más allá del acuse automático. Al asignarlos, transiciona cada uno de Under Support Review a Work in progress.

Cada ticket lleva dos bloques. El de cliente va neutral, corto y sin nada técnico. El interno lleva el análisis, los nombres y el Client ID, y no se le cuenta al cliente ni en resumen.

Client ID de ADUSA: 441.

## RCS-28535, adjuntos con error Forbidden · sugiero Edwin

Comentario al cliente:

```
Hi Leigh Ann,

Thank you, that detail helps.

We are looking into it and will come back to you with an update.

Thanks.
```

Comentario interno:

```
CLIENT: Ahold Delhaize USA / ADUSA (Client ID 441)

Leigh Ann narrowed this on 24 Aug at 14:11: clips of around 2 minutes upload fine,
files of 11 minutes or more fail at roughly 60% and return Forbidden.

Reads as an upload size or duration limit being hit, not a permissions failure.
That is an interpretation of her description, not confirmed. It would explain why the
RCS-28124 fix held on small files and why the symptom returned on body worn camera video.

Start on the size and timeout limits of the upload path rather than on permissions.

Cases supplied 24 Aug at 11:43:
2026-HANNAFORD BROS. CO., LLC-8327-51
2026-HANNAFORD BROS. CO., LLC-8109-161
2026-HANNAFORD BROS. CO., LLC-8109-164

Users reported: Ian Jordan (MP4 body worn camera), Kayla De Jesus-Morales, Erica Shrader.
Related: RCS-28124, closed 21 Aug.
```

Por qué Edwin. Viene del trabajo de rendimiento y de RCS-28407, y esto apunta a límites de carga, no a permisos.

## RCS-28519, usuarios que no ven ninguna tienda · sugiero Diego

Comentario al cliente:

```
Hi Jim,

Thank you for confirming the steps already tried.

We are reviewing both accounts and will come back to you with an update.

Thanks.
```

Comentario interno:

```
CLIENT: Ahold Delhaize USA / ADUSA (Client ID 441)

Two users cannot select any store when entering a case:
Deborah Jean, LP User Level 2, S&S 0498 (in the description)
Sammy Rivera (added by the reporter 21 Aug at 17:05, not in the description)

Sign out, browser cache clear and reboot were already tried, no change.
Reporter states cases are queued and unable to be entered.

Same symptom as RCS-28415, closed 19 Aug, which was corrected at the data level across a
much wider group. First check is whether these two accounts fell outside that correction.
That is a starting hypothesis, not a confirmed link.
```

Por qué Diego. Es revisión de cuentas y asignaciones de tienda, del mismo tipo que ya trabajó.

## RCS-28533, pantalla que no renderiza · sugiero Diego

Comentario al cliente:

```
Hi Jim,

Thank you for the screenshots, having both views side by side is what we needed.

We are looking into it and will come back to you with an update.

Thanks.
```

Comentario interno:

```
CLIENT: Ahold Delhaize USA / ADUSA (Client ID 441)

User Ralph Valentine. One LPMS screen renders with the columns compressed, leaving the
report narrative and the fields next to it unusable. Two screenshots on the ticket, his
view and a colleague's correct view of the same screen.

Reporter checked display resolution and font size on the laptop, both normal.
Single user reported so far.
```

## RCS-28482, este es tuyo, no lo traspases

Sigue asignado a ti y sin respuesta desde que Jim corrigió el malentendido el 22 a las 10:33. Hoy además te reenvió las capturas por correo. Van tres días.

Comentario al cliente:

```
Hi Jim,

Thank you for the screenshots, and apologies for the earlier reply that pointed you
somewhere else.

We are looking into the MISC tab specifically and will come back to you with an update.

Thanks.
```

Comentario interno:

```
CLIENT: Ahold Delhaize USA / ADUSA (Client ID 441)

Reporter clarified 22 Aug at 10:33: the blocked tab is MISC, used to change report
distribution and the run schedule. Data Sources does not carry that information, so the
earlier reply did not address the request.

From the screenshots he sent, the affected reports expose only Data Sources, Fields and
Preview, while a working report exposes the full set including MISC. The affected view
also shows a Distinct checkbox and a Results selector where the working view shows Records,
which suggests the two are not the same report type and that the available tabs follow
from the type. That is a reading of the screenshots, not verified.

Affected: PBI - Current Location Listing (Jim Cosseboom Test), Outlook Export
(Jim Cosseboom Test). One is a clone of the other. Both run normally, only editing is blocked.
```

## Qué cambió frente al borrador anterior

El primer borrador le explicaba al cliente el diagnóstico técnico: que era un timeout y no permisos, que se iban a revisar límites de la ruta de carga, que RCS-28415 se había corregido a nivel de datos, que se iban a comparar las capturas contra las reglas de renderizado. Todo eso es análisis interno y no va al cliente. Ahora está en el bloque interno de cada ticket.

También quité el atajo de partir el video en segmentos. Nadie lo probó, sale de inferir sobre lo que describió Leigh Ann, y ofrecerlo como solución sin verificarlo es afirmar un resultado que no está comprobado.

## Resumen de acciones

Asigna RCS-28535 a Edwin, RCS-28519 y RCS-28533 a Diego, transiciona los tres a Work in progress y pega los dos bloques en cada uno. El de RCS-28482 lo pegas tú.

El dato que reorienta RCS-28535 es el de Leigh Ann del 24 a las 14:11 sobre la duración del video. Pásaselo a Edwin de primero, no está en ningún otro lado.

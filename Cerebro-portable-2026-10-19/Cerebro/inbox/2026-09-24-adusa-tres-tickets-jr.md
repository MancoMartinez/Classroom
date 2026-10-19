# ADUSA · RCS-28596, RCS-28667, RCS-28683 · estado para J.R.

## Que pasa
J.R. mantiene el correo diario de Ahold hasta que estos tres queden limpios. Matt Kamminga esta fuera hasta el 5 oct y dos de los tres dependen de el.

## Causa
RCS-28596. CONFIRMADA y cerrada. LEFT JOIN a Store por StoreNo en EELookupList. Closed 15 sep, ENG-7904 Done.
RCS-28667. CONFIRMADA por Kiran: asignar jerarquia es tarea del admin. HIPOTESIS abierta: Chris ligo "the sign in ones" a ENG-8752, que automatiza la jerarquia desde los claims SSO Store Number y Banner. Si aplica, la respuesta a Leigh Ann describe un paso manual temporal.
RCS-28683. HIPOTESIS. Al copiar a otro asociado la app redirige a /nettrack/LPMS/CentralStationMaster.aspx en el host azurewebsites sin el slug /adusa, y el archivo no existe ahi. Defecto de codigo o despliegue.

## Evidencia
1. Jira hoy: RCS-28667 Under Customer Review, respuesta de Juan 15:03. RCS-28683 Accepted into Development, Shandana. ENG-8338 Backlog, asignado a Matt. ENG-8752 Ready for Code Review, Matt.
2. RCS-28683 comentario 3326640, Diego 3 sep: "The file '/nettrack/LPMS/CentralStationMaster.aspx' does not exist", referrer apps.apprissretail.com/adusa/.../LPMSEditMenu.aspx.
3. ENG-8752 descripcion: StoreNumber no es unico entre banners, '0001' mapea a Food Lion y Stop & Shop. Misma raiz que RCS-28596.

## Que hago hoy
1. Pega 2026-09-24-adusa-teams-jr.md en el hilo de "Sync on live prod issues".
2. Si Chris confirma que ENG-8752 cubre RCS-28667, pide a Shandana el link entre ambos y avisa a Leigh Ann que el paso manual es temporal.
3. Si Shandana no reasigna ENG-8338, la fecha real es despues del 5 oct. Dilo en el correo de Jim como "in October sprint", sin fecha.
4. RCS-28760 es clon de RCS-28683, Open. Revisa si es duplicado antes del correo de Jim.
5. Saca RCS-28596 del correo diario si sigue ahi.

## Precedentes
RCS-28415 y RCS-28519, usuarios sin jerarquia, arreglo manual. tickets/RCS-28415.md
Rebuild de pantallas 404 con ?ADMIN=9QQP, Kiran. Probable no aplica: CentralStationMaster.aspx es archivo fisico. brain/memoria/reference_screen_designer_rebuild.md
Store number no unico por division, RCS-28596. brain/markdown/26-adusa-estado-tickets-reuniones.md

## Compromisos
Ninguno nuevo al cliente. RCS-28683 no se comenta al cliente hasta Under Support Review.

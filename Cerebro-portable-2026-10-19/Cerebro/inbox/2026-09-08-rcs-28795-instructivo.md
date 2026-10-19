# Instructivo. RCS-28795. Bunnings, correo de notificacion de asignacion no llega

Runbook. La causa raiz de codigo ya esta confirmada en RCS-28766. Estos pasos reproducen el sintoma en el tenant de Bunnings, validan que se trata del mismo defecto, y dejan listo el enlace y el comentario. No repitas la investigacion de codigo de PR 56138, ya esta hecha.

## Paso 1. Reproducir el sintoma en el tenant de Bunnings

Donde se ejecuta. Portal de Bunnings, ambiente de produccion.

El comando o la accion.
```
1. Abre un caso existente en el tenant de Bunnings.
2. Reasigna el caso a un usuario distinto, por ejemplo a ti mismo o a otro agente de prueba.
3. Confirma en la bandeja del usuario reasignado si llega el correo de notificacion.
```

Que se espera ver. El correo no llega al usuario recien asignado. Si llega, este no es el mismo defecto y hay que abrir hipotesis nueva antes de vincular a RCS-28766.

Si falla. Si no puedes reproducir por falta de acceso al tenant, pide a Enrique Jimenez que lo corra el con un usuario de prueba y te confirme el resultado por Teams antes de seguir.

## Paso 2. Confirmar que la reasignacion pasa por la pantalla estandar

Donde se ejecuta. Portal de Bunnings, inspeccion de la URL o del formulario al reasignar.

El comando o la accion. Verifica que la pantalla de reasignacion sea la estandar y no una variante de Tier Level o SRMS.
```
1. Al reasignar el caso del paso 1, revisa la URL o el titulo de la pantalla.
2. Busca ReAssignCase en la URL o en el codigo fuente visible del formulario.
3. Descarta que sea una reasignacion de tier level o una reasignacion SRMS, esas pantallas si conservan el disparador de correo.
```

Que se espera ver. La pantalla es la reasignacion estandar de caso, ReAssignCase.aspx.vb. Esa es la pantalla afectada por PR 56138.

Si falla. Si la pantalla es UpdateTierLevel o ReAssignCaseSRMS, el correo deberia estar llegando segun el hallazgo de Diego. Si no llega ahi tampoco, este es un sintoma nuevo y distinto, no lo vincules a RCS-28766, escala como hallazgo separado.

## Paso 3. Validar el flag de configuracion del tenant

Donde se ejecuta. SQL contra la base de aplicacion Secure de Bunnings. Solo SELECT.

El comando o la accion.
```
SELECT EmailOnReassign FROM incident.Options;
```

Que se espera ver. Valor 1, flag activo. Esto descarta que Bunnings tenga el correo desactivado por configuracion propia, igual que se descarto para ADUSA.

Si falla. Si el valor es 0, el sintoma de Bunnings tiene una causa distinta a la de RCS-28766, es configuracion de tenant y no el bug de PR 56138. No lo vincules como el mismo defecto, documenta el valor encontrado y sigue por esa via en su lugar.

## Paso 4. Vincular RCS-28795 a RCS-28766

Quien autoriza. Juan Martinez, es tu ticket, tu ejecutas el enlace.

Donde se ejecuta. Jira, RCS-28795, menu de acciones del issue.

El comando o la accion.
```
1. Abre RCS-28795 en Jira.
2. Usa el boton Link o la opcion del menu de tres puntos.
3. Elige el tipo de enlace relates to.
4. Selecciona RCS-28766 como el issue vinculado.
```

Que se espera ver. RCS-28795 muestra el enlace relates to RCS-28766 en el panel de issue links.

Si falla. Si Jira no te deja enlazar por permisos, pide a Diego Buelvas o a Enrique Jimenez que lo haga, ambos tienen acceso al ticket.

## Paso 5. Pegar el comentario interno de escalacion

Quien autoriza. Juan Martinez.

Donde se ejecuta. Jira, RCS-28795, comentario interno, visible solo para Appriss.

El comando o la accion, en ingles, sin markdown ni guiones como conectores.
```
This ticket matches the root cause confirmed on RCS-28766. Root cause is confirmed, not a hypothesis. PR 56138, part of the ENG-7192 fix wave merged on 2026-08-14, removed the block in ReAssignCase.aspx.vb that read Options.EmailOnReassign and called CreateAlertInQueue with type REASSIGN. That removal left no trigger for the reassignment notification email on the standard reassignment screen. Sibling screens UpdateTierLevel.aspx.vb and ReAssignCaseSRMS.aspx.vb are unaffected. Bunnings is the second client reporting this symptom after Ahold Delhaize on 2026-09-01. RCS-28766 is Under Engineering Review, currently assigned to Mohammed Mutahhar for validation of the code analysis. No fix has been deployed yet. Do not open a separate code investigation for this ticket, track the fix on RCS-28766 and link back here once it ships.
```

Que se espera ver. El comentario queda visible en el historial interno del ticket, sin que el cliente lo vea.

Si falla. No aplica, es texto pegado, no una accion del sistema.

## Paso 6. No comuniques fecha de fix al cliente todavia

Donde se ejecuta. Jira, respuesta visible al cliente en RCS-28795.

El comando o la accion. Espera a que RCS-28766 transicione de Under Engineering Review a Under Support Review antes de prometer una fecha o un fix a Meagan McIntyre. Si Juan quiere responder ahora, usa cerebro-respuesta-cliente para el texto, comunicando que el equipo esta investigando, sin mencionar PR 56138 ni el nombre interno del defecto.

Que se espera ver. El cliente recibe estado de investigacion activa, sin compromiso de fecha.

Si falla. Si Enrique Jimenez ya prometio algo distinto, alinealo con este hallazgo antes de que el cliente reciba mensajes contradictorios.

## Transicion sugerida del ticket

RCS-28795 se queda en Work in progress hasta que el paso 4 y el paso 5 esten hechos. No lo muevas a Under Engineering Review por separado, ya existe ese seguimiento en RCS-28766.

## Comentario para pegar, resumen corto en espanol para Juan

El comentario del paso 5 ya esta listo para copiar y pegar completo, en ingles, sin edicion adicional.

Instructivo para cerrar RCS-28779. Ejecuta en orden.

Paso 1. Confirmar que no hay novedades desde la última lectura, antes de pegar nada.
Donde se ejecuta: Jira, lectura.
Que revisar: que el ticket siga en Work in progress, asignado a Vedant Shirude, y que no haya comentario nuevo posterior a las 07:43:09 EDT del 2026-09-04.
Que se espera ver: el mismo estado que reporta este instructivo. Si cambió, no pegues el comentario de abajo sin releer el ticket.
Si falla: si Vedant ya dejó un comentario con la causa, revisa que no contradiga el texto de abajo antes de pegarlo.

Paso 2. Pegar el comentario de cierre en el ticket. Escritura, autoriza Juan.
Donde se ejecuta: Jira, comentario en RCS-28779, visible para la cliente.

```
Hi Ericka,

Glad to hear EBR Secure is signing in for you now.

The sign in failures traced to an issue with a backend service that our authentication flow depends on. Our team restored it and access is back to normal.

I need nothing further from you on this one.

I am closing this ticket. Please open a new one if the issue comes back.

Best,
Appriss Retail Support
```

Que se espera ver: el comentario publicado y visible para la reportera.
Si falla: si Jira rechaza el comentario por permisos, revisa que el proyecto siga en modo comentario público habilitado para este issue type.

Paso 3. Transicionar el ticket a Completed.
Donde se ejecuta: Jira, transición de RCS-28779. Escritura, autoriza Juan.
Que hacer: ejecutar la transición "Resolve", id 111, que mueve el ticket a estado Completed.
Que se espera ver: status del ticket en Completed.
Si falla: si la transición pide un campo de resolución obligatorio, usa Resolution = Done o el equivalente que exponga la pantalla.

Paso 4. Guardar el hallazgo en Cerebro para que quede buscable.
Donde se ejecuta: terminal, `bin/guardar`. Escritura sobre la base de conocimiento, autoriza Juan.
Que hacer: correr los siguientes dos comandos, en orden.

```
bin/guardar --carpetas
cat inbox/2026-09-04-rcs-28779-informe.md | bin/guardar 16 "RCS-28779 THD Key Vault throttling en legacysecure SAML2"
```

Que se espera ver: confirmación de que el fragmento se indexó en la carpeta 16, RCS Soluciones.
Si falla: si `bin/guardar` reporta un error de escritura, revisa que Moscú no esté con el índice corrupto antes de reintentar, ver `cola/INFORME-recuperacion.md`.

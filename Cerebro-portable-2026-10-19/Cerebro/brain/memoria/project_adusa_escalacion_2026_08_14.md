---
name: project_adusa_escalacion_2026_08_14
description: "La escalación ejecutiva de Ahold Delhaize del 14 ago 2026: quién la convocó, qué se comprometió, y qué quedó mal dicho"
metadata: 
  node_type: memory
  type: project
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-14T19:28:51.225Z
---

Viernes 14 ago 2026, 13:55, 54 minutos. La convocó **el cliente**, no Appriss. Título del invite: "Discuss plan for resolving the ongoing Ahold Delhaize USA Incident System (LPMS) Outages". Organizó James Cosseboom.

**Del lado Ahold:** James Cosseboom, **Tom Blackburn (VP de IT de funciones corporativas)**, Leigh Ann Stubbs, Kara Holthaus, Carl Goldstein, April Valerio, Dane Hilton, Brandy McCabe.
**Del lado Appriss:** Matt Kamminga, Camila Cortes, Juan Martinez.

**Tom pidió rollback y se le dijo que no se puede porque ya están migrados.** Su respuesta textual: no lo saca de la mesa *"because you haven't adequately described to me why it's not an option"*. Y agregó que van a revisar el contrato. Eso no es una queja de soporte, es una posición contractual.

**El riesgo que plantearon es legal, no técnico.** Tienen ~130.000 casos cargados y la preocupación es no poder sacar los datos. Eso convierte el fallo de export de Izenda en un tema regulatorio.

**Tom rechazó la hoja de cálculo de Camila como update ejecutivo:** *"that's not an executive update"*. Quiere hechos, qué se hace, cuándo, y los temas abiertos, para pasárselo a los brand presidents y al CTO de ellos.

**Compromisos dados:**
- Confirmar **el mismo día** si los dos tickets nuevos (RCS-28378 y RCS-28379) son de la unificación.
- Recap por correo con el estado de los 16 tickets.
- **Avisar por correo a Leigh Ann y a Tom cada vez que algo se libere**, no solo en el ticket. Pedido explícito porque ella no vive en la aplicación.
- Cambiar el formato del update ejecutivo.
- Cuatro tickets liberados la semana que viene, **sin fecha puntual comprometida** y sin desplegar en fin de semana.
- Check-ins de 15 minutos dos veces por semana, martes y jueves, con el CTO de Appriss y J.R. Teagle invitados.

**El conteo que se le dio:** 16 tickets, 6 esperando confirmación del cliente, 4 en pruebas para la semana que viene, 6 en revisión.

**Riesgo de ese conteo:** de los ENG de ADUSA verificados ese mismo día, **ENG-7192, ENG-7268, ENG-7180 y ENG-7270 están en Backlog**. ENG-5649 en Ready for Development. El único que avanzó es ENG-6974, en Ready for Code Review. "Cuatro en pruebas" no se sostiene contra Jira y va a llegar al CTO del cliente.

**El giro del final:** Leigh Ann recibió **dos 502 en vivo durante la llamada** y la expulsaron del sistema. Tom preguntó si tiene sentido atacar tickets pequeños si la gente no puede ni entrar. Matt respondió que timeouts y errores de servidor son **prioridad uno** desde ese momento. Mientras eso siga, los seis tickets que esperan validación del cliente no se pueden confirmar.

**Dos cosas que quedaron mal dichas y hay que corregir internamente:**

1. **Se le atribuyó el problema al cliente.** Camila dijo que la información está y que no se muestra *"because the filters that you are applying"*. No se sostiene: en el visor el rango se revierte solo y los datos devueltos son independientes de lo que muestra la pantalla, y en los reportes programados el usuario no aplica ningún filtro.
2. **Se le pidió a Leigh Ann grabar una sesión con F12** para el 502 y su equipo no se lo permite. No hace falta: App Insights ya trae URL, código y duración. Alcanza con fecha, hora y zona horaria del incidente.

Ver [[project_adusa_ficha_y_tickets]], [[reference_izenda_adusa_dos_rutas]], [[reference_waf_cloudflare_bloqueos]].

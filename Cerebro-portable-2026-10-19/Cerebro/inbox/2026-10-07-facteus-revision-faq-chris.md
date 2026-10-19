Facteus, revisión del FAQ que armó Chris

Fecha 2026-10-07. Página: https://trebuco.atlassian.net/wiki/spaces/DS/pages/478282350598/Facteus+-+Support+FAQs. Contestó todo, incluido lo que pensábamos que seguía abierto.

El umbral de drop_ratio, resuelto. Chris dice que drop_ratio es solo informativo, no dispara nada. Lo que de verdad dispara la alerta es una ventana de 24 horas, revisando si llegó dato nuevo según _row_created en la tabla ARDM_Header. Ojo con un detalle menor, la página de Missing Clients habla de 26 horas y Chris ahora dice 24, no es grave pero vale la pena señalarlo como pregunta abierta, no como corrección, por si cambiaron el valor y no actualizaron la página vieja.

El artículo por tipo de alerta que pedía Shreyas, resuelto. Hay un documento central con todos los tipos de alerta y sus guías, cada una con sus pasos de triage, enlace https://trebuco.atlassian.net/wiki/x/A4AbUW8. La regla general que dio Chris, si se disparó la alerta hay que asumir que hay un problema real, y si una alerta genera puro ruido, se desactiva y se rediseña, eso también se escala a Data Engineering.

Nombrar o no al cliente, resuelto, y es una regla clara. Nunca mencionar nombres de clientes hablando con Facteus, los datos van ofuscados en ese feed. El único nombre que se menciona es el de Facteus mismo. Hay plantillas ya armadas en cada guía para esto.

Si la alerta se dispara cuando el problema es del cliente, resuelto. Sí se dispara. Si faltan varios clientes a la vez, se agrupan en un solo ticket en vez de uno por cliente. La responsabilidad ahí es notificar al cliente directamente, aparte de escalar a Data Engineering, eso no contradice la regla anterior, esa regla es sobre no nombrar clientes frente a Facteus, no sobre no contactar al cliente mismo.

Punto de contacto para escalar, canal, fin de semana y go-live, todo igual a lo que ya tenías, sin cambios frente a lo que te mandé antes.

Lo único que sigue sin resolver, son cosas nuestras, no de Chris

Levantar el ticket de helpdesk para crear el Product Type de Facteus en Jira, sigue sin hacerse, y sigue sin estar claro si lo hace Camila o Support directamente.

Decidir si Support ya está listo para aprobar que Facteus escriba directo al support desk, eso prende el go-live de External Alerts y depende solo de ustedes.

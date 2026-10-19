# Por qué el agente dudaba de los accesos de Juan, 16 octubre 2026

Síntoma: en la sesión de Wegmans C171 el agente escribió "acceso sin verificar" sobre SQL de producción y WISC. Juan tiene ambos desde julio.

Causa, confirmada
1. La regla "verifica antes de instruir" que se agregó el 15 oct en AGENTS.md, en la regla 10 de las instrucciones del proyecto y en cerebro-ticket y cerebro-comentario decía "lo no verificado va como pregunta" sin decir dónde están los accesos ya verificados. El agente la aplicó a los accesos.
2. Los accesos vivían solo en brain/memoria/project_juan_accesos.md. Una búsqueda por tema, "duplicados WISC Wegmans", nunca trae ese archivo. Medido el 16 oct: la consulta de Wegmans devuelve 8 resultados sin ningún archivo de accesos; "como accede Juan a SQL" lo devuelve primero.

Arreglo
1. AGENTS.md: sección Accesos de Juan, verificados, con límites reales, y la regla 3 de borradores reescrita: se verifica el dato, no el acceso.
2. CLAUDE.md: tres líneas de accesos arriba.
3. bin/cerebro_mcp.py: contexto_ticket siempre trae accesos_juan; buscar_conocimiento lo agrega cuando la consulta nombra SQL, consulta, WISC, Control Panel, Snowflake, Azure, APIS, permiso o login. test_cerebro_mcp.py lo comprueba y pasa.
4. Instrucciones del proyecto v2: inbox/2026-10-16-instrucciones-proyecto-v2.md.
5. Propuestas de skill: cerebro-ticket y cerebro-comentario.

Respaldos en .cerebro/*.antes-20261016.

# RCS-29465 respuesta de Enrique por Teams, 16 oct 2026, 6:08 PM Bogota

Texto que Juan pegó, sin cambios.

es un problema algo complejo. El problema en si no fue la referencia, sino que la consulta que se genera apunta a columnas que no existen en snowtime (tienen nombres un poco distintos). Luego de ver con Claude se llegó a la conclusion que lo mejor era hacer unos cambios en los arpfiles. Eso arregla el mapeo de las columnas y de paso varios problemas relacionados a eso

Al principio Claude sugeria mejor hacer cambios en otro lado. Pero luego de ver que hay muchas busquedas que dependen de campos como esos se decidió que lo mejor era hacer el cambio en los arpfiles

para probar yo hice manualmente el cambio de la referencia. En una copia de la busqueda obvio. Y solucioné el problema de la referencia, pero al correrla salia ese problema que te digo de los campos que no existen en las tablas de snowflake

a proposito ya pude probé en staging uno de los cambios que hice. Sabes con quien tengo que hablar para que lo aprueben?

## Verificado para responderle
- Confluence ARPDT, Azure DevOps Permissions, pagina 475770847254, modificada el 9 may 2025. Approval Lead Delivery aprueba PRs de ArpFiles y despliegues de ArpFile. Miembros de ejemplo, no exhaustivos: Carl, Simon, Ola, Tomasz. Approval All Delivery cubre releases solo de Arp.
- ENG-10078, Jira del 16 oct: Backlog, reportero y asignado Enrique Jimenez, un comentario con el link al PR 59321, enlazado como causa de RCS-29363.
- Analisis del PR pegado por Juan: falta aprobacion de Delivery, cajas de pruebas locales EUDev y USDev vacias, despliegue 839517 Canceled en US Staging.

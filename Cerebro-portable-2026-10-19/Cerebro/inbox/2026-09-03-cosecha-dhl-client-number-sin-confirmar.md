---
fecha: 2026-09-03
fuente: cosecha de sesion local, Cliente number lookup
sesion: local_6137e830-b3db-4d7c-9c70-5fd725feea4e
---

# DHL Global Mail, sin numero de cliente confirmado en ninguna fuente interna

Se revisaron Cerebro, Confluence y Jira. Ninguno trae un client ID confirmado para DHL Global Mail.

Tres perfiles distintos en Confluence marcan el client ID explicitamente como "to-confirm". Un
documento usa el formato "DHL (`dhl`)" para el slug, sin confirmarlo por URL como si se hace con
Advance Auto Parts, client 15778, o Ralph Lauren, client 110794.

La fuente autoritativa para este dato es el tracker `Incident Migration 2026.xlsx`, que vive fuera
de la carpeta Cerebro conectada. El paso para resolverlo es buscar DHL directo en Control Panel por
nombre y cruzarlo contra ese tracker.

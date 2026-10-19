# Flujo nuevo: verificar SecurityID post migracion

Guardado el 28 sep 2026 desde RCS-29147, Prada.

Kiran Vadday entrego en ENG-7189, el 13 ago 2026, un SELECT que compara incident.LPUser2.SecurityID contra membership.Users.SecurityID y marca OK o MISMATCH por usuario. El adjunto SecurityIDMismatchCheckandFix.txt trae ademas el UPDATE de correccion. Es la herramienta para cualquier ticket de SecurityLevel NULL, permisos que cambiaron con la migracion o Session Error al entrar a Incident.

La columna que se compara es SecurityID. SecurityLevel es el nombre legible y vive en incident.LPSecurity. En RCS-28061, Stater Bros, 595 de 596 usuarios tenian SecurityLevel NULL, asi que ese dato solo no discrimina.

Procedimiento completo y query verbatim: flujos/verificar-securityid-post-migracion.md. Entrada en flujos/INDICE.md.

Contactos: Kiran Vadday, duena de ENG-7189 y ENG-7000. Shandana Khan, triage Secure e Incident.

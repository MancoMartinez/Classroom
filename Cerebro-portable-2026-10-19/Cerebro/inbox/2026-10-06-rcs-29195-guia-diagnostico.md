# RCS-29195 guia de diagnostico con Diego, 6 oct

Pagina con consultas que se rellenan solas: https://claude.ai/artifact/BBM1tHcL8FmHfXLuu8hZw4

## Que pasa
Holly, 6 oct 9:50 AM ET: el correo no llego y la Smart Alert History de 26-288-15 esta en blanco. No hay fila en SmartAlertProcess. Tenant 387 gwmek sin confirmar contra gimi.org.

## Causa
Sin determinar. Tres caminos: la alerta no carga en el paso 4, el filtro 6a da 0, o la corrida se cuelga antes del 14.

## Orden
0 tenant en Contacts. 1 caso y ShopliftingID. 2 alerta y Build Filters. 3 base: 3.2 caso como lo lee el motor, 3.3 SmartAlertProcess, 3.4 consulta del paso 4 del motor para el tipo de caso, 3.5 runQuery contra el caso, 3.6 CRLF. 4 Grafana por ID y 6a. 5 reset y disparo solo si esta colgado. 6 SendGrid si hay 13b. 7 cierre.

## Nuevo frente a la guia del 30 sep
3.4 replica el paso 4 del motor con el tipo de caso y muestra StatusID, BeginDate y AlertGroup.
3.5 corre el runQuery y quita condiciones hasta encontrar la que excluye.
Una fila previa en SmartAlertProcess hace que el re disparo salte la alerta, leccion de RCS-29026 caso 1353-15.
SendGrid 7 dias: el guardado original puede estar fuera de la ventana.

## Compromisos
Diego responde a Holly despues de clasificar. Sin ETA.

## Respuesta de Kiran Vadday, 6 oct 9:43 a 9:48 Bogota
Options: comparar con un tenant que funcione. StoreIdent: asignarse una tienda. Usar su hoja de URLs de Incident. Solo los clientes Complete estan en modo PU. Revisar los tickets de smart alerts de Matt K por si se relacionan.
Lectura: 387 gwmek da 500 en Secure Incident y Executive Workbench vacio. Si Goodwill no esta Complete, el caso vive en legacy, apps.lpguys.net/<slug>/nettrack, base pd-lpms-uswest2-sqldb-001. Logs y ruta de disparo legacy por confirmar con Kiran.
Matt: ENG-9013 Vitamin Shoppe, ruta movil sin rama PU, Ready for Development. ENG-9152 Vallarta, intermitente, Backlog. ENG-7359 Quick Entry, Done 24 sep. Preguntar a Holly como se creo 26-288-15.

## Hoja Incident Migration 2026, 6 oct
Ningun Goodwill esta Complete. 379 a 390 siguen en apps.lpguys.net. 387 gwmek: DB Only, solo Run Lunar hecho, plan 8/17 sin prod. 380 goodwillcfl y 382 goodwillsacto: Date Planned 08/10, prod data migrated Yes, sin Prod Complete.
El caso vive en legacy: abrir en apps.lpguys.net/<slug>/nettrack, base en pd-lpms-uswest2-sqldb-001.database.windows.net, logs en Control Panel Support Incident Logs. Re disparo legacy por confirmar con Kiran.
Tenant de Holly sin confirmar: la hoja no trae dominios. Buscar gimi.org en Contacts de cada Goodwill.

## Teams a Kiran Vadday
Thanks Kiran Vadday. Per the sheet none of the Goodwill tenants are Complete, and 387 gwmek is DB Only, so https://trebuco.atlassian.net/browse/RCS-29195 is still on apps.lpguys.net. If I find a stuck case there, is ProcessCaseAlert.aspx under apps.lpguys.net/<slug>/nettrack the right way to re-trigger it?

## Donde viven los Goodwill legacy
URL directa: https://apps.lpguys.net/<slug>/nettrack/index.aspx, columna Current URL Incident de la hoja.
Servidor: Confluence AALPS Customer Server Profile 474658570288, Ryan Barlow, 10 jul. gwmek y gwmanasota node-l pd-lpms-iis-014, sin asterisco, base lpguys. goodwillsacto node-g con asterisco, base Platform. goodwillscw y gwnne node-f, goodwillcc nj sew node-h, goodwillcfl y sc node-k. gwmemphis y gwminnesota no aparecen.

## Login en tenants legacy con SSO
gwmanasota 386 tiene SSO = X en la hoja: index.aspx manda al login corporativo del cliente. En 1Password no hay Supervisor de Manasota.
Entrada de empleados Appriss, Confluence AALPS 474699628589 Setup Appriss SAML: https://apps.lpguys.net/<slug>/nettrack/index.aspx?APSAML=1, Next, credenciales trebu. Solo funciona si el tenant tiene ApprissSAML=1.
Si falla: pedir acceso a Kiran Vadday o Ryan Barlow.
Kiran Vadday, 6 oct: para tenants legacy con SSO usar ?nosaml=1. https://apps.lpguys.net/gwmanasota/nettrack/index.aspx?nosaml=1 muestra el login de usuario y clave. Credencial: buscar Manasota o GMA en 1Password, vault LPMS - Tenant Databases.

## Confirmado 6 oct 10:37
Caso 26-288-15 en 386 gwmanasota. ShopliftingID 23818, MasterCaseID 23451, StoreIdent 571, Blake Maute.
https://apps.lpguys.net/gwmanasota/nettrack/LPMS/LPMSEditMenu.aspx?MasterCaseID=23451&ShopliftingID=23818&SuspectID=23818&StoreIdent=571
Alerta Property Damage: Active, STANDARD, BeginDate 1/26/2022, Email Manager 1 Yes, plantilla Property Damage Incident Report.docx, Case Types Property Damage, GIM Property Damage, Fire, Arson, Donor Property Damage, Donor Vehicle Damage, Vehicle Damage. Configuracion pasa. Pendiente Build Filters, tipo del caso, logs.

## Causa confirmada 6 oct 11:00
Base legacy GWManasota, dbo. 23818: CaseType Property Damage, InProcess 0, sin filas en SmartAlertProcess, Suspect OK, Store OK, Region GIMI, CreatedDate 2026-09-29 18:19.
Alerta 111 Property Damage: StatusID 1, Standard, sin envio previo. runQuery exige CASETYPE = PROPERTY DAMAGE y ReportNarrative no vacio. LEN(ReportNarrative) = NULL. runQuery con 23818 devuelve 0 filas.
Tenant envia hoy: SmartAlertProcess con Success 5 y 6 oct, gimi.org y gipb.org.
Causa: configuracion, filtro exige narrativa y el caso no la tiene. No es defecto. Respuesta a Holly: 2026-10-06-rcs-29195-respuesta-holly.md
Leccion: tenant legacy no loguea en Grafana; diagnostico completo por SQL en la base legacy.

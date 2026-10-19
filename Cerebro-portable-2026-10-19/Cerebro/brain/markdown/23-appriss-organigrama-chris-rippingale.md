# Appriss — Organigrama (Chris Rippingale)

Carpeta 23 de la base de Moscú. 4 fragmentos.

## Equipo Support Appriss — roster real (Teams, 3 ago 2026)
_chunk 1442 · 2026-08-03 · fuente: teams://SupportAppriss/Miembros_

Fuente: pestaña Miembros del equipo "Support Appriss" en Teams, capturada el 3 de agosto de 2026. Esta es la unica fuente valida para decidir asignacion de tickets RCS. No deducir el equipo de quien aparece como asignatario en Jira, eso trae gente de otros equipos y ya causo un analisis de reparto completamente equivocado.

PROPIETARIO DEL EQUIPO
Camila Cortes, Support Manager (contractor). Hace seguimiento y comunicacion con clientes, no es asignataria tecnica.

MIEMBROS (11)
Juan Martinez, Lead Support Engineer. Colombia. Es el usuario.
Viraj Kansara, Lead Data Engineer (contractor). India. Es el otro lead, par de Juan, no su subordinado.
Diego Buelvas, Full Stack Engineer (contractor). Colombia.
Sebastian Rueda, Senior Data Engineer (contractor). Colombia.
Edwin Garzon, Data Engineer (contractor). Colombia.
Luis Hernandez, Senior Full Stack Engineer. Colombia.
David Vargas, Full Stack Engineer (contractor). Colombia.
Nikita Rathore, Full Stack Engineer (contractor). India.
Vedant Shirude, Senior Full Stack Engineer. India.
Bikash Kumar, Data Engineer (contractor). India.
Gulshan Kumar, DevOps / SRE (contractor). India.

DESAMBIGUACIONES QUE YA CAUSARON ERRORES
"Sebastian" en los mensajes de Peyman Motlagh es Sebastian Rueda.
"David" del equipo es David Vargas. David Beck y David Parraga NO son del equipo.
Charly Correa, Camilo Baquero, David Parraga y Andres Esteban NO son del equipo, aunque tengan tickets RCS asignados.

YA SALIERON DE LA EMPRESA
Tyrone Whitney. Sus cuatro tickets (RCS-28058, 28062, 28063, 28065) pasaron a Vedant Shirude.
Carlos Jacinto. Cuenta de Jira desactivada y todavia con tickets abiertos a su nombre, entre ellos RCS-27549 (ICA SE, High, abierto desde el 25 de junio con peticion formal de RCA).

CANDIDATOS DE COLOMBIA para llamadas y tickets que necesiten horario americano: Diego Buelvas, Sebastian Rueda, Edwin Garzon, Luis Hernandez, David Vargas.

## Carga de tickets del equipo Support Appriss al 3 ago 2026 y reglas para repartir
_chunk 1447 · 2026-08-03 · fuente: Jira, informe de carga 2026-08-03_

Carga de tickets abiertos del equipo Support Appriss al 3 de agosto de 2026, verificada en Jira. Total del subconjunto consultado: 26 tickets entre Sebastian Rueda, David Vargas, Gulshan Kumar y Luis Hernandez, mas los ya conocidos.

RANKING COMPLETO
Vedant Shirude 21. El mas cargado, recibio los cuatro de Tyrone Whitney.
Juan Martinez 14.
Sebastian Rueda 13. 1 Critical (RCS-28106 Santikos SmartAlerts) y 1 High (RCS-28077 Ahold Refund Searches Broken). Ademas RCS-26088 con 137 dias y RCS-26632 con 101 dias, los dos de duplicacion de datos.
Bikash Kumar 10.
Nikita Rathore 9.
Edwin Garzon 9.
David Vargas 8, pero SEIS estan en Under Customer Review, o sea carga activa real de 2.
Diego Buelvas 7, con tres High.
Gulshan Kumar 5, cuatro de ellos en Work in progress.
Luis Hernandez 0.

REGLAS QUE SALIERON DE ESTO
Los numeros crudos enganan. Hay que separar los que estan en Under Customer Review, porque esperar al cliente no es trabajar. La carga activa es la que importa para repartir.
El problema de antiguedad del equipo no esta en la cola sin asignar. El ticket sin asignar mas viejo tenia 82 dias. Sebastian tenia dos de 137 y 101 dias ya asignados. Los tickets realmente viejos tienen dueno y nadie los mira.
Orden correcto para repartir: primero el roster real de Teams, despues las cargas verificadas en Jira, despues el perfil tecnico. Saltarse cualquiera de los tres produce un reparto malo.

CLUSTER DE DUPLICACION EN SEBASTIAN RUEDA
Tiene cuatro tickets de duplicacion de datos: RCS-27910 (Alshaya SHR Report duplicate lines), RCS-27927 (033 hft data duplication, 13 dias), RCS-27344 (049 GAP duplication, 55 dias), RCS-26632 (171 WEG duplication, 101 dias). Es el dominio de conocimiento del equipo en duplicacion, pero sin capacidad. Los tickets sin asignar de duplicacion de filas en busquedas de Secure 5 (RCS-28026 de TJX EU y RCS-28049 de Smyths) deben linkearse a su RCS-27910 pero trabajarse por otra persona.

DUPLICADO PROBABLE
RCS-28117 (Alshaya, error correct count and amount incorrect, sin asignar) contra RCS-27951 (Alshaya, Error Correct Count not captured, de Sebastian). Mismo cliente, mismo sintoma. Linkear y cerrar uno.

CRUCE CRITICO
RCS-28106 (Santikos SmartAlerts Not working, Critical, Sebastian) toca el mismo endpoint que la degradacion de RCS-28112 de Stater Bros: 248 de los 255 errores HTTP 500 del app service de nettrack estaban en POST /nettrack/api/internal/SendSmartAlert.aspx durante la ventana del 31 de julio 20:30 a 22:35 UTC.

## Organigrama Appriss — estructura general + conexión con color teams
_chunk 1130 · 2026-07-09 · fuente: org chart Appriss jul-2026_

Fuente: org chart oficial de Appriss (jul-2026), de Chris Rippingale hacia abajo (lo que compete a nuaav). Chris Rippingale = SVP Engineering (310 Engineering), 10 reportes directos, 121 personas en total. NOTA: "Chris Rippingale" es el mismo "Christopher Ripp" a quien se envía la guía de onboarding moscu-ops.

TRES DEPARTAMENTOS (por código de badge):
- 310 Engineering (el core de Chris): ingeniería de producto, data, QA, DB, Engage.
- 312 Infrastructure: bajo Peter Tuttle (VP Infrastructure and Cloud).
- 421 Customer Support: bajo J.R. Teagle (VP Global Support). AQUÍ está nuaav: el equipo de camila cortes, donde trabaja Juan Martinez (Lead Support Engineer, contractor).

REPORTES DIRECTOS DE CHRIS (10): Peter Tuttle (312, VP Infra), J.R. Teagle (421, VP Global Support), Marc Lequime (310 contractor), Shandana Khan (Project Manager/Scrum Leader), Daniel Endersby (Enterprise Architect, 13), Nick Hawkins (Principal SWE, 2), Jon Morgan (Platform Services Manager, 8/10), Matt Kamminga (Director of Engineering, 10/11), Gina Pilato (QA Manager, 7), Kenny Vu (VP Engineering Engage, 3/6).

CONEXIÓN CON LOS COLOR TEAMS (scrum teams que cruzan a los managers, fuente: intake de Camila + all-hands 2026-06-17):
- Purple = Peter Tuttle (312) — Cloud & Infra: Azure, Terraform, on-prem.
- Green = Nick Hawkins (310) — Apps: Platform UI, C#, ASP.NET, React.
- Cyan = Matt Kamminga (310) — Incident & Audit: Legacy, LPMS/CAMS, APIS/AALPS. (Matt también es Director of Engineering y dueño del feed runbook APIS.)
- Yellow = Kenny Vu (310) — Engage API.
- Blue = Jon Morgan (310) — Platform & Database Services: Snowflake/Greenplum, .NET services.
- QA = Gina Pilato (310) — Testing, Go/No-Go de deploys.
NOTA de reconciliación: el deck del all-hands (chunk 921) etiquetaba a Matt Kamminga como "Green"; el intake dedicado de color teams (chunk 995) lo ubica en Cyan (Incident/Audit) y a Nick Hawkins en Green (Apps). Se usa este último como autoritativo. Ver [[Color Teams QA — Estructura de equipos de ingeniería]] y el chunk 921 (Org de Ingeniería, equipos por color y canales de Teams).

Escalación por tipo de ticket → color team: Infra/Azure→Purple; UI/React/C#→Green; Engage API→Yellow; LPMS/Secure Incident/Audit/Legacy/APIS→Cyan; DB/Snowflake/.NET→Blue; Testing/deploys→QA.

## Roster completo por departamento (org chart jul-2026)
_chunk 1131 · 2026-07-09 · fuente: org chart Appriss jul-2026_

312 INFRASTRUCTURE — Peter Tuttle (VP Infrastructure and Cloud, Purple Team, 16 total). Directos: Austin Flannery (Systems Engineer), Trey Hughes (Infra & Cloud Engineer), Michael Tasch (Infra & Cloud Engineer, 6) y Jose Parocua Andrade (Cloud Engineering Manager, 6).
- Bajo Michael Tasch: Lafayette Cope (Cloud Eng), Jesus Veira (DevOps, contractor), Giovanni Contreras (Infra & Cloud Eng), Russell Harmon (Sr Infra & Cloud), Juan Restrepo (DevOps, contractor), Diego Garcia (Lead DevOps, contractor).
- Bajo Jose Parocua Andrade: Marcin Czop (Lead Infra & Cloud), Jessey Clarke (Sr Infra & Cloud), Aleksandrs Saveljevs (Sr Infra & Cloud), Natalia Alzate (Sr DevOps, contractor), Aleksander Pawlak (Infra & Cloud), Rajesh Kancharla (DevOps, contractor).

421 CUSTOMER SUPPORT — J.R. Teagle (VP Global Support, 46 total, 9 directos): Peyman Motlagh (Support Data Engineer Manager, 3), Aimee Wadsworth (Customer Support Manager, 8, SALIENTE), Luke Du (Staff Data Engineer), Santhosh Bhat (Contractor L1 lead, 15 = equipo L1 UnifyCX/ex-Glowtouch), Mohammad Sheikh (Sr Support Engineer), Vlad Bogus (Monitoring Engineer, contractor), Matthew Everett (Sr Support Engineer), Carlos Jacinto (Support Engineer, contractor), camila cortes (Support Manager, contractor, 11 = equipo nuaav).
- Bajo Peyman Motlagh (Support Data Team): Chenuka Ratwatte, Smeet Kathiria, David Beck (Support Data Engineers).
- Bajo Aimee Wadsworth: Tyrone Whitney (Support Eng), Kristin Krogman (Sr Business Process Analyst, SALIENTE), Andrea Viveros (Sr Support Analyst, 2 → Kyle Nguyen + Nads Espinosa, Support Analysts), Dean Korbakis (Lead Support Eng), Carrie Allison (Sr Support Eng), BJ Probert (Support Eng).
- Bajo Santhosh Bhat (L1, todos contractors): Vismaya Thottada, Shireesh Ramdas, Rajith Y Suvarna, Neha Haridas, Manisha Naik, Madhuraj Gujaran, Sanath Acharya, Akshaya Purappemane, Anil Kumar P, Ganesh Nayak, Shreyas U, Muralidhara Poojari, Ayesha Mehar, Deekshitha Seetharama (+1).
- Bajo camila cortes (nuaav, todos contractors): Anubhav Jha (Full Stack), Vedant Shirude (Sr Full Stack), Sebastian Rueda (Sr Data), Nikita Rathore (Full Stack), Diego Buelvas (Full Stack), JUAN MARTINEZ (Lead Support Engineer), Bikash Kumar (Data), David Vargas (Full Stack), Viraj Kansara (Lead Data), Gulshan Kumar (DevOps/SRE) (+1).

310 ENGINEERING — Chris Rippingale directo:
- Marc Lequime (contractor). Shandana Khan (Project Manager/Scrum Leader, hace routing RCS de Incident/Secure).
- Daniel Endersby (Enterprise Architect, 13, Data Eng + SnowTime/Cloud): Andres Marciales, Anushka Chaudhary (Jr), Saurabh Singh (Lead DevOps), Anshul Choudhary (Sr Data), Shuchi Wason (Lead Program Delivery), Nitish Raj (Sr Data), Adarsh Kumar (Eng Manager), Andres Guacheta (Sr Data), Kapil Gulati, Camilo Baquero (Lead Data), Sumeet Jain (Sr Data), Laura Merchan (+1) — todos contractors.
- Nick Hawkins (Principal SWE, GREEN, 2): Jeremiasz Markiewicz (SWE), Dariusz Kostrzewa (Staff SWE).
- Jon Morgan (Platform Services Manager, BLUE, 10): Christopher Beck (Database Engineering Manager, 1 → Brandon Kays), Brad Nguyen (Sr DB Eng), Diego Gomez (DBA, contractor), Ben Pritchard (Software Engineering Manager, 1 → Chris Martin), Neil Abrahams (DB Eng), Mohammed Abdul-Mutah (SWE), Gabor Remenyi (Sr SWE), Santiago Forero (Sr Backend, contractor).
- Matt Kamminga (Director of Engineering, CYAN, 11): Juan Bonilla Alvarez (Full Stack, contractor), Eliott Robson (Sr SWE), Freddie Castelblanco (Lead Eng, contractor), Juan Ochoa (Lead Full Stack, contractor), Kiran Vadday (SWE), Matthew Gladden (SWE, 1), Thomas Walker (Sr SWE), Jack Chen (SWE), Scott Buric (SWE), Carlos Sanchez (Eng, contractor).
- Gina Pilato (QA Manager, QA, 7): Alejandro Cueca (contractor), Hannah Song (QA Eng Lead), Irina Druskin, Dave Abril (contractor), Nicolas Garcia (contractor), Jason Robinson, Daniel Salazar (Lead QA, contractor).
- Kenny Vu (VP Engineering Engage, YELLOW, 6): Steven Er (Sr SWE), Phillip Sanders (Principal SWE), Ian Williams (Software Engineering Manager, 3 → Shruti Golwalkar, Kevin Woo (Staff), Joseph Mayrose). Ian maneja la cola de Engage Engineering Tickets.

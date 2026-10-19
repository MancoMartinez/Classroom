RCS-28256. Revision profunda, 14 oct 2026. Fuentes: RCS-26519, RCS-27269, RCS-27578, RCS-27941, RCS-28256 en Jira, bitacora/RCS-27941.md, brain/memoria (esquema usuarios Incident, lpuser/lpuser2/membership, sso diagnostico, 28256), inbox/2026-08-28-meet-kiran-handoff.md.

Patron que nadie junto
Este tenant ya perdio arreglos por despliegues tres veces. RCS-26519 (29 jun): "a fix PR merged to main that was overwritten by a release deploy". RCS-27578 (1 jul): Dean pidio capturar el cambio de sso.GetUserSecurityLevel en Release "so it is not overwritten on the next deploy"; el hotfix vivo es PR 54159 y el permanente 54149 estaba "tested locally only". RCS-28256 (10 ago): el release reseteo dos feature flags por faltar en seed history, y desde el 6 ago las consultas de LPUser pasaron de 0,5 s a 57 s.
Los casos de nivel en blanco volvieron despues de julio: Chaz y Nancy 8 sep, Paul 28 sep, Chris 12 oct, Rachel 13 oct.

Hipotesis principal, sin verificar
Un despliegue posterior al 2 jul devolvio sso.GetUserSecurityLevel a leer solo Persistent = 1. El proc pisa membership.Users.SecurityID en cada login (ENG-7312). Si ignora la fila del feed, el usuario queda en NULL aunque el feed traiga nivel 5. Encaja con los seis: feed con 5, Persistent NULL, y los que tienen 5 en la cuenta lo tienen por arreglo manual (Chris por Colton el 12 oct).

Alternativa: los tres no han entrado desde que su fila llego. LastLoginDate lo separa.

Chris Orth
Sin fila en LHUA es la clase 2 del esquema de Kiran: entra pero no puede escoger tienda al crear caso. Soporte lo arregla desde Control Panel, pestana Hierarchies, Standard Location Hierarchy, nivel Location, con el LocationID (precedente RCS-28177, Jie Chen). Antes hay que saber si 90002005 existe en place.Location.

Otro dato
Los seis no tienen fila en incident.LPUser2. En ADUSA eso impedia buscar y ser dueno de caso. En TBI hay 267 asi y la mayoria no reclama. No discrimina, queda anotado.

Consultas: inbox/2026-10-14-rcs-28256-revision-profunda.sql

RESULTADOS 14 oct
1. sso.GetUserSecurityLevel hoy NO filtra Persistent = 1 (ORDER BY Persistent DESC, version arreglada). create 2026-04-16, modify 2026-10-09 09:11. Alguien lo redesplego el 9 oct; la definicion anterior no se ve desde la base.
2. El proc devuelve 5 para Paul, Nancy y Rachel.
3. LastLoginDate UTC: Vincent 08-28, Nancy 09-06, Chaz 09-08, Paul 09-26, Chris 10-12 19:50, Rachel 10-13 19:23.
   Rachel entro despues de la carga del 13 oct y despues del redespliegue del 9 oct, con el proc devolviendo 5, y su cuenta quedo en NULL. Descarta timing y descarta el proc como unica causa para ella. Algo en el login no aplica el nivel.
   Chris entro 12 oct 19:50 UTC (3:50 PM ET), despues de que Colton le puso Location Manager (3:35 PM ET) y sigue sin poder: su bloqueo es la jerarquia.
4. Usuarios con nivel en feed y cuenta en NULL, por mes de ultimo login: jul 6/38, ago 24/65, sep 16/85 (18 antes del arreglo manual de hoy), oct 1/41 (2 antes de hoy). 47 despues del 2 jul. Cota superior: no se sabe si su fila de feed existia en su ultimo login.
5. Ultima carga del feed 2026-10-13 10:42:27 en las dos tablas. La del 14 oct no aparece.
6. LocationID 90002005 NO existe en place.Location. 40001405 si (#1405 MONROE, LA). CAUSA de Chris: el feed le manda una ubicacion que no existe en el maestro, no se crea fila en LHUA, no puede escoger tienda. Accion: pedir a Colton la tienda correcta y asignarla desde Control Panel, pestana Hierarchies.

RESULTADOS 2, 14 oct
A. 47 filas, 46 usuarios (christi.winters dos filas: Persistent NULL y Persistent 1, ambas nivel 5) con nivel en feed y cuenta NULL, ultimo login entre 3 jul y 7 oct. Casi todos tiendas (menswearhouse, kgstores, mooresclothing, josabank) nivel 5; kristen.brookens y edgar.lara nivel 8. Ninguno despues del redespliegue del proc del 9 oct salvo Rachel (ya corregida).
   Christi Winters tiene override manual Persistent 1 y aun asi NULL tras login del 14 jul: si esa fila es anterior al login, el login no aplica el nivel ni con override. Prueba pendiente.
B. 266 usuarios, todos @tailoredbrands.com, 32 LocationID 9000xxxx, ninguno existe en place.Location. Mayores: 90001099 (40), 90005075 (22), 90005013 (21), 90001091 (19), 90004001 (19), 90002005 (16, Chris Orth). ResponseLog muestra oficinas con locationType OFF y UniqueLocID tipo SSU1099: los 9000xxxx parecen oficinas o centros, fuera del maestro de tiendas. Cualquiera de ellos que use Incident queda como Chris.
   alexandra.crossley esta en A y en B.
C. sso.ResponseLog: Id, InsertedDateTime (UTC), ProviderID, Summary, Response (XML SAML). Claims: nombre, email, title, location, locationType, region, company, UniqueLocID, district, Group (grupo Okta). NO trae team ni nivel de Incident: el nivel solo puede venir del feed.
   ResponseLog marca 2026-10-14 18:57 UTC y el feed sigue en 2026-10-13 10:42: la carga del 14 oct no ha llegado.

RESULTADOS 3, 14 oct
Christi Winters: fila Persistent 1 nivel 5 insertada 2026-04-17 01:12 UTC (coincide con el INSERT de Kiran en RCS-26519, 16 abr 21:29 ET). Su login fue 14 jul 19:36 UTC, tres meses despues. Cualquier version del proc devolvia 5. Su cuenta quedo NULL. CONFIRMADO: el login no aplica el nivel aunque el proc lo devuelva. El defecto no esta en el feed ni en el proc.
Jennifer Alba Faust (tienda, StoreUsers, entro hoy 18:57 UTC) tiene 5. Rachel Dill (tienda, StoreUsers, mismas claims) quedo NULL tras entrar el 13 oct. Shak Feaster NULL tras 7 oct. Las claims SAML no separan a quien recibe nivel de quien no.
287 usuarios ApprissCase Users tienen en el feed una ubicacion que no existe en place.Location.
Hipotesis siguiente: el login solo aplica el nivel cuando hay fila en incident.LPUser2 (los seis afectados no la tienen). Prueba: cruce LPUser2 x nivel en cuenta.

RESULTADOS 4, 14 oct. Cruce LPUser2 (solo por IncidentUserID) x nivel en cuenta, usuarios con nivel en feed y login desde 2 jul:
con LPUser2 y con nivel 79. sin LPUser2 y con nivel 102. sin LPUser2 y cuenta NULL 46. Con LPUser2 y NULL: 0.
Los 46 NULL estan todos sin fila por IncidentUserID. Tener fila garantiza nivel; no tenerla no garantiza el fallo (102 tienen nivel, parte por arreglos manuales).
LIMITE: el cruce uso una sola ruta de join. Regla de Kiran (reference_esquema_usuarios_incident, project_membership_users_13): sacar las dos rutas, IncidentUserID y LoginID o email, porque la fila puede existir por email con el puntero vacio o roto. Falta repetir con las dos rutas y filtrando cuentas @trebu.co.

RESULTADOS 5 y CONCLUSION, 14 oct. Dos rutas, sin @trebu.co: por ID con nivel 79; ninguna con nivel 101; ninguna y cuenta NULL 46. Los 46 no existen en LPUser2 por ninguna ruta. No es puntero roto (clase 3 con fila por email); es la falta de fila, el mismo defecto de alta que Kiran describio en ADUSA y que en TBI ya sumaba 267 en agosto.
CONFIRMADO 1: el login no aplica el nivel a parte de los usuarios sin fila en LPUser2 (Christi y Rachel con el proc devolviendo 5). Con fila, 79 de 79 lo reciben. Que separa a los 101 sin fila con nivel no se sabe (parte por arreglo manual). Es de Ingenieria.
CONFIRMADO 2: 287 usuarios ApprissCase Users con LocationID 9000xxxx inexistente en place.Location, sin LHUA, no pueden escoger tienda. Chris Orth es uno.
CONFIRMADO 3: la carga del feed del 14 oct no llego (ultima 13 oct 10:42).
Borradores: inbox/2026-10-14-rcs-28256-respuesta-hilo-jr.md (v3) y inbox/2026-10-14-rcs-28256-teams-matt.md (v2).

14 oct 15:39 ET, Colton (comentario 3396106): la tienda correcta de Chris es 40002005, #2005 MW TUX DC, Bakersfield CA, TMW-CAL-CALB. SSO+ muestra 90002005, Level Store, Persistent False, inserted 10/13/2026 05:42:27 AM: es la carga del feed (10:42 UTC en base). Confirma que InsertedDateTime del feed esta en UTC, asi que la carga del 14 oct si falta.
Patron probable: 9000xxxx = 4000xxxx + 50000000 para usuarios de oficina o centro. Falta verificar con la consulta de equivalencias y saber si el 9 viene en el archivo del cliente o lo arma nuestra carga.

Equivalencias 9000xxxx vs 4000xxxx, 14 oct: los 32 LocationID 9000xxxx tienen su gemelo 4000xxxx en place.Location (restar 50000000). 266 usuarios en total. Son DCs, hubs, oficinas y corporativo (#1099 CORPORATE 40 usuarios, #5075 JOSEPH ABBOUD MFG 22, #5013 PDC TUX HUB 21, #4001 AURORA DC 19, #1091 RETAIL DC-BVDC 19, #2005 MW TUX DC 16). CONFIRMADO: no faltan ubicaciones en el maestro, el feed trae el prefijo 9 en lugar de 4. Sin saber si el 9 viene en el archivo del cliente o lo arma nuestra carga (claims SAML de corporativos traen company SSU). El 287 de antes incluye 21 usuarios fuera de este rango, sin revisar.
Chris: LHUA sigue NULL; se arma en el siguiente login despues de la entrada persistente 40002005.

# RCS-29195 guion de llamada con Diego. Caso 26-288-15, alerta de Property Damage

Estado en Jira al 1 oct: Under Customer Review. Ultimo comentario de Diego, 30 sep 1:48 PM ET, a Holly: "Could you confirm what user are you using to check those alerts?". Sin respuesta.
Sigue el orden del runbook de Confluence: alerta y filtro, base, logs, re disparo, cierre.

---

## 0. Abrir la llamada (1 minuto)

Di:
"Diego, vamos a hacer este caso con el runbook de Smart Alerts, en orden: primero la alerta y su filtro, luego la base, luego los logs. Solo re disparamos si los logs muestran que el caso esta atascado. Tu manejas la pantalla, yo voy leyendo."

Pregunta, sin corregir:
"Le preguntaste a Holly que usuario usa para revisar las alertas. Que estabas viendo? Puede que yo este leyendo mal el ticket."
Escucha. Si sospecha permisos o visibilidad, anotalo como hipotesis aparte. Lo que sigue no depende de la respuesta de Holly.

---

## 1. Tenant (2 minutos)

Di: "Abre Control Panel, Home, Customers in USPROD y busca good."
Espera ver: fila 387, goodwill.org, slug gwmek.
Di: "Entra a la ficha 387, mosaico Contacts. Busca a Holly Garcia o gimi.org."
Si aparece: seguimos con 387 y gwmek.
Si no aparece: "Busca gimi en el filtro de clientes." Usamos el ClientID y slug que salgan.

ANOTA: ClientID ____ Slug ____

---

## 2. Alerta y filtro (10 minutos)

2.1 Di: "Vuelve a Home y en la fila del cliente haz clic en el logo de Click logo to sign in."
2.2 Di: "Busca el caso 26-288-15 y abrelo. Copia el ShopliftingID de la URL."
ANOTA: ShopliftingID ____
2.3 Di: "Leeme del caso: tipo de incidente, estado Open o Closed, tienda, division, fecha de creacion, y si tiene narrativa."
ANOTA: tipo ____ estado ____ tienda ____ creado ____
2.4 Di: "Abre Smart Alert History en el workbench."
  Vacio: seguimos.
  Fila de Property Damage con Success: la alerta salio. Salta a 4 y despues a entrega.
2.5 Di: "Ahora Admin, Manage Smart Alerts. Cual alerta tiene Property Damage en Case Types?"
ANOTA: nombre de la alerta ____
2.6 Di: "Abrela y leeme, campo por campo:"
  Alert Status. Tiene que decir Active.
  BeginDate. Tiene que ser anterior a la fecha del caso.
  Special Alerts. Tiene que decir Standard.
  Case Types. Tiene que incluir Property Damage.
  Template Document. Tiene que tener uno seleccionado.
  Email Group. Direcciones validas.
Si algo falla: "Ahi esta la causa. Toma captura." Ve a 4 para confirmarlo en el log 6a y luego a 6.
2.7 Di: "Pasa a Build Filters y leeme cada condicion."
Por cada condicion pregunta: "El caso la cumple?"
Si una AND no se cumple: "Esa es la causa. Captura." Confirmar en 4, luego 6.
Pregunta: "Sabes si el cliente edito esta alerta hace poco?" Si si, el filtro real se confirma en 4 con la linea 6a.

---

## 3. Base de datos, solo SELECT (8 minutos)

Di: "Abre Bastion, SSMS, servidor sqlmi-prd-wus2-arp-001 con el login de lectura."

3.1 Di: "Corre esto para ubicar la base:"
SELECT name FROM sys.databases WHERE name LIKE '%-387-%';
Selecciona la base que sale.

3.2 Di: "Ahora el caso:"
SELECT s.ShopliftingID, m.CaseNo, s.InProcess FROM incident.MasterCase m JOIN incident.Shoplifting s ON s.MasterCaseID = m.MasterCaseID WHERE m.CaseNo LIKE '%26-288-15%';
Tiene que coincidir con el ShopliftingID de 2.2. ANOTA InProcess ____

3.3 Di: "Historial de la alerta para este caso y para el cliente:"
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = <ID> ORDER BY RunDate DESC;
SELECT TOP 20 * FROM incident.SmartAlertProcess ORDER BY RunDate DESC;
Lee: si hay filas de hoy de otras alertas, el cliente envia alertas y el problema es de este caso o esta alerta.

3.4 Di: "La alerta como la guarda el motor:"
SELECT AlertConfigID, CaseType FROM incident.SmartAlertCaseTypes WHERE CaseType LIKE '%Property Damage%' OR CaseType = 'Any';
SELECT ac.StatusID, ac.EmailTemplate, ac.EmailGroup, sac.* FROM incident.SmartAlertConfig sac JOIN incident.AlertConfig ac ON ac.AlertConfigID = sac.AlertConfigID WHERE sac.AlertConfigID IN (<ids>);
Compara con la pantalla de 2.6 y 2.7. Si difieren, el filtro guardado no es el de pantalla.

3.5 Di: "Por ultimo, direcciones con salto de linea:"
SELECT AlertConfigID, EmailGroup FROM incident.AlertConfig WHERE EmailGroup LIKE '%' + CHAR(13) + '%' OR EmailGroup LIKE '%' + CHAR(10) + '%';

Recuerda en voz alta: "InProcess en 1 solo no prueba nada. Lo decide el log."

---

## 4. Logs (8 minutos)

Di: "Abre apprissretail.grafana.net, Explore, datasource grafanacloud-apprissretail-logs, cambia a Code y pega:"
{service_name=~".+", deployment_environment="usprod"} | clientId="387" |= "<ID>"
Di: "Rango desde la fecha de creacion del caso hasta ahora. Run query y ordena por hora."
Di: "Busca la linea 6a con el nombre de la alerta. Que dice Rows Returned?"

Decide en la llamada:
  13b EMAIL SENT, 14 y End: salio. Toca revisar entrega. Paso 6.
  6a con Rows Returned=0: el filtro excluye el caso. Copia el SQL de 6a, busca la condicion. Paso 6. No se re dispara.
  Hay corrida y no aparece la alerta: no es elegible. Volver a 2.6. No se re dispara.
  Ninguna linea del ID: ampliar el rango.
  13a sin 13b ni End, y despues Quit: atascado. Paso 5.
  12b y nada despues: atascado buscando adjuntos. Paso 5, puede volver a colgarse. Guarda las lineas.
  16 Warning BlobNotFound: falta plantilla o adjunto. Guarda la linea.

Recuerda: Grafana muestra hora del navegador, la base y Control Panel en UTC.

---

## 5. Re disparo, solo si 4 dio atascado (5 minutos)

Di: "Confirmemos antes: el log muestra atasco, Holly pidio este caso, tenemos el login de escritura, y es un caso, no una auditoria."
Di: "Con login de escritura corre:"
SELECT ShopliftingID, InProcess FROM incident.Shoplifting WHERE ShopliftingID = <ID>;
UPDATE incident.Shoplifting SET InProcess = 0 WHERE ShopliftingID = <ID>;
SELECT ShopliftingID, InProcess FROM incident.Shoplifting WHERE ShopliftingID = <ID>;
Tiene que quedar en 0.
Di: "En el navegador con sesion del cliente abre:"
https://apps.apprissretail.com/gwmek/nettrack/ProcessCaseAlert.aspx?ShopliftingID=<ID>
Si la ruta da error: "Abre el caso y guardalo sin cambios."
Di: "Grafana, misma consulta, ultimos 15 minutos."
  Bien: 6a=1, 8, 8a, 13a, 13b EMAIL SENT, 14, End.
  Mal: paramos. No repetimos el UPDATE. Guardamos las lineas en el ticket.
Di: "Confirma en la base y en Smart Alert History:"
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = <ID> ORDER BY RunDate DESC;
Fila de hoy con Success. Success dice que salio, no que llego.

---

## 6. Cierre (3 minutos)

Di: "Guarda capturas de la configuracion y de Build Filters, las lineas del log con hora, y los resultados de 3.2, 3.3 y 3.4 en el ticket."
Acuerden la respuesta a Holly segun el resultado:
  Filtro o configuracion: que condicion no cumplio el caso y que cambiar.
  Re disparo: que la alerta salio para 26-288-15 y que confirme si le llego.
  Salio y no llego: hora y destinatarios del log, y revisar entrega.
Di: "Redacta tu el comentario y lo revisamos juntos antes de enviarlo."

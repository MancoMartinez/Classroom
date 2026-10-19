# Como disparar una Smart Alert a mano. Procedimiento de Kiran Vadday, sep 2026, v2

Cuando usarlo
Solo para un caso cuya alerta quedo atascada y que el cliente quiere recibir. El fix de codigo corrige hacia adelante y no reenvia alertas perdidas. Disparar envia correo real a la lista real del cliente: confirmalo antes con el cliente. ADUSA pidio solo hacia adelante.

Antes de empezar
1. El fix tiene que estar desplegado en el ambiente del cliente. Si no, el caso se vuelve a atascar.
2. Base de Incident, esquema incident, en el servidor de PRODUCCION del tenant. No GP. DEVWUS2 es desarrollo y no tiene los casos del cliente.
3. El UPDATE es en produccion. Solo con visto bueno de Kiran o de Infra.
4. Un caso a la vez. No pases al siguiente hasta confirmar el anterior.
5. Solo aplica a casos, pSystemType=Case. Las auditorias, pSystemType=Audit, no tienen ShopliftingID y no usan ProcessCaseAlert.aspx. Para esas pregunta a Kiran.

Paso 1. Sacar el ShopliftingID
El cliente suele dar el numero de caso, por ejemplo 26-DCVA-DCEAC-718 seguido del nombre de la persona.
Opcion A: abre el caso en LPMS. La URL trae ShopliftingID=<numero>.
Opcion B, SELECT:
SELECT s.ShopliftingID, m.CaseNo, s.InProcess FROM incident.MasterCase m JOIN incident.Shoplifting s ON s.MasterCaseID = m.MasterCaseID WHERE m.CaseNo LIKE '%DCEAC-718%';
Si da error de columna, prueba s.CaseNo. Si no devuelve nada, puede ser auditoria.
En Grafana el ID aparece como pSystemID en las lineas de tipo Case.

Paso 2. Confirmar que esta atascado
SELECT ShopliftingID, InProcess FROM incident.Shoplifting WHERE ShopliftingID = <ID>;
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = <ID>;
Atascado es: InProcess = 1, sin fila en SmartAlertProcess para la alerta esperada, y en Grafana el caso llega a 13a sin 13b ni End, seguido de "0. Quit ProcessSmartAlert ... still on processing".
Ojo: InProcess = 1 solo no prueba nada. El flag vale 1 cada vez que corre una alerta.
Ojo: guardar el caso no dispara nada mientras InProcess este en 1.
Ojo: si en 6a sale Rows Returned=0, la alerta no aplica a ese caso por sus filtros. No es atasco.

Paso 3. Destrabar
UPDATE incident.Shoplifting SET InProcess = 0 WHERE ShopliftingID = <ID>;

Paso 4. Disparar
Con sesion abierta en el tenant:
https://apps.apprissretail.com/adusa/nettrack/ProcessCaseAlert.aspx?ShopliftingID=<ID>
Ruta confirmada para ADUSA. Para otro cliente cambia /adusa/ por la ruta del tenant y confirmala con Kiran. Es pagina de desarrollo y dispara sin guardar el caso.
Alternativa del metodo de Matt Kamminga, 18 sep: con InProcess en 0, volver a guardar el caso.

Paso 5. Mirar Grafana, ultimos 15 minutos
{service_name=~".+", deployment_environment="usprod"} | clientId="<clientId>" |= "<ID>"
ADUSA 441, Vitamin Shoppe 433, Vallarta 432.
Bien: 6a Rows Returned=1, 8, 8a, 13a, 13b EMAIL SENT, 14, End. Salen desordenados.
Mal: 13a sin 13b, un Quit, o un Warning 16.
Grafana muestra hora Bogota. La base guarda UTC, cinco horas mas.

Paso 6. Confirmar
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = <ID>;
Fila de hoy con Success. Revisa Smart Alert History en el caso.
Success confirma que Nettrack envio, no que llego. Para la entrega pide a Russ Harmon el log de SendGrid por asunto. SendGrid guarda 7 dias.

Paso 7. Siguiente
Si todo salio bien, repite con el siguiente caso. Si falla, para, no repitas el UPDATE en otros casos y manda a Kiran las lineas de Grafana.

Filtros
Cada alerta tiene filtros propios. Defrauded Customer-Food Lion exige caso Closed, narrativa, division FOOD LION ,LLC y fecha de creacion desde 4/30/2026. Los filtros completos se leen en la linea 6a de Grafana.

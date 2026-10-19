# Quitar duplicado de Harassment - Food Lion (config 209) desde LPMS (2026-10-07)

0. Respaldo antes de editar:
SELECT sac.SmartAlertConfigID, ac.AlertConfigID, ac.EmailGroup
FROM incident.SmartAlertConfig sac
JOIN incident.AlertConfig ac ON ac.AlertConfigID = sac.AlertConfigID
WHERE sac.SmartAlertConfigID IN (209, 197);
Copiar EmailGroup completo.
1. Control Panel, adusa, logo. LPMS, Admin, Manage Smart Alerts.
2. Harassment - Food Lion, Edit. Pestana Alert Configuration.
3. Email Group: borrar solo "Brian.Tanner@FoodLIon.com" y una de sus comas. Sin espacios ni saltos de linea (Enter = CRLF = SendGrid lo descarta). No tocar Build Filters ni otros campos.
4. Save.
5. Verificar: mismo SELECT, sin brian.tanner, y
SELECT AlertConfigID FROM incident.AlertConfig WHERE AlertConfigID = <AlertConfigID> AND (EmailGroup LIKE '%' + CHAR(13) + '%' OR EmailGroup LIKE '%' + CHAR(10) + '%');  -> 0 filas.
6. Reenviar: DELETE 371880 (BEGIN TRAN, @@ROWCOUNT=1, COMMIT), link ProcessCaseAlert 1603659, Grafana 13b sin brian en To, SendGrid jamie.holland Oct 7 Delivered.
Riesgo: Brian deja de recibir Harassment de tiendas donde no es gerente. Runbook: defecto conocido, editar una alerta puede dejar el filtro viejo en base; revisar 6a en la corrida.
Config 197 (Kimberly Williams): mismo procedimiento con Defrauded Customer-Food Lion, kimberly.WILLIAMS@FoodLion.com.
Avisar a Leigh Ann que se quitaron de la lista y por que.

## Respaldo EmailGroup antes de editar (10/7)
197: storepayments@foodlion.com,Dawn.Hendry@adusa.com,SLHyde@Foodlion.com,jbowens@foodlion.com,Jeremiah.Balthazr@foodlion.com,Zachary.Huber@foodlion.com,james.cosseboom@adusa.com,CentralStation@adusa.com,Candace.Hill@foodlion.com,lauren.linsenbach@adusa.com,troy.leshko@foodlion.com,leighann.stubbs@adusa.com,RETFLAssetProtectionDivisionalMgrsALL@retail.foodlion.com,dwalker@foodlion.com,Silvana.Baxter@foodlion.com,jamie.holland@adusa.com,Carmine.Willis@FoodLion.com,bj.robinson@foodlion.com,kimberly.WILLIAMS@FoodLion.com,Keith.Gouldman@FoodLion.com,Craig.Arcamone@foodlion.com
209: Grant.Thomas@FoodLion.com,Linda.Stiller@foodlion.com,Valarie.Wallace@foodlion.com,Neal.Cope@adusa.com,GAFinchum@FoodLion.com,CPhillips-Brown@adusa.Com,Kim.Lyda@adusa.com,James.Cosseboom@adusa.com,CentralStation@adusa.com,Brandi.Langford@FoodLion.com,troy.leshko@foodlion.com,Katherine.Kirby@foodlion.com,RETFLAssetProtectionDivisionalMgrsALL@retail.foodlion.com,DWalker@foodlion.com,Tommy.Postek@adusa.com,Brian.Tanner@FoodLIon.com,Silvana.Baxter@foodlion.com,Jamie.Holland@adusa.com,Carmine.Willis@FoodLion.com,bj.robinson@foodlion.com,Kimberly.WILLIAMS@FoodLion.com,Keith.Gouldman@FoodLion.com,Craig.Arcamone@foodlion.com
AlertConfigID 209 = SmartAlertConfigID 209.
Nota: en ambas listas hay gerentes de tienda (Kimberly, Silvana, BJ, Craig, Keith, Carmine, DWalker). Cualquiera puede chocar en otra tienda. Arreglo de fondo es deduplicar en codigo.
10/7: Brian.Tanner@FoodLIon.com quitado de AlertConfig 209 desde LPMS. Verificado: EmailGroup sin Brian, sin CR/LF. Siguiente: DELETE 371880 y reenvio.

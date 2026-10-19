# RCS-29026 causa: direccion duplicada entre To y CC (2026-10-07)

Alcance desde 9/15: 11 envios con la misma direccion en To (lista de la alerta) y CC (Email Managers de la tienda), mas 371425 (#1353 10/4, borrada):
config 197 Defrauded Customer-Food Lion, kimberly.williams: 368924 (9/20, 0619-27), 369132, 369444, 371160, 371167, 371168, 371350
config 209 Harassment - Food Lion, brian.tanner: 369310, 371066, 371425 (borrada), 371880
config 361, mark.sens: 371874
Verificados sin registro en SendGrid: 371350, 371874, 371425, 371880. 368924 fuera de retencion (Chris no lo encontro el 9/25).
Control entregado: 371801 (mark.sens dos veces, ambas en To).

## Nota interna (Jira)
Update 10/7. Root cause found for the Smart Alerts that show Success but never arrive.

When the same address is in To (alert email group) and in CC (store managers from Email Managers), even with different case, the email never reaches SendGrid. SmartAlert.vb still writes Success to SmartAlertProcess.

Evidence:
1. Case 1353-15, ShopliftingID 1603659. 13b on 10/4 16:20:19 UTC and on today's resend at 18:49:34 UTC (row 371880). Brian.Tanner@FoodLIon.com in To, Brian.Tanner@FoodLion.com in CC. No SendGrid entry for either send. Jamie Holland received other alerts at 18:40:41 and 19:02:15 UTC.
2. Case 0619-27 (9/20, row 368924), the original report: kimberly.WILLIAMS in To and Kimberly.WILLIAMS in CC.
3. 10/4 00:20 (row 371350, Kimberly Williams) and 10/7 18:00 (row 371874, Mark Sens): same pattern, not in SendGrid.
4. Control: 10/7 02:13 (row 371801) has Mark Sens twice, both in To, and was delivered.

Scope since 9/15: 11 sends. Config 197 Defrauded Customer-Food Lion (Kimberly Williams) 7, config 209 Harassment - Food Lion (Brian Tanner) 3 plus the 10/4 send, config 361 (Mark Sens) 1.

Also ruled out: the semicolon in EmailAddresses is the To/CC separator, sends with it are delivered.

Next: dedupe To and CC ignoring case before sending, and check the SendGrid response before writing Success. Shared with Kiran Vadday. Resend of 1353-15 pending until Brian is only in one of the two.

## Teams Kiran
Hi Kiran, following up on the Smart Alerts that show Success but never reach SendGrid. I checked all sends since 9/15 and found 11 where the same address is in To (alert list) and in CC (store managers), ignoring case. Every one I could check in SendGrid is missing, including 0619-27 and 1353-15 from RCS-29026. A send with the same address twice in To was delivered. Most are config 197 Defrauded Customer-Food Lion (Kimberly Williams, 7 sends) and 209 Harassment - Food Lion (Brian Tanner). Could we dedupe To and CC before sending? And for now, would it be ok to remove Kimberly from 197 and Brian from 209, since they get those alerts as store managers anyway? Then I'll resend 1353-15.

## Reenvio sin Brian en To (10/7 19:26 UTC)
Begin 19:26:12.327, 6a RR=1 (filtro correcto tras editar), 13b 19:26:21.061, 14, End 19:26:21.233. To sin Brian, cc con Brian.Tanner@FoodLion.com.
CAUSA EXACTA: 10c arma cc con 7 (BDWilliams;Brian.Tanner;Madelina.Fordham;kim.woods;Silvana.Baxter;Daniel.Analoro;bj.robinson). El 13b sale con 5: el codigo quito Silvana.Baxter@foodlion.com y bj.robinson@foodlion.com porque estan en To escritos IGUAL. O sea, Nettrack ya deduplica To/CC pero distinguiendo mayusculas. Brian.Tanner@FoodLIon.com vs @FoodLion.com, kimberly.WILLIAMS vs Kimberly.WILLIAMS, mark.sens vs Mark.Sens: no los quita y el correo se pierde.
Arreglo de codigo: comparacion sin mayusculas (una linea). Arreglo de datos sin quitar gente: escribir la direccion en la lista de la alerta igual que en el campo de gerente de la tienda (Brian.Tanner@FoodLion.com en 209, Kimberly.WILLIAMS@FoodLion.com en 197).
Pendiente: SendGrid jamie.holland Oct 7 a las 19:26:21.

Teams Kiran (reemplaza el anterior):
Hi Kiran, I think I found why some Smart Alerts show Success but never reach SendGrid. Nettrack already removes CC addresses that are also in To, but the comparison is case sensitive. In today's run for 1603659, line 10c had 7 CC addresses and 13b sent 5: Silvana.Baxter and bj.robinson were removed because they match To exactly. When the case differs (Brian.Tanner@FoodLIon.com in To vs Brian.Tanner@FoodLion.com in CC), the duplicate stays and the whole email never shows up in SendGrid. That matches every lost send I found since 9/15 (Kimberly Williams on 197, Brian Tanner on 209, Mark Sens on 361), including both sends from RCS-29026. Would it be possible to make that comparison case insensitive?

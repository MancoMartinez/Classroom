# Hola Enrique, revisión de tus tres tickets

Revisé los tres tickets en Jira, el video de RCS-29351, las capturas de los clientes y los PR. Abajo va lo que encontré y lo que haría en cada uno. Si algo no cuadra con lo que ves tú, dime y lo reviso.

## 1. [RCS-29245](https://trebuco.atlassian.net/browse/RCS-29245), el más cerca de cerrar

**Causa:** el [PR 59286](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/59286) devuelve a State una línea de `location.searchable` que estaba en City. La captura de Cathryn lo confirma: Store City y Store State muestran HOUSTON las dos.

**Qué hacer:**
1. Resuelve el hilo activo del PR. Es el único check requerido que falla, **Comments must be resolved**.
2. Pide a Delivery la aprobación de un miembro de **Approval All Delivery**. Yo ya aprobé.
3. Pide el cherry-pick a release y el deploy solo de arpfiles para el cliente 21, como dice tu descripción.
4. Enlaza [ENG-10063](https://trebuco.atlassian.net/browse/ENG-10063) al PR. Hoy el PR no tiene work items y el ENG sigue en Backlog. Pregunta a Delivery en qué estado lo quieren.
5. Después del deploy, confirma en Search Composer que `location_address3` genera `T2.State` y pide a Cathryn que valide.
6. Revisa si CTC 177 y NOR 138 traen lo mismo, porque el [PR 58545](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/58545) los convirtió el mismo día. Es una duda mía, no la verifiqué.

No prometas fecha al cliente hasta que Delivery la confirme.

## 2. [RCS-29351](https://trebuco.atlassian.net/browse/RCS-29351), Smart Track de AAP

**Lo que muestra el video** (17 segundos): Cathryn hace clic en el valor de Bruce Wood en Store SRA Activity Lookup, sale el menú **Select Where To Go**, elige Cashier Refunding to Own Card y se abre la query 1d con Trans Date en "The last 0 Days". Pone 7 días y sigue sin resultados. Ese menú es la opción que no te sale a ti.

**Dos datos nuevos:**
- En la captura del ticket, la copia pública de 1d, en Admin Reports > SRA Smart Tracks, tiene **Last Changed 10/08/26 11:41:55**. Las demás son de mayo. Cathryn editó esa copia el 8 oct, minutos antes de abrir el ticket.
- El link abre `/system/ebr/smarttracksearches/1d - Cashier Refunding to Own Card.search`, la copia del sistema. En [arpfiles](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles?path=/repo/21/system/ebr/smarttracksearches/1d%20-%20Cashier%20Refunding%20to%20Own%20Card.search&version=GBmain) ese archivo y la configuración de los links no cambian desde el 5 jun.

**Hipótesis, ninguna confirmada:**
1. El link pasa solo tienda y cajero y el rango de fechas queda en 0 días.
2. Su edición a la copia pública cambió algo que el link necesita.
3. La conversión de AAP a SnowTime del 2 oct dejó la query sin datos. Cathryn dice que el link funcionaba antes de su cambio, lo que debilita esta tercera.

**Qué hacer:**
1. Ejecuta 1d directo desde Composer con 30 días, tienda 7655 y cajero 947878. Si trae datos, el problema está en el link. Si sale vacío, está en la query o en los datos.
2. Compara la copia pública con la del sistema. Tu pregunta del 14 oct sobre qué cambió Cathryn sigue sin respuesta y es la que desempata.
3. Si el paso 1 sale vacío, pregunta a Carl Costelow, autor de los PR 58545 y [58554](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/58554), si la conversión cambia el resultado de 1d.

El atributo `search-name` del archivo dice 1c y el archivo es 1d. No sé si importa. Mira si algún link resuelve por ese nombre.

**Precedente:** en [RCS-28982](https://trebuco.atlassian.net/browse/RCS-28982) de TSC el fix fue un PR en arpfiles sobre el `.search`, el [PR 58842](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/58842). Si llegamos ahí, ya conoces el flujo.

## 3. [RCS-29326](https://trebuco.atlassian.net/browse/RCS-29326), Big Y

La captura de Kevin muestra la pantalla genérica de Incident con el enlace **Technical Details** sin abrir. Ahí va el stack. En [RCS-27573](https://trebuco.atlassian.net/browse/RCS-27573) de Tahoe Donner ese enlace dio la causa.

**Qué hacer:**
1. Pide a Kevin que haga clic en Technical Details y envíe captura.
2. Abre la URL de Kevin con tu sesión de soporte en bigy y busca el `Application_Error` de esa hora en Grafana.
3. Prueba un adjunto de un caso reciente de Big Y como control.
4. Con eso crea el ENG, como hiciste en RCS-29245. Escríbele a Matt en el comentario del ENG y no en Teams. El 8 oct respondió en el ENG de [RCS-28181](https://trebuco.atlassian.net/browse/RCS-28181) y pidió environment, client y URL. Dale client 362, la URL, la hora y el `Application_Error`. Pregunta si el archivo existe en el storage con ese nombre.

**Causa, hipótesis:** el nombre guardado es una ruta heredada con barras invertidas y corchetes, `\KCCMS Attachments\Case 7546\HPIM0285[1].jpg`. La otra hipótesis, sesión vencida, explicó el ticket de Big Y del 11 ago, que usaba `system=ERMS`. Este usa `LPMS`.

---

Escríbeme cuando tengas el resultado del paso 1 de RCS-29351 y la captura de Technical Details.

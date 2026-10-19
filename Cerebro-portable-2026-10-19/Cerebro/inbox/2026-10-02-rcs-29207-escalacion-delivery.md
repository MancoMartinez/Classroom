**Escalating to Delivery, Secure 5.** The SFE Star Farming same day high volume definition fails on every run since the 27 Aug SnowTime cutover, so no work items generate for fiscal period 24 Aug to 27 Sep. Support cannot change the definition.

## 1. Environment and steps to reproduce

Prod. Tenant starbucks-us, c166_sbx, ARDM_PRODUCTION.C166_SBX.

### Starbucks NA (SBX), reported 30 Sep

1. Snowflake, SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY, user SVC_ARP_PRODUCTION_166_USER, error_code 100038, from 30 Sep.
2. Open query ID 01c77251-0109-d5e7-0120-d20111b67fc7, 1 Oct 14:05 PT. Its columns are aliased Topic_-_SFE_-_Star_Farming_same_day_high_volume.
3. Executive Workbench, Workview Monitor set to this definition, date range 1 Jul to 1 Oct.

Expected: runs on 1 Jul, 29 Jul, 26 Aug and 30 Sep.
Actual: no run on 30 Sep. Error on condition `T9.x_MemberID <> 70267962874`:

```
Numeric value '1867074335977200' is not recognized
```

## 2. Findings

Detail and run counts by day in my internal note of 1 Oct.

**x_MemberID is TEXT in ARDM_PRODUCTION.C166_SBX. This definition compares it to an unquoted number.** Sebastian Rueda confirmed on 1 Oct that arpfiles PR 57459 retyped MemberID from Int64 to String. My reading, unverified: this definition's own condition still declares MemberID as Int64, the same pattern StarRewardTransactions.search had on https://trebuco.atlassian.net/browse/RCS-28873.

## 3. Troubleshooting performed

Snowflake query history for the service user. Executive Workbench for this definition and for control fiscal period definitions. Teams with Sebastian Rueda on 1 Oct. No other conversations. Support has no access to the definition condition.

## 4. Still open

1. Does this definition's condition carry its own Int64 type for MemberID?
2. Once corrected, can the 24 Aug to 27 Sep run be regenerated?

Related: https://trebuco.atlassian.net/browse/RCS-28873 and https://trebuco.atlassian.net/browse/RCS-29205

Ryan DeVries en Teams, 2 oct, 1:15pm
Dio su propio diagnostico de RCS-29207. Cree que el equipo de Carl Castelow cambio un field type y eso rompio el search. No sabe si el equipo de Carl lo arregla o va a Engineering. Probo borrar la columna del search y volver a agregarla, no funciono.

Conexion con lo ya documentado
Coincide con la pregunta abierta del 1 oct, Sebastian Rueda confirmo que PR 57459 retipeo MemberID de Int64 a String, sin verificar si la condicion propia de esta definicion seguia en Int64. El field type que ve Ryan es probablemente ese mismo retype.
Por que no funciono el workaround de borrar y recrear la columna, ese workaround refresca el binding de una columna de display, documentado en Cerebro para RCS-28843 Nordstrom y RTS-206268 Kinney. Pero el problema esta en la condicion de filtro guardada, T9.x_MemberID <> 70267962874 sin comillas, no en una columna de display.

Respuesta para Ryan en Teams, version corta

Thanks Ryan, that matches what I found, Sebastian confirmed PR 57459 retyped MemberID from Int64 to String, and I was not sure if this definition's condition still carries the old type. That is probably the field type change you saw, and why deleting the column did not help, that only refreshes the display binding, not the saved filter condition. Makes sense to start with Carl, if he says it is code we move it to Engineering.

Correccion, 2 oct
El mensaje anterior no aclaraba quien contacta a Carl Castelow. Ryan dijo a las 12:34 "Let me do some analysis", tomo la propiedad del analisis de los dos tickets, asi que "I would contact Carl Castelow" probablemente es su propio plan, no un pedido a Juan. No es inequivoco, se agrega pregunta directa en vez de asumir.

Respuesta para Ryan en Teams, version con pregunta de ownership

Thanks Ryan, that matches what I found, Sebastian confirmed PR 57459 retyped MemberID from Int64 to String, and I was not sure if this definition's condition still carries the old type. That is probably the field type change you saw, and why deleting the column did not help, that only refreshes the display binding, not the saved filter condition. Are you reaching out to Carl, or would you like me to?

Juan ya envio el mensaje anterior a Ryan sin la pregunta de ownership, asume que el contacta a Carl directamente.

Mensaje para Carl Castelow en Teams, corto y directo

Hi Carl, could you check the SFE Star Farming same day high volume work item for c166_sbx? Its trigger search has been failing since the Aug 27 cutover, error is Numeric value not recognized on T9.x_MemberID <> 70267962874. Sebastian confirmed PR 57459 retyped MemberID from Int64 to String, looks like this definition's own condition still has it as Int64. Can you confirm and fix if that is configuration, or let me know if it needs Engineering instead. Ticket, https://trebuco.atlassian.net/browse/RCS-29207

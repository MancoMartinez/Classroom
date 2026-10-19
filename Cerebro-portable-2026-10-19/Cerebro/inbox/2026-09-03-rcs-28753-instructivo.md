# RCS-28753 — Instructivo

## Paso 1. Confirmar el estado real del ticket en Jira

Donde se ejecuta: Jira, lectura.

Confirmado en esta sesion con getJiraIssue. Estado Under Support Review, asignado Juan Martinez, prioridad High. No hace falta repetirlo.

## Paso 2. Escalar a Peyman Motlagh, no a un canal generico

Donde se ejecuta: Jira, escritura, comentario interno en RCS-28753. Autoriza Juan Martinez antes de pegarlo. Un comentario interno en el ticket deja evidencia, a diferencia de un mensaje en Teams.

Peyman resolvio la misma familia de preguntas para Nike en RCS-21540, con una tabla de definiciones de ocho campos de descuento y su columna fuente. El campo mas cercano que el describio ahi es Total Discount Modify Amount, el total de overrides manuales del cajero. Pegale esto en RCS-28753, mencionandolo:

@Peyman Motlagh Nike is asking for the logic behind Manual Discount Amount in Secure 5. This looks close to Total Discount Modify Amount, the field you defined in https://trebuco.atlassian.net/browse/RCS-21540 as the sum of manual cashier overrides. Can you confirm if it is the same field or a different one, and where it gets calculated.

Que se espera ver: confirmacion de Peyman del campo exacto y su formula, o la correccion de que es otro campo distinto.

Si falla: si Peyman no responde en un dia habil, dado que Damir marco esto como prioridad sobre los otros cuatro tickets de Nike, escala con su lead o con quien haya quedado a cargo de RCS-28420, que es el mismo schema de Nike.

## Paso 3. Si Peyman confirma que es un campo nuevo, pedir el Searchable o la funcion fuente

Donde se ejecuta: Jira, escritura, comentario interno. Solo si el Paso 2 no cierra la pregunta.

Si Peyman dice que Manual Discount Amount no es Total Discount Modify Amount ni ningun campo que el conozca, pide que identifique el Searchable en Secure 5 o la funcion de Snowflake que lo genera. El archivo mas probable para revisar es este, del override client specific de Nike, id 67, encontrado en el comentario de Vlad Bogus en RCS-28420:

dev.azure.com/apprissdevops/Sysrepublic Secure/_git/Secure, ruta Sources/Databases/Snowflake/Programmability/Snowflake/ClientSpecific/67/ArdmDependent/Common/Functions/secure/GetTransactionJson.sql, rama main

Que se espera ver: el nombre del Searchable o de la funcion, y la logica de calculo exacta.

Si falla: si nadie en Ingenieria reconoce el campo con ese nombre exacto, pide que revisen si Manual Discount Amount es un alias que se configuro solo para Nike en el mapeo de su Searchable, en vez de un campo estandar de Secure 5.

## Paso 4. Redactar la respuesta al cliente solo cuando llegue la confirmacion

Donde se ejecuta: Cerebro, skill cerebro-respuesta-cliente.

No respondas a Damir con ninguna de las dos hipotesis de este informe sin que Ingenieria las confirme primero. Cuando llegue la respuesta del Paso 2 o el Paso 3, usa cerebro-respuesta-cliente para redactar el texto final con la formula confirmada.

Que se espera ver: un borrador de respuesta a Damir con la logica exacta, sin fechas futuras de Ingenieria si el ticket sigue en revision.

Si falla: si Ingenieria entrega solo una explicacion parcial, marca en el informe que la respuesta al cliente queda incompleta y por que.

## Transicion sugerida

El ticket se queda en Under Support Review hasta que llegue la respuesta de Peyman del Paso 2. No hay transicion que ejecutar todavia.

## Comentario que Juan pega

@Peyman Motlagh Nike is asking for the logic behind Manual Discount Amount in Secure 5. This looks close to Total Discount Modify Amount, the field you defined in https://trebuco.atlassian.net/browse/RCS-21540 as the sum of manual cashier overrides. Can you confirm if it is the same field or a different one, and where it gets calculated.

# RCS-28997, que es singles info y como se reproduce

## Que pasa

RCS-28997 reporta que Store 449 de FinishLine no puede ingresar singles info en el sistema. El ticket esta en Work in progress desde el 18 sep 2026, asignado a Enrique Jimenez, sin adjuntos ni mensaje de error registrado.

## Causa

HIPOTESIS. Singles info no tiene definicion en Cerebro ni en Confluence. FinishLine vende calzado. La hipotesis de trabajo ubica singles como el registro de zapatos sueltos o de un solo zapato dentro del modulo Incident, categoria de shrink propia de retail de calzado. Nada del corpus consultado confirma esta lectura.

## Evidencia

getJiraIssue RCS-28997, campo description completo. "Store 449 is not able to enter singles information into the system." Sin adjuntos. Dos comentarios de plantilla, 18 sep 11:32 y 12:55.
bin/buscar "singles" y "SinglesInfo" contra brain/markdown, memorias, tickets y confluence/RTS-triage. Cero coincidencias.
inbox/2026-09-18-rcs-28997-finish-line-client-ids-prod-staging.md, nota propia sobre este mismo ticket. Deja pendiente confirmar si Store 449 pertenece al client 375 FLP o al 376 FIN.

## Que hago hoy

1. Redacto el texto para pedirle a Viviana Adkins el mensaje de error exacto y una captura de la pantalla donde intenta ingresar singles info. Sin eso no hay sintoma que reproducir.
2. Confirmo en Control Panel a cual de los dos tenants de Finish Line pertenece Store 449, 375 FLP o 376 FIN. Busco la tienda por numero dentro de Incident en cada uno. No infiero por el dominio del correo de la reportera.
3. Con el tenant confirmado, entro como Store Reporter de Store 449 y busco el campo o formulario singles en New Case o en Screen Designer. Si no aparece, el sintoma cambia de error de ingreso a campo inexistente y la escalacion cambia con el.
4. Si el campo existe y falla, comparo su configuracion en Screen Designer contra un tenant de calzado que si funcione. Si no tengo acceso a Screen Designer para este tenant, pido la comparacion a Matt Kamminga, delivery de Secure Incident and Audit.

## Precedentes

tickets/RCS-28701.md, misma pareja de client IDs 375 y 376 de Finish Line, sin resolver a que tienda pertenece cada uno.
inbox/2026-09-18-rcs-28997-finish-line-client-ids-prod-staging.md, nota propia sobre Prod vs Staging para este ticket.

## Compromisos

Ninguno entregado a Viviana Adkins todavia. El siguiente paso depende de que ella responda el mensaje de error y la captura pedidos en el paso 1.

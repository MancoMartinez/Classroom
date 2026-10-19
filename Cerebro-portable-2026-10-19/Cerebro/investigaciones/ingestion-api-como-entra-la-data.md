# Ingestion API. Como entra la data del cliente a Appriss

Fuente: Confluence PD, "Ingestion API - EventHub", pagina 477499490306, autor Carl Costelow,
modificada 2026-03-23. Repositorio gateway_eventhub.

Leelo antes de responderle a cualquier cliente que pregunte como consumimos su data. La respuesta
corta es que no la consumimos, ellos la publican.

## El flujo

    [Cliente] POST /api/{customer}/{data}
        |
     Inbound API, gateway.inbound.event.api.json
        |
     menor a 1 MB  ->  Event Hub  c{customerID}_rawdata_{dataType}
     1 MB o mas    ->  Blob Storage  large_{data}_{customerIdPadded}_{correlationId}

El cliente hace POST con cuerpo binario crudo. Appriss enruta por tamaño de payload. El nombre del
Event Hub se construye solo, con el customer ID numerico y el tipo de dato. Por eso c67_rawdata_order
es Nike, cliente 067, dataType order.

## Las tres validaciones, en orden

1. Formato del nombre de cliente en la URI. Solo letras. Falla con 400, resultCode 10.
2. Identidad. El parametro customer de la URI debe coincidir con el ClientID de OAuth, partido por
   guion bajo, y con el ClientScope. Falla con 401, resultCode 12.
3. Tipo de dato permitido. El parametro data debe estar en la lista allowed.data.types del entorno.
   Falla con 400, resultCode 11.

Esas tres son la primera sospecha cuando un cliente deja de entregar sin aviso. Un cambio de
credencial o de nombre de dataType del lado del cliente produce 401 o 400, y del lado de Appriss no
entra nada al hub. Las metricas del Event Hub se ven identicas a "el cliente dejo de mandar".
La unica forma de distinguirlo son los logs de la API.

## Log codes del inbound

ClientID, ClientScope, CustomerID, CustomerHubName, DocId, DataSize, BlobLocation.
Con esos se prueba si las llamadas del cliente llegaron y que respuesta recibieron.

## Que es seguro compartir con el cliente

Comparte lo que el cliente controla y ya conoce: que la entrega es un POST autenticado con OAuth a
su endpoint, que el enrutamiento interno depende del tamaño del payload, que no aplicamos filtros de
contenido, y los codigos de respuesta que su lado recibe.

No compartas la infraestructura interna: nombre del namespace de Event Hubs, nombre del hub
c{id}_rawdata_{tipo}, el ID numerico de cliente, el repositorio, las rutas de blob, las claves de
configuracion ni los nombres de log code.

Precedente de criterio: en RCS-28753 Peyman Motlagh le compartio a Nike nombres de campos y de
feeds, y escribio "Although, I cannot share our exact code". Nombres funcionales si, implementacion
no.

## Enlaces

Confluence PD, Ingestion API - EventHub, 477499490306.
Confluence RSI, Ingestion API Setup Guide, 475680243749.
Confluence RSI, Customer Implementations, 4236059772. Lista de clientes, IDs y a donde envian.
Confluence RSI, Ingestion API Project Stages, 475693744156. Los detalles de la API se le entregan al
cliente por 1Password, o sea el cliente ya los tiene.

Aplicado en RCS-28756.

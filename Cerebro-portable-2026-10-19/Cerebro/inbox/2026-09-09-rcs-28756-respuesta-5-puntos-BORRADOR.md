NO ENVIAR. Faltan los puntos 1 a 4. Rellena y borra esta linea antes de pegar.

Thanks Madhuraj. Here are the five points in order.

1. Exact stream names.
[PENDIENTE Peyman o DataOps. Candidato: entity c67_rawdata_order on namespace prd-datacloud-wus2-ehub-1. Confirmar que es lo que Nike reconoce de su lado antes de enviarlo.]

2. Consumer client ID.
[PENDIENTE Peyman o DataOps.]

3. How the data is being consumed.
[PENDIENTE Peyman o DataOps. Confirmar primero si Nike publica directo al hub o si hay un componente nuestro en medio. La respuesta cambia segun eso.]

4. Filters being used.
[PENDIENTE Peyman o DataOps. El borrador interno dice que no aplicamos filtros adicionales. Confirmarlo antes de afirmarlo.]

5. Examples of missing data.
This is a complete absence of ECOM order data, not individual missing events. The last order data reached us on 2026-08-27 at 19:02 UTC. Trading day 2026-08-28 is the first day with zero ECOM records, which is why our earlier note referred to the loss starting on 2026-08-28, and the gap has continued every day since. Daily volume before the stop ran between 195,352 and 234,363 ECOM transactions.

One request for Nike. Ask them for the name of the outbound stream they publish this order data from, and the timestamp of the last record their side shows as sent. That gives us both ends against a single point in time.

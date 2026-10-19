# RCS-28997, Finish Line client IDs 375/376 y diferencia Prod vs Staging

## Client IDs de Finish Line, confirmado en Confluence

Fuente: pagina "Customer Escalation Handoffs -- Secure Audit & Legacy" (espacio RTS, id 478022139957), seccion 5, perfil Finish Line. Cita textual:

"Note: two Finish Line tenants exist -- client 375 (FLP, finishline.com/hr) and client 376 (FIN, finishline.com/lp)."

Client 375, codigo FLP, path finishline.com/hr.
Client 376, codigo FIN, path finishline.com/lp.

HR y LP no son Human Resources ni Loss Prevention como area de negocio. Son el segmento de URL con el que Control Panel diferencia dos tenants separados que comparten el nombre comercial Finish Line, igual que Walmart tiene 300, 301, 303, 308 y 309 para paises distintos bajo el mismo nombre. La pagina de Confluence es especifica de Secure Audit, CAMS y netTrack. No confirma si esa misma separacion 375/376 aplica igual del lado de Incident o LPMS, que es el producto de RCS-28997, singles entry en Store 449.

Precedente relacionado: tickets/RCS-28701.md ya habia registrado que 375 y 376 existen como dos tenants de Finish Line, sin resolver a cual pertenece cada tienda.

Pendiente antes de actuar en RCS-28997: confirmar en Control Panel, con la tienda 449, cual de los dos tenants la contiene. Buscar la tienda por numero dentro de cada uno de los dos client IDs en el modulo de Incident, no asumir por el nombre del reporter ni por el dominio del correo.

## Prod vs Staging, por que una tienda aparece en uno y no en el otro

Fuente: brain/markdown/14-appriss-ingeniería-docs-fuente.md, chunk 447, "Environments · Environment Summary", y chunk 451 "Environments · Notes".

Staging es el ambiente de preproduccion, tambien llamado Test. Es customer facing, se usa para UAT y para el sign off de release antes de pasar a Production. Production es el ambiente vivo con datos reales del cliente, acceso restringido y requiere justificacion.

Cada ambiente tiene su propio set de bases de datos por tenant, separado por region. Una tienda puede existir en Staging y no en Production, o al reves, porque la carga de tiendas en cada ambiente es independiente. Staging normalmente trae un subconjunto de tiendas usado para pruebas, no la lista completa de produccion, y esa lista se actualiza en momentos distintos entre los dos ambientes. Que una tienda aparezca en uno y no en el otro no es en si mismo un defecto, es reflejo de que cada ambiente tiene su propia carga de datos de tienda.

Para RCS-28997 esto importa si Store 449 aparece en un ambiente y no en el otro dentro de Control Panel. Si la tienda existe en Production pero el problema de singles se reproduce ahi, no es un tema de ambiente. Si la tienda solo existe en Staging o falta en el ambiente correcto, ahi si hay que revisar la carga de tiendas de ese tenant antes de tocar el codigo de singles entry.

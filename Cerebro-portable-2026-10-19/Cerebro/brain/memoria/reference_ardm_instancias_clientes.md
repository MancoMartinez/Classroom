---
name: reference_ardm_instancias_clientes
description: "En qué instancia de Greenplum vive cada cliente, dónde está el Product Delivery Client Matrix y cómo se accede a los clusters"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-11T23:41:11.939Z
---

**El Product Delivery Client Matrix** es el Excel que pasó Peyman el 11 ago 2026 (copia en `~/Downloads/Product Delivery Client Matrix.xlsx`, una hoja `Clients`, 373 filas). Una fila por cliente con ID, código de tres letras, instancia de Greenplum, esquema ARDM, versión, plataforma y POS. Es la forma más rápida de ubicar un cliente.

Verificados contra lo que se vio en pantalla:

| ID | Código | Cliente | Instancia | Esquema |
|---|---|---|---|---|
| 67 | NKE | Nike | GP11 | ardm_067 |
| 112 | AHL | Ahold | GP9 | ardm_112 |
| 138 | NOR | Nordstrom | GP9 | ardm_138 |
| 164 | COP | Coop UK | GP8 | ardm_164 |
| 176 | UNS | Marks & Spencer | GP6 | ardm_176 |
| 209 | TBI | Tailored Brands | GP9 | ardm_209 |

**`BYF` es Big Y Foods, cliente 362.** Sale del matrix y cierra la pregunta abierta de la página de Confluence de la ola de unificación, que decía que había que identificar al cliente de RCS-28153.

**Los clientes nuevos no tienen instancia de Greenplum.** 362 BYF, 378 GEL, 423 SBS, 433 VSE, 438 TGJ y 505 ALO están vacíos en esas columnas porque nacieron en la plataforma nueva. Si un ticket de esos habla de ARDM, algo no cuadra.

**El matrix tiene filas viejas.** Lo creó un jefe de hace años y se actualiza a mano. Ejemplo del propio Peyman: dice CRDM para Ahold y hoy ya es GP. Sirve para orientarse, no para citarlo en un ticket.

**Las otras dos formas de ubicar la instancia**: en Azure DevOps, proyecto DataOps, el icono azul son los pipelines (buscar por número de cliente o por código, el nombre del job trae la instancia) y el naranja son los repos. O directamente por el esquema, que se llama `ardm_<id>` a tres dígitos; en Snowflake es `ARDMPROD.ARDM_<id>`.

**Acceso a los clusters** (Confluence R&D, página *Cluster Access*, 478097309697): todos por un salto al jump server LA4, `10.22.0.220` por RDP con credenciales trebu.co. GP3, GP6 y GP9 son on premise, SSH con credenciales `gpadmin` del password book. **GP1 y GP11 están en Azure** y usan llave `gp5newnew.ppk`, no contraseña. **GP1 es dev y QA**: las conexiones de producción llevan `appriss` en el nombre, las de dev llevan `dev`.

Relacionado: [[reference_ardm_playbook_peyman]], [[reference_acceso_sql_tenants]].

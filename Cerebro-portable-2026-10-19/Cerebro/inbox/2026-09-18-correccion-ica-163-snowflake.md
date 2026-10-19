# Correccion, cliente 163 ICA ya esta en SnowTime, no en GP8

El archivo reference_ardm_instancias_clientes.md, sacado del Product Delivery Client Matrix, decia GP8 para el cliente 163 ICA. Ese dato quedo viejo.

Peyman Motlagh confirmo en chat, cita textual: "Client 163 is in EU and all EU clients have moved to Snow Time. If you have a US client that you want to know, you can go to the Control Panel and look into the Switcher."

Metodo que Peyman muestra para confirmar la fuente de cualquier cliente US: Control Panel, USPROD, entrar al tenant, tarjeta ARDM Switcher, la pantalla dice Currently pointing at y POS data source. Para clientes EU no hace falta el Switcher, ya estan todos en SnowTime.

Conclusion para consultas de ARDM del cliente 163 ICA: la fuente correcta es Snowflake, ARDMPROD.ARDM_163. No usar Greenplum GP8 para este cliente, ese dato del matrix esta obsoleto.

Contexto de origen: verificacion de RCS-28992, transaction id 2609179959263358647, 0 filas en ARDM_HEADER y en ARDM_TENDER contra Snowflake, confirmado como fuente correcta, no como consulta a la base equivocada.

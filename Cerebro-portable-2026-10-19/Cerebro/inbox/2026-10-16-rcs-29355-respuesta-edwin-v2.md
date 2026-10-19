RCS-29355 respuesta a Edwin, Teams, interno, v2. Reemplaza la v1 en ingles. Hipotesis: la lectura de Talos en RCS-29347 sobre los dos QA no esta confirmada.

Edwin, revisé el ticket y encontré dos cosas que te pueden servir.

En agosto Vlad Bogus ya cargó a mano datos de prueba de Delhaize en los dos QA, Secure 3 y 5. Fue en RCS-28125 y Rodney le dejó los archivos en 046DHZ_TEST. Pregúntale a Vlad cómo los cargó y desde dónde. Ese camino puede servir para los de la tienda 9916 sin esperar a que arranque la ingesta de staging.

Además RCS-29347 es de Shaun Callow y trata de automatizar las cargas POS en los dos QA de Delhaize. El triage de Talos ahí dice que el QA de cara al cliente lee una copia de staging encima de producción y que el QA interno usa datos de muestra vacíos. Es la lectura de un bot, así que pregunta en ese ticket a qué esquema lee cada QA antes de tocar los patrones de RecallExtract y POS_Navistore. Si Talos acierta, que ARDM_STAGING esté vacío puede ser normal.

Dime si lo estoy leyendo mal. Con Rodney, ninguna fecha todavía.

RCS-29245 AAP, Store State muestra la ciudad
Jira en vivo 16 oct: Work in progress. ENG-10063 en Backlog. PR 59286 Active.

QUE PASA
En AAP, cliente 21, el campo Store State de Location en Secure Store muestra la ciudad.

CAUSA
Confirmada por el diff del PR 59286: location.searchable tenía Description City en la línea 467 y el PR la devuelve a State. El PR atribuye el cambio a la conversión SnowTime de AAP, PR 58545, mergeado el 2 oct. No verifiqué esa atribución en el diff de 58545. Cerca de 78 searches guardados tratan Address3 como estado. La hipótesis de Talos sobre nombres de display no aplica.

EVIDENCIA
1. PR 59286: un archivo, repo/21/system/ebr/ardm/store/searchable/location.searchable, una línea cambiada.
2. Checks: Jira ID Validation OK, Validate ArpFiles OK, Deploy to Staging OK. Falla Comments must be resolved y falta un miembro de Approval All Delivery.
3. Juan aprobó. El PR no tiene work items enlazados.

QUE HAGO HOY
1. Resuelve el hilo activo, el de "Deployed on staging and tested". El check de comentarios pasa.
2. Pide a Delivery la aprobación y el cherry-pick a release. El PR indica deploy solo de arpfiles para el cliente 21.
3. Enlaza ENG-10063 al PR y pregunta a Delivery en qué estado debe estar el ENG.
4. Después del deploy, abre Search Composer y confirma que location_address3 genera T2.State. Pide a Cathryn que confirme en Secure Store.
5. Revisa si CTC 177 y NOR 138 arrastran el mismo cambio. PR 58545 los convirtió el mismo día. Hipótesis.

PRECEDENTES
RCS-29351 comparte la conversión de AAP. RCS-28982 muestra el patrón de fix por PR en arpfiles.

SIGUIENTE PASO
Delivery: aprobar PR 59286 y programar el deploy del cliente 21.
Cathryn: sin fecha hasta que Delivery la confirme.

Lectura directa de Azure DevOps por navegador, 17 septiembre 2026. Sin modificaciones.

PR 40748, completado 14 mayo 2025, 11:17 Bogotá. Crea repo/44/system/ebr/smarttracksearches/sametendercard.search. Líneas 77 y 82 añaden tender_accountnumber y customer_customerfullname con data-type System.Double. Cambia además el parámetro del enlace en detail-panel.html de cardno a tender_accountnumber. Objetivo declarado: arreglar el autopoblamiento de cuenta en SmartTrack, RCS-19380. Pruebas declaradas: Delivery y Event Viewer. No consta validación Excel en esa descripción.
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/40748?_a=files&path=/repo/44/system/ebr/smarttracksearches/sametendercard.search

PR 43459, completado 11 agosto 2025, 05:40 Bogotá. Modifica solo parámetro y variable de la búsqueda de tender_accountnumber a cardno, y el enlace correspondiente en detail-panel.html. No cambia los tipos de DisplayField.
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/43459?_a=files

PR 51987, completado 10 mayo 2026, 15:15 Bogotá. Un archivo, dos líneas reemplazadas. Líneas 77 y 82 pasan de System.Double a System.String. Commit b9e76df95c3c08c6a175dc818f435584a2173ffa. Descripción explica diferencia entre grilla y escritor Excel. Rama destino main.
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/51987?_a=files

PR 52242, completado 13 mayo 2026, 10:42 Bogotá. Cherry-pick b9e76df9 a release. Descripción Hotfix con mismo cambio, marca prueba en Staging y aprobación QA de Jason Robinson. No equivale a prueba del estado efectivo actual de producción.
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/52242

Historial del archivo en main muestra tres entradas: creación 40748, parámetro 43459, corrección 51987. El archivo conservó en el repositorio los tipos incorrectos durante septiembre 2025 y marzo 2026. No asumir fecha de introducción en producción: RCS-19380 ya describe campos personalizados de producción el 2 mayo 2025, antes del primer commit visible.
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles?path=/repo/44/system/ebr/smarttracksearches/sametendercard.search&version=GBmain&_a=history

Control Panel: https://usprod.apprissretailcloud.com/control devuelve Sorry, you have been blocked. Cloudflare Ray ID a3c941032b7b1e0e. No inspeccioné configuración efectiva, logs ni tareas desde ese portal.

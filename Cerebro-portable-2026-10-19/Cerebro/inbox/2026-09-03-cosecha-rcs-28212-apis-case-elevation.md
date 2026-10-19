---
fecha: 2026-09-03
fuente: cosecha de sesion local, RCS-28212 ticket resolution
sesion: local_fe6e5567-7400-4bc1-b3ef-44b95546c918
---

# RCS-28212, hipotesis con evidencia dura de capturas de pantalla

Las capturas de pantalla que llegaron cambiaron el diagnostico. Sigue siendo hipotesis, faltan dos
verificaciones dentro de APIS.

## Lo que las capturas muestran

El reporte 5165 filtra `case.event_type` con operador `=` contra el literal `Corporate`. El caso
`CA-44541-COR-2026-0001` guarda el valor `* COR`. Ese filtro lo excluye por construccion, no por un
bug del reporte.

El asterisco es la pista. Aparece en dos campos a la vez, `* COR` y `* CORPORATE EMPLOYEE`. La
aplicacion pinta el asterisco cuando el valor guardado no existe en la lista activa del dropdown del
tenant. El caso trae `Related incident: IN-44541-COR-2026-0001 (Elevated)` y el campo requerido
`Event Alpha Code` vacio. La hipotesis es que la elevacion de incidente a caso copia el codigo del
incidente sin mapearlo a la lista de casos.

## Verificaciones que faltan, pasos 3 y 4 del instructivo

Abrir el dropdown de Case Type en APIS y confirmar si `COR` esta o no en la lista del tenant.
Abrir `CA-43895-CORP-2026-0001` y confirmar que los casos buenos no vienen de una elevacion.

## Lo que Cerebro tenia y lo que no tenia

Los siete reflejos de troubleshooting de APIS que enseño Kristine estan en
`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md`, lineas 499 a 512. El acceso PROD por la
cuenta de Julie Barber esta en la linea 527. Nada en Cerebro ni en Confluence cubre case types de
APIS, COR, CORP, ni la elevacion incidente a caso. El espacio AALPS de Confluence tiene dos paginas
de 2021 y la principal apunta a un manual de administracion en el OneDrive de una cuenta desactivada.

## Que hacer y que no hacer todavia

El workaround que desbloquea al cliente hoy es cambiar el operador del reporte de `=` a `IN` con
`Corporate,COR`. Es trabajo de soporte, Juan tiene acceso PROD para hacerlo. La correccion de datos
exige escritura en base y es territorio de Kamminga.

No comentar al cliente todavia. El ticket sigue en Under Engineering Review con assignee de
Engineering. Comentar ahi repite el error que ya paso en RCS-28161. El instructivo trae el comentario
interno para Kamminga con cinco huecos que se llenan con lo que salga de los pasos 3 a 7.

Dato que acota la ventana: 7-Eleven migra a Incident alrededor de septiembre u octubre de 2026. La
ventana util de cualquier arreglo en APIS es de semanas, no de meses.

## Pendiente manual para Juan

Los PNG originales no se pudieron mover a `adjuntos/RCS-28212/` porque bash estaba denegado en esa
sesion. Arrastrarlos ahi a mano como `image-20260806-133803.png` y `image-20260806-134110.png`. La
descripcion en texto ya quedo guardada y buscable.

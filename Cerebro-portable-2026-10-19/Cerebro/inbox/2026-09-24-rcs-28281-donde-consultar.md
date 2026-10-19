# RCS-28281. Dónde verificar si llegó el lote del 8/12. Versión 2

Ahold es cliente 112, código AHL, GP9, esquema ardm_112. El contenedor de blob existe y se llama 112ahl, visto por Juan el 24 sep.

Verificado por Juan el 24 sep: la columna 21 del xlsx del 8/12 está en cero los 60 minutos, de 22:00 a 22:19 también, y 22:20 marca 281.

## 1. Blob 112ahl

El portal rechaza la clave de acceso: `listKeys/action` denegado. Tu usuario no puede leer con clave. Prueba con tu identidad.

1. En el portal, pulsa `Switch to Microsoft Entra user account`, encima de la lista. Si aparecen carpetas, entra a Archive, Prod, 2026, 08, 12.
2. Si sale un error de data action o de rol, abre Storage Explorer en el Bastion. Ve a Retail-Infra-Prod, Storage Accounts, stprdwus2shrdtlog, Blob Containers, 112ahl. El grupo de recursos Retail-Infra-Prod-US cuelga de esa suscripción.
3. Si Storage Explorer también rechaza, te falta el rol `Storage Blob Data Reader` sobre stprdwus2shrdtlog. Pídeselo a Viraj o a IT Helpdesk. Mientras llega, sigue con los pasos 2 y 3.
4. Dentro de la carpeta del día, anota cuántos `Ahold_TLOG_20260812*` hay, con hora y tamaño. Revisa también las carpetas 13 y 14.

## 2. Azure DevOps. Repo primero, pipeline después

1. Ve a Repos y busca `c112ahl`. Cambia a la rama `Production`.
2. Abre `ardm/python` y lee el script de carga. Busca la máscara de archivo y la tabla donde escribe. Si el script guarda el nombre del archivo en una columna, esa columna es la que usamos en GP9.
3. Abre el `.yaml`. Dice si la carga es Daily o Trickle y cada cuánto corre.
4. Ve a Pipelines, pestaña All, y filtra por `112`. Abre el job `c112ahl ARDM ... GP9` y mira sus corridas del 12 al 14 de agosto. Los logs duran cerca de un mes, así que lo más probable es que solo veas el estado de cada corrida.
5. Solo lectura. No relances nada.

## 3. GP9. Solo SELECT

Entra por RDP al jump LA4, 10.22.0.220, con credenciales trebu.co. Abre DBeaver con la conexión de producción de GP9, la que lleva appriss en el nombre.

Corre primero esta consulta. Ubica la tabla de transacciones y la columna que guarda el archivo:

```sql
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'ardm_112'
  AND (column_name ILIKE '%file%'
    OR column_name ILIKE '%batch%'
    OR column_name ILIKE '%insert%'
    OR column_name ILIKE '%end%'
    OR column_name ILIKE '%trans%date%')
ORDER BY 1, 2;
```

Pégame el resultado. Con los nombres reales arma esta consulta. Mira los bordes del hueco:

```sql
SELECT date_trunc('minute', <col_fin_transaccion>) AS minuto,
       <col_archivo>,
       MIN(<col_inserted>) AS primera_carga,
       MAX(<col_inserted>) AS ultima_carga,
       COUNT(*) AS transacciones
FROM ardm_112.<tabla_cabecera>
WHERE <col_fin_transaccion> >= '2026-08-12 20:20'
  AND <col_fin_transaccion> <  '2026-08-12 22:30'
GROUP BY 1, 2
ORDER BY 1, 2;
```

La consulta nombra el archivo que trajo el minuto 20:28 y el que trajo el 22:20. El hueco queda entre esos dos. Si la tabla no guarda archivo, `inserted` agrupa por corrida de carga y sirve igual.

## Cómo se decide

| Blob | GP9 | Lectura | Siguiente paso |
|---|---|---|---|
| Hay un archivo entre los dos bordes | Ventana vacía | Falla de carga interna | Reproceso con Data Team |
| No hay archivo entre los bordes | Ventana vacía | No llegó de DXC | ADUSA reenvía solo 8/12 20:29 a 22:19 |
| Sin acceso al blob | Bordes identificados | Parcial | Pregunta a Viraj por los archivos entre esas dos cargas |

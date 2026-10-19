---
name: reference_recreate_caseno_changelocation
description: "El bug de ChangeLocation que deja el case number viejo, la herramienta RecreateCaseNo.aspx que lo arregla, y cómo verificar que no se duplicó el caso"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-14T15:14:05.977Z
---

**El síntoma.** El usuario cambia la tienda de un caso en Incident/LPMS y el `Location #` sí cambia, pero el `Case No` sigue con el número de la tienda anterior. El cliente lo reporta como "cambié la ubicación varias veces y no pasó nada" y suele venir con miedo de que se haya duplicado o perdido el caso.

**La causa.** `ChangeLocation.aspx`, botón Save, revienta con 500 en `Incident.ArchiveManagers`, en `DAL.ExecuteNonQuery` sobre `DELETE FROM ManagerHistory WHERE MasterCaseID = @lvMasterCaseID`, con el error *"Unable to open configSource file 'App_Data\ConnectionStrings.config'"* (web.config línea 19). La actualización de ubicación ya quedó escrita, el renumerado del caso nunca corre porque el guardado aborta antes. Por eso cada reintento muere en el mismo punto. Visto en Ahold/adusa (Client ID 441) el 2026-08-04, DLL 5.3.0, RCS-28369. Code fix en ENG-7270.

Esto es problema de configuración o despliegue del sitio nettrack, **no de la migración de julio**, aunque el ticket lleve label `Uni_Jul_26_DataIntegrity`. Ver [[feedback_agrupar_no_es_causa_raiz]].

**El arreglo de datos** (lo corrió Matt Kamminga, no es de soporte L2 salvo que él lo autorice):

```
https://apps.apprissretail.com/<tenant>/nettrack/admin/RecreateCaseNo.aspx
```

Renumera **en sitio**, no clona. El sufijo cambia al siguiente correlativo de la tienda nueva, no conserva el anterior: en RCS-28369 pasó de `...-6510-22` a `...-6314-30`. **Hay que decírselo al cliente explícitamente** o va a pensar que es otro caso.

**Cómo verificar antes de confirmarle al cliente**, todo desde la UI, sin base de datos. Search For Incident (`nettrack/LPMS/CaseLog.aspx`):

1. Filtrar por `Location #` de la tienda nueva y comparar contra la captura del cliente cinco campos: incident date & time, incident type, case status, total value y case owner. Si los cinco calzan, es el mismo caso renumerado.
2. Poner el **número viejo completo** en `Case No`. Debe devolver cero filas.
3. Filtrar por la tienda vieja con el mismo owner y tipo de incidente. La grilla sale ordenada por fecha descendente, así que un duplicado aparecería en la primera fila. Si el más reciente es anterior al del caso, no hay duplicado.

**El campo `Case No` es de coincidencia exacta.** No acepta parciales. Buscar `6314-30` devuelve "No data to display" aunque el caso exista. Es fácil concluir mal por esto.

No usar Active Cases del Main Menu para buscar: cuenta solo los casos propios del usuario y marca 0.

Ver [[reference_jerarquia_ubicaciones_incident]], [[reference_screen_designer_rebuild]], [[reference_control_panel_admin]].

Borrador no publicado. Sin ID confirmado. Fuente: J.R., chat2 oct07:00/09:01 y llamada3,03:13 a03:43. Tabla candidata por historial local, sin consulta actual ADUSA. Informe: investigaciones/2026-10-02-adusa-save-y-fechas-screen-designer.md.

Title: Incident Screen Designer does not maintain the last saved timestamp in the database while the last build timestamp is populated

Problem: During RCS-29234, J.R. reported that the database timestamp for saving screen configuration is not populated or updated, while the build timestamp is available. On October 2 he clarified that the save date is not displayed in the GUI. In the customer call, he explained that missing metadata prevents Support from distinguishing saved changes from built changes.

Expected: A successful screen configuration save records an accurate last saved timestamp. Build metadata remains accurate for successful builds. Confirm the intended timestamp behavior for Save and Save and Build with the product owner.

Actual: Support reports missing or stale save metadata while build metadata is populated. The affected row and current database values still need to be attached. Historical schema evidence identifies incident.ScreenMaster.LastSavedDate and LastBuildDate as candidates; confirm these in the affected environment.

Validation needed: In an approved test environment, capture screen identifier and timestamps before and after Save, then before and after Save and Build. Include action time and timezone, persisted configuration, and database evidence for both timestamps. These validation steps have not yet been executed for this report.

Impact: Incomplete change history makes troubleshooting and correlation with configuration changes unreliable. No causal link between this metadata issue and the RCS-29234 case save failure has been established.

Related context: RCS-29234. ENG-556 concerns build date timezone display and is not an exact duplicate. No exact duplicate was identified in the searches performed. J.R. requested filing this defect on October 2; confirm whether an issue was created under another title before submitting. No fix date is committed.

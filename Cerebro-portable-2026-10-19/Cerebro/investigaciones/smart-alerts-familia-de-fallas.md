# Smart Alerts: siete mecanismos distintos bajo el mismo sintoma

Escrito el 8 sep 2026 a partir de lo que ya estaba en la base. 46 de las 443 fichas de ticket
hablan de Smart Alerts, el 10%. Ninguna entrada de `flujos/INDICE.md` ni de
`investigaciones/INDICE.md` cubria el tema hasta hoy, asi que cada caso se investigaba de cero.

El cliente siempre reporta lo mismo: "las alertas no llegan". Debajo hay siete mecanismos que no
comparten causa, ni arreglo, ni dueño. Empieza por el discriminador.

## Discriminador. Cuatro preguntas antes de investigar

1. **¿La alerta existia y dejo de salir, o nunca salio?** Dejo de salir apunta a los mecanismos 3,
   4 y 7, todos ligados a un cambio de plataforma con fecha. Nunca salio apunta a 1 y 5.
2. **¿El cliente edito la configuracion de la alerta antes de que fallara?** Si edito tipos de
   auditoria en una alerta existente, es el mecanismo 1, y la UI le mintio.
3. **¿El sintoma es intermitente o con retraso de un dia?** Retraso de un dia es el mecanismo 6,
   frontera UTC. Intermitente sin patron horario apunta al 2.
4. **¿La alerta depende de un adjunto o de un documento de impresion?** Si depende, mira 3 y 4
   antes que nada.

## 1. `ManageSmartAlerts.aspx` no regenera `FiltersSQL`

**Sintoma.** El cliente edita los tipos de auditoria de una alerta ya configurada, la UI acepta el
cambio y lo muestra guardado, y la alerta nunca dispara para los tipos nuevos.

**Causa, confirmada.** La pagina no regenera las columnas `Filters` ni `FiltersSQL` de
`dbo.SmartAlertConfig` al guardar. La base conserva el filtro viejo. Fallo silencioso: no hay error
en pantalla ni en log.

**Evidencia.** Tyrone Whitney lo reprodujo dos veces de forma independiente, el 17 de junio y el 2
de julio, con el mismo resultado. Afecta las ocho alertas SSVR de PPG, `SmartAlertConfigID` 33 a 40.
Impacto acumulado de casi cuatro meses sin alertas desde el 6 de mayo de 2026.

**Alcance.** No es exclusivo de PPG. Cualquier tenant que edite tipos de auditoria en una alerta
existente sufre lo mismo. Ryan Barlow dijo el 2 de julio que no lo habia visto en otros clientes.
Tyrone lo reprodujo dos veces el mismo dia.

**Estado.** RCS-27407, PPG, reporter Annie Brown. Fix de codigo bajo ENG-8117. Engineering no toma
el desarrollo, Support lo ejecuta, autorizado por Shandana Khan el 1 sep 2026. Queda confirmar repo
y pipeline para netTrack legado, que la guia de code change no cubre.

**Trampa.** El primer intento de Tyrone fue corregir desde la UI el 17 de junio y dio el ticket por
resuelto. Annie reporto el 22 que seguia sin llegar. Corregir desde la UI reproduce el bug.

## 2. `SendSmartAlert.aspx` agotando el tiempo de la peticion web

**Sintoma.** Alertas intermitentes, lentitud general de la aplicacion, entrada de casos que se
recupera sola.

**Medicion.** El 31 de julio de 2026, entre las 20:30 y las 22:35 UTC, el app service de netTrack
acumulo cerca de 2495 client timeouts contra 255 errores HTTP 500. 248 de esos 500 cayeron en un
solo endpoint, `POST /nettrack/api/internal/SendSmartAlert.aspx`.

**Lectura, no confirmada por logs.** Juan la marco como suya: la proporcion apunta a timeout de
peticion web y no a command timeout de SQL, porque un command timeout saldria como 500 con excepcion
y ese volumen no aparece. Nadie ha separado los timeouts por tenant. Eso sigue ofrecible.

**Cruce que vale nombrar.** RCS-28106 de Santikos, Critical, y la degradacion de Stater Bros en
RCS-28112 son el mismo endpoint visto desde dos lados.

## 3. Adjunto o documento de impresion ausente en el blob

**Causa.** La subida a blob tenia un tope de 4 MB, sin relacion con archivos bloqueados por tipo.
Las Smart Alerts fallaban por esa misma causa aguas arriba, porque la alerta no encontraba el
adjunto.

**Estado.** Liberado a produccion el 13 ago 2026. A Support le toca verificar que el monitoreo de
Smart Alerts quedo en pie. Cadena de comunicacion escrita en la pagina: Matt, luego Support, luego
el cliente.

## 4. Rutas de adjunto rotas en modo Platform Cohesion

**Causa, dos bugs en `Sources/Incident/Components/LPSBO/SmartAlert.vb`.**

Linea 703. El guard de separador final solo revisaba `\`. En Platform Cohesion las rutas usan `/`,
asi que el codigo agregaba `\` encima y producia rutas invalidas del tipo
`/incident/411/lpms/\filename.pdf`. Falla el lookup del adjunto.

Linea 1106, mas las ramas Case y HR alrededor de L1433 y SRMS alrededor de L1475. El codigo llamaba
`FileLen(strPath)` en vez de `AzureFilesystem.GetBlobSize(strPath)`. En Cohesion los archivos viven
en Azure Blob Storage. `FileLen` mira el filesystem local, tira file not found y descarta el adjunto
en silencio.

**Patron que nombra Engineering.** "Blob storage gate pattern failure": codigo que condiciona en
`IsPlatformCohesionMode()` en algunas ramas y no en todas. Busca ese patron antes de descartar.

**Estado.** ENG-6612, Matthew Kamminga, PR 55537, liberado en Secure August 2026 Release 1/2 el 13
ago 2026. Resolvio RCS-28106 de Santikos.

## 5. Quick Entry sin cookie `cpf`

**Causa.** Los usuarios que entran por Quick Entry no reciben la cookie `cpf` y no autentican al
iniciar sesion. La alerta no se crea ni se envia.

**Estado.** ENG-7359, "Smart Alert not working with Quick Entry", Matthew Kamminga, creado el 17 ago
2026, en Backlog. Describe el mecanismo sobre el caso 48786. Conecta con la medicion de 308 cuentas
con `LastLoginDate` nulo.

## 6. Frontera de fecha UTC

**Sintoma literal del cliente.** "trigger until the following day".

**Mecanismo.** El guardado ocurre a las 5:23 PM hora del Pacifico, que en contexto UTC cae despues
de medianoche. El caso queda del lado del dia siguiente y la alerta sale en la corrida de la mañana.

**Estado.** RCS-28294, Vallarta, reporter Tatiana Barcenas. Hipotesis H1, encaja con el sintoma
literal. La H2 alternativa es el envio sincronico que falla y reintenta, apoyada en la medicion del
mecanismo 2. Los pasos de reproduccion completos, con precondiciones, ocho pasos numerados y query
de verificacion, estan en el comentario del 26 de agosto. No existe ENG auto creado para este
ticket, verificado con barrido del proyecto ENG.

## 7. La alerta REASSIGN borrada por un PR

**Causa.** El PR 56138, ENG-7192-Part2, mergeado el 14 ago 2026, borro el bloque completo de
`ReAssignCase.aspx.vb` que leia `Options.EmailOnReassign` y llamaba a
`CreateAlertInQueue("REASSIGN", ...)`. El correo de reasignacion se dispara como un SmartAlert de
tipo REASSIGN encolado por esa llamada.

**Alcance.** Multi cliente, escrito asi por Diego. Bunnings confirma que no fue un caso aislado de
ADUSA. Cualquier tenant con `EmailOnReassign` activo y reasignaciones frecuentes pierde visibilidad
de SLA en cada reasignacion desde mediados o finales de agosto.

**Estado.** RCS-28795.

## Casos abiertos sin mecanismo asignado

**RCS-28452, SpartanNash.** Sebastian Rueda. Mismo string de error "TempArea" que ENG-2154.

El precedente ENG-2154 se resolvio en Secure May 2026 Release 2/2. `ASPxUploadControl` tenia
`AdvancedModeSettings-TemporaryFolder="~/TempArea"` fijo en el markup. En Azure App Service
`~/TempArea` resuelve a `C:\home\site\wwwroot\nettrack\TempArea`, ruta que no existe. El fix movio
la asignacion a `Page_Init` chequeando `LPSDAL.GlobalAppConfiguration.RunningInAzure`. El archivo
afectado fue `CAMSImportAudit.aspx`, no `SmartAlert.vb`.

El patron compartido es ruta temporal mal resuelta en Azure y en Cohesion. Es punto de arranque de
la investigacion, no causa confirmada para RCS-28452. Sin respuesta desde el 19 de agosto, follow up
pendiente a Jason Mann.

**RCS-28131, Sportsman's.** Smart Alerts dejaron de funcionar tras la migracion de base de datos.
Etiquetado `Uni_Jul_26_AlertsNotifications`. Sin categoria que lo cubra en la clasificacion de la
Unificacion.

## Donde vive cada cosa

| Que | Donde |
|---|---|
| Causa de `FiltersSQL`, texto completo del hallazgo | chunk 1712, carpeta 16, y `tickets/RCS-27407.md` |
| Medicion de los 248 errores 500 en `SendSmartAlert.aspx` | `brain/markdown/16-rcs-soluciones.md` |
| Los dos bugs de `SmartAlert.vb` y el precedente ENG-2154 | chunk 1754, cosecha del 27 ago 2026 |
| Tope de 4 MB en el blob y la cadena de comunicacion | `brain/memoria/reference_unificacion_patrones.md` |
| Hipotesis H1 y H2 de la frontera UTC | chunk 1728, y `tickets/RCS-28294.md` |
| El PR que borro la alerta REASSIGN | chunk 1752, y `tickets/RCS-28795.md` |
| Etiquetas de la Unificacion que tocan alertas | `brain/markdown/19-rcs-procesos-playbook.md` |

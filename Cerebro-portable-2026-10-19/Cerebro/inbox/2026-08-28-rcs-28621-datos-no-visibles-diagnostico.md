# RCS-28621 — Sebastian cargo el archivo, la clienta no ve los datos. Diagnostico

Fecha: 28 ago 2026. Pregunta de Juan: Sebastian reporto el import exitoso, Cathryn Garcia dice que
no ve los empleados nuevos, RCS-25389 es el ticket enlazado y esta cerrado con el mismo patron de
carga manual. Que pudo fallar.

## Estado verificado en Jira

RCS-28621 sigue en Work in progress. Cathryn Garcia comento a las 13:43 del 28 ago:

> "I spot checked and am not seeing newly hired TM's populate. For example, I don't see any results
> for TM #1012863. Is it possibly still loading?"

Sebastian habia comentado a las 12:29:

> "Import was completed via LPImport.exe on the QA-LPMS-RDP-001 Bastion (Employee Import tab, Comma
> delimiter, "Use Employee ID as key"). Test import result: [# updated 27178 / # created 6674].
> Final import result: [# updated 27178 / # created 6674]."

## Hipotesis principal. Import corrido desde la maquina equivocada

Viraj Kansara cargo el archivo gemelo, RCS-28622, el mismo dia. Su log declara la ruta del INI:

    C:\Users\vkansara\The Retail Equation, Inc\LP Software - Clients\Advance Auto\LPMS\LPMS.INI

Esa ruta esta bajo el perfil personal de Viraj. La carpeta "LP Software - Clients" es la carpeta de
cliente sincronizada en la maquina de cada agente, con el LPMS.INI que apunta a la base de datos de
ese cliente especifico.

Sebastian declara un origen distinto. Corrio LPImport.exe en QA-LPMS-RDP-001, un Bastion de Azure.
La base de conocimiento describe ese Bastion con acceso de grupo `qa-lpms-rdp_Reader_Bastion_Access`,
alcance de lectura y QA. Fuente: `brain/markdown/13-appriss-onboarding-base-de-conocimiento.md`,
seccion "Acceso a logs de LPMS / nettrack via Azure Bastion".

La bitacora de esta manana ya habia marcado el riesgo antes de que Sebastian ejecutara nada:

> "Sebastian no aparece con historial de imports en esta lista. Antes de que Sebastian lo ejecute,
> confirmar que tiene el acceso [a LP Software - Clients de Advance Auto]."

Sebastian no tiene esa carpeta sincronizada. Corrio la herramienta desde el Bastion compartido en su
lugar. El runbook exige verificar la base de datos en el encabezado de LPImport.exe antes de
importar, paso 3 de "Manual Workarounds - LPMS", Confluence RTS 474897482599. El comentario de
Sebastian no menciona esa verificacion. Si el LPMS.INI que encontro en esa maquina compartida
apuntaba a una base distinta a la produccion de Advance Auto, el import corrio limpio y escribio en
el lugar equivocado. Los conteos que reporta, 27178 actualizados y 6674 creados identicos entre Test
y Final, son compatibles con un import real contra una base que no es la que la clienta consulta.

Esto no esta confirmado. Falta que Sebastian confirme el nombre de la base que vio en el encabezado
de la herramienta cuando corrio el import.

## Correccion y precision, con la llamada con Kiran Vadday del 3 ago 2026

La base de conocimiento marcaba el Bastion qa-lpms-rdp-001 como alcance de lectura y QA. Esa
etiqueta corresponde solo al grupo AAD `qa-lpms-rdp_Reader_Bastion_Access`, dedicado a leer logs. El
mismo Bastion tiene otro camino de acceso, listado en `brain/markdown/17-reuniones-prep.md` bajo el
request de acceso de Vedant Shirude:

    Azure Bastion / RDP (qa-lpms-rdp-001)
    Database Access (MSSQL Prod):
    pd-lpms-uswest2-sqldb-001
    pc-lpms-canadacentral-sql-001
    pe-lpms-northeurope-sql-001

`pd-lpms-uswest2-sqldb-001` es la base de produccion de LPMS para US West, la region de Advance
Auto Parts. El Bastion qa-lpms-rdp-001 si es un camino valido hacia produccion. El nombre "QA" es
enganoso, no indica el entorno del dato.

Kiran Vadday describe el mismo camino en la llamada del 3 ago 2026, minuto 54:58, hablando de su
propia sesion en un jump server equivalente, PLAFRMTRDP01:

> "VPN step one, activation step two, RDP step three, and then in the RDP you can connect to SQL MI,
> PD, whatever that thing is, and you have to production and here is my staging that which I play
> with."

El dato que importa es ese ultimo tramo. Conectado al mismo RDP, Kiran tiene a la vista produccion y
staging al mismo tiempo, y elegir uno u otro es una accion manual, no algo que el acceso resuelve
solo. Este patron se repite en el jump server PLAFRMTRDP01 hacia SQL MI, documentado en
`brain/markdown/17-reuniones-prep.md` lineas 1037 a 1046.

La hipotesis principal queda mas precisa. El riesgo no es que qa-lpms-rdp-001 sea un entorno de QA
sin salida a produccion. El riesgo es que desde ese mismo acceso hay mas de un destino disponible,
produccion y staging, y el runbook de LPMS pide verificar el encabezado de LPImport.exe
precisamente porque esa eleccion no es automatica. Sebastian no reporta haber hecho esa
verificacion. Viraj, al correr LPImport.exe desde el LPMS.INI bajo su perfil personal apuntado ya al
cliente Advance Auto, se salta esa ambiguedad por construccion. Sebastian, sin esa carpeta
sincronizada, no tenia esa garantia.

## Confirmacion directa, captura de pantalla de Juan

Juan comparte una captura de LPImport.exe abierto. El encabezado de la ventana dice:

    LPMS Import (Version 6.50.3840) Database: AALPS-QA (60)

Esto ya no es hipotesis. El runbook exige exactamente esa verificacion en el paso 4: "ensure that
the Database reflects the client you're looking to do the import for (at the top of the LPImport.exe
tool)". El encabezado muestra AALPS-QA (60), una base QA, no la produccion de Advance Auto Parts.
El import de Sebastian se ejecuto contra esa base QA. Por eso Cathryn no ve los empleados nuevos en
produccion.

La captura muestra ademas el origen del archivo: `C:\Users\gsarces\Downloads\LPMS Em...`. El runbook
pide en el paso 3 dejar el archivo en la ruta `LP Software - Clients > Advance Auto > Imports`, la
carpeta publica del cliente. Sebastian trabajo con su propia copia en Downloads, fuera de esa ruta.
Esa desviacion del paso 3 explica por que tambien se salto el paso 4 sin notarlo, la instancia de
LPImport.exe que abrio no era la del cliente correcto.

## Precedente que resuelve sin la carpeta OneDrive. RCS-25133

Juan no tiene sincronizada "LP Software - Clients" y no puede entrar a otra cuenta que la tenga.
RCS-25133 ya resolvio exactamente esta situacion, del lado del cliente, no de un agente, pero la
mecanica es la misma herramienta.

Cathryn no podia instalar LPImport en su laptop nueva por politica de InfoSec. Dean Korbakis le
adjunto el ejecutable portable directo en el ticket, `LPImport6.50.3839.exe`, 1888256 bytes, 1.8 MB.
Coincide en tamano con el archivo de la captura de Juan. Instruccion textual de Dean:

> "It automatically will run without an install process, but you will need to copy over the
> lpms.ini file from your old machine and place it into your C:Windows folder on the new machine."

LPImport.exe es portable. No requiere instalacion ni la carpeta OneDrive de nadie. Lo unico que fija
la base de datos a la que se conecta es el archivo `lpms.ini` que este en `C:\Windows` junto al
ejecutable. Sin ese INI, o con uno de otra sesion, el header muestra lo que sea que diga ese archivo,
en el caso de Sebastian, AALPS-QA.

Camino sin la carpeta de Viraj y sin otra cuenta: pedirle a Viraj el `lpms.ini` que uso para el
gemelo RCS-28622, apuntado a produccion de Advance Auto. Copiarlo a `C:\Windows` en la maquina o
sesion donde se va a correr el import. Abrir el LPImport.exe portable. Verificar que el header ya no
diga AALPS-QA.

## El lpms.ini de Juan, leido completo

Juan comparte el contenido real del archivo en `C:\Windows\lpms.ini`. Primera linea:
`# Managed by saltstack.` Esto no es un archivo de Advance Auto mal configurado. Es un archivo
distinto por completo.

    LPDatabase=AALPS-QA
    LPDATAPATH=lpmsdb1.lpguys.net,1433
    PROGRAMPATH=F:\IIS\Clients\qa450\windows
    LPDOCPATH=F:\IIS\Clients\qa450\windows\Docs
    SAMLLPMSLOGINURL=https://login-test.lpguys.net/login_qa450/login.php
    MOBILEWEBSERVICE=https://test.lpguys.net/qa450/nettrack/api/mobileservice.asmx
    ClientID=

`qa450` es el tenant de staging para regression, documentado en
`brain/markdown/13-appriss-onboarding-base-de-conocimiento.md`, Parte VII 7.4, junto a `QaAuto`
como el otro entorno de pruebas. No es una copia QA de Advance Auto. Es el entorno generico de
pruebas que usa cualquier equipo para regression testing. `ClientID` esta vacio, otra senal de que
este archivo no esta atado a ningun cliente real. Cambiar solo `LPDatabase` no alcanza, cada ruta
del archivo apunta a `qa450`, URLs de login y de mobile service incluidas.

El comentario `Managed by saltstack` es una advertencia operativa. Este archivo lo despliega un
sistema de gestion de configuracion, probablemente igual en varias maquinas. Editarlo a mano puede
revertirse solo, y dejarlo modificado puede romper el testing de regression de otro equipo en esa
misma maquina.

## El proceso correcto para corregir esto

1. Sebastian cierra esta sesion de LPImport.exe sin volver a importar nada mas ahi. El import ya
   corrido contra AALPS-QA (60) queda como dato a revisar aparte, no a repetir en esa base.
2. Antes de tocar nada, copiar el `lpms.ini` actual de `C:\Windows` a otra carpeta como respaldo.
   Es el archivo managed by saltstack, hay que devolverlo a su lugar despues.
3. Pedirle a Viraj el contenido completo de su `lpms.ini` de Advance Auto, el mismo que uso para el
   gemelo RCS-28622. Necesita traer los valores reales, `LPDatabase`, `LPDATAPATH`, `PROGRAMPATH`,
   `ClientID` y las llaves de cifrado de ese entorno. Copiar y pegar el contenido, no solo la ruta.
4. Reemplazar el contenido de `C:\Windows\lpms.ini` por el de Viraj.
5. Abrir el LPImport.exe portable que ya tiene Juan. Verificar que el header ya no diga AALPS-QA y
   que muestre la base de produccion de Advance Auto con el ClientID correcto.
6. Confirmar que el archivo `LPMS Employee File - For Import - 8.12.26.csv` es el que se va a
   cargar, el mismo adjunto del ticket.
7. Correr el import completo. EE Import, delimitador Comma, cargar el archivo, Save, apuntar Log
   File Location al propio usuario, correr Test Import y leer el log. Cerrar y reabrir el LPImport.exe,
   verificar los campos y correr Import.
8. Confirmar el TM #1012863 en la base de produccion antes de contestarle a Cathryn.
9. Devolver el `lpms.ini` original de saltstack a `C:\Windows` desde el respaldo del paso 2, para
   no dejar esa maquina apuntada a Advance Auto si otro equipo la usa para regression testing.
10. Reportar aparte, sin mezclarlo con la respuesta al cliente, que 56113 registros de empleados de
    Advance Auto quedaron cargados en AALPS-QA. Es dato de produccion en una base de staging
    compartida. Vale que Engineering o QA decidan si eso hay que limpiarlo.

## Hipotesis secundaria. El registro cae en el lote con dato inconsistente

El mismo comentario de Sebastian marca un lote separado dentro del archivo:

> "Flagged for awareness: ~6,645 records show Pay Status = 'Active' with a Termination Date
> populated (inconsistency in source data, not a blocker)."

TM #1012863 es un empleado nuevo, no deberia tener Termination Date. Esta hipotesis pesa menos que
la primera porque Sebastian reporta "not a blocker" y su conteo de creados, 6674, es casi identico
al tamano de ese lote inconsistente, 6645. La cercania entre los dos numeros vale la pena revisar,
puede ser coincidencia o puede ser la misma poblacion.

## Por que RCS-25389 no aplica como precedente de causa

RCS-25389 fija el canal, RCS abre el ticket y Soporte carga el archivo, no fija el procedimiento
tecnico del import ni documenta una falla de datos. Cerro en febrero de 2026 sin que Cathryn
reportara nunca un caso de datos ausentes tras una carga. El patron que se repite entre RCS-28621 y
RCS-25389 es el canal de trabajo, no un sintoma tecnico compartido. Preguntar "que fallo en esta
carga especifica" no tiene respuesta en RCS-25389.

## Que verificar antes de responderle a la clienta

1. Confirmado con la captura de Juan. El import corrio contra AALPS-QA (60), no contra produccion.
2. Repetir el import contra la base de produccion siguiendo el proceso de la seccion anterior, y
   guardar el nuevo log.
3. Buscar a TM #1012863 en el CSV fuente, `LPMS Employee File - For Import - 8.12.26.csv`, confirmar
   si cae en el lote de ~6645 registros con Pay Status Active y Termination Date poblado. Revisar
   esto aun despues de corregir la base, por si se suma un segundo problema.
4. Confirmar si Sebastian tiene o no la carpeta "LP Software - Clients" de Advance Auto sincronizada
   en su propia maquina. Si no la tiene, pedirle a Viraj que corra el employee file en su sesion,
   igual que hizo con el location file en RCS-28622.

## Fuentes

RCS-28621, RCS-28622, RCS-25389 en Jira, comentarios del 27 y 28 ago 2026.
`brain/markdown/13-appriss-onboarding-base-de-conocimiento.md`, acceso Bastion QA-LPMS-RDP-001.
`brain/markdown/17-reuniones-prep.md`, request de acceso de Vedant Shirude con la lista de bases
MSSQL Prod, y llamada con Kiran Vadday del 3 ago 2026, minuto 54:58.
`inbox/2026-08-28-rcs-28621-quien-carga-el-archivo.md`, bloqueador operativo registrado antes del
import.
Confluence RTS 474897482599, "Manual Workarounds - LPMS", texto completo obtenido en vivo.
Captura de pantalla de Juan, LPMS Import Version 6.50.3840, Database AALPS-QA (60).
RCS-25133 en Jira, comentarios de Dean Korbakis del 22 y 23 ene 2026, adjunto LPImport6.50.3839.exe.

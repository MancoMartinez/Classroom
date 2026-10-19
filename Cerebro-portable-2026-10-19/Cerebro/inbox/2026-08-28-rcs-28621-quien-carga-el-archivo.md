# RCS-28621 — Import Employee File for Incident (AAP). Quién ejecuta la carga

Fecha: 28 ago 2026. Pregunta de Juan: el ticket pide cargar un archivo manualmente, hay un ticket
enlazado, y no está claro si lo hace Soporte o se escaló a otro equipo.

## Respuesta

Lo hace Soporte. No se escala. El precedente que lo cierra es del mismo día y del mismo cliente.

## Estado verificado en Jira

| Ticket | Qué | Estado | Assignee |
|---|---|---|---|
| RCS-28621 | AAP employee file para Incident | Work in progress | Sebastian Garces |
| RCS-28622 | AAP location file para Incident | Closed, Resolved | Viraj Kansara |
| RCS-25389 | El ticket enlazado, alta de SFTP | Closed, Resolved | Kathryn Scheldberg |
| RCS-27345 | AAP employee file, junio | Closed, Resolved | BJ Probert |
| RCS-25133 | AAP, LP Import Tool no instalable | Closed, Resolved | Dean Korbakis |

## Evidencia 1. El gemelo ya se cargó, y lo cargó Soporte

RCS-28622 llegó 40 minutos después de RCS-28621, mismo reporter, el archivo hermano. Viraj Kansara
lo ejecutó hoy 28 ago a las 14:31 y pegó el log:

    Start import: 8/28/2026 2:31:47 PM
    INI File    : C:\Users\vkansara\The Retail Equation, Inc\LP Software - Clients\Advance Auto\LPMS\LPMS.INI
    Stores Updated: 4224
    Stores Created:  24
    STATUS:08/28/2026:PASS

Cerró con Resolution `Support Resolved - Performed Customer Requested Operation`. La ruta del INI
está bajo el perfil de Viraj, o sea corrió LPImport.exe desde su propia máquina contra la carpeta
LP Software - Clients de Advance Auto.

## Evidencia 2. El ticket enlazado no escala nada, define el canal

RCS-25389 no es una escalación pendiente. Es el ticket donde se acordó el canal. Katy Scheldberg,
Implementation Manager, cerró así el 13 feb 2026:

> "Until that time, open a RCS ticket with your new files and we will manage moving the files to the
> appropriate location to run the load process manually."

Y la clienta eligió esa vía el mismo día:

> "I think for now the best option is to send the location file and employee file in an RCS ticket
> and request them be manually loaded into Incident. I only update the employee file about once a
> quarter."

El SFTP automatizado quedó como plan futuro, condicionado a que el equipo de IT de AAP empuje los
archivos. Mientras eso no pase, cada archivo entra por un ticket RCS y lo carga Soporte.

## Evidencia 3. El precedente idéntico de junio

RCS-27345, mismo pedido de employee file, BJ Probert lo ejecutó sin escalar:

> "This has been imported with no errors - how does it look on your end?"

Cerró con la misma Resolution después de que la clienta confirmó por spot check. En abril se repitió
con RCS-26462 y RCS-26464, mismo cliente, misma dupla employee y location, ambos cerrados por
Probert.

## Evidencia 4. Confluence lo tiene tabulado como trabajo de Soporte

Página RTS 478005657601, "2026 Customer-Requested Imports — RCS (Incident / Audit)":

> "This page lists retailers who requested Support to conduct data imports/uploads during the first
> half of 2026 [...] Total kept: 72 tickets across 11 customers"

Advance Auto Parts aparece con 4 tickets, tipos Employee y Location, producto Incident. DHL lidera
con 28 y Luxottica con 19. Setenta y dos cargas en seis meses. Es trabajo rutinario de la mesa.

## El procedimiento

Runbook: Confluence RTS 474897482599, "Manual Workarounds - LPMS", sección Store, Employee & User
File Import. Está en estado archived, sigue siendo el único paso a paso que existe.

1. Entrar al Bastion y ubicar la carpeta LP Software - Clients.
2. Ir a LP Software - Clients, cliente, Imports y confirmar que el archivo está ahí.
3. Ir a LP Software - Clients, cliente, LPMS y abrir LPImport.exe en su última versión. Verificar
   que la base de datos que muestra el encabezado de la herramienta es la del cliente correcto.
4. Elegir EE Import para el employee file, Store Import para el location file.
5. Antes de importar, revisar el archivo. Confirmar que es tab delimited y que cada registro es un
   ítem nuevo.
6. Apuntar el Log File Location a tu propio usuario. Guardar.
7. Correr Test Import y leer el log. Si la diferencia de números es enorme, preguntarle al cliente
   antes de seguir.
8. Cerrar y reabrir LPImport.exe, verificar los campos y correr Import.
9. Si el import arroja errores, devolverle los errores al cliente para que corrija y reenvíe.
10. Pegar el log al ticket, pedir confirmación al cliente, cerrar con
    `Support Resolved - Performed Customer Requested Operation`.

Contexto de la herramienta, de RCS-25133: la clienta usaba LP Import Tool 6.5.3837 en su laptop y su
InfoSec dejó de aprobarla. Dean Korbakis le pasó el ejecutable portable y le advirtió que hay que
copiar el lpms.ini a C:\Windows. Ese fue el disparador de todo el hilo. Las clásicas se están
retirando, palabras de Korbakis: "we are retiring the old classic applications and are no longer
providing support for any bug related issues that may arise".

## Discrepancias que hay que resolver antes de cargar

1. La descripción de RCS-28621 dice "Please import the attached **location** file into Incident".
   El adjunto es `LPMS Employee File - For Import - 8.12.26.csv`. El summary dice Employee. El
   location file ya se cargó en RCS-28622 con el archivo del 8.27.26. Manda el adjunto y el summary.
   La palabra "location" en la descripción es copia y pega de la plantilla.
2. El archivo del ticket lleva fecha 8.12.26, quince días antes del ticket. El location file que
   Cathryn adjuntó al gemelo lleva fecha 8.27.26. Vale confirmar con ella si el employee del 12 de
   agosto es el vigente o si tiene uno más nuevo.
3. Pesa 12.3 MB contra 1.0 MB del location file. Es diez veces el otro. Revisar el conteo de
   registros en el Test Import antes de correr el Import real.

## Lo que falta en Cerebro

No existe ficha de RCS-28621 ni de RCS-25389 en `tickets/`. No existe flujo en `flujos/` para
"import attached file". El runbook de arriba hay que guardarlo en carpeta 19, RCS Procesos y
Playbook. Los archivos `asignaciones/2026-08-27.md` e `inbox/2026-08-28-cosecha-asignacion-reglas.md`
ya habían marcado este ticket como "sin procedimiento resuelto". Ya lo hay.

## Bloqueador operativo real

El paso 1 pide acceso al Bastion y a la carpeta LP Software - Clients de Advance Auto. Viraj Kansara
la tiene sincronizada y corrió el import hoy. Sebastián no aparece con historial de imports en esta
lista. Antes de que Sebastián lo ejecute, confirmar que tiene el acceso. Si no lo tiene, la ruta
corta es pedirle a Viraj que corra el employee file en la misma sesión, ya tiene el LPMS.INI de
Advance Auto abierto.

## Fuentes

RCS-28621, RCS-28622, RCS-25389, RCS-27345, RCS-25133 en Jira.
Confluence RTS 478005657601, RTS 474897482599.

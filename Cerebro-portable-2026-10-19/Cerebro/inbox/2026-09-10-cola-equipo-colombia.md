# Cola del equipo Colombia, 10 sep 2026

88 tickets abiertos entre seis personas. Fuente: Jira en vivo, statusCategory != Done.
Roster tomado de brain/memoria/project_appriss_support_team.md. David Vargas salio el 25 ago.

## Carga por persona

La columna que decide es carga activa, no abiertos. Esperar al cliente no es trabajar.

| Persona | Abiertos | Activa | Esperando cliente | High+ | Mas de 90 dias | Quietos +14d |
|---|---|---|---|---|---|---|
| Juan Martinez | 20 | 9 | 11 | 4 | 0 | 2 |
| Sebastian Rueda | 19 | 13 | 6 | 2 | 4 | 6 |
| Diego Buelvas | 17 | 7 | 10 | 3 | 0 | 1 |
| Edwin Garzon | 15 | 8 | 7 | 1 | 2 | 2 |
| Luis Hernandez | 10 | 6 | 4 | 0 | 0 | 0 |
| Sebastian Garces | 7 | 4 | 3 | 0 | 0 | 0 |

Sebastian Rueda concentra la carga activa real, los cuatro tickets de mas de 90 dias y seis
de los once quietos del equipo. Diego tiene 17 abiertos con solo 7 activos.

## Estados globales

    Under Customer Review          41
    Work in progress               23
    Under Support Review           11
    Waiting for Software Release    6
    Resolution Suggested            3
    Under Delivery Review           2
    Under Infrastructure Review     1
    Escalated                       1

47 por ciento de la cola espera al cliente.

## Quietos mas de 14 dias, once tickets

    50d  Rueda   RCS-27927  Under Support Review    Appriss Internal 033 hft data duplication
    45d  Rueda   RCS-26632  Work in progress        Appriss Internal 171 WEG duplication
    42d  Rueda   RCS-27699  Waiting for Software    Alshaya Delivery Charge as Gift
    37d  Juan    RCS-27676  Under Customer Review   RLC SFTP IP/Hostname Change
    32d  Rueda   RCS-27344  Under Support Review    Appriss Internal 049 GAP duplication
    28d  Diego   RCS-28060  Waiting for Software    SBX NA open investigations
    20d  Edwin   RCS-28274  Under Delivery Review   TG Jones Original Transaction Amount
    16d  Rueda   RCS-27973  Work in progress        GAP cancelled orders data sync
    15d  Rueda   RCS-28452  Under Support Review    SpartanNash PDF Associate Theft
    15d  Juan    RCS-28099  Under Customer Review   CWH HYP to RCS Item Discount Logic
    15d  Edwin   RCS-26878  Under Support Review    Loblaw Wallet ID not populating

Cuatro de los cinco tickets de duplicacion Appriss Internal son de Rueda y ninguno se ha
movido en un mes. Se parecen entre si. Revisar si son el mismo defecto.

## Entradas de hoy

    RCS-28871  Juan   Medium  Walgreens Peak Season Readiness 3rd party connect
    RCS-28876  Rueda  High    Advanced Auto Parts error al acceder
    RCS-28873  Rueda  High    Sbux NA searches con error y lentitud general

Rueda recibio los dos High del dia teniendo ya la carga activa mas alta del equipo.

## Compromisos

Decidir si los tickets de duplicacion Appriss Internal se agrupan en una sola investigacion.
Evaluar reparto: Luis Hernandez y Sebastian Garces tienen margen, Rueda no.

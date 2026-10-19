---
ticket: RCS-28638
tipo: prompt para la sesion de Claude Code en C:\git\SnowTime\SnowTime
mcps_disponibles: snowflake-eu, snowflake-us, azure, dataloader-eu, dataloader-us
---

# Prompt para la sesion de Claude Code sobre el repo SnowTime

Contexto de la maquina de Juan. Repo local en `C:\git\SnowTime\SnowTime`, venv `.dbt-venv` activo,
Claude Code con cinco MCP. Myer es cliente australiano y vive bajo la region `us` en este repo, el
pipeline de deploy se llama `Deploy - SnowTime DBT / US - C109_MYR`, asi que el MCP correcto es
**snowflake-us**, no snowflake-eu.

Con el repo local el orden cambia respecto al plan original. El grep es instantaneo y no necesita
credenciales, asi que va primero. La fase de Snowflake despues.

---

## El prompt. Pegalo completo en la sesion de Claude Code

    Estoy investigando el ticket RCS-28638 de Appriss Retail. Trabaja en modo solo lectura.

    REGLAS QUE NO SE NEGOCIAN EN ESTA SESION
    No modifiques ningun archivo del repo. No hagas commit, branch, push ni PR.
    No corras dbt run, dbt build ni dbt seed. El venv esta activo, ignoralo.
    Contra Snowflake solo SELECT, SHOW y DESCRIBE. Nada de INSERT, UPDATE, DELETE, MERGE, CREATE
    ni DROP. Ningun rebuild ni REBUILD_RANGE bajo ninguna circunstancia.
    Usa el MCP snowflake-us. Myer es cliente australiano pero vive bajo la region us en este repo.
    Si algo no lo puedes verificar, dilo. No completes con suposiciones.

    EL PROBLEMA
    Cliente Myer Australia, client 109, codigo MYR, schema ARDM_PRODUCTION.C109_MYR.
    El cliente reporta que tres campos de Header Ext dejaron de poblarse en las transacciones:
    Proof Type, Order Number y Financial Statement Date. Fecha de perdida declarada 09/08/2026.

    Evidencia que ya tengo, de capturas del cliente sobre la transaccion 2608273342446971618:
    Las columnas del search muestran los tres campos vacios.
    La vista Retail Transaction Details de esa MISMA transaccion muestra los valores presentes,
    Proof Type CUSTOMER ORDER RETURN y Customer Order Number 2002504903.
    El receipt view muestra los labels Financial Statement Date y Proof Type sin valor.
    En la misma vista aparece un token de plantilla sin resolver,
    Reason Description:$lineItemDomainSpecific.returns.returnNotes, mientras el detalle guarda
    Reason ID:RC19. El recibo cae a OTHER REASON.
    Transaccion de referencia declarada correcta por el cliente en el ticket hermano RCS-28640:
    2608098315964575603, del 09/08/2026.

    CONTEXTO DE CAUSA RAIZ YA ESTABLECIDO EN TICKETS HERMANOS
    Myer migro de Greenplum legacy a SnowTime. Go live ENG-6418 cerrado el 17 ago 2026, el break se
    hace visible el 13 ago. La reimplementacion del pyardm legacy en SnowTime dejo ramas de logica
    sin portar, y cada defecto de mapeo de Myer es una omision distinta de la misma migracion.
    Dos patrones confirmados por Matthew Everett, con cita textual:
    Uno, mapping gap. "map_ardm_tender.sql:333 emits null::VARCHAR as accountnumber. Legacy pyardm
    ARDM_1_Tender.sql:128-132 populated it via a four-branch CASE; SnowTime implements only branch
    4. Branch 3 was never reimplemented."
    Dos, destruccion de historico. "A large rewrite on 2026-08-14 then re-ran that mapping across
    historical tradingdays that were already correctly populated, replacing good values with NULL."
    Ese rewrite del 14 de agosto explica por que el cliente ve perdida desde el 09/08, seis dias
    antes del cutover. El tradingday no cambia, el escritor de la fila si.

    FASE 1, GREP DEL REPO. Empieza por aqui, no necesita credenciales.

    1a. Busca los tres campos en el reporte de paridad y en la doc de mapeo. Matthew encontro su
        columna marcada BLOCKED en ArdmProdParity.md linea 748, asi que el formato existe.
        Busca en ArdmProdParity.md y en models/ardm_mapping.md, sin distinguir mayusculas, los
        terminos: proof, prooftype, ordernumber, order_no, financialstatement, financial_statement,
        headerext, header_ext.
        Reportame cada acierto con el numero de linea, el estado que trae, BLOCKED u otro, y el
        porcentaje de match si lo hay.

    1b. Localiza el mapeo de header de Myer. Deberia estar en
        dbt/clients/us/c109_myr/models/mapping/. Lista los archivos de esa carpeta.
        Abre map_ardm_header.sql y busca la rama tct, la que emite los documentos
        TenderControlTransaction, y cualquier bloque que produzca los campos de Header Ext.

    1c. La pregunta que tengo que responder es una sola. La rama que puebla Proof Type, Order
        Number y Financial Statement Date, existe en el codigo o emite NULL.
        Busca en toda la carpeta de mapeo del cliente 109 los patrones null::VARCHAR, null::DATE,
        null::TIMESTAMP y cast(null en cercania de esos tres campos.
        Si encuentras un NULL literal donde deberia ir el mapeo, dame archivo, numero de linea y
        las diez lineas de contexto.

    1d. Busca si el pyardm legacy esta disponible localmente, como carpeta, submodulo o copia.
        Los archivos legacy citados en otros tickets son ARDM_1_Tender.sql y ARDM_91_Poshash.sql,
        asi que el de header sigue la misma convencion numerada.
        Si lo encuentras, compara rama por rama que poblaba pyardm y que pobla SnowTime para estos
        tres campos. Si no esta en la maquina, dimelo y no inventes el contenido.

    1e. Busca detail-panel.html en el repo. Matthew documento que las lineas 303-305 hacen un
        fallback de tres pasos para Card No y que las 130-137 renderizan {{pipo.reasontext}} sin
        prefijo de etiqueta.
        Localiza el bloque que renderiza Return/Exchange With Proof Of Purchase y dime de donde lee
        Proof Type y Financial Statement Date. Busca tambien el token
        lineItemDomainSpecific.returns.returnNotes en todo el repo, para saber si esta hardcodeado
        en una plantilla o si viene del payload.

    PARA AL TERMINAR LA FASE 1 y dame el resumen antes de tocar Snowflake.

    FASE 2, SNOWFLAKE. Solo despues de que yo apruebe la fase 1.

    2a. Fija los nombres reales de tabla y columna, no los asumas.
        SHOW TABLES LIKE '%HEADER%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;
        Si existe una tabla de extension de header, lista sus columnas.
        Si los tres campos no aparecen ahi, amplia la busqueda de columnas a todo el schema con
        LIKE '%PROOF%', '%ORDER%' y '%FINANCIAL%'.
        Dame los nombres exactos que encuentres.

    2b. El test de dos filas, con los nombres reales del paso 2a.
        Trae transactionid, tradingday, _ROW_CREATED y los tres campos para las transacciones
        2608273342446971618 y 2608098315964575603.
        Lo que quiero comparar es si la del 09/08 tiene _ROW_CREATED temprano y valores presentes,
        y la del 27/08 tiene _ROW_CREATED posterior y NULL.

    2c. La cross tab. Es el test que decide el ticket. Fija el mes del tradingday, varia el mes de
        _ROW_CREATED, y dame el conteo total y el poblado de cada uno de los tres campos, con
        porcentaje, desde 2026-05-01 en adelante.
        Interpretalo asi y dime cual de los tres casos es:
        Si un mismo mes de tradingday sale poblado con escritor del mismo mes y en cero con
        escritor de agosto, la causa es el rewrite del 14 de agosto.
        Si sale en cero en todos los escritores sin ninguna fila previa poblada, la rama nunca se
        reimplemento en SnowTime.
        Si sale poblado en todos los escritores, el dato esta en la tabla y el defecto esta en el
        search o en el render, no en el mapeo.

    2d. Si el caso es el rewrite, acota el alcance. Cuantas transacciones y desde que tradingday
        tienen los tres campos en NULL. Dame el numero por mes.

    ENTREGABLE
    Al final dame un resumen con esta estructura, en ingles, sin markdown, sin negritas y sin
    guiones como conectores, porque lo voy a pegar en Jira:
    Status, Root cause con archivo y numero de linea, Production evidence con los numeros de las
    consultas, Scope con cuantas transacciones y desde cuando, Related y por que arreglar otro
    ticket no arregla este, Required action.
    No afirmes nada que las consultas no hayan medido. Si el remedio no esta probado, escribe que
    no esta probado.

---

## Notas para Juan sobre esta sesion

El MCP correcto es snowflake-us. Si snowflake-eu devuelve vacio para C109_MYR, no es un problema de
permisos, es la region equivocada.

Ese repo tiene el venv de dbt activo y Claude Code puede escribir. El prompt lo prohibe de forma
explicita en la primera linea. Si en algun momento te propone correr dbt o abrir un PR, esa es la
señal de que perdio la instruccion y hay que reiniciar el hilo.

La fase 1 puede cerrar el diagnostico sola. Si `ArdmProdParity.md` trae los tres campos como
BLOCKED y `map_ardm_header.sql` tiene un NULL literal donde deberia ir el mapeo, tienes causa raiz
sin tocar Snowflake. La fase 2 pasa entonces a ser la medicion de alcance para el hand over.

La parada entre fase 1 y fase 2 es deliberada. Traeme el resultado de la fase 1 y decidimos si la
fase 2 sigue igual o cambia.

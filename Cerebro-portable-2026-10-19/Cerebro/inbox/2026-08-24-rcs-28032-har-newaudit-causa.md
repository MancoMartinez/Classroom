# RCS-28032 · analisis del HAR de NewAudit.aspx · dos fallas separadas, una con causa en red

Fecha: 2026-08-25 00:36 UTC, sesion propia de Juan con alcance de admin
Fuente: `adjuntos/RCS-28032/HARVit1.har`, 80 entradas, pagina
`https://apps.apprissretail.com/vitaminshoppe/nettrack/Audit/NewAudit.aspx`
Build de la app: `6.26.8`. Tenant 433.

## Hallazgo 1. La tienda 1016 es del distrito 501, no del 504

El typeahead del campo Select Location define sus columnas asi, en el HTML de la pagina:

    dxpQueryTable: 'Store'
    dxpValueField: 'StoreIdent'
    dxpQueryColumns: 'StoreNo|StoreName|StoreIdent|City|State|OpsRegion|OpsDistrict|Address1|Zip|Country|Inactive'

Y la respuesta del servidor al escribir 1016, entrada 62 del HAR, devuelve:

    ['1016','Federal Way WA Store','946','Federal Way','WA','3','501','1401 S 348th Street, Suite M102','98003','USA','0']

Mapeado contra las columnas: StoreNo 1016, StoreName Federal Way WA Store, **StoreIdent 946**, City Federal
Way, State WA, OpsRegion 3, **OpsDistrict 501**, Zip 98003, Inactive 0.

Dayna adjunto esa tienda para probar: *"If I choose a store in D504, it won't load the location number"*.
La tienda es del 501. El 11 de agosto el 501 era el distrito que ella si tenia activo.

**Su queja de New Audit no es un problema de alcance de distrito.** No podia seleccionar una tienda de su
propio distrito. Ya no hace falta el SELECT para establecerlo, lo dice la aplicacion.

## Hallazgo 2. El StoreIdent nunca se persiste en el formulario

Esta es la causa del error que veia Dayna y del boton que no responde. La secuencia completa esta en el HAR.

1. Entrada 62, callback `fld_storeident$STOREID`. El typeahead resuelve StoreNo 1016 y devuelve StoreIdent
   946. Correcto.
2. Entrada 63, callback `fld_storeident$cpStoreLookupCallbackPanel` con `__CALLBACKPARAM = c0:946`. El
   navegador manda el StoreIdent al servidor. Correcto.
3. La respuesta de esa entrada 63 devuelve el control re-renderizado:

       <input type="hidden" id="fld_storeident$cpStoreLookupCallbackPanel$hfStoreLookup"
              name="fld_storeident$cpStoreLookupCallbackPanel$hfStoreLookup" value="" />

   **Vuelve con value vacio.** El 946 entra y no sale.
4. Entrada 67, el ultimo POST de la sesion, ya con el combo mostrando en pantalla
   `1016 -  Federal Way WA Store,  Federal Way,  WA,  3`. Los campos ocultos siguen asi:

       fld_storeident$fld_storeident = 0
       fld_storeident$fld_storeno    = 0
       fld_storeident$screentypecode = 0
       clientid                      = 0

La pantalla muestra la tienda. El formulario no la tiene. Para el servidor no hay ubicacion seleccionada, y
por eso responde "Please select a location and try again".

## Hallazgo 3. El clic en Next no genera ningun request

El ultimo trafico hacia la aplicacion es la entrada 67, a las 00:36:47. De ahi hasta el final del HAR, a las
00:44:02, solo hay llamadas a `data.useranalytics.apprissretail.com`, que es Pendo. **Juan pulso Next y no
salio un solo request HTTP.** Se corta en el navegador.

El markup explica por que puede cortarse ahi:

    <input id="btn_Save_I" class="dxb-hb"
           value="Could not Find entry in Screen Label table (btn_Next)"
           type="button" name="btn_Save" readonly="readonly" />

    ASPx.createControl(ASPxClientButton,'btn_Save','',
      {'autoPostBack':true,'serverEvents':['Click'],'useSubmitBehavior':false,
       'autoPostBackFunction':function(postBackArg){ WebForm_DoPostBackWithOptions(...) }},
      {'Click':function(s,e){ lps.Show(); btnSave_Click(s,e); }});

El boton tiene handler y tiene postback configurado. El postback pasa por `btnSave_Click`, una funcion
propia. Interpretacion, no verificada: `btnSave_Click` valida la ubicacion contra el hidden que sigue en 0
y aborta antes de disparar el postback, sin pintar mensaje. Se confirma con un breakpoint o con la consola.
Falta el log de Console, el HAR no lo lleva.

Diferencia con el 11 de agosto: a Dayna el flujo si llegaba al servidor y devolvia el mensaje de validacion.
Hoy no llega. Mismo origen, el StoreIdent en 0. Distinto punto de corte.

## Hallazgo 4. Screen Labels, y por que puede no ser cosmetico

30 etiquetas salen como fallback en el HTML de la pagina. Entre ellas, y esto es lo que importa:

    Store_StoreNo, Store_StoreName, Store_City, Store_State,
    Store_OpsRegion, Store_OpsDistrict, Store_Address1, Store_Zip, Store_Country

Son los encabezados de columna del propio store lookup, el control que esta fallando, y el control corre con
`dxpDisplayColumns: true`. El resto son de navegacion y botones: `mnu_BackToMenu`, `mnu_UserTools`,
`mnu_UserMenu`, `mnu_Preferences`, `mnu_ChangePassword`, `mnu_Contacts`, `mnu_ChangeLocation`, `mnu_Logoff`,
`mnu_PrintBlankForms`, `sys_PleaseFindStore`, `sys_DisplaySaveMessage`, `title_storelookup`,
`title_SelectAuditName`, `title_AuditName`, `btn_Next`, y `LPUser_Language`.

Hipotesis para ingenieria, sin probar: si `OnStoreLookupEndCallback` ubica la columna StoreIdent por nombre
de columna en vez de por indice, los labels rotos rompen el mapeo y ahi se pierde el 946. Si mapea por
indice, los labels son cosmeticos y el hallazgo 2 tiene otra causa. Es una linea de codigo la que lo decide.

**Pista de idioma.** El bundle que carga la pagina es
`/platform/_react/dist/allApps___v6.26.8_433en-GB_-1874327775.js`. El tenant 433 resuelve la cultura como
**en-GB**. El HTML contiene en-US y en-GB. El control `LPUser_Language` del header tambien sale roto. Causa
candidata: las filas de Screen Labels existen para en-US y la sesion pide en-GB. Se verifica con un SELECT
sobre la tabla de labels filtrando por las claves de arriba y por cultura.

## El error de SQL que te salio en Bastion

    Msg 245, Level 16, State 1, Line 1
    Conversion failed when converting the nvarchar value 'CLOSED241' to data type int.

`incident.Store.StoreNo` es nvarchar y guarda tiendas cerradas con el prefijo CLOSED, como 'CLOSED241'. Al
comparar contra una lista de enteros, SQL Server convierte la columna entera a int y revienta en la primera
fila con texto. Se arregla comparando como texto:

    SELECT StoreIdent, StoreNo, StoreName, Region, District, DistrictManagerID
    FROM incident.Store
    WHERE StoreNo IN ('1016','249','500');

O por StoreIdent, que si es int, con los tres valores ya conocidos:

    SELECT StoreIdent, StoreNo, StoreName, Region, District, DistrictManagerID
    FROM incident.Store
    WHERE StoreIdent IN (946, 617, 466);

946 es la tienda 1016 Federal Way. 617 es la 249 Tanasbourne OR. 466 es la 500 Everett WA. Ya no decide la
escalacion, el HAR contesto la pregunta. Sirve para confirmar y para cerrar el mapa de distritos de Dayna.

## Como queda el ticket

Son dos problemas y ahora se separan con evidencia.

| | Que es | Evidencia | Depende de permisos |
|---|---|---|---|
| **A. Alcance** | AuditLog.aspx imprime Ops District 501 como alcance efectivo. Dayna cubre 501 y 504 | Capturas del 11 ago, y el analisis de LHUA del 11 ago | Si |
| **B. New Audit** | No se puede seleccionar ninguna tienda. El StoreIdent no se persiste. Next no dispara | Este HAR | No. Juan lo reprodujo con alcance de admin |

B es la que Dayna documento en sus capturas creyendo que era A. B es reproducible por cualquiera y no
depende del usuario, lo cual la hace mas grave y mas facil de escalar.

## Que sigue

1. Console del navegador al pulsar Next, para cerrar el hallazgo 3. Es lo unico que falta del lado de Juan.
2. Probar NewAudit.aspx en otro tenant. Si ahi la tienda si se persiste, el problema es de 433 o de su
   configuracion de labels. Si falla igual, es de la version 6.26.8 y afecta a todos.
3. Escalar B a Engineering con este HAR adjunto. Cumple los requisitos de Aimee: entorno Produccion, pasos
   de reproduccion, evidencia. Transicion `231` "Waiting for Engineering", reasignar a Shandana Khan.
4. A queda en el mismo ticket o se separa, segun lo que diga ingenieria. El analisis de LHUA del 11 de
   agosto sigue valido y no lo toca nada de esto.

## Correccion al cerebro

`brain/memoria/reference_multidistrito_lhua.md` cita el caso de Dayna como confirmacion del multidistrito.
El comportamiento del AuditLog sigue sosteniendolo. La captura de New Audit con la tienda 1016 no, y esa
memoria no la menciona, asi que no hay que corregirla. Si hay que agregar que New Audit falla por otra causa,
para que nadie vuelva a leer esas capturas como prueba de alcance.

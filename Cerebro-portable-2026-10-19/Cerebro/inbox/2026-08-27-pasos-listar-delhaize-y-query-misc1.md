# Paso a paso: listar F:\Clients\Delhaize y consultar MISC1

Fecha: 27 ago 2026
Objetivo: identificar que campo del feed de empleados de ADUSA aterriza en `incident.Employee.MISC1`
y medir con que frecuencia llega vacio. Soporta RCS-28093.

Dato nuevo del task 3, Execute Refloader:

```
Working directory   F:\Clients\Delhaize\Refloader_PROD
Command             F:\Clients\Delhaize\Refloader_PROD\Custom_Load_ReferenceLPMS.cmd
Arguments           vacio
Run Task as         No Credential
```

`Custom_Load_ReferenceLPMS.cmd` es un batch de Windows. Adentro esta la llamada real a LPImport
con el archivo de configuracion que declara el mapeo columna por columna. Ese archivo es el
objetivo. Leerlo responde la pregunta sin descifrar ningun feed.

---

# PARTE A. Listar la carpeta y leer el .cmd

La unidad F pertenece a QA-LPMS-VC-001, no al escritorio remoto QA-LPMS-RDP-001 donde estas.
Hay tres formas de llegar, de mas simple a mas segura.

## A1. Explorador de archivos por ruta UNC

1. En la VM QA-LPMS-RDP-001, abre el Explorador de archivos con la tecla Windows mas E.
2. Haz clic en la barra de direccion, arriba, donde dice la ruta actual.
3. Borra lo que haya y escribe exactamente esto, luego Enter:

```
\\qa-lpms-vc-001.lpguys.net\F$\Clients\Delhaize
```

4. Si pide credenciales, usa `trebu\jmartinez` y tu contrasena de dominio.
5. Vas a ver las subcarpetas de Delhaize. Anota los nombres. Busca cualquiera que diga employee,
   emp, hr, associate, people o personnel.
6. Entra a `Refloader_PROD`. Ahi esta `Custom_Load_ReferenceLPMS.cmd`.
7. Haz clic derecho sobre el .cmd, elige Abrir con, y selecciona Bloc de notas.
   No hagas doble clic. Doble clic lo ejecuta.
8. Copia todo el contenido. Ahi vas a ver la ruta del archivo de configuracion.
9. Abre ese archivo de configuracion con Bloc de notas por el mismo metodo. Busca MISC1.

Si `F$` da acceso denegado, pasa a A2.

## A2. Acceso directo VC-Clients del escritorio

El runbook del Bastion documenta un acceso directo llamado VC-Clients que apunta a
`qa-lpms-vc-001.lpguys.net`.

1. Minimiza todo y mira el escritorio de la VM.
2. Busca el icono VC-Clients y abrelo.
3. Navega a la carpeta Clients, luego Delhaize.
4. Sigue desde el paso 5 de A1.

## A3. Navegador de archivos de VisualCron

Esta via lee el disco de VC-001 desde el propio cliente, sin depender de permisos de share.
Es solo lectura mientras no pulses Ok.

1. Con el task `Execute Refloader` abierto, mira el campo Working directory.
2. A la derecha del campo hay un icono de carpeta. Pulsalo.
3. Se abre un navegador que recorre el sistema de archivos de QA-LPMS-VC-001.
4. Navega a F, luego Clients, luego Delhaize. Anota las subcarpetas que veas.
5. Pulsa Cancelar para salir sin cambiar nada.
6. Cierra el task con Cancel, nunca con Ok.

Esta via lista carpetas. No abre el contenido del .cmd. Sirve para confirmar que existe una
carpeta de employee separada de Refloader_PROD.

## Regla mientras trabajas ahi

Solo lectura. No ejecutes el .cmd, no muevas archivos, no borres nada de `\archive`.
Si necesitas descifrar un `.pgp`, copialo primero a `C:\Temp\` de tu sesion y trabaja sobre la
copia, siguiendo el runbook LPMS - Decrypt client file de Confluence.

---

# PARTE B. Consultar MISC1 en SQL Server

## B1. Conectar SSMS

1. En la VM, busca Microsoft SQL Server Management Studio en el menu Inicio y abrelo.
2. En la ventana Connect to Server llena asi:

```
Server type        Database Engine
Server name        pd-lpms-uswest2-sqldb-001.database.windows.net
Authentication     Azure Active Directory - Universal with MFA
User name          jmartinez@trebu.co
```

3. Pulsa Connect. Va a pedir el segundo factor en el telefono.
4. En el panel Object Explorer, a la izquierda, expande el nodo Databases.
5. Busca la base de ADUSA o Delhaize. Los nombres suelen llevar la marca del cliente.
   Anota el nombre exacto.
6. Pulsa New Query, arriba a la izquierda.
7. En el dropdown de bases de datos de la barra superior, selecciona la base de ADUSA.
   Sin este paso las consultas corren contra master y fallan.

Prod acepta solo SELECT. No escribas INSERT, UPDATE, DELETE ni TRUNCATE.

## B2. Descubrir el esquema real

No asumas nombres de columna. Corre esto primero:

```sql
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Employee'
ORDER BY TABLE_SCHEMA, ORDINAL_POSITION;
```

Esto te da el esquema exacto y la lista de columnas. Confirma que existe MISC1 y anota como se
llama la columna de tienda y la de marca o division.

Si no aparece nada, busca la tabla por nombre parcial:

```sql
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%Employee%'
ORDER BY TABLE_SCHEMA, TABLE_NAME;
```

## B3. Ver una muestra

```sql
SELECT TOP 50 *
FROM incident.Employee;
```

Mira que trae MISC1 en las filas que si lo tienen. Deberian ser nombres de marca del grupo:
Food Lion, Stop and Shop, Giant, Hannaford.

## B4. El conteo que pide RCS-28093

Cuantas filas llegan sin marca:

```sql
SELECT
    COUNT(*) AS total_empleados,
    SUM(CASE WHEN MISC1 IS NULL OR LTRIM(RTRIM(MISC1)) = '' THEN 1 ELSE 0 END) AS sin_misc1,
    CAST(100.0 * SUM(CASE WHEN MISC1 IS NULL OR LTRIM(RTRIM(MISC1)) = '' THEN 1 ELSE 0 END)
         / NULLIF(COUNT(*), 0) AS DECIMAL(5,2)) AS pct_sin_misc1
FROM incident.Employee;
```

## B5. Distribucion de valores

```sql
SELECT
    ISNULL(NULLIF(LTRIM(RTRIM(MISC1)), ''), '(vacio)') AS division,
    COUNT(*) AS filas
FROM incident.Employee
GROUP BY ISNULL(NULLIF(LTRIM(RTRIM(MISC1)), ''), '(vacio)')
ORDER BY filas DESC;
```

Te dice cuantas marcas distintas viajan en MISC1 y cuanto pesa el vacio contra el total.

## B6. El cruce de fondo del ticket

RCS-28093 dice que cerca de 300 numeros de tienda existen en mas de una marca. Esta consulta lo
mide. Ajusta el nombre de la columna de tienda con lo que te devolvio B2.

```sql
SELECT
    StoreNumber,
    COUNT(DISTINCT LTRIM(RTRIM(MISC1))) AS marcas_distintas,
    STRING_AGG(DISTINCT LTRIM(RTRIM(MISC1)), ' | ') AS lista_marcas
FROM incident.Employee
WHERE MISC1 IS NOT NULL
  AND LTRIM(RTRIM(MISC1)) <> ''
GROUP BY StoreNumber
HAVING COUNT(DISTINCT LTRIM(RTRIM(MISC1))) > 1
ORDER BY marcas_distintas DESC;
```

Para el conteo agregado que Matt se comprometio a entregar:

```sql
SELECT COUNT(*) AS tiendas_en_varias_marcas
FROM (
    SELECT StoreNumber
    FROM incident.Employee
    WHERE MISC1 IS NOT NULL
      AND LTRIM(RTRIM(MISC1)) <> ''
    GROUP BY StoreNumber
    HAVING COUNT(DISTINCT LTRIM(RTRIM(MISC1))) > 1
) t;
```

## B7. Empleados afectados por la intermitencia

Los que comparten numero de tienda y no traen marca. Son los que rompen la busqueda entre marcas.

```sql
SELECT TOP 200 *
FROM incident.Employee
WHERE MISC1 IS NULL OR LTRIM(RTRIM(MISC1)) = ''
ORDER BY StoreNumber;
```

---

# Que hacer con los resultados

Guarda cada resultado con el boton derecho sobre la grilla, Save Results As, formato CSV.
Con el porcentaje de B4 y el conteo de B6 ya tienes evidencia numerica para el comentario del
ticket. Del .cmd y su config sale el nombre del campo de origen que alimenta MISC1.

Notas de verificacion pendientes:

- El nombre de la columna de tienda esta asumido como StoreNumber. B2 lo confirma o lo corrige.
- El esquema `incident` viene de como Juan nombro el campo. B2 lo confirma.
- `STRING_AGG` requiere SQL Server 2017 o superior. Azure SQL lo soporta.
- Falta confirmar que el Refloader sea el proceso que alimenta employee. La Parte A lo resuelve.

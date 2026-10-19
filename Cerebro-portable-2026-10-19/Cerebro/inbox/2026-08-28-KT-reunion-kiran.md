# KT de la reunión con Kiran Vadday, 28 ago 2026

Support-Eng Process Review. 53 minutos, Juan Martinez y Kiran Vadday.
Fuente: grabación y transcripción completas. Las rutas, queries y IDs salen de la pantalla
que Kiran compartió, no de memoria.

Este documento es para el equipo. Todo lo técnico está verificado contra el video.

---

## 1. Credenciales de netTrack. Se acabó pedirlas

**Este es el entregable más grande de la reunión.** Kiran nos dio la ubicación del archivo
que tiene todos los usuarios y contraseñas de netTrack, para que nadie más tenga que
pedírselas a ella ni a Matt.

**Ruta exacta, vista en pantalla:**

```
C:\LPMS Utilities\VB Scripts\SELECT\DB_SELECT.vbs
```

23 KB, VBScript Script File. En esa misma carpeta hay además `Notes`, `SQL` y
`SQL_DB_STORAGE`, más una subcarpeta `Scott`.

**Cómo llegar:** Azure Bastion hacia el servidor `qa-lpms-rdp-001`. El nombre completo que
Kiran usó es **QALPMSRDP001**. Ese servidor tiene la red de producción y la de QA.

**Cómo abrirlo:** clic derecho, Edit in Notepad. Si Notepad++ lanza el aviso de Network Path
Warning apuntando a `\\pd-lpms-iis-007\Clients\<cliente>\nettrack\App_Data\connectionstrings.config`,
darle Skip a todos los mensajes.

**Qué contiene:** los seis entornos. Kiran los enumeró así, y la regla mnemotécnica es suya:

> "PE I think is Europe, QC, QE, QA. You know, anything with A is like PD PQ A, USA, PE QE,
> Europe, PC, QC, Canada. So these three, so total six."

- **PD / QA** = Estados Unidos
- **PE / QE** = Europa
- **PC / QC** = Canadá

Producción y QA de cada región. Con esas credenciales tienes operaciones CRUD completas en
netTrack. Sin ellas puedes entrar, pero solo lees.

> "with these you do have the credentials, operations possible. Without that, you can still
> access, but you won't be able to do all the CRUD work."

**Lo que Kiran pidió que hiciéramos:**

> "If do yourself a favor, create some account in one password, I mean a vault. Throw them
> in there so you don't have to go this horrible route."

Cada uno guarda las credenciales en su bóveda de 1Password con su propio tag. No se
comparten por chat ni por correo.

### El lado Platform no necesita credenciales

Ojo con esta distinción, es importante y mucha gente la confunde:

> "Coming to platform, it's not like that. It totally gets off based off your Windows
> thingy. And all you need to do is teaming up onto the server, then turning on the VPN,
> then RDP into platform RDP 01. And you should be able to do all the CRUD operations
> without any interruption. So you don't need credentials there."

**Platform: autenticación integrada de Windows, cero credenciales.** VPN, RDP al servidor de
platform, y ya tienes CRUD.
**netTrack: sí necesitas el archivo.** Y netTrack va a desaparecer:

> "eventually we'll get away from netTrack anyways."

---

## 2. RCS-28342 y el problema de los títulos

### Dónde vive el título de un usuario, y por qué está en dos sitios

La historia completa, en palabras de Kiran. Cuando se migró de `incident.LPUser2` a
`membership.Users`, el equipo creyó que `membership.Users` no tenía columna de título. Para
acomodar lo que netTrack necesitaba, metieron el título en una tabla aparte:

```
incident.LPUser2  ->  membership.Users
                      membership.UserExtensionData   (aquí se guardó el Title)
```

`membership.UserExtensionData` funciona por atributos: `UserID`, `AttributeName`,
`AttributeValue`. Cuando `AttributeName = 'Title'`, el `AttributeValue` es el título.

La vista `LPUser` arma el resultado uniendo las dos: todos los datos vienen de
`membership.Users` y el título de `membership.UserExtensionData`, mapeado por el **UserID
GUID grande de membership**, no por el UserID numérico.

Kiran lo describió sin adornos:

> "But that's what happened there because we were not tying directly between the two. We
> were going in squiggly lines."

### El query que ella corrió, verbatim de la pantalla

```sql
WITH Candidates AS (
    SELECT
        u.UserId,
        MAX(lp2.Title) AS Lp2Title      -- MAX handles any accidental LPUser2 duplicates
    FROM membership.Users u
    JOIN incident.LPUser2 lp2
        ON lp2.LoginID = u.UserName
    LEFT JOIN membership.UserExtensionData ued
        ON  ued.UserId        = u.UserId
        AND ued.AttributeName = 'Title'
    WHERE lp2.Title IS NOT NULL
      AND LTRIM(RTRIM(lp2.Title)) <> ''
      AND (
            ued.UserId IS NULL
         OR ued.AttributeValue IS NULL
         OR LTRIM(RTRIM(ued.AttributeValue)) = ''
      )
    GROUP BY u.UserId
)
MERGE membership.UserExtensionData AS target
USING Candidates AS source
    ON  target.UserId        = source.UserId
    AND target.AttributeName = 'Title'
WHEN MATCHED
 AND (target.AttributeValue IS NULL OR LTRIM(RTRIM(target.AttributeValue)) = '')
    THEN UPDATE
        SET target.AttributeValue = source.Lp2Title
WHEN NOT MATCHED BY TARGET
    THEN INSERT (UserId, AttributeName, AttributeValue)
        VALUES (source.UserId, 'Title', source.Lp2Title);
```

Target es `membership.UserExtensionData`. Source es el CTE que cruza `membership.Users` con
`incident.LPUser2` por LoginID igual a UserName. El ticket incluye primero un SELECT de
preview y después el MERGE.

**Esto es DML. Cualquiera del equipo con escritura lo puede correr.**

### Y esto cambia el 15 de septiembre

`membership.Users` **sí tiene** una columna llamada `JobDescription`. Se dieron cuenta
tarde. El nuevo stored procedure va a mapear el título directo a `membership.Users.JobDescription`,
y la UI va a leer de ahí.

> "So going forward, we will be mapping title to job description. I'm still inserting in
> here, but we won't be looking at that anymore. You can ignore it."

> "PR is not still in, but by September 15th, that should be in main, that should be across
> the board."

**Qué significa para nosotros.** Los clientes que ya se desplegaron, más de 20, no reciben
ese cambio. Para ellos hay que correr un update a mano. Kiran nos dijo cómo:

> "Or simply write update statement from title directly from LPUser2.Title to
> JobDescription. Why should we even go to the user extension data? Just try to run it
> right away."

**Advertencia que dio y que hay que respetar:**

> "But make sure that they did not make any changes to job description already because
> we'll be overriding them."

Antes de correr ese update, verificar que `JobDescription` no traiga ya datos del cliente.
Si los trae, los pisas.

**Después del 15 de septiembre, el título en la UI, en Users Settings, tiene que venir de
`membership.Users.JobDescription`, no de `UserExtensionData`.** Si ves lo contrario en un
tenant desplegado, ya sabes por qué.

---

## 3. RCS-28379 y la causa raíz de los nombres en blanco

### Por qué pasó

Este es el conocimiento más valioso de la reunión, porque explica una familia entera de
tickets.

Cuando se escribió el script de migración de `incident.LPUser2` a `membership.Users`, se le
pusieron **reglas extensas de exclusión**: no traer cuentas inactivas, no traer correos
duplicados, y varias más. Sonaba razonable. Era un error.

> "Imagine they have one, one one two, one three, but it's the same person. So we got only
> one record. We totally lost the big picture that there are one twos, one threes in the
> master case, audit master store. Everything has user ID in it, like audit assigned to,
> audit case owner ID, incident, suspect. Every employee table has some user IDs."

Traducción: una misma persona tenía tres cuentas. La migración trajo una sola. Pero esa
persona creó casos y auditorías **con las otras dos cuentas**, y esos registros apuntan a
UserIDs que ya no existen en `membership.Users`.

> "So when they open a case that created by you, but using your second account, your name
> won't come up after platform migration because we did not bring two and three. We thought,
> oh, it's the same person. But yeah, it's the same person, but that same person has three
> accounts and those three accounts are used to create cases, audits, case changes."

### Qué hizo ella, y por qué ya no lo haría así

Lo hizo a mano. Identificó quién era la persona real en `membership.Users`, vio cuál era el
IncidentUserID correcto, y actualizó todos los registros para que apuntaran ahí.

> "So figured out who the person is actually in membership.users and saw what the incident
> user ID is. So what is the wrong incident user ID and updated all the records to have
> that person."

**Pero hoy lo haría al revés, y esto es lo que el equipo tiene que aprender:**

> "In the latest case, if it were for me today, I would find if Juan 2 is in LPUser2, yes it
> is in LPUser, is it on the case owner ID, Juan 2, Juan 2 is missing on membership.users, I
> would actually create that user. Much easier and I don't need to update like 11 to 50
> tables."

**La regla nueva: no persigas los registros. Trae al usuario que falta.**

> "So bring in duplicate Juan 2, Juan 3, keep everything as it is, give this incident user
> ID to that membership.users.IncidentUserID, map it, and we should be good. They should be
> able to see it's the same name that comes up. Juan Martinez, Juan Martinez, but behind the
> scenes, that's a different incident user ID. But who cares?"

Y el criterio de decisión, textual:

> "Incident user ID is the holy truth to user ID. If you don't see that incident user ID
> coming up in membership.users, fix it. Bring it in. Let's bring it in."

**`IncidentUserID` es la verdad. Si no aparece en `membership.Users`, créalo.**

### Las reglas de migración ya no existen

> "So going forward again, you should not have this issue because now we have no rules. It's
> an open season and we bring in every person. Inactive, active, deleted, we don't care."

> "membership.Users, which used to be pristine, nice table, is now trash because I'm
> bringing in everybody. Dead and alive, inactive, active, deleted, undeleted. Everybody is
> now mapped."

La razón de negocio detrás, y conviene tenerla a mano cuando alguien discuta la integridad
de la tabla:

> "At the end they wanted to see the names, they don't want to know which account it is
> coming from. They are simply looking at, I open a case, I open an audit, I want to see who
> it's created by. They see a name, they are happy, we are happy, bye bye."

### Dos scripts que Kiran ofreció y hay que reclamarle

1. **El script completo de todas las tablas de netTrack.** Cubre todas las tablas que llevan
   UserID. Lo generó con Claude.
   > "I wrote an entire, Claude gave me an entire script to cover all the netTrack tables.
   > That covers every table. So I still have that script if you want to grab it anytime."

2. **El script de migración de un solo usuario.** Le das el IncidentUserID y el correo, lo
   corres, e inserta en `membership.Users`.
   > "I also have a single user migration script if that might help you. So you can put in
   > that incident user ID and email and it will run the script and it will insert into
   > membership.users."

**Acción: pedirle los dos por escrito y guardarlos en el cerebro.**

---

## 4. RCS-28196 y el bug del default 0. Cómo se construyen las tablas nuevas

Kiran abrió el proyecto de bases de datos y explicó el mecanismo completo. Esto sirve para
entender toda una clase de bugs post migración.

### El mecanismo

Hay dos archivos que trabajan juntos en el proyecto `Databases`:

- **`IncidentDbContextExtensions.cs`** — aquí van los modelos. Enlistas las columnas y dices
  el tipo: string, long, datetime, decimal, integer.
- **`IncidentDbContext`** — aquí se crean las tablas. `modelBuilder.Entity<AccidentEquipment>`
  y le dices nombre de tabla, nombre de esquema, y la clave, que se copia del lado de
  netTrack porque solo se está recreando lo que ya existía.

### La regla que se violó

> "What we shouldn't be doing is we should not be adding integers in this schema. You only
> mention the columns to which you want to mention a property."

**Solo declaras en la tabla las columnas a las que les vas a dar una propiedad.** Un string
sí, porque hay que decir el largo, ya que por defecto es nvarchar. Una moneda sí, porque hay
que decir cuántos decimales. **Un entero no. Un entero no se menciona.**

> "We made the mistake of mentioning integers and saying default to value 0. That caused
> problem because now we copied the data. Law enforcement column, there null, and here we
> said default to zero. So null became zero and zero is no. One is yes. Null should have
> been null, which would have not been a problem, but null becoming a zero."

**El daño concreto:** la columna Law Enforcement era NULL en el sistema viejo. El
`HasDefaultValue(0)` la convirtió en 0 al copiar. Y en esa tabla 0 significa No y 1 significa
Sí. Un campo que estaba en blanco pasó a decir "No" explícitamente. Por eso el cliente vio
items que antes salían vacíos y ahora salen en NO.

> "In the new version, it was always zeros and ones, and there is no scope of nulls because
> we said it has to have a default value of 0."

### El fix

Gabor quitó la propiedad. PR visto en pantalla:

```
dev.azure.com/apprissdevops/Sysrepublic Secure/_git/Secure/pullrequest/55835
```

> "has to remove, has default value of 0, no need anymore. Just simply mention the column
> type and we don't need this."

Y un dato sobre el snapshot que evita confusión al leer el diff:

> "You don't even create the snapshot. Snapshot is auto-generated by EF migrations."

**Cómo usar esto.** Cuando un cliente migrado reporte que un campo que antes estaba vacío
ahora tiene un valor por defecto, la primera hipótesis es esta: un `HasDefaultValue` sobre
una columna entera en el DbContext. Es verificable comparando el valor viejo contra el nuevo.

---

## 5. RCS-28321, Boot Barn. Dos problemas apilados

Kiran separó el ticket en dos cosas distintas. Hay que tratarlas por separado.

### Problema uno, el conteo del tile. Es nuestro bug y está reconocido

El 15 de agosto Kiran desplegó un cambio de permisos en la pantalla de Active Audits. Antes
mostraba todas las auditorías. Ahora muestra solo las que te pertenecen y para las que
tienes permiso. Ese es el comportamiento correcto.

> "But what I didn't do is I did not fix the tile count. So I fixed the inside. I did not
> apply that to the tile count. I do have a PR up that fixes the tile count."

**El tile y la grilla no coinciden porque el fix se aplicó a una y no a la otra.**

Lo que hay que decirle al cliente, y ella lo dictó:

> "I would simply go back to the customer and say, yeah, the tile count and the active
> audits don't match, and our engineering team is working on getting the tile count match
> the active audits."

Está trabajando con **Ryan Barlow** en esto. Contexto útil sobre Ryan:

> "He's like the netTrack OG, at least in our company. He knows every bit. He's the
> implementation manager. He speaks with the clients, he sets the rules. If he can't set the
> rules, he speaks with the product and decides what the rules are."

Kiran fue a Ryan porque el cambio de permisos lo hizo por su cuenta y quería confirmación de
que era el comportamiento correcto. Matt le dijo que no había dirección clara.

**Ryan Barlow es la persona a la que se le preguntan las reglas de negocio de netTrack.**

### Problema dos, el registro huérfano. Es dato malo del cliente

Evidencia vista en pantalla:

```sql
select * from AuditConfig where AuditConfigID = 68 order by Description
select * from AuditMaster where AuditMasterID = 232
```

Resultado:

| Tabla | Valor |
|---|---|
| AuditConfig 68 | Description = **FY25** DM Business Review Upload, AuditClass Operational, Version 1.7, LastEdited 2024-04-02 15:36, LastEditedBy 15695, AuditRangeID 2, LayoutAudit BootBarn.docx |
| AuditMaster 232 | AuditConfigID 68, Description = **FY24** DM Business Review Upload, DateCreated NULL, LastEdited NULL, TargetStartDate 2023-04-04, TargetCompletionDate 2024-04-02, Status 2, Version 1.6 |

El AuditMaster 232 apunta al AuditConfig 68, pero uno dice FY24 y el otro FY25. **Es un
huérfano de 2024.**

> "So right now it's like an orphan. So it comes up on everybody's chart. I can see it as a
> support person when I log in as a support security level. So this I would say is bad data
> on their part."

> "Basically you, me, whoever logs in, we should not be seeing anything because nothing's
> assigned to us. I am going in as Kiran, and I still see that. You go in, you see that, and
> she's going in, she's seeing that."

**Le aparece a todo el mundo.** Kiran quiso borrarlo y no lo hizo:

> "I almost wanted to delete it, but I don't want because it's production."

El mensaje al cliente es que ese registro está universalmente visible por el desajuste, que
esa auditoría ya no existe, y que si quieren la relacionan de nuevo o la ignoran.

### El orden de la conversación con el cliente, dictado por Kiran

1. Primero: sí, el tile y la grilla no coinciden, ingeniería lo está arreglando. Eso cierra
   la primera mitad del reclamo.
2. Después: pedirle **cuál** es la auditoría que intenta editar. Número de auditoría o de
   caso, más captura.
3. Con ese número, verificar en base si está asignada a ella.
4. Si es de ella, decir que ingeniería lo está arreglando. Si no es de ella, decir que no
   tiene permisos y cerrar.

> "Check if it's assigned to her or at least has audit on her ID. If it is hers, then go
> back and say, oh, our engineering team is working on it. If it's not, say that hey, you
> don't have permissions. We know the tiles and this don't match and this is not opening
> because you don't have permissions. End the story, close the ticket."

### Un detalle de comportamiento que vale como diagnóstico

> "See, it goes back to the previous screen only when you don't have permissions."

**Si al hacer clic en una auditoría la pantalla te devuelve a la anterior, es falta de
permisos.** No es un error, es el comportamiento. Con el fix nuevo ni siquiera vas a ver el
registro, así que no vas a poder hacer clic.

---

## 6. Datos sueltos que conviene guardar

- **La única forma en que Kiran entra a un tenant** es con nivel de seguridad de soporte.
  > "I can see it as a support person when I log in as a support security level. That's the
  > only way I can log in."
- **El archivo YAML del cron** solo copia archivos. Kiran cambia el horario y nada más.
  > "I don't do the cron stuff. Except for this YAML file, but for that I just simply changed
  > the time. I have zero clue what it does."
- **Ryan Barlow** es el dueño de las reglas de negocio de netTrack.
- **Matt Kamminga** es el otro punto de contacto para credenciales de netTrack mientras
  existan.
- **Ray ID de Cloudflare**: Kiran lo mencionó por Matt, no porque ella lo use.
  > "I am not a Cloudflare person, but I heard Matt million times asking for Ray IDs."
- Kiran está en la rotación de RCSQ **una vez cada ocho semanas**, aproximadamente cada dos
  meses. Antes era más seguido.

---

## 7. Lo que hay que hacer esta semana

1. **Cada uno saca las credenciales de netTrack** de `C:\LPMS Utilities\VB Scripts\SELECT\DB_SELECT.vbs`
   vía Bastion a `qa-lpms-rdp-001` y las guarda en su bóveda de 1Password. Se acabó pedirlas.
2. **Pedirle a Kiran los dos scripts** que ofreció: el de todas las tablas de netTrack y el
   de migración de usuario único. Guardarlos en el cerebro.
3. **Preparar el update de Title a JobDescription** para los más de 20 clientes ya
   desplegados, con la verificación previa de que JobDescription no traiga datos del cliente.
4. **Cambiar el reflejo ante un usuario faltante**: ya no se persiguen los registros por 50
   tablas, se crea el usuario en `membership.Users` con el IncidentUserID correcto.
5. **Aplicar el protocolo de admisión** que está en el documento de recomendaciones.

---

Documento de recomendaciones de Kiran al equipo: `inbox/2026-08-28-recomendaciones-kiran-equipo.md`
Capturas de pantalla extraídas del video: carpeta `vidframes` en outputs.

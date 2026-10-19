# Verificar el SecurityID de un usuario despues de la migracion

Escrito el 28 sep 2026 desde RCS-29147, Prada. Aplica a cualquier tenant de Incident migrado a Platform.

Sinonimos para que bin/buscar lo encuentre: SecurityLevel NULL, SecurityLevel vacio, nivel de seguridad, permisos cambiaron despues de la migracion, Session Error, "Your Incident session could not be established", no puede entrar a Incident.

## Lo primero: la columna que importa es SecurityID

SecurityLevel es el nombre legible del nivel y vive en incident.LPSecurity. La comparacion se hace sobre SecurityID. Revisar si "SecurityLevel esta NULL en LPUser2" no dice nada por si solo. En Stater Bros, RCS-28061, 595 de 596 usuarios lo tenian NULL y solo algunos fallaban.

## La herramienta ya existe. ENG-7189, Kiran Vadday, 13 ago 2026

Matt Kamminga se la pidio a Kiran para que soporte deje de discutir con el cliente y conteste con evidencia. Ticket en Done.

1. SELECT en el comentario de Kiran, copiado abajo.
2. Adjunto SecurityIDMismatchCheckandFix.txt en ENG-7189, con el check y el UPDATE de correccion. El UPDATE no esta copiado aqui. Bajalo del ticket.

## Pasos

1. Corre el SELECT en la base del tenant descomentando el filtro por LoginID del usuario.
2. Lee SecurityID_Status. MISMATCH, o NewSystem_SecurityID NULL, confirma la causa. NewSystem_UserID NULL significa que el usuario no se migro, y eso es otro problema, ENG-6975.
3. Corre el mismo SELECT con el filtro "mismatches only" para medir cuantos usuarios del tenant estan igual. Si son muchos, se escala agrupado.
4. MISMATCH: el UPDATE del adjunto lo corre quien tenga escritura en produccion y aprobacion. Soporte corre solo SELECT.
5. OK: el SecurityID no es la causa. Escala a Kiran con la salida del SELECT pegada.

## El SELECT, verbatim de ENG-7189

```sql
SELECT
      lpu.UserID                              AS [OldSystem_UserID],
      u.UserID                                AS [NewSystem_UserID],
      u.IncidentUserID                        AS [NewSystem_IncidentUserID],
      lpu.LoginID                             AS [OldSystem_LoginID],
      u.UserName                              AS [NewSystem_UserName],
      lpu.EmailAddr                           AS [OldSystem_EmailAddr],
      u.Email                                 AS [NewSystem_Email],
      lpu.FirstName                           AS [OldSystem_FirstName],
      u.FirstName                             AS [NewSystem_FirstName],
      lpu.LastName                            AS [OldSystem_LastName],
      u.LastName                              AS [NewSystem_LastName],
      lpu.SecurityID                          AS [OldSystem_SecurityID],
      u.SecurityID                            AS [NewSystem_SecurityID],
      sec.SecurityLevel                       AS [SecurityLevel_Name],
      CASE
          WHEN ISNULL(lpu.SecurityID, -1) = ISNULL(u.SecurityID, -1) THEN 'OK'
          ELSE 'MISMATCH'
      END                                     AS [SecurityID_Status],
      CASE WHEN lpu.Inactive = 1 THEN 'Inactive' ELSE 'Active' END
                                              AS [OldSystem_Status],
      CASE WHEN u.Disabled = 1 THEN 'Disabled' ELSE 'Enabled' END
                                              AS [NewSystem_Status],
      CASE WHEN u.Deleted = 1 THEN 'Yes' ELSE 'No' END
                                              AS [NewSystem_Deleted]
  FROM incident.LPUser2 AS lpu
  LEFT JOIN membership.Users AS u
      ON u.IncidentUserID = lpu.UserID
  LEFT JOIN incident.LPSecurity AS sec
      ON lpu.SecurityID = sec.SecurityID
  WHERE 1 = 1
      -- AND lpu.LoginID            = 'jsmith@example.com'
      -- AND u.UserName             = 'jsmith@example.com'
      -- AND lpu.UserID             = 12345
      -- AND u.IncidentUserID       = 12345
      -- AND u.UserID               = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
      -- AND (lpu.EmailAddr LIKE '%@example.com%'
      --      OR u.Email LIKE '%@example.com%')
      -- AND lpu.SecurityID         = 7
      -- AND u.SecurityID           = 7
      -- AND (ISNULL(lpu.SecurityID, -1) <> ISNULL(u.SecurityID, -1))  -- mismatches only
      -- AND u.UserID IS NOT NULL                                        -- migrated users only
      -- AND u.UserID IS NULL                                            -- NOT yet migrated
  ORDER BY
      [SecurityID_Status] DESC,
      lpu.LastName,
      lpu.FirstName;
```

## Cuidado: OK no siempre significa sano

Descubierto el 28 sep 2026 en RCS-29147, Prada, cuando el SELECT dio OK y el usuario seguia sin entrar.

El CASE compara ISNULL(SecurityID, -1). Si los dos lados son NULL, marca OK. Un usuario sin nivel en ninguno de los dos sistemas sale como OK.

SecurityLevel_Name sale de un LEFT JOIN a incident.LPSecurity. Si el SecurityID apunta a un nivel que ya se borro, los dos lados coinciden, marca OK y SecurityLevel_Name sale NULL. Ese es el huerfano que describe ENG-7312: LPSecurity.DeleteSecurity borra sin FK y deja el SecurityID colgando en LPUser2, membership.Users y sso.SecurityLevelAssignments.

Antes de aceptar un OK, mira tres columnas de la fila: OldSystem_SecurityID, NewSystem_SecurityID y SecurityLevel_Name. OK con SecurityID NULL, o con SecurityLevel_Name NULL, es un falso negativo. Confirma el huerfano con:

```sql
SELECT SecurityID, SecurityLevel FROM incident.LPSecurity WHERE SecurityID = <SecurityID del usuario>;
```

Sin fila, el nivel no existe. Eso es dato de ingenieria, ENG-7312, y se escala a Kiran.

## Si el SecurityID sale sano y el usuario sigue sin entrar

Caso RCS-29147, Prada, 28 sep 2026: SecurityID 1 en los dos lados, nivel existente. El login no lee solo ese SecurityID. sso.GetUserSecurityLevel consulta sso.SecurityLevelAssignments y una fila ahi pisa el nivel sin dejar log, ENG-7312. Revisa:

```sql
SELECT UserName, SecurityID, Persistent, InsertedDateTime, UtcDateFrom, UtcDateTo
FROM sso.SecurityLevelAssignments
WHERE UserName LIKE '%usuario%'
ORDER BY Persistent DESC, InsertedDateTime DESC;
```

Revisa tambien NewSystem_Status y NewSystem_Deleted en la fila de ENG-7189.

## Cuidado con el join

El SELECT une por IncidentUserID. Si ese puntero esta roto, el usuario sale con NewSystem vacio aunque exista en membership.Users. Repite la busqueda por u.UserName o por email antes de concluir que no se migro. Detalle en brain/memoria/reference_esquema_usuarios_incident.md.

## Contactos

Kiran Vadday, autora de ENG-7189 y de ENG-7000, el Session Error de Stater Bros. Shandana Khan, triage de Secure e Incident en Engineering.

## Casos

RCS-29147 Prada, 28 sep 2026, primer uso. RCS-28061 Stater Bros, Session Error, resuelto en Engineering via ENG-7000. ENG-7189 enlaza RCS-28094 Vallarta, RCS-28122 Blain's, RCS-28141 Smart and Final, RCS-28211 Skechers, RCS-28217 Smart & Final.

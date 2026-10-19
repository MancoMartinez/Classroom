# Correccion, Company ID de 7-Eleven en APIS trae typo

Client Contacts.xlsx, pestaña APIS Outage List, columna Customer ID's, tiene `7eleven` para
produccion. Ese valor da "invalid company ID" en `https://apis.apprissretailcloud.com`.

El correcto es `7-eleven`, con guion. Confirmado hoy con login exitoso de `jbarber`, captura en
`bitacora/RCS-28212.md`, entrada del 15 sep "acceso resuelto".

Afecta a cualquier ticket futuro de 7-Eleven APIS que necesite entrar a produccion. El prep
`7-eleven-prep` no se probo hoy, pero ya trae el guion en el dato original, no debería tener el
mismo problema.

Pendiente: avisar a quien mantiene Client Contacts.xlsx, Kristin ya no esta, seria Aimee Wadsworth
o Colleen Knoblock, para corregir la celda en el Excel compartido.

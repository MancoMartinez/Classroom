# Blain Supply, Vivian See no aparece en el sistema

Sin ticket RCS. Llego por correo el 9 sep 2026. Juan pregunta si se relaciona con RCS-28294.

## Que pasa

Soporte no encuentra a Vivian See (Blain Supply) y pregunta si la crean para poder atender un
reset de contrasena cuyo link ya vencio. La pregunta llega como correo, no hay ticket abierto.

## Causa

HIPOTESIS. Usuario que no vinculo email antes del corte de julio, nunca se creo la fila en
`membership.Users`, y Forgot Password no lo rescata. Patron confirmado en Stater Bros, Mattress
Firm y Sportsman's. Sin buscar en las dos tablas no se puede afirmar.

No hay relacion con RCS-28294. Ese es Vallarta, la cuenta si existe y resuelve, y el sintoma es
Session Error en Chrome despues de cambiar la clave. Aqui el tenant es otro y la cuenta no
aparece. Comparten la familia de la Unificacion, no la causa.

## Evidencia

- RCS-28294 comentario de Tatiana del 2 sep 16:17: entra por Internet Explorer con la misma
  cuenta y la misma clave nueva. La cuenta existe.
- `reference_unificacion_patrones.md`: "Sin email en lpguys no se creo cuenta ninguna".
- `reference_esquema_usuarios_incident.md`: el alta escribe en `membership.Users` y se salta
  `LPUser2` y `lhua`. 77 usuarios asi en ADUSA el 10 ago, entran y no ven tiendas.

## Que hago hoy

1. Preguntale a quien mando el correo en cual sistema busco. Control Panel del tenant o el
   portal de Jira. Si es el portal, esto es alta de contacto y no toca la plataforma.
2. Antes de crear nada, busca por apellido y por nombre, sin filtrar por dominio, en
   `incident.lpuser2` (`loginid`, `emailaddress`) y en `membership.Users` (`username`).
   LPUser2 guarda el dominio viejo y membership el de la marca. Buscar por uno solo da falso
   negativo. Prueba tambien nombre y apellido invertidos.
3. Si aparece en LPUser2 y no en membership, no se crea usuario nuevo. Se corrige el email y
   despues se resetea. Crear duplica la identidad y le corta el historial.
4. Si no aparece en ninguna, es alta normal por Control Panel. Verifica despues que quedaron las
   filas en LPUser2 y en `lhua`, o entra y no ve tiendas.
5. Abre ticket RCS antes de ejecutar. Hoy no hay rastro del reset.

## Precedentes

- RCS-27555 Blain's, alta de usuarios, cerrado. Bug de validacion en `ManageUsers.aspx`, no de
  identidad. No aplica aqui.
- RCS-27406 Blain's, login con multiples cuentas, cerrado. Familia de duplicados con sufijo.

## Compromisos

Ninguno con el cliente. Nada se prometio por este correo.

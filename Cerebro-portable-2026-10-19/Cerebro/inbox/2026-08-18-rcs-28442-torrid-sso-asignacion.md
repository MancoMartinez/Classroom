# RCS-28442 Torrid SSO — a quien asignar, y por que la premisa del ticket esta mal

Fecha: 2026-08-18
Pedido en Teams (Aimee Wadsworth, 3:47 pm): "verificar los registros del SSO para ver
si la certificacion ya expiro".

## CONCLUSION CORTA

A quien: **Diego Buelvas**. Segunda opcion David Vargas.
NO Sebastian Rueda, aunque sea el de menor carga. Explicado abajo.

Pero antes de asignar: esto no es un ticket de Torrid. Es un incidente multi tenant.

## 1. La hipotesis del certificado expirado no cuadra

### Evidencia A: volumen anomalo
Tickets de login/access/SSO creados en RCS:
- 8 al 15 de agosto:  8 tickets   (linea base)
- 15 al 18 de agosto: 21 tickets  (casi 3x)

### Evidencia B: multiples clientes distintos, misma ventana
- RCS-28442 Torrid, Login Error, Critical, 18 ago
- RCS-28440 VSS, Login error with SSO, High, 18 ago
- RCS-28431 Stater Bros, Login Failure ("LPMS completamente caido"), 18 ago
- RCS-28429 Hobby Lobby, Server Error SSO Saml, 17 ago, YA CERRADO
- RCS-28409 Smart and Final, No Access, Session Error
- RCS-28419 Big Y, LPMS crashes
Un certificado de Torrid no tumba a Stater Bros, Hobby Lobby y Smart & Final.

### Evidencia C: el mismo AJ Mueller mata la hipotesis
Comentario del 18 a las 13:07: "at HQ this morning and I am able to login".
Y a las 16:39 su field team volvio a fallar.
Un certificado SAML expirado falla igual para todos, desde cualquier red, todo el tiempo.
Que dependa de la ubicacion apunta a red, IP allowlist o balanceo, no a cert.

### Evidencia D: la mas fuerte
RCS-28429 (Hobby Lobby, mismo error SAML) se cerro el 17 ago 19:34 con resolucion
**"Engineer Resolved - Restored Services"**. Sin nota de causa raiz.
"Restored Services" significa que alguien del lado Appriss restauro algo y volvio.
Eso encaja exacto con que AJ pudiera entrar el 18 en la manana y su equipo fallara
en la tarde. Servicio inestable, no certificado vencido.

### Que si hay que revisar primero
Preguntar a quien cerro RCS-28429 QUE restauro exactamente. Es muy probable que sea
la misma causa raiz y la respuesta ya exista, sin investigar nada desde cero.

## 2. Carga real del equipo Colombia

Tickets RCS abiertos (statusCategory != Done) al 18 ago 2026:

| Persona          | Abiertos | Tickets SSO/login historicos | Estado |
|---|---|---|---|
| Sebastian Rueda  | 10 | 0  | disponible |
| David Vargas     | 12 | 4  | ya tiene RCS-28219 Nordstrom |
| Diego Buelvas    | 13 | 4  | disponible |
| Camila Cortes    | -- | -- | FUERA DE OFICINA (aviso en Teams) |
| David Lora       | -- | -- | sin cuenta Jira activa |
| Julian Orjuela   | -- | -- | sin cuenta Jira activa |

## 3. Por que Diego Buelvas y no Sebastian Rueda

La diferencia 10 vs 12 vs 13 es ruido, no es carga distinta. Asi que la carga no
puede ser el criterio. El criterio real es el perfil.

Sebastian Rueda tiene **cero** tickets de SSO, login, SAML o acceso en su historial.
Su carga abierta es toda de datos y pipeline: Nike data load, Nike receipts null,
CWH voided PLU, Gen Parts receipt items, Alshaya error counts. Es el perfil de datos
del equipo. Meterlo en un incidente de autenticacion multi tenant, en Critical y con
el cliente encima, es ponerlo a aprender bajo presion en el peor momento posible.

Diego Buelvas tiene 4 tickets de SSO/login/acceso y solo un ticket abierto mas que
Rueda. Es la opcion correcta.

David Vargas tambien tiene 4 y funciona, pero ya carga RCS-28219 de Nordstrom, que
tambien es investigacion abierta. Dejarlo como segunda opcion.

## 4. Mensaje para Teams (ingles, pegable)

Happy to take this one. Before we chase the certificate angle, one thing worth flagging.

This does not look like a Torrid specific certificate expiry. We have 21 login and SSO
tickets created since August 15, against 8 in the previous week, and they span different
tenants: Torrid, VSS, Stater Bros, Hobby Lobby, Smart and Final and Big Y. A tenant
certificate would not affect all of them at once.

Two more things point away from an expired cert. AJ Mueller reported he could log in from
HQ on Tuesday morning while his field team still could not, and an expired SAML cert fails
the same way from every network. And RCS-28429 for Hobby Lobby, which is the same SAML
server error, was closed on August 17 as Engineer Resolved, Restored Services, with no root
cause recorded.

Suggested first step is to find out what was actually restored on RCS-28429, since it is
very likely the same root cause and the answer may already exist. Diego Buelvas has the
background on SSO tickets and can pick this up.

## 5. Pendientes
- Confirmar con quien cerro RCS-28429 que se restauro exactamente.
- Si se confirma causa comun, agrupar los 21 tickets bajo un solo incidente en vez de
  investigarlos por separado.

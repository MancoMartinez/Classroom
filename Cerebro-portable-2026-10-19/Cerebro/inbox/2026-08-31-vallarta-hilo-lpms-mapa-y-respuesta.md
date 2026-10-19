# Vallarta, hilo "RE: LPMS Open Ticket". A qué ticket apunta cada cosa y cómo avanzamos

Fecha: 2026-08-31
Verificado contra Jira hoy. Jira es la fuente de verdad.

## La pregunta directa: a qué ticket se refiere Noemi

RCS-28165, "Vallarta-Unable to export Excel files from exporting". Reporter Hector Flores, creado el
4 ago, assignee Viraj Kansara, label `Uni_Jul_26_ReportsExports`, estado hoy **Resolution Suggested**.

La promesa del jueves nació dentro de ese ticket, no en el correo. Viraj Kansara, 26 ago 03:12,
comentario público:

> our engineering team has completed a fix to address the export issue. We are currently planning to
> release this update this week, and it is expected to be available on your Vallarta instance by
> Thursday.

J.R. Teagle la repitió por correo ese mismo día. Viraj cerró el círculo el 27 ago 10:34:

> I'm pleased to let you know that the fix has now been released to production.

El 28 ago 04:16 el ticket pasó a Resolution Suggested sin comentario que acompañe la transición.
Noemi escribe hoy que el sistema sigue sin mostrar reportes. El ticket está declarado resuelto y el
cliente dice que no. Ahí está el conflicto.

## Cuidado antes de responder: "not showing reports" no es lo mismo que "export"

RCS-28165 arrastra dos defectos distintos desde el repro de David Vargas del 13 ago. Uno, los filtros
de fecha se resetean solos. Dos, la exportación devuelve un stub HTML de 20 B en lugar del archivo,
en XLS, CSV y XML.

Noemi dice "the system is still not showing reports". Eso describe el visor sin datos, no la descarga.
`reference_izenda_adusa_dos_rutas` fija el discriminador: si el usuario dice *receiving* o *reports we
receive*, es entrega programada por correo. Si abre el reporte y lo corre, es el visor. Son
investigaciones distintas y confundirlas cuesta horas.

Existe una tercera lectura y encaja con el resto del hilo. La lista de reportes puede venir vacía por
permisos, que es exactamente lo que RCS-28572 dejó sin cerrar. Antes de reabrir 28165 por el motivo
equivocado, hay que saber qué ve ella en pantalla.

## El mapa completo del hilo contra Jira

| Lo que dice el hilo | Ticket | Estado real hoy | Quién debe moverse |
|---|---|---|---|
| Export de Excel roto, la promesa del jueves | RCS-28165 | Resolution Suggested, Viraj Kansara | Appriss. El cliente lo contradijo |
| Cambios de perfil de usuario que no se aplican | RCS-28572 | Under Customer Review, Edwin Garzon, Low | Edwin lo dio por resuelto el 26 ago. Adalberto y Noemi dicen que no |
| AD HOC Shrink Audit sin datos en dos distritos | RCS-28637 | Work in progress, Vedant Shirude | Appriss. 4 días sin análisis técnico |
| Session Error de Noemi tras resetear contraseña | RCS-28676 | Under Support Review, **sin assignee** | Appriss. Es tuyo por defecto |
| Smart Alerts no disparan | RCS-28294 | Under Support Review, Juan | Tuyo. Escalación lista, frenada |
| Noemi debe estar en el Admin group | **sin ticket** | RCS-28094 ya la había restituido el 31 jul | Appriss |
| Auditores no pueden crear audits | **sin ticket** | Encaja con la caché de roles de 28572 | Appriss |
| Cuenta de Christian Torres | **sin ticket** | Segundo caso del mismo síntoma de 28572 | Appriss |

## Lo que el cerebro ya sabe y aplica aquí

**El export de Vallarta es ENG-5649, el defecto global de Izenda.** Ficha en `tickets/ENG-5649.md`.
El alcance documentado ahí nombra Guess, Tailored Brands, Casey's, Chemist Warehouse, WSS, PVH y Alo
Yoga. Vallarta no aparece nombrada. El síntoma es el mismo, el request de export nunca llega a
`rs.aspx`. Al 24 ago el cerebro registra que el síntoma A no tenía evidencia de fix, solo el B, el de
los reportes programados. Uso interno, no va al cliente.

**Los admins que pierden permission groups en el corte son patrón conocido.**
`reference_unificacion_patrones`: se resuelve a mano agregando `Administrators` más los tres grupos
base, y no hace falta escalarlo. Kiran sobre por qué pasa: *"Absolutely no clue. They should all
have."* RCS-28094 ya restituyó a Hector, Carlos Ardon y Noemi el 31 jul. Si Noemi volvió a perderlo,
o nunca se le aplicó, esto es reincidencia y vale documentarla.

**Dos usuarios de Vallarta bloqueados hoy tras resetear contraseña.** Noemi en RCS-28676 y Tatiana
Barcenas en RCS-28294 el mismo 31 ago a las 10:38. La causa del bucket de login es la migración en dos
pasos y ahí el reset sí resolvía. Acá el reset devuelve Session Error y el modo incógnito sí entra.
Eso apunta a cookie de sesión, no a credenciales. Es un síntoma nuevo, distinto al patrón escrito.

**Riesgo de escalación.** Adalberto Roman entró al hilo con lenguaje de compliance, *"critical to our
operational and compliance processes"*. J.R. Teagle y Colleen Knoblock están en copia. Es la misma
secuencia que ADUSA en agosto, documentada en `project_adusa_escalacion_2026_08_14`.

## Orden para hoy

1. Toma RCS-28676. Está sin assignee y es el único de Vallarta sin dueño.
2. Responde en RCS-28165 con el texto de abajo. No pegues nada de la sección anterior.
3. Devuelve RCS-28572 a Work in progress. Edwin lo dejó en Under Customer Review el 26 ago dando la
   caché por limpiada, y hoy el cliente reporta el mismo síntoma con dos casos nuevos, Christian
   Torres y los auditores. Pásale a Edwin esos dos nombres.
4. El Admin group de Noemi se resuelve a mano por el patrón de unificación. Verifica primero si
   RCS-28094 se le aplicó de verdad.
5. RCS-28294 sigue frenado porque Tatiana no puede entrar. Desbloquéala y el paquete de escalación
   que ya está listo sale.

---

## Comentario para RCS-28165, dirigido a Noemi

Hi Noemi,

Thank you for confirming that the portal access is working.

I owe you a correction on this one. We told you the export fix would be live on your instance, and we
confirmed it was released. You are telling me reports still do not come up. I am reopening this on our
side and taking it back into investigation.

Two things only you can tell me, and they decide where I look.

First, when you open the report, does the screen come back with no rows at all, or does it show rows
and the download never starts?

Second, name the report you are running. There are several report paths in the platform and they do
not fail the same way.

I will verify the export path on your Vallarta instance directly and update this ticket with what I
find.

Juan Martinez
Lead Support Engineer

---

## Compromisos que crea este texto

1. Reabrir RCS-28165 en la práctica, no solo en el comentario. Sacarlo de Resolution Suggested.
2. Verificar la ruta de export en la instancia de Vallarta y publicar el hallazgo en el ticket.
3. Ninguna fecha entregada. El próximo contacto queda anclado a la verificación, no al calendario.

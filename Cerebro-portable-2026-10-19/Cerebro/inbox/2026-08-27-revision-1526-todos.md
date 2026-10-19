# Revisión de cola, 27 ago 2026, 15:26 hora Colombia

Segundo pull del día. 18 tickets abiertos, uno más que a las 13:42. Niveles crudos 1=1, 2=2, 3=7, 4=8.
Aviso vigente: `eval_cola.py` sigue en 9/13 = 69%. El orden crudo no es confiable. Abajo va la
reclasificación a mano.

## Movimiento desde las 13:42

Un solo cambio real. RCS-28581 entró a la cola, Juan lo tomó a las 15:36. Ningún cliente escribió
en las últimas dos horas. Ningún otro ticket cambió de nivel.

## TODOs que el clasificador no ve

Cinco compromisos abiertos que ningún nivel captura:

1. RCS-28223. Matthew Kamminga preguntó a David Vargas el 25 ago: "are the affected questions all
   grid style questions? Are you able to provide reproduction steps on how to recreate this error?"
   Nadie contestó. La escalación a Engineering está frenada ahí. El ticket lo tienes tú asignado.
2. RCS-27959 PACSUN. Automation avisó el 26 ago que el ticket se cierra solo en 14 días. Pediste
   confirmación de las tres IP el 12 ago y nadie respondió.
3. RCS-28153 BYF. Mismo aviso de cierre automático el 25 ago. High, 16 días sin que el cliente oiga
   nada. Engineering ya tiene QA hecho, Gina Pilato dejó `session-cookie-refresh-platform.spec.ts`
   el 20 ago. Hay noticia buena sin comunicar.
4. RCS-28496 PVH. Automation avisó hoy 27 ago que el cliente no responde hace 7 días. Prometiste
   volver el 21 ago.
5. RCS-28093 Ahold. Prometiste el 26 ago confirmar el campo exacto con el equipo de datos. Verifica
   si el data team ya contestó.

## Contradicción abierta en RCS-27991

El 26 ago le escribiste a Paul Marderosian que corregías tu diagnóstico de julio y que lo tratabas
como issue separado. El 27 ago Shandana Khan pide cerrarlo como duplicado de un RCS de cliente ya
aceptado en el backlog de Engineering. Las dos posiciones no se sostienen a la vez frente al mismo
reporter. Decide primero, escribe después.

Tu bitácora del 26 ago ya tiene el material: RCS-28068 lululemon es el mismo defecto, Accepted into
Development desde el 18 ago con Shandana tras dictamen de Jon Morgan. Precedente RCS-23643 Foot
Locker con causa raíz y ADO 66220.

## Orden real de hoy

### 1. RCS-27991 Engage Analytics Not Populating Sections
High, Under Support Review, Paul Marderosian, 30 días. Shandana te menciona directo y espera desde
hoy. Tienes la evidencia lista. Es la única decisión que bloquea a otra persona de Appriss.

### 2. RCS-28482 AHL/DLZ Greyed out fields in Izenda
Low, Jim Cosseboom respondió el 26 ago y sigue sin respuesta. El texto está redactado desde el 24 ago
en la bitácora y nunca se pegó. Cierra en minutos.

### 3. RCS-28223 McDonald's Cash Audit Questions
Medium, Under Support Review, 21 días, 19 comentarios. Matthew Kamminga espera desde el 25 ago.
Responder desbloquea la escalación.

### 4. RCS-28327 Delhaize Loyalty Discounts not Specified
Medium, 14 días de silencio con el cliente. Prometiste update el 12 ago y no llegó. Edwin Garzón dejó
el RCA corregido el 20 ago: el cliente correcto es c046dhz, no ARDM_112. Tu plan de validación está
en `inbox/2026-08-24-rcs-28327-validacion-composer.md`. Hay qué decir y no se ha dicho.

### 5. RCS-28153 BYF Errors and logging users out
High, 16 días de silencio, cierre automático corriendo. El fix tiene QA. Escribe al cliente antes de
que el reloj lo cierre.

### 6. RCS-27959 PACSUN IP Whitelisting
Medium, 14 días de silencio, cierre automático corriendo. Persigue la confirmación de las tres IP.

### 7. RCS-28581 CWH POS Number has regressed to previous mapping
Medium, nuevo hoy. James McKenna reportó, retiró el reporte, y volvió a abrirlo el 26 ago diciendo
que el fallo aparece en otro periodo de datos. Ya tomaste ownership. Empieza la investigación cuando
bajes lo de arriba.

## Resto, sin acción hoy

- RCS-28123 ADUSA Case assignment. Prometiste update el 26 ago. Engineering revisa el issue del popup
  de confirmación. Sigue vivo, no vencido.
- RCS-28256 Appriss Incident timeouts. High. Pediste confirmación a Colton Neal el 25 ago. Debes el
  follow up del login de Vincent Fortner. Vence en dos días.
- RCS-28294 Vallarta Smart Alerts. Respondiste a Shandana el 26 ago con los pasos de reproducción.
  En movimiento interno.
- RCS-27676 RLC SFTP. 23 días de silencio, el más largo. Pediste las IP públicas a Tyler Aken.
  Persigue esta semana.
- RCS-28122 Blain's. 8 días de silencio. Preguntaste por Admin Tools y por las fotos de Compliance
  Audit el 19 ago.
- RCS-28282 Co-op. 5 días. Esperas la lista de países.
- RCS-28099 CWH Item Discount Logic. Lo lleva David Vargas. Bryant McAnnally arma el set de datos.
- RCS-27765 Winn-Dixie. Hilo reunificado el 25 ago, monitoreando el correo.
- RCS-28289 Vitamin Shoppe. Joe Austin espera a que Scott vuelva de vacaciones.

## Recomendación única

Empieza por RCS-27991. Es lo único donde una persona de Appriss está bloqueada esperándote, la
respuesta está armada desde ayer, y hay una contradicción con lo que le dijiste al reporter que se
agrava cada hora que pasa.

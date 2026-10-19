# Consolidado de las cinco reuniones — 2026-08-28

Fuentes, todas transcritas con whisper large-v3-turbo el 2026-08-28:

- `2026-08-28-end-of-week-meeting.md`, 28 min, equipo de soporte con Zach/J.R.
- `2026-08-28-l2-l3-meet.md`, 28 min, L2-L3 con Zach, Payman, Matt, Amy, Viraj.
- `2026-08-28-consejos-jr-2.md`, 12 min, uno a uno de Zach con Juan.
- `2026-08-28-another-meet-jr.md`, 9 min, Zach con Angie del cliente, más cierre con Juan.
- `2026-08-28-town-hall-agosto.md`, 59 min, Town Hall de compañía.

---

## 1. Lo último que J.R. dijo sobre Ahold al final de la EoW

Son tres cosas distintas, en este orden dentro de la grabación. La tercera va después de las
despedidas, cuando la reunión ya se había disuelto y quedaron J.R. y Juan.

### 1.3 Tres tickets nuevos de ADUSA, minuto 27:44, lo literalmente último

J.R. retuvo a Juan al cierre: "Juan, I need to catch you still. I've got a meeting right now, but
maybe 11:30 my time, which I think is 10:30 your time." Tema declarado: "it's about three new
tickets that were fired for. Basically I think two of them are already closed up by Ryan Barrow.
The other one is in development or something right now. We just need to make sure that those go
onto the list." Pidió buscarlos antes para que la reunión fuera corta y preguntó si estaban en el
tracker. Juan respondió que no sabía.

Los tres están identificados y verificados contra Jira hoy 28 de agosto. Son los tres que faltaron
en el D8 y entraron en el D9. J.R. dijo Ryan Barrow. El nombre real es **Ryan Barlow**.

| Ticket | Resumen | Estado en Jira | Asignado | Reporter |
|---|---|---|---|---|
| RCS-28588 | Ahold - Store numbers should be 4 digits | Completed, Resolved, 27 ago 11:16 | Ryan Barlow | Leigh Ann Stubbs |
| RCS-28589 | Ahold - Store file showing invalid characters before numeric value | Completed, Resolved, 27 ago 12:14 | Ryan Barlow | Leigh Ann Stubbs |
| RCS-28596 | Ahold-Delhaize - Employees Duplicated in a View | Accepted into Development, tocado hoy 08:25 | Shandana Khan | Jim Cosseboom |

Los tres se crearon el 26 de agosto por la mañana, antes de armar el D8, y el barrido del D8 nunca
buscó tickets nuevos del cliente. Por eso no estaban en la lista cuando J.R. preguntó.

Estado al momento de la reunión de las 10:30:

- **Ya están en el tracker.** El D9 los incorporó. RCS-28588 y RCS-28589 abrieron el tema nuevo
  "Store file and location data".
- **RCS-28596 tiene causa confirmada en código.** El query de búsqueda de empleado hace LEFT JOIN a
  Store por StoreNo. En Delhaize la tienda solo es única por Division más StoreNo. El mismo arreglo
  ya se aplicó para Lux, quitando el join en `EELookupList.aspx.vb`.
- **RCS-28093 comparte esa raíz y no comparte el arreglo.** RCS-28596 es código del lado de
  Appriss. RCS-28093 depende de que ADUSA pueble la posición 20 de `DA_Employee_Info.dat`. Van
  separados.

Lo que J.R. no sabía y conviene decirle: el hueco no fue de esos tres tickets. Fue del método de
barrido. El barrido de hoy ya filtra por reporter de dominio adusa.com, así que el fallo no se
repite.

### Las otras dos menciones, en orden de aparición

**Caché antes de probar cualquier fix de unificación. Esta es la última.** Minuto 25:25 al 26:01.
J.R. lo dijo dirigido a Juan, Santosh y Viraj, y lo enmarcó como falla repetida con Ahold. Cita
textual: "I've already seen it multiple times with Ahold, they don't clear their cache first and
the fix doesn't." Instrucción concreta: cuando le pidas al cliente probar un arreglo, mándale en
el mismo mensaje las instrucciones para limpiar caché en Mac y en PC. Lo llamó "part of our DNA".

Acción directa para el tracker de Ahold: los tickets en verificación que llevan días sin
confirmación del cliente pueden estar bloqueados por caché, no por el fix. RCS-28535 lleva sin
prueba y sin respuesta del cliente.

**Escalación ejecutiva de Ahold.** Minuto 24:42. J.R. usó a Jim como ejemplo del ejecutivo que
salta el ticket. Cita: "when their executives, like the guy Jim from Ahold, when he's like, what
the fuck is happening, that way he can bypass all the ticket shit and just go directly to somebody
and talk about it." El camino contractual queda en tres niveles: support manager, o sea Camila y
en su ausencia uno de los leads. Después customer success manager. Después J.R., con móvil y
correo en los contratos.

Ojo con el nombre. Hay dos Jim en las grabaciones de hoy. Jim Cosseboom es el contacto de Ahold y
es el de esta mención. Jim Dijon es interno de Appriss y renunció, ver punto 5.

---

## 2. Jira se muda de RCS a SUP

El cliente radica en SUP. Nosotros somos dueños de ese ticket de punta a punta y nunca lo soltamos.
Cuando otro equipo tiene que trabajar, creamos ticket en ENG o en el proyecto de delivery y lo
enlazamos. La actualización del ticket ajeno se refleja en el nuestro. RTS sobrevive para los
tickets generados por alerta. Los RCS viejos siguen visibles para el cliente.

Llega dentro del próximo mes, con sesión de entrenamiento antes.

El modelo de enlace ya corre en unificación: un ENG amarrado a 16 o 17 tickets de soporte. Ese es
el argumento de escala. Una persona dueña de 30 tickets del mismo defecto hace bulk updates y
cierra en bloque.

El dashboard de Jira queda desactualizado. Hoy cubre RCS y RTS. Hay que añadir SUP y tracking de
tickets ENG. Ese segundo punto lo levantó Viraj y J.R. lo aceptó en la llamada.

---

## 3. SLAs nuevos, 30 de septiembre

Se elimina el compromiso de resolution time. Se habla de remediation y no se compromete tiempo.

Existe un set de fallback guardado con legal, finanzas y ventas para negociaciones duras. Trae
first reply más agresivo y remediation comprometido. Nunca resolution. Cualquier cosa fuera de ese
set necesita aprobación de J.R.

TJX es el caso que se quiere desarmar. Exige 15 minutos de respuesta y en algunos casos 15 minutos
de resolución. J.R. lo llamó insostenible. Los clientes con SLA custom viejo se renegocian en
renovación de contrato con ventas empujando.

**Prioridad y customer impact se separan.** En SUP el cliente no ve priority. Ve customer impact
critical, high, medium, low, y le preguntan por qué le impacta. Priority queda del lado interno y
la define el contrato. L1 sigue pudiendo cambiar priority para alinearla al contrato, con TJX como
excepción.

El escalate dentro del ticket deja de ser un status. Pasa a ser un checkbox que dispara preguntas
sobre el impacto al negocio. Esto es distinto de la escalación contractual del punto 1.

---

## 4. Backfill de datos, política fijada por J.R. en la EoW

El retention period marca el techo razonable de lo que el cliente puede pedir.

| Situación | Por defecto | Si el cliente empuja |
|---|---|---|
| Caso general | 3 meses, y se le pide validar | hasta 1 año |
| El cliente dañó la data | solo hacia adelante | 3 meses |
| Nosotros dañamos la data | hasta 1 año siempre | hasta 1 año |

El costo de Snowflake no cambia la respuesta al cliente. Se come el costo y después se discute con
ingeniería. Payman levantó el tema desde un caso real donde el cliente pidió un año de corrección.

---

## 5. Lo que cambió en la operación

**Jim Dijon renunció.** Último día el 15. Se va a fundar algo propio y no es parte de Project
Atlas. Conoce Secure y sus clientes desde la fundación. J.R. lo llama irreemplazable. Quedan tres
trainings antes de que salga, probablemente miércoles, viernes y lunes, sobre cómo usar el
producto. Quedan grabados. Si eres empleado y no te llegó la invitación al final del día, avisa,
porque significa que no estás en la lista de distribución. Matt tiene el encargo de sacarle a Jim
las notas personales y cuadernos que nunca compartió.

**SAS se murió.** La licencia venció y el periodo de gracia de 15 días se agotó. Es Statistical
Analytics Software, no software as a service. Con eso corría el ETL de la compañía y ahí están
escritos todos los `master*.sas`. Engage depende de eso. Si ves alertas de monitoreo de Engage
rotas, avisa a Payman. No hay arreglo y la licencia no se renueva. Nadie le avisó a los clientes.
Amy le pidió a Rip el mensaje oficial. J.R. reconoció que no existe política de end of life y que
la va a construir.

**Tickets de la migración a Snowtime, proceso de Matt y J.R.:**

1. Triage primero, confirmar que el problema lo causó la migración. J.R. citó cinco tickets donde
   cuatro eran de la migración y uno era anterior.
2. Primera pregunta al cliente: cuándo empezó el problema, con fecha.
3. Truco de Payman para verificar en base de datos: los transaction ID nuevos son más largos que
   los viejos. ID largo es post conversión.
4. Revisar el canal de Snowtime, sección migration milestones. Ahí está el cliente, la fecha de
   migración y el desarrollador asignado.
5. Escalar al desarrollador de esa lista. Duda general va a Adarsh, manager del programa. Si Adarsh
   no responde, Daniel Undersby ayuda a ubicar a la persona.
6. Configuración de Secure no la toca ese equipo. Un ticket de Maya cayó ahí por error.

Los clientes en migración reciben notificación desde hace dos o tres semanas, vaga a propósito
porque hay varias migraciones corriendo a la vez.

**Amy sobre la cola:** vigilar high y critical y confirmar que se asignan dentro del SLA. Hay
clientes a los que se les paga de vuelta cuando se incumple. L1 postea esos tickets en Teams.

**Board de low hanging fruit.** Matt arma un tablero de defectos para quien tenga tiempo libre y
quiera tocar código. La cola de soporte manda. Solo se toca el board si la cola está bajo control o
si el defecto tumba algo de la propia cola.

---

## 6. Lo que J.R. le pidió a Juan

**Sesión diaria de 30 minutos con Amy.** Amy está hasta finales de septiembre. El encargo es
sentarse a revisar la cola: quién está disponible y qué tickets se asignan. J.R. quiere a Baraj en
esa llamada si los horarios cuadran. Hoy no cuadran y el ajuste del horario del equipo de Baraj
espera a que Camila regrese. Si Baraj no entra, el output se le pasa igual: "Baraj, look, I need
you to take these five tickets and assign them to somebody in your team first thing in the
morning." La razón declarada es meter a Baraj en el patrón de asignar a diario.

**Método uno, bounce the ball.** Todo ticket nuevo recibe respuesta proactiva rápido. Cinco
minutos de lectura y una o dos preguntas concretas: screenshot, pasos exactos de reproducción, ID
de la alerta. El punto no es resolver. El punto es que el cliente sepa que alguien lo está mirando.
Cuando devuelves la pelota, la respuesta puede tardar una semana, y ese tiempo se invierte en
clientes que sí están trabajando contigo.

**Método dos, barrer tickets sin comentario público.** Arma la vista donde quieras. J.R. fue
explícito en que la herramienta le da igual. Regla actual: mínimo una respuesta pública por semana
por ticket. La meta es cada dos o tres días hábiles. El comentario puede ser mínimo. Decir algo.

**Bloquear 30 minutos diarios.** Rutina obligatoria de team lead: barrer la cola del equipo,
barrer la cola sin asignar, barrer escalaciones. El resto del trabajo va en las seis o siete horas
restantes. J.R. dijo explícitamente que no quiere jornadas de 12 o 13 horas. Quiere 8 a 9 horas
contando almuerzo.

**Hacer estrellas al equipo, no ser la estrella.** J.R. pidió competencia sana con el equipo de
Viraj y dijo que a Viraj le puso el mismo encargo. Esa comparación se habla solo con él.

**Advertencia de carga.** "The more you show me you can do, the more I'm going to give you, up
until the point when you're like J.R. you gotta stop, and then I'll back off." El freno lo pone
Juan.

J.R. aclaró dos veces que nada de esto es crítica. Descartó la técnica del sándwich para este caso.

### Menciones públicas a Juan

- "Juan has a good handle on what all the issues are for the unification project."
- "Juan's been out there by himself. I left him, Camila left him. He's been manning the ship. He's
  enjoying calls with all the delays and angry customers."
- Juan reportó el primer cambio de código hecho desde soporte y el primer cambio a base de datos de
  producción. En la L2-L3 lo enmarcó así: soporte ya no se detiene en diagnosticar y entregar el
  problema a ingeniería, ahora arregla parte.
- En la llamada con Angie, J.R. aclaró que Juan entró como opcional y no perdió nada por llegar
  tarde: "I would have pinged you in chat if it was actually important for you to join."

---

## 7. Pendientes concretos que salieron de las llamadas

1. **Reunión con J.R. el viernes, 11:30 hora de él, 10:30 hora de Juan.** Tema: los tres tickets
   nuevos de ADUSA. Resueltos en el punto 1.3, con estado verificado en Jira y ya en el D9.
2. **Reunión con Santosh y Baraj** para repartir el follow-up de los cerca de 100 tickets de
   unificación del Excel. J.R. la autorizó a pedido de Santosh, que ofreció a L1.
3. **Instrucciones de limpieza de caché** para Mac y PC, listas para pegar junto a cada petición de
   prueba de fix. Ver punto 1.
4. **Vista de tickets sin respuesta pública** en X días hábiles, para el barrido diario.
5. **Agendar la sesión diaria con Amy**, y meter a Baraj si el horario lo permite.

---

## 8. Town Hall, lo que aplica al trabajo diario

**Gasto de AI bajo control de niveles.** El gasto de enero a julio se disparó, con un salto de 113%
en un solo mes. Oz fue explícito en que no es orden de gastar menos. El objetivo es predictibilidad.
Cada equipo quedó en uno de seis niveles según su uso de julio. El nivel pone techo de gasto y
controla qué modelos se pueden usar. Hasta ahora los únicos que tocaron techo son ingenieros. Si
tocas el techo, hay una fila en el help desk para "claude limit reached". No es aprobación
automática. Preguntan qué modelos usas, en qué proyecto y cómo lo estás abordando.

Elección de modelo según Rick: Haiku para clasificar, etiquetar y extraer datos. Sonnet como
default para todo, incluido redactar correos, armar slides, resumir reportes y escribir código.
Opus solo para extended thinking, pasos dependientes con trade offs reales o información
contradictoria. Alto riesgo no es lo mismo que alta complejidad. Un correo importante sigue siendo
un correo. Sonnet 5 viene en effort alto y se puede bajar a medio. Sonnet 5 en medio rinde parecido
a Sonnet 4.6 en alto. Sube el effort antes de saltar a extended thinking.

**Platform unification golpeó la pared.** Lo dijeron sin adornos. Migraron 20 clientes a principios
de mes y salió mal. Hubo problemas de desempeño e ingeniería asumió el error de forma explícita.
Prioridad uno fue estabilizar a los afectados, hecho. Siguen root cause analysis y revisión de los
demás clientes. No avanzan más con el proyecto hasta resolverlo.

**Snowflake a RDM terminado**, 99 clientes migrados desde Greenplum. Greenplum queda fuera en todas
partes. Snowtime va en 47 clientes mapeados en el año. Salida de data centers a Azure va por más de
la mitad.

**Linking 2.0 en vivo para todos los clientes.** Vinculación de devolución con consumidor original
subió de 50% a 65%. Tasa de denegación pasó de 1.78% a cerca de 2%. Cliente nuevo entra con un
cambio de configuración.

**Dos releases grandes de Secure en septiembre:** trending metrics con detección de anomalías vía
Sidekick, y spotlight search con Ctrl+K o Cmd+K sobre 10 tipos de objeto.

**Financiero:** net ARR growth entró en rojo por primera vez en el año. Bookings van 2.5 millones
bajo plan. La proyección de cierre queda cerca de un millón corta contra la meta de 7.8 millones.
EBITDA sigue en verde. Home Depot renovó por tres años y va camino a 6.2 millones.

---

## 9. Contradicciones y cosas que hay que verificar

- **Dos Jim.** Jim Cosseboom es Ahold. Jim Dijon es interno y renunció. Whisper no los distingue y
  las transcripciones dicen solo "Jim" en varios puntos. Al citar cualquiera de las dos
  grabaciones, nombra el apellido.
- **Whisper no reconoce "Appriss Retail".** Aparece como Everest Retail, No Fish Retail y April.
  También convierte Ahold en Ahol, Viraj en Miraj y Barrage, y Juan en Kwan, Quan, Ron y Fawn.
- **El archivo `Consejos JR.m4a` no es coaching.** Es el Town Hall completo. El nombre engaña.
- **Ryan Barrow no existe.** Es Ryan Barlow, rbarlow@apprissretail.com. Whisper le comió la ele.
- **La grabación con Angie queda en silencio desde 09:13** y whisper alucinó una cola de "Bye-bye"
  hasta el 10:58. Ese tramo está recortado.
- **El retention period del caso de Payman está sin confirmar.** Dijo 13 meses "probablemente, no
  lo he chequeado". El cliente dice 12. Nadie lo verificó en la llamada. El nombre del cliente sale
  como "Ali's" en la transcripción y no es legible. Sin ese dato, la tabla del punto 4 no se puede
  aplicar a ese caso.

---
fecha: 2026-09-14
autor: Claude, cerebro-ticket
tema: RCS-28881, plan de reproduccion paso a paso en nexcom-prep
---

# Punto de partida

Juan entra a nexcom-prep en `apis-uat.apprissretailcloud.com` con la cuenta jbarber. El dashboard
Claims carga completo: Case List con filas, Incident Status Report-T con totales, Audit Graph con
las barras de Operational Review Administration en estados 0, 1, 4 y COMPLETE. El entorno de APIS
para ese tenant rinde pantallas y consultas sin problema.

El Audit Graph nombra Operational Review Administration. Es la familia del audit del ticket, que
Carlo llama Annual Ops/Services Review.

Regla de la sesion: solo inspeccionar. Nada de Build All Screens, nada de guardar en Admin, nada
de tocar System Options. Prep no es un ambiente desechable, es el sitio de demo del cliente.

# Pasos

1. Confirmar version de UI. Admin, Users, tu propio usuario, o el footer. 270 es la clasica, 275
   la renovada. Kristin lo pone como paso previo a diagnosticar porque el render del formulario
   cambia entre las dos. Anotar cual es.

2. Audit Section, Audit Center. Buscar el template Annual Ops/Services Review, o el nombre mas
   cercano de la familia Operational Review. Anotar el nombre exacto y el Template ID.
   Si el template no existe en prep, la reproduccion se acaba aqui y hay que pedirle a Milan un
   export o los logs. Decirlo asi de claro.

3. Abrir ese audit en modo edicion, que es lo que hacia Carlo. No en vista.
   Resultado A, sale en blanco. Reproducido. Ya no dependes de NEXCOM para diagnosticar.
   Resultado B, abre normal. Prep esta sano y la diferencia vive en prod, en la data del template
   o en una edicion que solo esta alla.

4. Con el panel en blanco en pantalla, abrir las herramientas de desarrollador antes de recargar.
   En Safari hay que habilitar el menu Develop en Ajustes, Avanzado. Chrome sirve igual con F12.
   Recargar con la pestaña Network abierta y mirar la peticion del frame de contenido.
   Interesa el status HTTP y el tamaño de la respuesta. 500 apunta a excepcion del servidor.
   200 con cuerpo vacio apunta al render del template. 524 o 504 apunta a timeout, que es el
   patron de RCS-28139. Guardar la captura y el HAR.

5. Abrir otro template de audit cualquiera en el mismo prep, en edicion.
   Si ese abre y el de Operational Review no, el problema es del template y no del modulo.
   Ese es el hallazgo que cierra la hipotesis.

6. Segundo sintoma. En el mismo prep, Common Tasks, New Case, y ver si la pantalla de creacion de
   caso abre. Eso separa el case entry de APIS del portal de Jira sin tener que preguntarle nada
   a Carlo.

# Lo que cada resultado significa para el ticket

Blanco en prep y en prod, con otros templates abriendo: template corrupto, alcance un cliente,
sigue con Megha, y la salida es que NEXCOM restaure su version anterior.

Blanco en todos los templates de audit en prep: es el modulo de Audit de APIS. Sube el alcance a
los quince clientes APIS activos y deja de ser Medium.

Todo abre bien en prep: la diferencia esta en prod de NEXCOM. Ahi si toca Milan Djordjevic con
los logs de IIS, y el ticket se queda esperando al cliente.

# Antes de escribir a Carlo

No mandar el texto del otro archivo hasta tener el resultado del paso 3. Si reproduces en prep, la
peticion al cliente cambia y le quitas de encima la prueba de abrir otros templates.

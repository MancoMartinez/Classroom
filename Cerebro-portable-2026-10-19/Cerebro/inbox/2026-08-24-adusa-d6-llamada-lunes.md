# ADUSA · llamada del lunes, tres tickets sin dueño, D6 y correo · 24 ago 2026

Verifiqué los 39 tickets contra Jira en vivo. El tracker de Chris trae los cuatro nuevos con las celdas de estado vacías y RCS-28482 duplicado en dos filas, la 60 y la 61. El D6 corrige las dos cosas. Cada ticket queda completo abajo, sin remitir a otra sección.

## 1. Lo urgente, tres tickets sin dueño

Ninguno de los tres tiene assignee en Jira y ninguno tiene una sola respuesta de Appriss más allá del acuse automático.

RCS-28519, usuarios que no ven ninguna tienda. Jim lo abrió el 21 a las 05:18. Van tres días. Jim agregó a Sammy Rivera el 21 a las 17:05 y a las 17:06 escribió que ya probaron cerrar sesión, limpiar caché y reiniciar sin resultado. Nadie contestó. En la llamada dijo que tienen veintitantos casos esperando para entrar al sistema por esto. La descripción del ticket solo nombra a Deborah Jean, LP User Level 2, tienda S&S 0498. Sammy Rivera está en el comentario, no en la descripción, por eso parecía faltar.

RCS-28533, pantalla que no renderiza. Jim lo abrió el 22 a las 13:39. Van dos días. El usuario es Ralph Valentine, la descripción lo nombra aunque en la llamada Jim no lo dijo. Tiene las dos capturas adjuntas, la vista rota y la vista correcta de un colega. Nadie contestó.

RCS-28535, error Forbidden al subir adjuntos. Jim lo abrió el 23 a las 07:16 después de que cerraras RCS-28124. Empezó con un usuario, Ian Jordan, subiendo video de body worn camera en MP4. **Hoy a las 11:43 Leigh Ann agregó dos usuarias más de Hannaford**, Kayla De Jesus-Morales y Erica Shrader, con tres números de caso concretos: 2026-HANNAFORD BROS. CO., LLC-8327-51, 2026-HANNAFORD BROS. CO., LLC-8109-161 y 2026-HANNAFORD BROS. CO., LLC-8109-164. Ese comentario tampoco tiene respuesta.

Ese dato de Leigh Ann contradice lo que Jim dijo en la llamada, que solo un usuario lo había reportado. Su comentario entró a las 11:43, probablemente después de la llamada. Ya no es un caso aislado.

Asigna los tres y contesta. Para el 28535, el comentario:

```
Hi Jim and Leigh Ann,

Thanks for the case numbers. We have three to work from now, and the earlier fix on RCS-28124 clearly does not cover these.

We are checking the three cases against the upload path to see whether the MP4 size or the format is what triggers the Forbidden response. We will come back with what we find.

Thanks.
```

Para el 28519:

```
Hi Jim,

Thanks for confirming the usual steps were already tried. We are reviewing both accounts, Deborah Jean and Sammy Rivera, against their store assignments and profile level.

RCS-28415 was the same symptom across a much wider group and was fixed at the data level, so we are checking whether these two were missed by that correction rather than treating this as something new.

Thanks.
```

Para el 28533:

```
Hi Jim,

Thanks for the two screenshots, having his view alongside a working one is what we needed.

We are comparing them against how that screen is meant to lay out to work out what differs on his session. We will come back once we know.

Thanks.
```

Transiciones: los tres pasan de Under Support Review a Work in progress al asignarlos.

## 2. Donde me equivoqué el viernes

RCS-28482, campos grises en Izenda. Estado Work in progress, dueño tú. Jim respondió el 22 a las 10:33, textual: "I think there is a misunderstanding, what I am trying to do is go to the MISC tab at the top to change report distribution which I am unable to access. That info is not in the Data Sources".

El comentario que redacté el viernes salió de lo que Kiran describió en la reunión, que los campos se alcanzan por Data Sources. Kiran diagnosticó acceso a campos. Jim no necesita campos, necesita la pestaña MISC para cambiar la distribución del reporte. La respuesta no aplicaba al problema y Jim lo dijo. Lleva dos días sin contestar.

En la llamada Jim lo repitió con más detalle: son dos reportes, uno clonado del otro, quiere cambiar la hora de ejecución programada de las 7:30 de la mañana, tiene la primera y la última pestaña disponibles y la del medio no. Los reportes corren bien, lo único bloqueado es editarlos.

```
Hi Jim,

Understood, and apologies for the earlier reply that pointed you at the wrong place. The MISC tab is where the distribution and schedule settings live, and that is what is rendering greyed out.

We are looking at what governs that tab specifically on those two reports rather than at field access. We will come back with what we find.

Thanks.
```

## 3. Lo que la llamada cierra

RCS-28353, error 502 al actualizar la tienda. Jim lo probó varias veces el viernes sin fallos y dijo que quedó más rápido que antes, lo que confirma que el error venía de la latencia del lookup. Ya está Closed en Jira.

RCS-28356, lentitud general. Jim no ha tenido reportes desde el despliegue del jueves y él mismo lo probó desde un avión, condiciones malas, sin problemas. Ya está Completed.

RCS-28407, errores 502. Jim lo da por resuelto, con la salvedad de que un 502 suelto puede pasar en cualquier plataforma web y lo que le preocuparía es un patrón. Ya está Completed.

RCS-28292, migración del servidor. Esto resuelve lo que quedó pendiente el viernes. Jim confirmó en la llamada, a las 16:11, que revisó una tienda Food Lion al azar y los cambios que subió al FTP el viernes se aplicaron correctamente, incluido el cambio de Sylvana Baxter de regional AP manager a director. Appriss no vio nada raro de su lado. El ticket ya está en Under Customer Review.

## 4. Lo que sale con el release del jueves 27

Appriss se comprometió a cuatro cosas en ese release, todas sujetas a QA.

RCS-28342, títulos de puesto. La data ya está corregida por completo. Falta un cambio de código para que la sincronización no se pierda con usuarios nuevos. Jim propuso revisar hoy los usuarios afectados y volver a validar el jueves después del release, porque si algo falla hoy pero se arregla el jueves, sabrán que era eso y no otra cosa.

RCS-28093, búsqueda de empleados por marca. El cambio está construido y sale el jueves. Nada que validar hasta entonces.

RCS-28021, export de Izenda. Jim confirmó que el viernes y el sábado seguía fallando. Appriss lo está probando y apunta al jueves.

RCS-28304, ancho del campo Case tier. Va más atrás en pruebas que los otros tres. Appriss avisará de una forma u otra antes del release.

## 5. Lo que espera confirmación de Ahold

RCS-28123, asignación de casos. Ya está en Under Customer Review. Jim le pidió a Leigh Ann seguir con los usuarios que reportaron el error. Él ya les había escrito y no tuvo respuesta, lo cual interpretó como buena señal.

RCS-28196, campos con null. Estado real en Jira: Work in progress. En la llamada Appriss dijo que ya está resuelto en el ambiente y que solo falta que Leigh Ann lo verifique. Ese es el mismo caso que el 28123, que sí está en Under Customer Review. Te recomiendo transicionarlo para que los dos queden parejos. El D6 lo deja en Work in progress porque es lo que dice Jira ahora mismo.

## 6. D6 generado

Archivo: Appriss ADUSA-Support-Tracker - 08242026 D6.xlsx, construido sobre el D5.

Verifiqué los 39 tickets uno por uno contra Jira. Cero desviaciones.

Tres tickets nuevos: RCS-28519 en Store and brand restrictions, RCS-28533 en Case entry and assignment, RCS-28535 en Attachments and file handling. Los tres en Under Support Review, Active with Appriss, sin dueño.

Estados alineados con Jira: RCS-28093 a Work in progress, RCS-28123 a Under Customer Review, RCS-28353 a Closed, RCS-28356 a Completed, RCS-28407 a Completed, RCS-28292 a Under Customer Review, RCS-28482 a Work in progress.

Total 39 tickets. Resolved 27, Pending Ahold verification 3, Awaiting Ahold input 0, Active with Appriss 9.

Dejé fuera RCS-28447, cerrado el 19 y nunca contado en el tracker del cliente, igual que en el D5.

## 7. Correo para Jim

Appriss se comprometió en la llamada a avisar por correo qué pasó QA para el release del jueves. Jim eligió correo sobre comentarios en los tickets cuando se lo preguntaron. Ese aviso no se puede mandar todavía, los cambios no han pasado QA.

Hoy va el tracker, el dato de que los tres tickets del fin de semana ya tienen ingeniero, y la confirmación de los dos compromisos. No hay nada que pedirle, en la llamada entregó todo y Leigh Ann completó lo que faltaba en RCS-28535.

```
Hi Jim,

Tracker attached, updated through today's call.

The three you raised over the weekend are now assigned and being worked.

We will email the group once the release items clear QA, so you know what is landing before you test Thursday morning. Confirming the check-in for late morning Thursday, Matt will be on from our side.

Thanks,
```

## 8. Estado final del D6, con los dueños ya asignados

Los tres tickets quedaron asignados a las 20:22 y el D6 se regeneró con eso. RCS-28535 a Edwin Garzon, RCS-28519 y RCS-28533 a Diego Buelvas, los tres en Work in progress. Cero desviaciones contra Jira.

Total 39 tickets. Resolved 27, Pending Ahold verification 3, Awaiting Ahold input 0, Active with Appriss 9.

Ningún ticket queda sin dueño. Es la primera vez en la semana que se cumple.

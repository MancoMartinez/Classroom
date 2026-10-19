# Cambios desde el D12, para el D13

Fecha: miércoles 2 sep 2026. Baseline: Appriss ADUSA-Support-Tracker - 09012026 D12.xlsx, 45 tickets, 35 resueltos, 10 activos.

Aviso primero. Bash sigue bloqueado en esta sesión después del reinicio. No puedo abrir ni generar el .xlsx todavía. Lo de abajo es la verificación completa contra Jira y el texto listo para pegar. El archivo del tracker lo tienes que armar tú a mano hoy, o esperamos a que se habilite el acceso.

## Ticket nuevo que falta en el tracker

RCS-28681, Delhaize/DHZ: Refund Searches are Broken. Reporter Becky LaPierre, un contacto nuevo de ADUSA que no habíamos visto antes. Creado 31 ago 14:43, cerrado 1 sep 09:55 por Vlad Bogus. Causa: se cargaron dos archivos de tiendas el mismo día y quedó un número de tienda duplicado en ARDM_046.REFERENCE_LOCATION, lo que duplicaba cada fila de refund search. Vlad quitó el duplicado y Becky confirmó que ya funciona. Va como resuelto en el D13.

Si ya lo tienes en el tracker (6) que subiste, dime y no lo cuento dos veces.

## Los 10 activos del D12. Qué cambió en cada uno

RCS-28093. Pasó a Accepted into Development. Tú le preguntaste a Matt Kamminga el 31 ago si el loader está descartando la posición 20 para algunos empleados, aunque ADUSA confirmó que no hay vacíos de su lado. Matt no ha contestado todavía. Sigue activo, ahora en manos de ingeniería.

RCS-28123. Matt Kamminga contestó el 1 sep. La ruta de reasignación no lleva a una pantalla de confirmación porque esa ruta se quitó del código a propósito hace tres años y medio. No es un defecto. Marcar un caso completo sí lleva a una pantalla así, y esa parte funciona como se espera. Esto responde lo que le dijiste a Jim el 26 que ingeniería estaba revisando. Ya hay respuesta para pegar, ver abajo.

RCS-28281. Sin cambios desde el 31 ago. Sigue con el hueco del 22 de agosto y varias fechas 100 a 200 mil por debajo del promedio, según el correo de Jacquelyn del 31.

RCS-28482. Sin ningún movimiento desde el 26 de agosto. Ya son siete días. Nadie de Appriss volvió a comentar después de que Jim confirmó que el reporte corre pero no se puede editar el tab MISC.

RCS-28535. Sin comentario nuevo desde el 26 de agosto. Sigue esperando el tamaño en MB y la hora de una falla concreta que le pediste a Leigh Ann.

RCS-28589. Cambió a Under Engineering Review el 1 sep a las 18:46. Jim reportó esa misma mañana que las comillas simples siguen apareciendo cuando se exporta el location listing. Ryan Barlow confirmó que el valor en base de datos no tiene comilla, así que la entra Excel o la función de exportar. Shandana lo asignó a Matt Kamminga para que ingeniería revise la exportación a archivo. Hay texto para pegarle a Jim, ver abajo.

RCS-28596. Sin movimiento desde el 28 de agosto. Ya son cinco días. La causa técnica está documentada, el join a Store produce los duplicados de empleado, pero sigue sin ticket de ENG.

RCS-28667. Megha escaló hoy 2 sep a las 03:03. La sospecha es que la unificación deja las cuentas nuevas sin jerarquía asignada por defecto, y pidió a ingeniería confirmar si es un backfill puntual o un defecto permanente para todo usuario nuevo. Sigue en Under Engineering Review.

RCS-28683. J.R. le pidió a Megha el 1 sep que consiga pasos de reproducción y abra el ENG. Nada nuevo desde entonces.

RCS-28693. El más movido de todos hoy. Vlad le hizo cuatro preguntas a Leigh Ann a las 06:21. Leigh Ann contestó a las 08:48 con las URLs de test y producción, y confirmó que Harrison Xu debería tener el rol AAG-PP-LPMS-AP-LEVEL-2-AHOLD y que todavía no está provisionado. Vlad volvió a escribir a las 11:13, hace unos minutos, confirmando que test y producción usan la misma configuración SSO salvo el certificado, y quedó esperando la prueba de Harrison. Estado Under Customer Review, y es correcto, la pelota está en ADUSA.

## Conteo para el D13

46 tickets totales, 36 resueltos, 10 activos. Los mismos 10 del D12, más RCS-28681 que entra resuelto.

## Comentario para pegar en RCS-28123, saludo a Jim

Hi Jim,

Thank you for your patience on this one.

Reassigning a case takes you straight to the workbench and does not show a confirmation popup. That is how the reassignment path works, it is not a defect from the platform move.

Marking a case complete does show a confirmation screen, and that part works as expected.

Printing or viewing the case as a PDF is available from the workbench, which matches what Leigh Ann already found works.

I need nothing from you on this one.

Thank you.

Compromiso que crea este texto: ninguno. Cierra la duda, no abre nada nuevo.

## Comentario para pegar en RCS-28589, saludo a Jim

Hi Jim,

Thank you for confirming the apostrophes are still showing up on the location listing export.

The underlying data does not carry an apostrophe. It is being added through the export path itself.

This is now with engineering to review the export to file function specifically.

I need nothing from you on this one.

Thank you.

Compromiso que crea este texto: avisar cuando ingeniería devuelva algo sobre la exportación. Anótalo para no perderlo.

## Antes del correo de hoy

Falta armar el D13.xlsx. En cuanto me digas cómo seguimos con el tema de bash, te dejo listo también el correo de estado para Jim y la sala, con la misma estructura de los días anteriores. Prefiero no escribirlo todavía porque cambia si al final decides pegar los dos comentarios de arriba hoy o los dejas para mañana, y el correo no puede repetir lo que ya quedó en el ticket.

# RCS-29469: cierre de validación de lectura

Juan aportó definición actual de sso.GetUserSecurityLevel obtenida con SELECT OBJECT_DEFINITION. Copia de evidencia: adjuntos/RCS-29469/2026-10-16-GetUserSecurityLevel-definition.sql. El CREATE de esa copia es evidencia, no una instrucción de despliegue.

Confirmado en la definición: compara UserName, acepta UtcDateFrom/UtcDateTo NULL o vigentes, selecciona TOP 1 SecurityID y ordena Persistent DESC. No exige Persistent=1. No llama a la asignación de membership.Users; devuelve el nivel al consumidor. No se ejecutó el procedimiento en esta sesión.

Combinado con resultados aportados: los cinco tienen Location Manager en sso.teams y nivel 5 en la carga del 15 octubre. Las fechas de vigencia son NULL. El resultado esperado del resolver es 5 para todos. En Christi la fila Persistent=1 tiene prioridad sobre la fila NULL y ambas contienen 5; estas dos filas no muestran conflicto de nivel. No se prueba con esto el código ejecutado en julio ni el loader exacto del día 13.

Lo pendiente no requiere repetir más consultas de estructura. Los cinco últimos logins preceden a la carga del 15. La lectura actual no demuestra que alguno haya recibido un login fallido después de esa carga. La evidencia limpia del alta de Rachel ya sigue en RCS-29451/ENG-10069.

Siguiente validación: coordinar con Colton un único usuario afectado disponible, por ejemplo Christi si puede participar, para un inicio normal por SSO. Capturar antes nivel de cuenta, asignaciones y UTC; no editar el nivel. Registrar hora exacta del login y revisar nivel después. Si pasa a 5, documentar aplicación actual sin declarar resuelto el histórico ni el alta de nuevos usuarios. Si queda NULL, recopilar logs de esa ventana y aportar reproducción actual al ENG existente. Si el login falla antes de completarse, investigar ese fallo sin asumir que probó la asignación posterior.

No pedir a los cinco que entren ni vender el segundo login como arreglo. No crear cuentas, suplantar usuarios ni usar una sesión de Soporte como sustituto de su SSO. Si no se puede coordinar, dejar esta limitación y seguir el caso de Christi histórico con Ingeniería.

El siguiente comentario se redacta cuando haya resultado de esta validación o se necesite solicitar al cliente la prueba. No se publicó ni se preparó mensaje nuevo con esta nota.

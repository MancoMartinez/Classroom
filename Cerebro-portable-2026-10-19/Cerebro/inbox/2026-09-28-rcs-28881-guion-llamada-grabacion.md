# Antes de arrancar

Pide permiso para grabar la llamada y avisa que también vas a necesitar que él comparta pantalla completo, no solo una pestaña, para ver cualquier popup de Chrome. Dile el objetivo en una frase: conseguir video, red y consola juntos para que ingeniería pueda actuar sin pedir otra ronda de pruebas.

# Paso a paso para Carlo, en orden

1. Que comparta pantalla completo.
2. Que abra una ventana de incógnito nueva en Chrome, Ctrl+Shift+N o Cmd+Shift+N en Mac. Así no queda cookie vieja de sesión de por medio.
3. Que inicie sesión en APIS producción desde esa ventana.
4. Antes de tocar el form 576, que abra DevTools, F12 o clic derecho, Inspeccionar.
5. Que vaya a la pestaña Network y marque Preserve log y Disable cache si las ve.
6. Que vaya a la pestaña Console, para que cualquier error en rojo quede visible.
7. En Console, que pegue esto y presione Enter. Puede pedir escribir "allow pasting" primero, es normal:

setInterval(() => { document.querySelectorAll('frameset').forEach(f => { if (f.getAttribute('rows') && f.getAttribute('rows').startsWith('90')) f.setAttribute('rows', '50%,10%,10%,10%,10%,10%'); }); }, 500);

Esto deja las franjas ocultas visibles desde el arranque y evita que se reviertan solas, como pasó la vez pasada al editarlas directo en Elements.

8. Que empiece a grabar pantalla, o confirma que tú lo estás grabando por la llamada.
9. Que navegue a Audit Center, Templates, ANNUAL OPS/SERVICES REVIEW, y haga clic en el form 576.
10. Que no toque nada más. Nada de volver a hacer clic ni refrescar aunque parezca que no pasa nada.
11. Que deje correr hasta que pase una de dos cosas, la página carga o Chrome muestra el aviso de página no responde. Son entre 8 y 10 minutos, avísale que la llamada va a tener ese tramo en silencio.
12. Que no minimice ni cambie de pestaña mientras espera, para no perder la franja de DevTools en la grabación.

# Al terminar

13. Que pare la grabación.
14. En Network, clic derecho sobre cualquier fila, Save all as HAR with content. Ese archivo es la evidencia más fuerte para ingeniería.
15. Que te mande el HAR, el video, y una captura final de la franja inferior de DevTools.

# Si el paso 7 no se sostiene

Si el valor vuelve a 90% apenas lo cambia, pídele que repita el mismo comando desde Console, no que edite el atributo directo en Elements. Por Console se sostuvo la vez pasada, por Elements se revertía solo.

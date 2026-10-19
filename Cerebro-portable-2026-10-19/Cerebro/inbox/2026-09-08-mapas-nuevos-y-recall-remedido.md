# Dos mapas nuevos y el recall remedido

Nota de sistema del Cerebro. No es la ficha de ningun ticket.

## Que se escribio

`investigaciones/sso-cuatro-capas-donde-falla-el-login.md`. El cliente siempre reporta que los
usuarios no pueden entrar, y el fallo puede estar en cuatro capas distintas. El borde, cuando una
regla de firewall rechaza el trafico antes de llegar a la aplicacion. Una dependencia interna
agotada, que tumba el handshake sin que nadie toque configuracion. El handshake y el mapeo de
claims. Y lo que el propio login reescribe al entrar, que borra la asignacion de equipo del usuario
cada dia. El archivo abre con cuatro preguntas que separan las capas.

La memoria que existia cubre bien una sola capa, la tercera, y solo para Incident. Las otras tres
aparecieron entre el 30 de julio y el 4 de septiembre y no estaban recogidas. Dos de ellas ni
siquiera son de Incident.

`flujos/diagnostico-por-codigo-de-error.md`. Tabla de entrada que dice que significa cada codigo y
a que memoria ir. Las tres memorias de lentitud estan bien escritas y si se citan entre si. Lo que
faltaba era saber cual abrir sin leer las tres.

## Correccion a lo que dije antes

Dije que esas tres memorias no se citaban entre si. Es falso, si se enlazan. Lo que faltaba era la
tabla de entrada, no la conexion.

## Recall de la busqueda, remedido

El set de evaluacion paso de 32 a 101 preguntas. FTS5 da 33% de recall@5, no el 48% que estaba
escrito.

La causa de la diferencia es de medicion, no de degradacion. Diez de los 32 casos originales tenian
anclas que apuntaban a mas de treinta fragmentos, y una no apuntaba a ninguno. Un ancla que abarca
cien fragmentos se acierta por azar. Al apretarlas y ampliar el set, el numero honesto queda en 33%.

Quedo escrita la regla de calidad dentro del propio archivo: un ancla debe apuntar a entre 1 y 30
fragmentos. Fuera de ese rango la pregunta no mide nada.

Dos de cada tres preguntas escritas en lenguaje de sintoma no traen el fragmento correcto en los
primeros cinco resultados. Eso es lo establecido.

## Lo que no se pudo correr

La comparacion contra el canal semantico necesita scikit-learn. El Python de Homebrew esta
gestionado externamente y `pip3 install` se niega sin forzar. El evaluador ahora degrada en vez de
morirse: mide FTS5 sin ninguna dependencia, dice que falta el resto, y calcula McNemar exacto solo
cuando los cuatro brazos si corren.

La decision pendiente es entre un entorno virtual usado solo por el evaluador, que deja los comandos
diarios sin dependencias, o forzar la instalacion en el Python del sistema.

## Que sigue

Correr la comparacion cuando este resuelto lo de scikit-learn. Con 101 preguntas la prueba de
McNemar ya tiene con que distinguir, que era la razon de ampliar el set.

# Embeddings: la decision, medida y cerrada

Nota de sistema del Cerebro. No es la ficha de ningun ticket.

## Que pasa

La pregunta llevaba semanas abierta: si el cerebro necesita vectores. La respuesta escrita era que
no se sabia, con 48% contra 58% sobre 31 preguntas y p igual a 0.51. Se llevo el set a 101
preguntas, se corrieron los cinco brazos, y la respuesta es no.

## Causa de que estuviera abierta

El set era chico y ademas estaba flojo. Diez de los 32 casos originales tenian anclas que apuntaban
a mas de treinta fragmentos, y una no apuntaba a ninguno. Un ancla que abarca cien fragmentos se
acierta por azar. Al apretarlas, la cifra honesta de FTS5 baja de 48% a 33%.

Quedo escrita la regla de calidad dentro del propio archivo del set: un ancla debe apuntar a entre
1 y 30 fragmentos.

## Evidencia

Cinco brazos sobre 101 preguntas, recall@5. FTS5 33%, BM25 38%, LSA 38%, RRF 39%, BM25 mas LSA 39%.

McNemar exacto en las cuatro comparaciones: BM25 contra LSA p igual a 1.00, FTS5 contra BM25 p igual
a 0.44, FTS5 contra RRF p igual a 0.26, BM25 contra BM25 mas LSA p igual a 1.00. Ninguna pareja se
separa.

## Lo que decide

El contraste correcto no es FTS5 contra el hibrido. FTS5 rankea peor que BM25, asi que cualquier
cosa que se le sume parece que ayuda y el numero engaña.

El contraste correcto es BM25 contra BM25 mas el canal semantico. Mueve cinco preguntas en total,
dos a favor de uno y tres a favor del otro, con p igual a 1.00. Sobre un ranking lexico bueno, la
semantica no aporta nada medible.

BM25 y LSA empatan en 38% y fallan en preguntas distintas, diez y diez. Encuentran cosas distintas y
ninguno es mejor.

## Conclusion

No instales torch para arreglar el recall. El techo no lo pone el recuperador. Cinco metodos
distintos, dos lexicos, uno semantico y dos fusiones, se estancan en la misma banda de 33 a 39%. Si
el metodo de ranking fuera el cuello de botella, algun brazo se separaria y ninguno lo hace.

## Limitacion que hay que decir

El evaluador busca solo contra los fragmentos de conocimiento. La busqueda que Juan usa mira ademas
las memorias, las fichas de ticket, la mesa de trabajo y el inbox. El 33% es un piso del sistema
real, no lo que Juan experimenta.

## Que sigue

La pregunta util cambio. Ya no es que recuperador rankea mejor. Es por que cinco recuperadores
distintos fallan en las mismas dos terceras partes de las preguntas. Eso apunta aguas arriba del
ranking: al tamaño de los fragmentos, a los titulos con los que se guardan, o a que la respuesta
viva en un canal que el evaluador no mira.

Lo barato de probar primero es medir el evaluador contra los cinco canales que la busqueda real usa,
en vez de contra uno solo. Si el recall sube mucho ahi, el problema nunca fue el ranking.

scikit-learn quedo instalado en el Python del sistema con `--break-system-packages`, decision de
Juan del 8 sep 2026. Los comandos diarios de Cerebro siguen sin ninguna dependencia.

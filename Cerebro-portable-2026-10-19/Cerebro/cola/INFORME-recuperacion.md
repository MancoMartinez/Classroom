# Vectores si o no: lo que dio la medicion

24 ago 2026. Reproducible con `python3 bin/eval_recuperacion.py`.

## El hallazgo que no esperaba y que vale mas que la pregunta original

El indice FTS5 de `chunks_fts` estaba corrupto. De 28 consultas de dos palabras unidas por OR, 25
devolvian `database disk image is malformed`. Cada termino por separado funcionaba. La combinacion
rompia.

Eso significa que `bin/buscar` fallaba en silencio en casi toda consulta de varias palabras que no
tuviera coincidencia exacta con AND, que es el caso normal. La busqueda del cerebro llevaba tiempo
rota y nadie lo vio, porque el script se traga los errores con `2>/dev/null`.

Causa: `chunks_fts` era una tabla de contenido externo y sus triggers borraban del indice usando
`old.body`, mientras el trigger de insercion indexaba `contextualized_body`. Cualquier UPDATE o
DELETE historico en `knowledge_chunks` dejaba entradas huerfanas. `pragma integrity_check` pasaba
igual, porque valida la estructura y no el contenido.

Arreglo aplicado: `chunks_fts` e `items_fts` pasaron a FTS5 autonomo, reindexadas desde cero con
`contextualized_body` cuando existe y `body` cuando no. Los seis triggers se reescribieron para
borrar por rowid. Verificado: 0 de 28 consultas OR fallan, y un ciclo insert, update y delete deja
el indice consistente. La base crecio de 25.4 a 31.9 MB. Copia previa en
`brain/sessions.db.bak-fts-*`.

## La medicion que pediste

Metodo: 32 preguntas escritas como las escribirias tu, sintoma primero, evitando a proposito el
vocabulario del fragmento correcto. Ahi es donde un recuperador semantico deberia ganarle a uno
lexico. Una pregunta se descarto porque su ancla no encontro ningun fragmento. Quedan 31.

Metrica: recall@5. Acierta si el fragmento correcto sale en los primeros cinco.

| Recuperador | recall@5 |
|---|---|
| FTS5, el que ya tienes | 15/31 = 48% |
| BM25 sobre TF-IDF | 14/31 = 45% |
| LSA, semantico denso con SVD | 15/31 = 48% |
| RRF, fusion de FTS5 y LSA | 18/31 = 58% |

## Que se puede concluir y que no

El hibrido saco 10 puntos mas. **Ese numero no aguanta la prueba estadistica.** RRF gana en 6
preguntas donde FTS5 falla, FTS5 gana en 3 donde RRF falla. McNemar exacto da p igual a 0.51. Con 31
casos, una diferencia de 10 puntos es indistinguible del ruido.

Yo te dije que FTS5 iba a alcanzar. La medicion no me da la razon y tampoco me la quita. Lo unico
honesto es que este set es demasiado chico para decidir.

Lo que si es solido y no depende del tamaño de la muestra: **el recall absoluto es bajo.** Entre 48
y 58 por ciento significa que cuatro de cada diez preguntas reales no traen el fragmento correcto en
los primeros cinco. Ese es el problema, no cual recuperador elegir.

Sesgo del experimento, dicho de frente: las preguntas evitan el vocabulario tecnico a proposito.
Cuando escribes "izenda" o "LHUA" la recuperacion es mucho mejor. El 48 por ciento es el piso del
caso dificil, no el rendimiento tipico. El caso dificil es justo cuando necesitas el cerebro.

## Que sigue

1. Llevar el set a 100 preguntas. Con 31 no se decide nada. Con 100, una diferencia de 10 puntos se
   vuelve medible.
2. Correr el brazo que falta. Embeddings reales, no LSA. `sentence-transformers` arrastra torch y no
   entra en el sandbox de Cowork, ni sobrevive entre llamadas. En tu Mac M4 corre sin problema. Ese
   es el unico lugar donde se puede probar el hibrido de verdad.
3. Mientras tanto, el arreglo del indice ya entrego mas mejora que cualquier eleccion de
   recuperador. Ese era el cuello de botella real.

## Reproducir

```bash
python3 bin/eval_recuperacion.py
```

Las preguntas y las anclas viven en `cola/EVAL-recuperacion.json`. Agregar casos es agregar objetos
a ese archivo. El ancla es una expresion regular que identifica el fragmento correcto sin aparecer
en la pregunta.

---

# Anexo, 8 sep 2026. El set a 101 preguntas y el contraste que decide

## Que cambio en la medicion

El set paso de 32 a 101 preguntas. Al revisarlo aparecio un defecto de metodo: diez de los 32 casos
originales tenian anclas que apuntaban a mas de treinta fragmentos, y una no apuntaba a ninguno. Un
ancla amplia se acierta por azar y no mide nada. Un ancla vacia descarta la pregunta en silencio.

Quedo escrita la regla dentro del propio set: **un ancla debe apuntar a entre 1 y 30 fragmentos.**

Con las anclas apretadas y el set ampliado, la cifra honesta de FTS5 baja de 48% a **33%**.

## Los cinco brazos sobre 101 preguntas

| Recuperador | recall@5 |
|---|---|
| FTS5 | 33/101 = 33% |
| BM25 | 38/101 = 38% |
| LSA | 38/101 = 38% |
| RRF, fusion de FTS5 y LSA | 39/101 = 39% |
| BM25 mas LSA | 39/101 = 39% |

## McNemar exacto, todas las parejas

| Comparacion | Solo el primero | Solo el segundo | p | Veredicto |
|---|---|---|---|---|
| BM25 contra LSA | 10 | 10 | 1.000 | no concluyente |
| FTS5 contra BM25 | 11 | 16 | 0.442 | no concluyente |
| FTS5 contra RRF | 7 | 13 | 0.263 | no concluyente |
| BM25 contra BM25+LSA | 2 | 3 | 1.000 | no concluyente |

## Lo que se puede afirmar

**Ninguna pareja se separa, ni con 101 preguntas.** Los cinco brazos caen en la banda de 33% a 39%.
Con el set triplicado, la prueba sigue sin distinguir.

**Añadir el canal semantico a un ranking lexico bueno mueve cinco preguntas en total, dos a favor de
uno y tres a favor del otro, con p igual a 1.00.** Ese es el contraste que responde la pregunta de
si hacen falta vectores, y no la comparacion contra FTS5. FTS5 rankea peor que BM25, asi que
cualquier cosa que se le sume parece que ayuda.

**BM25 y LSA empatan en 38% y se equivocan en preguntas distintas, diez y diez.** Encuentran cosas
distintas y ninguno es mejor. Eso descarta que el problema sea la ausencia de un canal semantico.

**El techo no lo pone el recuperador.** Cinco metodos distintos, dos lexicos, uno semantico y dos
fusiones, se estancan en la misma banda. Si el metodo de ranking fuera el cuello de botella, algun
brazo se separaria. Ninguno lo hace.

## Limitacion del propio experimento, que hay que decir

**Este evaluador mide un solo canal.** Busca contra `knowledge_chunks` y nada mas. `bin/buscar`, que
es lo que Juan usa, busca ademas en memorias, fichas de ticket, mesa de trabajo e inbox. El 33% es
un piso del sistema real, no la experiencia de Juan.

Antes de invertir en embeddings, la pregunta util no es que recuperador rankea mejor. Es por que
cinco recuperadores distintos fallan en las mismas dos terceras partes de las preguntas. Eso apunta
aguas arriba del ranking: al tamaño de los fragmentos, a los titulos, o a que la respuesta no este
en el canal que el evaluador mira.

## Como reproducirlo

```bash
python3 bin/eval_recuperacion.py
```

Sin scikit-learn el script mide FTS5 solo y lo dice, en vez de morirse. scikit-learn se instalo en
esta Mac el 8 sep 2026 con `pip3 install --break-system-packages`, decision de Juan. Los comandos
diarios de Cerebro siguen sin ninguna dependencia.

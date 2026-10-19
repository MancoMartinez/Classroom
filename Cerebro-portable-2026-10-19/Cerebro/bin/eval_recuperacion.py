#!/usr/bin/env python3
"""Mide si el cerebro necesita vectores, en vez de suponerlo.

Compara cuatro recuperadores sobre los mismos fragmentos y las mismas preguntas:

  FTS5     el indice que ya tiene la base, coincidencia lexica con prefijos
  TF-IDF     ranking lexico clasico sobre TF-IDF, la linea base honesta
  LSA      TF-IDF reducido con SVD, un canal semantico denso sin redes neuronales
  RRF      fusion de rangos reciprocos de FTS5 y LSA, el hibrido

La metrica es hit-rate@5 sobre `cola/EVAL-recuperacion.json`. Cada pregunta esta escrita
evitando el vocabulario del fragmento correcto, que es donde un recuperador semantico
deberia ganarle a uno lexico. Este set no permite generalizar a otros modelos o corpus.

Uso:  python3 bin/eval_recuperacion.py
"""
import json, math, os, re, sqlite3, sys, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DB = os.environ.get("CEREBRO_DB", os.path.join(ROOT, "brain", "sessions.db"))
K = 5


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(c) != "Mn")


def cargar():
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    filas = con.execute("SELECT id, title, body FROM knowledge_chunks ORDER BY id").fetchall()
    con.close()
    return [(i, f"{t}\n{b}") for i, t, b in filas]


def gold(docs, patron):
    rx = re.compile(patron, re.I | re.S)
    return {i for i, txt in docs if rx.search(txt)}


def fts5(consulta, k):
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    palabras = [w + "*" for w in re.findall(r"[\wáéíóúñ]{3,}", consulta.lower())]
    for expr in (" ".join(palabras), " OR ".join(palabras)):
        if not expr:
            continue
        try:
            r = [x[0] for x in con.execute(
                "SELECT rowid FROM chunks_fts WHERE chunks_fts MATCH ? ORDER BY rank LIMIT ?",
                (expr, k))]
        except sqlite3.OperationalError:
            r = []
        if r:
            con.close()
            return r
    con.close()
    return []


def main():
    casos = json.load(open(os.path.join(ROOT, "cola", "EVAL-recuperacion.json"),
                           encoding="utf-8"))["casos"]
    docs = cargar()
    ids = [i for i, _ in docs]
    textos = [sin_tildes(t) for _, t in docs]
    print(f"{len(docs)} fragmentos, {len(casos)} preguntas, hit-rate@{K}\n")

    # FTS5 mide siempre, sin una sola dependencia. Los tres brazos semanticos necesitan
    # scikit-learn. Si no esta, el script mide lo que puede y lo dice, en vez de morirse.
    semantico = True
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.decomposition import TruncatedSVD
        from sklearn.preprocessing import normalize
        import numpy as np
    except ImportError:
        semantico = False
        print("scikit-learn no esta instalado. Se mide solo FTS5, que es el recuperador que")
        print("el cerebro usa hoy. Para los brazos TF-IDF, LSA y RRF:  pip3 install scikit-learn")
        print()

    if semantico:
        tfidf = TfidfVectorizer(sublinear_tf=True, min_df=1, ngram_range=(1, 2),
                                max_features=200000)
        X = tfidf.fit_transform(textos)
        svd = TruncatedSVD(n_components=256, random_state=0)
        Z = normalize(svd.fit_transform(X))

    aciertos = {"FTS5": 0, "TF-IDF": 0, "LSA": 0, "RRF": 0, "TF-IDF+LSA": 0}
    vacios = 0
    fallos_fts = []
    pares = []      # (acerto FTS5, acerto RRF) por pregunta, para McNemar
    pares_bl = []   # (acerto TF-IDF, acerto TF-IDF+LSA), el contraste que decide

    for c in casos:
        g = gold(docs, c["ancla"])
        if not g:
            vacios += 1
            continue
        q = c["q"]
        r_fts = fts5(q, K)
        r_bm = r_lsa = r_rrf = []

        if semantico:
            qv = tfidf.transform([sin_tildes(q)])
            sim_bm = (X @ qv.T).toarray().ravel()
            r_bm = [ids[j] for j in np.argsort(-sim_bm)[:K]]

            qz = normalize(svd.transform(qv))
            sim_lsa = (Z @ qz.T).ravel()
            orden_lsa = [ids[j] for j in np.argsort(-sim_lsa)[:50]]
            r_lsa = orden_lsa[:K]

            # Reciprocal rank fusion de FTS5 y LSA.
            puntos = {}
            for rank, d in enumerate(fts5(q, 50)):
                puntos[d] = puntos.get(d, 0) + 1 / (60 + rank)
            for rank, d in enumerate(orden_lsa):
                puntos[d] = puntos.get(d, 0) + 1 / (60 + rank)
            r_rrf = [d for d, _ in sorted(puntos.items(), key=lambda x: -x[1])[:K]]

            # Compara TF-IDF contra TF-IDF más LSA; no evalúa embeddings neuronales.
            orden_bm = [ids[j] for j in np.argsort(-sim_bm)[:50]]
            p2 = {}
            for rank, d in enumerate(orden_bm):
                p2[d] = p2.get(d, 0) + 1 / (60 + rank)
            for rank, d in enumerate(orden_lsa):
                p2[d] = p2.get(d, 0) + 1 / (60 + rank)
            r_bl = [d for d, _ in sorted(p2.items(), key=lambda x: -x[1])[:K]]
            aciertos["TF-IDF+LSA"] = aciertos.get("TF-IDF+LSA", 0) + (1 if g & set(r_bl) else 0)
            pares_bl.append((bool(g & set(r_bm)), bool(g & set(r_bl))))

        for nombre, r in (("FTS5", r_fts), ("TF-IDF", r_bm), ("LSA", r_lsa), ("RRF", r_rrf)):
            if r and g & set(r):
                aciertos[nombre] += 1
        pares.append((bool(g & set(r_fts)), bool(r_rrf and g & set(r_rrf))))
        if not (g & set(r_fts)):
            fallos_fts.append((q, c["ancla"], len(g), bool(r_rrf and g & set(r_rrf))))

    n = len(casos) - vacios
    if vacios:
        print(f"{vacios} preguntas descartadas: el ancla no encontro ningun fragmento\n")
    print(f"{'recuperador':10} {'hit-rate@5':>9}")
    brazos = ("FTS5", "TF-IDF", "LSA", "RRF", "TF-IDF+LSA") if semantico else ("FTS5",)
    for nombre in brazos:
        print(f"{nombre:10} {aciertos[nombre]}/{n} = {aciertos[nombre]/n:>6.0%}")

    if semantico:
        # McNemar exacto, FTS5 contra el hibrido. Solo cuentan las preguntas donde
        # difieren. Sin esto, una diferencia de recall se lee como si fuera real.
        b = sum(1 for f, r in pares if f and not r)
        c_ = sum(1 for f, r in pares if r and not f)
        n_dis = b + c_
        if n_dis == 0:
            print("\nMcNemar: los dos recuperadores aciertan y fallan en las mismas preguntas.")
        else:
            cola_ = sum(math.comb(n_dis, k) for k in range(min(b, c_) + 1)) / (2 ** n_dis)
            pval = min(1.0, 2 * cola_)
            print(f"\nMcNemar exacto, FTS5 contra RRF: solo FTS5 acierta en {b}, "
                  f"solo RRF acierta en {c_}, p = {pval:.2f}")
            if pval > 0.05:
                print("La diferencia no es concluyente. No afirmes que los vectores sobran "
                      "ni que hacen falta.")
            else:
                print("La diferencia es significativa al 5%.")
        b2 = sum(1 for x, y in pares_bl if x and not y)
        c2 = sum(1 for x, y in pares_bl if y and not x)
        d2 = b2 + c2
        if d2:
            cola2 = sum(math.comb(d2, k) for k in range(min(b2, c2) + 1)) / (2 ** d2)
            p2v = min(1.0, 2 * cola2)
            print(f"McNemar exacto, TF-IDF contra TF-IDF+LSA: solo TF-IDF acierta en {b2}, "
                  f"solo el hibrido en {c2}, p = {p2v:.2f}")
            print("Este contraste mide LSA añadido a TF-IDF en este set, no embeddings neuronales.")
        if n < 100:
            print(f"\nEl set tiene {n} preguntas utiles. Con menos de 100 la prueba casi nunca "
                  "alcanza a distinguir.")

    if fallos_fts:
        print(f"\nDonde FTS5 falla ({len(fallos_fts)}):")
        for q, a, ng, rescatado in fallos_fts:
            marca = "RRF lo rescata" if rescatado else "el hibrido tampoco"
            print(f"  · {q[:66]:68} {marca}")

    print("\nLimitacion honesta: LSA es un canal semantico sin redes neuronales. "
          "Un modelo de embeddings real puede rendir mejor. Ese brazo del experimento "
          "no corre en el sandbox de Cowork, hay que correrlo en el Mac.")


if __name__ == "__main__":
    main()

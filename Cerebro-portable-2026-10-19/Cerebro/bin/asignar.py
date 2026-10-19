#!/usr/bin/env python3
"""
Prepara el reparto diario de la cola unassigned de RCS.

Uso:
    python3 bin/asignar.py asignaciones/unassigned.json asignaciones/carga.json

Escribe asignaciones/estado-reparto.json con:
  - antes:    foto del backlog unassigned, conteos y edades
  - equipo:   carga cruda y carga activa por persona, cupo disponible
  - tickets:  cada unassigned con edad, bucket tecnico, nivel de dificultad y flag ADUSA

No decide el reparto. Clasifica y mide. La decision la toma Claude leyendo este JSON.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "asignaciones" / "estado-reparto.json"

# Roster Colombia. Fuente: brain/memoria/project_appriss_support_team.md
# accountId verificado contra Jira el 25 ago 2026.
# El roster NO se deduce de quien aparece como asignatario en Jira.
EQUIPO = {
    "Luis Hernandez": {
        "accountId": "712020:7cb67354-171b-4f4b-b5f6-46a5c57cbd4d",
        "nivel": "normal",
        "puesto": "Senior Full Stack Engineer",
        "perfil": "React y .NET. Senior Full Stack, ya nivelado con el resto del equipo desde el 28 sep 2026.",
        "techo_abiertos": 16,
        "incremento_diario": 3,
    },
    "Sebastian Garces": {
        "accountId": "712020:239d8bd1-42fb-47ac-8e49-8698e657fbba",
        "nivel": "normal",
        "puesto": "Support Engineer",
        "perfil": "Ya nivelado con el resto del equipo desde el 28 sep 2026, sin restriccion de nuevo.",
        "techo_abiertos": 16,
        "incremento_diario": 3,
    },
    "Diego Buelvas": {
        "accountId": "712020:20065f69-a041-443a-8b58-b79b1649d0b4",
        "nivel": "normal",
        "puesto": "Full Stack Engineer",
        "perfil": "Attachments y print docs. Exports e Izenda. Rendering y UI. Lleva Delhaize.",
        "techo_abiertos": 16,
        "incremento_diario": 3,
    },
    "Edwin Garzon": {
        "accountId": "712020:9e64bce4-462c-48d2-887a-2d2e3dee5936",
        "nivel": "normal",
        "puesto": "Data Engineer",
        "perfil": "Location hierarchy. Cargas de datos y feeds. Campos faltantes en transacciones.",
        "techo_abiertos": 16,
        "incremento_diario": 3,
    },
    "Sebastian Rueda": {
        "accountId": "712020:ae769ae6-4093-403d-847f-a3a13075b642",
        "nivel": "normal",
        "puesto": "Senior Data Engineer",
        "perfil": "Data integrity. Duplicacion de filas. Mapeo de campos. Feeds y loads.",
        "techo_abiertos": 16,
        "incremento_diario": 3,
    },
}

# David Vargas trabaja hasta el 25 ago 2026. Sus tickets nunca aparecen en la cola sin
# asignar, hay que sacarlos a mano. Ver brain/memoria/project_reparto_cola_2026_08_11.md.
SALIENTES = {
    "David Vargas": "712020:be5d8a1b-57c3-4b11-b8e7-567c0e58538a",
}

# Marcas ADUSA, Ahold Delhaize USA. Cliente critical.
ADUSA = [
    "adusa", "ahold", "delhaize", "food lion", "giant food", "the giant company",
    "giant company", "hannaford", "stop & shop", "stop and shop", "peapod",
]

# Buckets tecnicos. Fuente: brain/memoria/project_reparto_cola_2026_08_11.md
BUCKETS = {
    "acceso": ["login", "sso", "saml", "password", "blocked", "permission", "access level",
               "new user", "user profile", "cannot view", "unable to access", "waf", "403"],
    "attachments": ["attachment", "upload", "print", "document", "pdf", "receipt image"],
    "reportes": ["izenda", "report", "export", "excel", "dashboard", "workview", "metrics",
                 "fiscal calendar"],
    "alertas": ["alert", "notification", "smart alert", "email distribution", "user task"],
    "datos": ["data load", "not loaded", "missing data", "missing item", "missing information",
              "feed", "duplicat", "sync", "mapping", "data gap", "migration", "velocity",
              "not calculating", "missing transaction", "missing employee"],
    "jerarquia": ["hierarchy", "location", "store", "district", "region"],
    "latencia": ["timeout", "time out", "slow", "latency", "performance", "502", "524"],
    "ui": ["render", "not visible", "not showing", "display", "screen", "page not",
           "unable to close", "case class"],
}

# Un ticket basico cabe en la cola de un nuevo. Senales de que NO es basico.
NO_BASICO = [
    "systemic", "multiple stores", "rca", "root cause", "migration", "data gap",
    "not loaded", "duplicat", "sow estimation", "outage", "security issue",
    "api key", "fiscal calendar", "velocity",
]
# Senales de que SI es basico: un usuario, una config, una pregunta.
SI_BASICO = [
    "new user", "user blocked", "login issue", "how do i", "access level",
    "user profile", "permission", "password", "email distribution", "question",
    "not able to forward", "time out too short",
]


def dias(iso):
    """Jira devuelve el offset sin dos puntos, -0400. fromisoformat lo rechaza antes de 3.11."""
    if not iso:
        return None
    s = iso.replace("Z", "+00:00")
    s = re.sub(r"([+-]\d{2})(\d{2})$", r"\1:\2", s)
    t = datetime.fromisoformat(s)
    return round((datetime.now(timezone.utc) - t).total_seconds() / 86400, 1)


def nodos(ruta):
    d = json.loads(Path(ruta).read_text(encoding="utf-8"))
    return d.get("issues", {}).get("nodes", [])


def clasificar(texto):
    t = texto.lower()
    encontrados = [b for b, claves in BUCKETS.items() if any(k in t for k in claves)]
    return encontrados or ["sin clasificar"]


def dificultad(nodo, texto):
    t = texto.lower()
    prio = (nodo["fields"].get("priority") or {}).get("name", "")
    if prio in ("Critical", "High"):
        return "normal", f"prioridad {prio}"
    for k in NO_BASICO:
        if k in t:
            return "normal", f"senal de alcance amplio: {k}"
    for k in SI_BASICO:
        if k in t:
            return "basico", f"un usuario o una config: {k}"
    return "normal", "sin senal clara de ticket basico"


def es_adusa(nodo, texto):
    t = texto.lower()
    correo = ((nodo["fields"].get("reporter") or {}).get("emailAddress") or "").lower()
    for m in ADUSA:
        if m in t:
            return True, m
    if "adusa.com" in correo or "delhaize" in correo or "aholddelhaize" in correo:
        return True, correo
    return False, None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    sin_asignar = nodos(sys.argv[1])
    carga = nodos(sys.argv[2])

    # Carga por persona. Cruda y activa. Esperar no es trabajar.
    porid = {v["accountId"]: k for k, v in EQUIPO.items()}
    equipo = {}
    for nombre, meta in EQUIPO.items():
        equipo[nombre] = {**{k: v for k, v in meta.items()}, "cruda": 0, "activa": 0,
                          "espera": 0, "abiertos": []}
    for n in carga:
        a = (n["fields"].get("assignee") or {}).get("accountId")
        nombre = porid.get(a)
        if not nombre:
            continue
        est = (n["fields"].get("status") or {}).get("name", "")
        prio = (n["fields"].get("priority") or {}).get("name", "")
        equipo[nombre]["cruda"] += 1
        if re.search(r"customer review", est, re.I):
            equipo[nombre]["espera"] += 1
        else:
            equipo[nombre]["activa"] += 1
        equipo[nombre]["abiertos"].append(
            {"key": n["key"], "estado": est, "prioridad": prio,
             "summary": n["fields"].get("summary", "")}
        )
    for nombre, d in equipo.items():
        # Dos frenos. El techo de abiertos por persona, y el incremento del dia.
        # Juan fijo 15 a 17 abiertos para los tres con experiencia, 5 para los nuevos.
        # El incremento existe porque el techo no se llena de golpe: hoy una parte,
        # manana otra.
        d["margen_techo"] = max(0, d["techo_abiertos"] - d["cruda"])
        d["cupo"] = min(d["incremento_diario"], d["margen_techo"])

    # Foto del backlog unassigned.
    tickets = []
    for n in sin_asignar:
        f = n["fields"]
        texto = f.get("summary", "")
        adusa, motivo_adusa = es_adusa(n, texto)
        nivel, motivo = dificultad(n, texto)
        tickets.append({
            "key": n["key"],
            "summary": texto,
            "prioridad": (f.get("priority") or {}).get("name"),
            "tipo": (f.get("issuetype") or {}).get("name"),
            "estado": (f.get("status") or {}).get("name"),
            "reporter": (f.get("reporter") or {}).get("emailAddress"),
            "edad_dias": dias(f.get("created")),
            "callado_dias": dias(f.get("updated")),
            "buckets": clasificar(texto),
            "dificultad": nivel,
            "motivo_dificultad": motivo,
            "adusa": adusa,
            "motivo_adusa": motivo_adusa,
            "url": n.get("webUrl"),
        })

    # ADUSA arriba, despues el mas viejo.
    tickets.sort(key=lambda x: (not x["adusa"], -(x["edad_dias"] or 0)))

    edades = [t["edad_dias"] for t in tickets if t["edad_dias"] is not None]
    antes = {
        "total": len(tickets),
        "adusa": sum(1 for t in tickets if t["adusa"]),
        "basicos": sum(1 for t in tickets if t["dificultad"] == "basico"),
        "por_prioridad": {},
        "edad_media_dias": round(sum(edades) / len(edades), 1) if edades else 0,
        "edad_max_dias": max(edades) if edades else 0,
        "mas_de_7_dias": sum(1 for e in edades if e > 7),
    }
    for t in tickets:
        p = t["prioridad"] or "sin prioridad"
        antes["por_prioridad"][p] = antes["por_prioridad"].get(p, 0) + 1

    estado = {
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "antes": antes,
        "cupo_total": sum(d["cupo"] for d in equipo.values()),
        "equipo": equipo,
        "tickets": tickets,
    }
    SALIDA.parent.mkdir(exist_ok=True)
    SALIDA.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"ANTES  unassigned {antes['total']}  ADUSA {antes['adusa']}  "
          f"basicos {antes['basicos']}  edad media {antes['edad_media_dias']}d  "
          f"mas de 7d {antes['mas_de_7_dias']}")
    print(f"CUPO   total {estado['cupo_total']}")
    for nombre, d in sorted(equipo.items(), key=lambda x: x[1]["cruda"]):
        print(f"  {nombre:20s} cruda {d['cruda']:2d}/{d['techo_abiertos']:2d}  "
              f"activa {d['activa']:2d}  espera {d['espera']:2d}  "
              f"margen {d['margen_techo']:2d}  cupo hoy {d['cupo']}  [{d['nivel']}]")
    print(f"\nEscrito {SALIDA}")


if __name__ == "__main__":
    main()

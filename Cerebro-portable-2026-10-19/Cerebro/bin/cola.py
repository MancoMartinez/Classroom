#!/usr/bin/env python3
"""Ordena la cola de tickets de Juan de mas urgente a menos.

El modelo es lexicografico, no un puntaje opaco. Cuatro niveles, y dentro de cada nivel
se ordena por dias de silencio de cara al cliente. Cada ticket sale con el motivo escrito
para que se pueda auditar y discutir.

  Nivel 1  TE TOCA RESPONDER      el ultimo humano que hablo fue el cliente
  Nivel 2  PROMESA SIN CUMPLIR    tu ultimo comentario prometio un update que no llego
  Nivel 3  ESPERANDO AL CLIENTE   preguntaste y no contestan, toca perseguir
  Nivel 4  EN MOVIMIENTO INTERNO  ingenieria trabajando, nada pendiente de cara al cliente

Reglas que respeta, tomadas de brain/memoria:
  · `updated` de Jira no es señal de actividad. El reloj cuenta desde el ultimo comentario real.
  · Los comentarios de Automation for Jira y las notas internas no responden al cliente.
  · Jira es la fuente de verdad. Este script solo lee un volcado, nunca escribe en Jira.

Uso:
    python3 bin/cola.py cola/jira-dump.json
    python3 bin/cola.py cola/jira-dump.json --json     # solo el estado, sin markdown
"""
import json, sys, os, re, datetime, html

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
JUAN = "712020:688bd119-6d13-450b-95ac-b1ef3fbb547b"
JIRA = "https://trebuco.atlassian.net/browse/"

# Identificacion del cliente. Tres vias, en orden.
#   1. Cuenta de Jira Service Management, el caso normal.
#   2. Dominio del correo en el nombre visible. Medido el 8 sep 2026 sobre los 46 autores del
#      volcado: de los 33 sin `qm:`, uno solo era cliente, damir.demirovic@nike.com con cuenta
#      712020:. Los otros 32 eran Appriss e ingenieria.
#   3. Lista manual, para el cliente que no muestra correo ni tiene cuenta qm:.
DOMINIOS_INTERNOS = ("apprissretail.com", "appriss.com", "nuaav.com", "sysrepublic.com",
                     "trebuco.com", "apprissinsights.com")
CLIENTES_MANUALES = ("712020:9c60cf80-4b59-4d63-8e7f-e75980d4a367",)   # accountIds. Agrega aqui al cliente que las dos vias de arriba no atrapen.
RE_CORREO = re.compile(r"[\w.+-]+@([\w-]+\.[\w.-]+)")


def es_cliente(aid, nombre=""):
    if aid.startswith("qm:") or aid in CLIENTES_MANUALES:
        return True
    m = RE_CORREO.search(nombre or "")
    return bool(m) and m.group(1).lower().rstrip(".") not in DOMINIOS_INTERNOS


# Compatibilidad con quien llame sin el nombre. Sin nombre solo puede ver la cuenta.
ES_CLIENTE = lambda aid: es_cliente(aid, "")
# Bots y automatizaciones. No hablan por Appriss ni por el cliente.
BOTS = ("557058:",)
MARCAS_INTERNAS = ("internal note", "a comment has been made on the internal",
                   "the following linked issue was commented")

# Compromisos de cara al cliente. Alta precision, en ingles, tal como se escriben en RCS.
PROMESA = [
    r"i will provide an update", r"will provide an update",
    r"i will get back", r"we will get back", r"get back to you",
    r"we will come back", r"will come back with",
    r"we are checking", r"we are reviewing", r"we are looking",
    r"i am looking into", r"looking into (it|this)", r"have begun reviewing",
    r"will follow up", r"i'?ll follow up", r"we will follow up",
    r"we'?ll confirm", r"will confirm once", r"once that is done",
    r"we will pass", r"we will update", r"will let you know", r"keep you posted",
    r"as soon as i have something", r"as soon as possible",
    r"we will take it from there", r"we are working on",
    r"i'?ll update you", r"i will update you", r"once i have more",
    r"actively investigating", r"we will investigate", r"i will investigate",
    r"will continue to (look|investigate|work|dig)", r"will see what we can do",
    r"i'?ll (look|check|review|dig)", r"we'?ll (look|check|review)",
    r"more findings", r"will provide", r"we will let",
    # 9 sep 2026: RCS-28342 quedaba en nivel 4 con "I'll keep you updated" de hace 4 dias.
    r"will update (this|the) ticket", r"will confirm here once", r"i'?ll send over the calendar invite",
    r"keep you (updated|informed|in the loop)", r"keep u updated",
    r"i'?ll be working on", r"i will be working on", r"i'?m working on", r"i am working on",
]
# Pedidos al cliente. Cuando el ultimo movimiento es esto, la pelota es del cliente.
PREGUNTA = [
    r"could you", r"can you", r"would you", r"are you able",
    r"please confirm", r"please provide", r"please let us know", r"please try",
    r"please have", r"please share", r"please send", r"please ask",
    r"please check", r"please verify", r"please review", r"please attempt",
    r"do you (have|know|already)", r"we (still )?need (the|a|you)",
    r"waiting on", r"we are still waiting",
    r"i'?ll wait for", r"i will wait", r"we'?ll wait", r"we will wait",
    r"i'?ll be waiting", r"i will be waiting", r"we'?ll be waiting",
    r"we will be waiting", r"still waiting (to hear|for|on)",
    r"awaiting (your|the|a)", r"pending your",
    # 9 sep 2026: peticiones al cliente que el lexico no veia. Dos tickets, RCS-27941 y
    # RCS-28294, quedaron en nivel 4 con una peticion viva encima.
    r"if you (could|can)",
    # 9 sep 2026: peticiones en imperativo, sin formula de cortesia. Juan las escribe asi.
    r"i need (you|your)", r"we need (you|your)", r"i want you to", r"i need to know",
    r"it'?s important that you", r"send me", r"send us", r"ask \w+ to",
    r"can \w+ (run|check|try|send|confirm|attempt|verify)",
    r"verify if", r"confirm (which|whether|if)",
    r"you can (ask|try|clear|close|check|log|have)",
    r"try (clearing|again|once more|logging)", r"retry",
]

# El cliente se compromete a volver el. Cuando su mensaje cierra asi, la pelota es suya y el
# ticket no te toca a ti. Medido en RCS-28289: "Once I hear back from IT, I will let you know".
CLIENTE_DEVUELVE = [
    r"i'?ll let you know", r"i will let you know", r"we'?ll let you know", r"we will let you know",
    r"i'?ll get back", r"i will get back", r"we'?ll get back", r"we will get back",
    r"get back to you", r"come back to you",
    r"i'?ll work on", r"i will work on", r"i am working on", r"i'?m working on",
    r"we are (still )?working on", r"we'?re (still )?working on", r"still working on",
    r"i'?ll (check|review|confirm|follow up|update|send|reach out)",
    r"i will (check|review|confirm|follow up|update|send|reach out)",
    r"we'?ll (check|review|confirm|follow up|update|send)",
    r"we will (check|review|confirm|follow up|update|send)",
    r"once i hear back", r"once we hear back", r"as soon as i (hear|know|have)",
    r"waiting (on|for) (my|our|it|the) ", r"i'?ll be in touch", r"will keep you posted",
    # 15 oct 2026 (RCS-28240): "I'm still trying to get help internally on this matter".
    r"still trying to", r"(help|answer|feedback|input|approval) internally",
    r"checking internally", r"(i'?m|i am|we'?re|we are) (still )?(checking|looking into|reviewing) (this|it|that|with)",
]
# Pedido o reclamo del cliente. Esto si te toca a ti, aunque venga con las gracias delante.
# 9 sep 2026: promesa condicionada. "I will follow up once I hear back from your team" no es
# una promesa pendiente de Appriss, es la pelota en el campo del cliente. Sin esta lista,
# RCS-28240 y RCS-28351 subian a nivel 2 con el cliente debiendo datos.
CONDICIONADA = [
    r"once (i|we) hear back", r"once (that|this|it) is confirmed", r"once confirmed",
    r"once you", r"when you", r"after you", r"as soon as you",
    r"if you (are|do|still|see|continue)", r"upon (your|receipt)",
    r"pending (your|the customer|the client)",
]

# 15 sep 2026, pedido de Juan: distinguir "tome el ticket" de "avance real en la solucion".
# Si nunca aparece nada de esta lista en un comentario tuyo, no hay diagnostico escrito,
# solo acuse de recibo. SLA_DIAS es un techo de trabajo, no un SLA contractual de Appriss,
# Juan lo ajusta si no calza.
SUSTANCIA = [
    r"root cause", r"the cause (is|was)", r"caused by", r"confirmed", r"we found",
    r"i found", r"identified", r"reproduced", r"here is what", r"the issue is",
    r"fix(ed)?", r"deploy(ed)?", r"patch", r"eng-\d+", r"verified", r"tested",
    r"attached (a |the )?(screenshot|log|trace)", r"query", r"the data shows",
]
SLA_DIAS = {"critical": 1, "highest": 1, "high": 3, "medium": 7, "low": 14}

# 15 oct 2026, regla de Juan. El estado del ticket manda antes que el reloj.
#   Estados de espera del cliente (Under Customer Review y similares) pausan el SLA en Jira.
#   Ahi no hay SLA en riesgo. Si el cliente calla de 5 a 7 dias habiles toca seguimiento, nada mas.
#   Estados activos (Under Support Review, Work in progress y los de ingenieria) corren el reloj.
#   El riesgo es tiempo sin comentario publico de Appriss: Critical 30 min, High 24 h,
#   Medium 4 a 5 dias habiles. Low no tiene regla escrita de Juan, se usa 7 a 10 dias habiles.
#   Una fecha comprometida en el ultimo comentario de Appriss reemplaza ese techo.
#   Los campos SLA de Jira Service Management mandan cuando traen un ciclo en curso.
ESTADOS_PAUSA = re.compile(r"(under|waiting for|waiting on|pending|awaiting) customer|customer review|"
                           r"pending closure|resolved", re.I)
# Horas habiles, sin sabados ni domingos. (aviso, vencido)
CADENCIA_HORAS = {"critical": (20 / 60, 0.5), "highest": (20 / 60, 0.5), "blocker": (20 / 60, 0.5),
                  "high": (18, 24), "medium": (4 * 24, 5 * 24), "low": (7 * 24, 10 * 24),
                  "lowest": (7 * 24, 10 * 24)}
SEGUIMIENTO_DIAS = 5
TZ_BOG = datetime.timezone(datetime.timedelta(hours=-5))
MESES = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
DIAS_SEMANA = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def horas_habiles(desde, hasta):
    """Horas entre dos instantes sin contar sabados ni domingos, en hora de Bogota."""
    if not desde or not hasta or hasta <= desde:
        return 0.0
    a, b = desde.astimezone(TZ_BOG), hasta.astimezone(TZ_BOG)
    total, cur = 0.0, a
    while cur < b:
        fin_dia = (cur + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        tramo = min(fin_dia, b)
        if cur.weekday() < 5:
            total += (tramo - cur).total_seconds() / 3600
        cur = tramo
    return total


def fmt_horas(h):
    if h < 1:
        return f"{int(round(h * 60))} min"
    if h < 48:
        return f"{h:.0f} h habiles"
    return f"{h / 24:.1f} dias habiles"


def fecha_comprometida(texto, base):
    """La fecha mas lejana, de hoy en adelante y dentro de 30 dias, que el comentario nombra.
    "October 13th", "Oct 13", "tomorrow", "end of day", "on Tuesday". Una fecha pasada en el
    texto es historia ("the file load on October 13"), no compromiso, y se ignora."""
    t = sin_citas(texto).lower()
    b = base.astimezone(TZ_BOG).date()
    fechas = []
    for m in re.finditer(r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{1,2})(st|nd|rd|th)?\b", t):
        try:
            fechas.append(datetime.date(b.year, MESES[m.group(1)], int(m.group(2))))
        except ValueError:
            pass
    if re.search(r"\btomorrow\b", t):
        fechas.append(b + datetime.timedelta(days=1))
    if re.search(r"\b(end of (the )?day|eod|later today|by today)\b", t):
        fechas.append(b)
    for m in re.finditer(r"\b(on|by|this|next|until)\s+(monday|tuesday|wednesday|thursday|friday)\b", t):
        delta = (DIAS_SEMANA.index(m.group(2)) - b.weekday()) % 7 or 7
        fechas.append(b + datetime.timedelta(days=delta))
    validas = [f for f in fechas if b <= f <= b + datetime.timedelta(days=30)]
    return max(validas) if validas else None


def slas_jira(fields):
    """Ciclos SLA en curso de Jira Service Management. Se detectan por forma, no por id, asi
    entran Target First Response, Assigned Team First Response, Time to resolution, Target
    Assignment Time y las variantes TJX sin listar customfields."""
    out = []
    for k, v in fields.items():
        if not k.startswith("customfield_") or not isinstance(v, dict):
            continue
        oc = v.get("ongoingCycle")
        if not oc or "name" not in v:
            continue
        meta = (oc.get("goalDuration") or {}).get("millis")
        rest = (oc.get("remainingTime") or {}).get("millis")
        out.append({"nombre": v["name"], "pausado": bool(oc.get("paused")),
                    "vencido": bool(oc.get("breached")), "restante_ms": rest, "meta_ms": meta,
                    "restante": (oc.get("remainingTime") or {}).get("friendly", ""),
                    "resolucion": "resolution" in v["name"].lower()})
    return out


def sla_umbral(prioridad):
    return SLA_DIAS.get((prioridad or "").lower(), SLA_DIAS["medium"])

CLIENTE_PIDE = [
    r"\?", r"could you", r"can you", r"would you", r"please ",
    r"we need", r"i need", r"any update", r"do you have", r"do you know",
    r"when will", r"what is the status", r"still (not|seeing|having|getting)",
    r"is there (any|a)", r"let me know",
]
# Acuse de recibo puro. Solo cuenta si el mensaje no dice nada mas.
CLIENTE_ACUSA = [
    r"^(hi|hello|hey|good (morning|afternoon))?\s*[\w .,@-]{0,24}?\b"
    r"(thanks|thank you|ok|okay|got it|received|noted|perfect|great|understood)\b",
    r"appreciate (it|the|your)",
]

# Bloques que Appriss pega dentro de su comentario y que no son palabras de Appriss: correos
# reenviados del cliente, cabeceras de Outlook, firmas y pies de portal. El lexico se aplica
# solo a lo que Appriss escribio de su puño. Medido en RCS-27765, donde "Do you have a request
# or problem", el pie del portal de IT del cliente, se leia como un pedido de Appriss.
CORTES_CITA = [
    r"email from (the )?customer", r"correo del cliente",
    r"\s-{3,}\s", r"-{2,}\s*original message",
    r"\bfrom:\s*[\w.+-]+@", r"\bon .{0,70}\bwrote:",
    r"do you have a request or problem", r"log a ticket",
    r"planned pto\s*:", r"confidentiality notice",
    r"this (e-?mail|message)[^.]{0,60}(is intended|is confidential|and any attachments)",
    r"sent from my (iphone|ipad|android|mobile)",
]


def sin_citas(texto):
    """Recorta el comentario en el primer bloque citado o firma. Devuelve lo que Appriss
    escribio de su puño. Si el comentario empieza con la cita, devuelve cadena vacia y el
    ticket cae solo a nivel 4, que es lo correcto: Appriss no dijo nada propio."""
    bajo = texto.lower()
    corte = len(texto)
    for pat in CORTES_CITA:
        m = re.search(pat, bajo)
        if m:
            corte = min(corte, m.start())
    return texto[:corte].strip()


def cliente_devuelve_pelota(texto, autor=None):
    """Devuelve (cede, tipo). cede es True cuando el ultimo mensaje del cliente deja la
    pelota de su lado: se compromete el a volver ("compromiso"), o solo acusa recibo sin
    dejar nada pendiente ("acuse"). Un pedido o una pregunta manda siempre a nivel 1, cede
    False, tipo None. autor es el nombre de quien firma, si se conoce, para cortar su firma."""
    t = sin_citas(texto)
    bajo = t.lower()
    # 17 sep 2026 (RCS-27791): "Suspicion of theft? Contact the LP Hotline at..." es texto
    # fijo de firma corporativa, no una pregunta al equipo. Trae su propio "?" y disparaba
    # CLIENTE_PIDE antes de llegar a mirar si el mensaje real era un cierre puro. La firma
    # se corta ANTES de cualquier chequeo, no solo antes de medir sustancia.
    sin_firma = re.sub(
        r"^(hi|hello|hey|dear)\s+[a-z][a-z'\-]*(\s+[a-z][a-z'\-]*){0,2}[,!.]?\s*",
        " ", bajo)
    sin_firma = re.sub(
        r"(regards|best regards|kind regards|sincerely|best|thanks|thank you)[,.]?\s*"
        r"[a-z][a-z'\-]*(\s+[a-z][a-z'\-]*){0,2}\s*$",
        " ", sin_firma)
    if autor:
        partes = [p for p in re.sub(r"[^a-z ]", "", autor.lower()).split() if len(p) > 2]
        if partes:
            patron = r"\b" + r"\s+".join(re.escape(p) for p in partes) + r"\b"
            m = re.search(patron, sin_firma)
            if m:
                sin_firma = sin_firma[:m.start()]
    m = re.search(r"\b(office|phone|tel|mobile|cell|fax)\s*:|mailto:|\bhotline\b", sin_firma)
    if m:
        sin_firma = sin_firma[:m.start()]
    if any(re.search(p, sin_firma) for p in CLIENTE_PIDE):
        return False, None
    if any(re.search(p, sin_firma) for p in CLIENTE_DEVUELVE):
        return True, "compromiso"
    # Acuse puro. Solo si el mensaje no trae contenido propio mas alla del saludo, la
    # firma y la cortesia de cierre.
    # 15 sep 2026 (RCS-28294): "Hello Juan, Thank you for your assistance and updates.
    # Regards, Tatiana Barcenas" media 53 caracteres de sustancia porque el nombre del
    # destinatario del saludo y la firma del cliente no se quitaban antes de contar.
    sustancia = re.sub(r"\b(hi|hello|hey|dear|thanks|thank you|regards|best regards|"
                       r"kind regards|best|sincerely|good morning|good afternoon|ok|"
                       r"okay|got it|noted|perfect|great|yes|yeah|yep)\b", " ", sin_firma)
    sustancia = re.sub(r"\bfor your (assistance|help|support|patience|time|"
                       r"understanding|updates?|cooperation|prompt response)\b", " ", sustancia)
    sustancia = re.sub(r"[^a-z]+", " ", sustancia).strip()
    # 17 sep 2026 (RCS-27791): un acuse puro ("yes, thank you") no es una promesa de volver,
    # es un cierre. Antes ambos caian en nivel 3 con el mismo motivo "se comprometio a
    # volver", que es falso para un acuse. tipo distingue los dos en clasificar().
    puro = any(re.search(p, bajo) for p in CLIENTE_ACUSA) and len(sustancia) < 25
    return puro, "acuse"


def parse_fecha(s):
    s = re.sub(r"([+-]\d{2})(\d{2})$", r"\1:\2", s)
    return datetime.datetime.fromisoformat(s)


def limpiar(texto):
    """Quita mentions, smartlinks, imagenes y el sello EXTERNAL SENDER."""
    texto = html.unescape(re.sub(r"<[^>]+>", " ", texto))
    t = re.sub(r"<custom[^>]*>(.*?)</custom>", r"\1", texto, flags=re.S)
    t = re.sub(r"!\[\]\([^)]*\)", " ", t)
    t = t.replace("EXTERNAL SENDER", " ")
    # 14 sep 2026: el 14% de los comentarios de Jira traen apostrofe curvo (Outlook, iOS,
    # autocorrect). Todo el lexico de contracciones usa "'?" con apostrofe recto y fallaba
    # en silencio contra "i'll", "we're", "don't" escritos con ’. RCS-28753 se colo asi,
    # el cliente dijo "I'll reach out" y el clasificador no lo vio como cierre.
    t = t.replace("’", "'").replace("‘", "'")
    t = t.replace("“", '"').replace("”", '"')
    t = t.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", t).strip()


def es_interno(cuerpo):
    b = cuerpo.lower()[:220]
    return any(m in b for m in MARCAS_INTERNAS)


def es_bot(comentario):
    author=comentario.get('author',{})
    return author.get('accountType')=='app' or author.get('accountId','').startswith(BOTS)

def comentario_interno(comentario):
    # El atributo del servicio es la evidencia; el texto es solo compatibilidad de volcados antiguos.
    if isinstance(comentario.get('jsdPublic'),bool): return not comentario['jsdPublic']
    return es_interno(comentario.get('body',''))


def ultima_posicion(texto, patrones):
    """Devuelve la posicion del ultimo patron que aparece, o -1. Sirve de desempate:
    lo que se dijo mas cerca del final es lo que quedo en el aire."""
    bajo = texto.lower()
    pos = -1
    for p in patrones:
        for m in re.finditer(p, bajo):
            pos = max(pos, m.start())
    return pos


def causa_de(tid):
    """Lee tickets/<tid>.md, busca la seccion ## Causa mas reciente y su estado declarado.
    15 sep 2026, pedido de Juan: saber si el ticket ya tiene causa o solucion identificada
    sin abrir la ficha. Best effort, texto libre escrito por Claude en sesiones previas."""
    p = os.path.join(ROOT, "tickets", f"{tid}.md")
    if not os.path.exists(p):
        return {"estado": "sin ficha", "texto": ""}
    txt = open(p, encoding="utf-8", errors="replace").read()
    bloques = re.findall(r"^##\s*Causa\s*\n(.*?)(?=\n##\s|\Z)", txt, flags=re.S | re.M)
    if not bloques:
        return {"estado": "sin causa registrada", "texto": ""}
    bloque = bloques[-1].strip()
    bajo = bloque.lower()
    if "confirmad" in bajo[:60] or bajo.startswith("confirmad"):
        estado = "confirmada"
    elif "hipotesis" in bajo[:60] or "hipótesis" in bajo[:60]:
        estado = "hipotesis"
    else:
        estado = "registrada, sin marca"
    return {"estado": estado, "texto": bloque[:220]}


def bitacora_de(tid):
    """Ultima entrada que Juan reporto por chat. Formato: '## AAAA-MM-DD' al inicio de linea.
    bin/anotar cierra cada nota con '(HH:MM)'. Si esa hora esta, se usa para saber si la nota
    es realmente posterior al ultimo comentario del mismo dia. Sin hora explícita se marca
    incierta. Una bitácora no demuestra que se respondió públicamente."""
    p = os.path.join(ROOT, "bitacora", f"{tid}.md")
    if not os.path.exists(p):
        return None
    txt = open(p, encoding="utf-8", errors="replace").read()
    fechas = re.findall(r"^##\s*(\d{4}-\d{2}-\d{2})", txt, flags=re.M)
    if not fechas:
        return None
    ult = max(fechas)
    bloque = txt.split(f"## {ult}", 1)[1].strip().split("\n## ")[0].strip()
    m = re.search(r"\((\d{2}:\d{2})\)\s*$", bloque)
    hora = m.group(1) if m else "00:00"
    return {"fecha": ult, "nota": bloque[:400], "hora": hora, "hora_cierta": bool(m)}


def clasificar(issue, ahora):
    f = issue["fields"]
    comentarios = sorted(f.get("comment", {}).get("comments", []), key=lambda c: parse_fecha(c["created"]))
    tid = issue["key"]

    # Ultimo comentario de cada lado, ignorando bots.
    ult_cliente = ult_appriss = ult_publico = None
    for c in comentarios:
        aid = c["author"]["accountId"]
        if es_bot(c):
            continue
        cuerpo = limpiar(c["body"])
        interno = comentario_interno(c)
        nombre = c["author"]["displayName"]
        cliente = es_cliente(aid, nombre+" "+c["author"].get("emailAddress", ""))
        reg = {"fecha": parse_fecha(c["created"]), "autor": nombre,
               "cuerpo": cuerpo, "interno": interno, "cliente": cliente,
               "mio": aid == JUAN}
        if not interno:
            ult_publico = reg
        if cliente:
            ult_cliente = reg
        elif not interno:
            ult_appriss = reg

    dias = lambda r: (ahora - r["fecha"]).days if r else None

    # 15 sep 2026, pedido de Juan: "tome el ticket" no es "avance en la solucion". Recorre
    # TODOS tus comentarios, no solo el ultimo. avance_real queda True apenas uno solo trae
    # diagnostico escrito. primera_toma es tu primer comentario en el ticket, el reloj del
    # SLA de trabajo corre desde ahi, no desde el ultimo mensaje.
    avance_real = False
    primera_toma = None
    for c in comentarios:
        if c["author"]["accountId"] != JUAN or es_bot(c):
            continue
        fch = parse_fecha(c["created"])
        if primera_toma is None or fch < primera_toma:
            primera_toma = fch
        cuerpo_juan = sin_citas(limpiar(c["body"])).lower()
        if any(re.search(p, cuerpo_juan) for p in SUSTANCIA):
            avance_real = True

    # Señales que no cambian el nivel pero si obligan a mirar el ticket.
    alertas = []
    estado = (f.get("status") or {}).get("name", "")
    prioridad = (f.get("priority") or {}).get("name", "") or "Medium"
    pausado = bool(ESTADOS_PAUSA.search(estado))
    sla = {"reloj": "pausado" if pausado else "activo", "riesgo": None, "motivo": "",
           "jira": slas_jira(f), "seguimiento": None, "horas_sin_appriss": None,
           "fecha_comprometida": None}
    if pausado:
        # Reloj detenido. Solo seguimiento cuando el cliente calla, nunca SLA en riesgo.
        if ult_publico and not ult_publico["cliente"]:
            dh = horas_habiles(ult_publico["fecha"], ahora) / 24
            if dh >= SEGUIMIENTO_DIAS:
                sla["seguimiento"] = int(dh)
                alertas.append(f"seguimiento: el cliente no contesta hace {int(dh)} dias habiles, "
                               f"SLA pausado por {estado}")
    else:
        desde = ult_appriss["fecha"] if ult_appriss else (parse_fecha(f["created"]) if f.get("created") else None)
        hs = horas_habiles(desde, ahora)
        sla["horas_sin_appriss"] = round(hs, 1)
        aviso, techo = CADENCIA_HORAS.get(prioridad.lower(), CADENCIA_HORAS["medium"])
        fc = fecha_comprometida(ult_appriss["cuerpo"], ult_appriss["fecha"]) if ult_appriss else None
        if fc:
            sla["fecha_comprometida"] = fc.isoformat()
            hoy = ahora.astimezone(TZ_BOG).date()
            if hoy > fc:
                sla["riesgo"] = "vencido"
                sla["motivo"] = (f"paso la fecha comprometida {fc.isoformat()} y no hay update "
                                 f"publico de Appriss desde {desde.astimezone(TZ_BOG).date().isoformat()}")
        elif hs >= techo:
            sla["riesgo"] = "vencido"
            sla["motivo"] = f"{fmt_horas(hs)} sin comentario publico de Appriss, techo {prioridad} {fmt_horas(techo)}"
        elif hs >= aviso:
            sla["riesgo"] = "por vencer"
            sla["motivo"] = f"{fmt_horas(hs)} sin comentario publico de Appriss, techo {prioridad} {fmt_horas(techo)}"
        for j in sla["jira"]:
            if j["pausado"]:
                continue
            if j["vencido"] and not j["resolucion"]:
                sla["riesgo"] = "vencido"
                sla["motivo"] = f"Jira marca {j['nombre']} vencido ({j['restante']})"
            elif (not j["vencido"] and j["restante_ms"] is not None and j["meta_ms"]
                  and j["restante_ms"] <= 0.25 * j["meta_ms"]):
                if sla["riesgo"] != "vencido":
                    sla["riesgo"] = "por vencer"
                    sla["motivo"] = f"Jira {j['nombre']} vence en {j['restante']}"
        if sla["riesgo"]:
            alertas.append(f"SLA {sla['riesgo']}: {sla['motivo']}")
        for j in sla["jira"]:
            if j["resolucion"] and j["vencido"] and not j["pausado"]:
                alertas.append(f"Jira {j['nombre']} ya vencido ({j['restante']}), no cambia la prioridad del dia")
    ultimo_cualquiera = None
    for c in comentarios:
        if not es_bot(c):
            ultimo_cualquiera = c
    if ultimo_cualquiera and ultimo_cualquiera["author"]["accountId"] != JUAN \
            and "juan martinez" in ultimo_cualquiera["body"].lower():
        alertas.append(f"{ultimo_cualquiera['author']['displayName']} te menciono directo")
    # 15 oct 2026: la alerta "dias desde la toma sin avance escrito" salio. Medida por lexico
    # sobre dias corridos marcaba en riesgo tickets en Under Customer Review con el reloj
    # detenido (RCS-28099). El riesgo ahora es la cadencia de arriba, por estado.

    dias_desde_toma = (ahora - primera_toma).days if primera_toma else None

    def r(nivel, etiqueta, motivo, ref):
        # 15 oct 2026, regla de Juan: con el reloj activo, la pelota en el cliente y el estado
        # sin mover, Jira sigue contando. Se avisa, la transicion la hace Juan.
        if nivel == 3 and not pausado:
            alertas.append(f"la pelota esta en el cliente y {estado} deja correr el reloj; "
                           f"revisa si toca pasarlo a Under Customer Review")
        return {"nivel": nivel, "etiqueta": etiqueta, "motivo": motivo,
                "dias": dias(ref) if ref else 9999, "ultimo": ref, "alertas": alertas,
                "silencio_cliente": dias(ult_appriss) if ult_appriss else None,
                "avance_real": avance_real, "dias_desde_toma": dias_desde_toma, "sla": sla}

    # 15 sep 2026 (RCS-28294): un cierre generico del cliente ("gracias por todo") puede
    # tapar un pedido directo mas viejo que sigue sin contestar. Si lo ultimo publico es un
    # cierre puro del cliente, se mira el comentario publico inmediatamente anterior: si es
    # de otra persona, te menciona directo por nombre y trae un pedido, ese pedido sigue vivo,
    # el cierre no lo contesta.
    publicos = [c for c in comentarios if not es_bot(c)
                and not comentario_interno(c)]
    cede = tipo = None
    if ult_publico and ult_publico["cliente"]:
        cede, tipo = cliente_devuelve_pelota(ult_publico["cuerpo"], ult_publico["autor"])
    pedido_tapado = None
    if cede and len(publicos) >= 2:
        anterior = publicos[-2]
        if anterior["author"]["accountId"] != JUAN:
            cuerpo_ant = limpiar(anterior["body"])
            if "juan martinez" in cuerpo_ant.lower() and (
                    "?" in cuerpo_ant or any(re.search(p, cuerpo_ant.lower()) for p in PREGUNTA)):
                pedido_tapado = {
                    "fecha": parse_fecha(anterior["created"]),
                    "autor": anterior["author"]["displayName"],
                    "cuerpo": cuerpo_ant, "interno": False,
                    "cliente": es_cliente(anterior["author"]["accountId"], anterior["author"]["displayName"]),
                    "mio": False,
                }

    # Nivel 1: el ultimo que hablo de cara al cliente fue el cliente, y dejo algo pendiente
    # para Appriss. Si el cliente se comprometio el, la pelota es suya y el ticket baja a
    # nivel 3. Si solo acuso recibo sin dejar nada pendiente, no hay nada que esperar, baja a
    # nivel 4. Decision de Juan del 8 sep 2026, refinada el 17 sep 2026 tras RCS-27791: un
    # "yes, thank you" no es una promesa de volver, es un cierre.
    if ult_publico and ult_publico["cliente"]:
        if cede:
            if pedido_tapado:
                return r(1, "TE TOCA RESPONDER",
                         f"{pedido_tapado['autor']} te pidio algo directo hace "
                         f"{dias(pedido_tapado)} dias, nadie de Appriss contesto y el cierre "
                         f"de {ult_publico['autor']} no responde eso", pedido_tapado)
            if tipo == "acuse":
                return r(4, "EN MOVIMIENTO INTERNO",
                         f"{ult_publico['autor']} acuso recibo puro, nada pendiente de cara "
                         f"al cliente", ult_publico)
            return r(3, "ESPERANDO AL CLIENTE",
                     f"{ult_publico['autor']} se comprometio a volver hace {dias(ult_publico)} dias "
                     f"y no ha vuelto", ult_publico)
        extra = (f", el estado sigue en {estado} con el reloj pausado; contesta y revisa el estado"
                 if pausado else "")
        return r(1, "TE TOCA RESPONDER",
                 f"{ult_publico['autor']} escribio hace {dias(ult_publico)} dias y nadie de Appriss contesto{extra}",
                 ult_publico)

    if ult_appriss:
        texto = sin_citas(ult_appriss["cuerpo"])
        p_prom = ultima_posicion(texto, PROMESA)
        p_preg = ultima_posicion(texto, PREGUNTA)
        p_cond = ultima_posicion(texto, CONDICIONADA)
        d = dias(ult_appriss)
        quien = "prometiste" if ult_appriss["mio"] else f"{ult_appriss['autor']} prometio"
        # 11 sep 2026: un colega de Appriss puede pedirte algo A TI, no al cliente, casi
        # siempre relayando un pedido del cliente. RCS-28756, Akshaya Purappemane escribe
        # "@Juan Martinez... if you could please provide any logs". La posicion del pedido
        # ganaba y el ticket bajaba a ESPERANDO AL CLIENTE cuando el que debe algo eres tu.
        te_piden_a_ti = (not ult_appriss["mio"]) and "juan martinez" in texto.lower()
        # Nivel 3: lo ultimo que quedo en el aire fue un pedido al cliente. La posicion sola
        # no decide. Una promesa condicionada al cliente cede la pelota aunque cierre el texto.
        if p_preg >= 0 and (p_preg > p_prom or p_cond >= 0) and not te_piden_a_ti:
            pedido = "pediste" if ult_appriss["mio"] else f"{ult_appriss['autor']} pidio"
            return r(3, "ESPERANDO AL CLIENTE",
                     f"{pedido} algo hace {d} dias y no hay respuesta", ult_appriss)
        if p_preg >= 0 and te_piden_a_ti:
            return r(1, "TE TOCA RESPONDER",
                     f"{ult_appriss['autor']} te pidio algo directo hace {d} dias y nadie de Appriss "
                     f"contesto", ult_appriss)
        # Nivel 2: prometiste un update y no volviste.
        if p_prom >= 0:
            return r(2, "PROMESA SIN CUMPLIR",
                     f"{quien} un update hace {d} dias y no llego", ult_appriss)

    # 15 oct 2026, regla de Juan: despues del ownership, si el reloj esta activo y el techo de
    # cadencia o la fecha comprometida ya pasaron sin nada para el cliente, eso es deuda,
    # aunque el lexico no vea una promesa. RCS-28881: sesion del 13 oct sin resultado publicado.
    if sla["riesgo"] and not pausado:
        ref = ult_appriss or ult_publico
        return r(2, "UPDATE VENCIDO" if sla["riesgo"] == "vencido" else "UPDATE POR VENCER",
                 sla["motivo"], ref)

    # Nivel 4: ingenieria moviendose, nada pendiente de cara al cliente.
    ref = ult_appriss or ult_publico
    return r(4, "EN MOVIMIENTO INTERNO",
             "sin deuda detectada por reglas; requiere revisión humana" if ref else "sin comentarios", ref)


def clasificar_final(issue, ahora):
    """clasificar() mas el override de bitacora. Este es el pipeline completo, el mismo
    que corre main(). eval_cola.py debe medir esto, no clasificar() a secas, o el eval
    reprueba casos que el override ya resuelve."""
    c = clasificar(issue, ahora)
    bit = bitacora_de(issue["key"])
    # Una investigación o borrador local no prueba respuesta pública ni cumplimiento.
    if bit:
        c['alertas'] = c['alertas'] + [f"Hay trabajo local del {bit['fecha']}; verificar si se comunicó antes de dar el compromiso por cumplido"]
    return c, bit


def main():
    dump = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "cola", "jira-dump.json")
    solo_json = "--json" in sys.argv
    d = json.load(open(dump, encoding="utf-8"))
    nodos = d["issues"]["nodes"] if isinstance(d["issues"],dict) else d["issues"]
    ahora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5)))

    filas = []
    for i in nodos:
        f = i["fields"]
        c, bit = clasificar_final(i, ahora)
        causa = causa_de(i["key"])
        filas.append({
            "ticket": i["key"], "resumen": f["summary"],
            "estado": f["status"]["name"],
            "prioridad": (f.get("priority") or {}).get("name", ""),
            "reporta": (f.get("reporter") or {}).get("displayName", ""),
            "labels": f.get("labels", []),
            "edad": (ahora - parse_fecha(f["created"])).days if f.get("created") else None,
            "nivel": c["nivel"], "etiqueta": c["etiqueta"], "motivo": c["motivo"],
            "dias": c["dias"], "alertas": c.get("alertas", []),
            "silencio_cliente": c.get("silencio_cliente"),
            "avance_real": c.get("avance_real"), "dias_desde_toma": c.get("dias_desde_toma"),
            "reloj_sla": c["sla"]["reloj"], "riesgo_sla": c["sla"]["riesgo"],
            "sla_motivo": c["sla"]["motivo"], "seguimiento_dias": c["sla"]["seguimiento"],
            "horas_sin_appriss": c["sla"]["horas_sin_appriss"],
            "fecha_comprometida": c["sla"]["fecha_comprometida"],
            "sla_jira": c["sla"]["jira"],
            "causa_estado": causa["estado"], "causa_texto": causa["texto"],
            "ultimo_autor": c["ultimo"]["autor"] if c["ultimo"] else "",
            "ultimo_texto": (c["ultimo"]["cuerpo"][:300] if c["ultimo"] else ""),
            "bitacora": bit,
            "url": JIRA + i["key"],
        })

    # Dentro del nivel: reloj activo antes que pausado, SLA vencido antes que por vencer,
    # despues mas dias callado.
    rango = {"vencido": 0, "por vencer": 1}
    filas.sort(key=lambda r: (r["nivel"], r["reloj_sla"] == "pausado",
                              rango.get(r["riesgo_sla"], 2), -r["dias"]))

    os.makedirs(os.path.join(ROOT, "cola"), exist_ok=True)
    estado = {"generado": ahora.isoformat(), "total": len(filas), "tickets": filas}
    with open(os.path.join(ROOT, "cola", "estado.json"), "w", encoding="utf-8") as fh:
        json.dump(estado, fh, ensure_ascii=False, indent=1, default=str)
    if solo_json:
        print(f"{len(filas)} tickets en cola/estado.json")
        return

    niveles = {1: "Te toca responder", 2: "Prometiste o debes update y no llego",
               3: "Esperando al cliente", 4: "Revisar: sin deuda detectada por reglas"}
    conteo = {n: sum(1 for r in filas if r["nivel"] == n) for n in niveles}

    L = [f"# Cola de Juan", "",
         f"Generado {ahora.strftime('%Y-%m-%d %H:%M')} hora Colombia, desde el volcado local {os.path.basename(dump)}. "
         f"{len(filas)} tickets abiertos asignados.", "",
         "Orden: primero de quien es la pelota, despues cuanto lleva callado. "
         "El estado real siempre esta en Jira. Clasificación orientativa por expresiones; no sustituye leer compromisos ni impacto. "
         "La revisión integral del 28 sep está en inbox/2026-09-28-cola-prioridades-auditoria.md.", "",
         "| Nivel | Que significa | Cuantos |", "|---|---|---|"]
    for n, nom in niveles.items():
        L.append(f"| {n} | {nom} | {conteo[n]} |")
    L.append("")

    pos = 0
    nivel_actual = None
    for r in filas:
        if r["nivel"] != nivel_actual:
            nivel_actual = r["nivel"]
            L += ["", f"## Nivel {nivel_actual}. {niveles[nivel_actual]}", ""]
        pos += 1
        L.append(f"### {pos}. [{r['ticket']}]({r['url']}) · {r['resumen']}")
        L.append(f"`{r['estado']}` · reloj SLA {r['reloj_sla']} · prioridad {r['prioridad'] or 'sin definir'} · "
                 f"reporta {r['reporta'] or 'sin dato'}" + (f" · abierto hace {r['edad']} dias" if r['edad'] is not None else ""))
        L.append("")
        L.append(f"**{r['etiqueta']}.** {r['motivo'][0].upper() + r['motivo'][1:]}.")
        for a in r["alertas"]:
            L.append("")
            L.append(f"Aviso: {a}.")
        if r["ultimo_texto"]:
            L.append("")
            L.append(f"> Ultimo movimiento, {r['ultimo_autor']}: {r['ultimo_texto']}…")
        if r["bitacora"]:
            L.append("")
            L.append(f"Bitacora {r['bitacora']['fecha']}: {r['bitacora']['nota'][:220]}")
        L.append("")
        L.append(f"Ficha: `tickets/{r['ticket']}.md` · Bitacora: `bitacora/{r['ticket']}.md`")
        L.append("")

    with open(os.path.join(ROOT, "cola", "COLA.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L).rstrip() + "\n")
    print(f"{len(filas)} tickets. Niveles: " +
          ", ".join(f"{n}={conteo[n]}" for n in niveles))
    print(f"escrito: cola/COLA.md y cola/estado.json")


if __name__ == "__main__":
    main()

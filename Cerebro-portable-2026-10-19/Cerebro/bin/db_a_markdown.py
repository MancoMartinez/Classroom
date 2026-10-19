#!/usr/bin/env python3
"""Vuelca la base de Moscu a markdown plano, un archivo por carpeta de conocimiento.
El objetivo es que el cerebro sea legible sin SQLite, sin la app y sin ninguna key."""
import sqlite3, sys, os, re, datetime

db, out = sys.argv[1], sys.argv[2]
con = sqlite3.connect(db); con.row_factory = sqlite3.Row
os.makedirs(out, exist_ok=True)

def slug(s):
    s = re.sub(r'[^\w\s-]', '', s, flags=re.UNICODE).strip().lower()
    return re.sub(r'[\s]+', '-', s)[:60] or 'sin-nombre'

folders = con.execute("SELECT id,name FROM knowledge_folders ORDER BY id").fetchall()
for f in folders:
    chunks = con.execute(
        "SELECT id,title,body,source_path,created_at FROM knowledge_chunks "
        "WHERE folder_id=? ORDER BY ord,id", (f["id"],)).fetchall()
    if not chunks: continue
    lines = [f"# {f['name']}", "",
             f"Carpeta {f['id']} de la base de Moscú. {len(chunks)} fragmentos.", ""]
    for c in chunks:
        when = datetime.datetime.fromtimestamp(c["created_at"]).strftime("%Y-%m-%d") if c["created_at"] else ""
        lines.append(f"## {c['title'] or '(sin título)'}")
        meta = [f"chunk {c['id']}"]
        if when: meta.append(when)
        if c["source_path"]: meta.append(f"fuente: {c['source_path']}")
        lines.append(f"_{' · '.join(meta)}_"); lines.append("")
        lines.append(c["body"].rstrip()); lines.append("")
    path = os.path.join(out, f"{f['id']:02d}-{slug(f['name'])}.md")
    open(path, "w").write("\n".join(lines))
    print(f"   {os.path.basename(path)}  ({len(chunks)} fragmentos)")

# Items, contextos y categorías: la mesa de trabajo
try:
    rows = con.execute("""
        SELECT i.id,i.title,i.body,i.status,i.type,i.priority,i.due_at,i.source_ref,i.created_at,
               COALESCE(ct.name,'') ctx, COALESCE(cat.name,'') cat
        FROM items i
        LEFT JOIN categories cat ON cat.id=i.category_id
        LEFT JOIN contexts   ct  ON ct.id=i.context_id
        ORDER BY (i.status='open') DESC, ct.name, cat.name, i.id""").fetchall()
    if rows:
        lines = ["# Mesa de trabajo — items", "", f"{len(rows)} items.", ""]
        last = None
        for r in rows:
            key = (r["ctx"], r["cat"])
            if key != last:
                lines.append(f"\n## {r['ctx'] or 'Sin contexto'} › {r['cat'] or 'Sin categoría'}\n"); last = key
            bits = [b for b in (r["type"], r["status"]) if b]
            if r["due_at"]:
                bits.append("vence " + datetime.datetime.fromtimestamp(r["due_at"]).strftime("%Y-%m-%d"))
            if r["source_ref"]: bits.append(r["source_ref"])
            lines.append(f"### {r['title']}")
            lines.append(f"_{' · '.join(bits)}_")
            if r["body"]: lines.append(""); lines.append(r["body"].rstrip())
            lines.append("")
        open(os.path.join(out, "00-mesa-de-trabajo.md"), "w").write("\n".join(lines))
        print(f"   00-mesa-de-trabajo.md  ({len(rows)} items)")
except sqlite3.OperationalError as e:
    print("   (items no exportados:", e, ")")

# Conversaciones de chat guardadas
try:
    convs = con.execute("SELECT id,title,updated_at FROM chat_conversations ORDER BY updated_at DESC").fetchall()
    if convs:
        lines = ["# Conversaciones guardadas en Moscú", ""]
        for cv in convs:
            msgs = con.execute("SELECT role,content FROM chat_messages WHERE conversation_id=? ORDER BY id",(cv["id"],)).fetchall()
            if not msgs: continue
            when = datetime.datetime.fromtimestamp(cv["updated_at"]).strftime("%Y-%m-%d") if cv["updated_at"] else ""
            lines.append(f"\n## {cv['title'] or f'Conversación {cv[chr(34)+chr(34)]}'} ({when})\n" if False else f"\n## {cv['title'] or 'Conversación '+str(cv['id'])} ({when})\n")
            for m in msgs:
                who = "Yo" if m["role"] == "user" else "Moscú"
                lines.append(f"**{who}:** {(m['content'] or '').strip()}\n")
        open(os.path.join(out, "00-conversaciones.md"), "w").write("\n".join(lines))
        print(f"   00-conversaciones.md  ({len(convs)} conversaciones)")
except sqlite3.OperationalError as e:
    print("   (chats no exportados:", e, ")")
con.close()

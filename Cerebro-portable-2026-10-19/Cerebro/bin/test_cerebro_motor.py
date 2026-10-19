"""Prueba de regresión aislada; nunca abre la base real para escritura."""
import contextlib,sqlite3,tempfile
import numpy as np
from pathlib import Path
import cerebro_motor as b

def main():
    old_root,old_cache=b.ROOT,b.CACHE
    with tempfile.TemporaryDirectory() as td:
        b.ROOT=Path(td).resolve();b.CACHE=b.ROOT/'.cerebro'
        (b.ROOT/'brain').mkdir();(b.ROOT/'inbox').mkdir();(b.ROOT/'investigaciones').mkdir();(b.ROOT/'tickets').mkdir()
        p=b.ROOT/'brain/sessions.db'
        with sqlite3.connect(p) as c:
            c.executescript('CREATE TABLE knowledge_chunks(id INTEGER,title TEXT,body TEXT,created_at INTEGER); CREATE TABLE items(id INTEGER,title TEXT,body TEXT,status TEXT);')
            c.execute('INSERT INTO knowledge_chunks VALUES(1,?,?,0)',('Acceso','RCS-10001 usuario sin jerarquia'))
        before=p.read_bytes()
        source=b.ROOT/'inbox/2026-09-28-RCS-10001.md'
        source.write_text('# Corrección\nLa hipótesis previa quedó descartada. RCS-10002 comparte síntoma.\nÚltima evidencia: quetzaltest',encoding='utf-8')
        (b.ROOT/'tickets/RCS-10001.md').write_text('Ficha antigua')
        (b.ROOT/'investigaciones/mapa.md').write_text('# Mapa\nRecreateCaseNo arregla el número antiguo',encoding='utf-8')
        b.sync()
        packet=b.ticket_packet('RCS-10001')
        assert packet['found'] and any('quetzaltest' in r['body'] for r in packet['direct_evidence'])
        assert any(r['ticket']=='RCS-10002' for r in packet['related_mentions'])
        assert not b.ticket_packet('RCS-1000')['found']
        assert not b.search('RCS-99999',mode='bm25')['found']
        assert b.search('RecreateCaseNo',mode='bm25')['results'][0]['path']=='investigaciones/mapa.md'
        assert b.search('quetzaltest',mode='bm25')['results']
        source.write_text('Texto reemplazado: nuevohallazgo',encoding='utf-8');b.sync()
        assert not b.search('quetzaltest',mode='bm25')['results']
        assert b.search('nuevohallazgo',mode='bm25')['results']
        source.unlink();b.sync()
        assert not b.search('nuevohallazgo',mode='bm25')['results']
        assert 'usuario sin jerarquia' in b.read_source('db:knowledge_chunks/1')['text']
        for path in ('../secret.txt','bin/buscar','brain/sessions.db'):
            try:b.read_source(path)
            except ValueError:pass
            else:raise AssertionError('Lectura fuera del corpus: '+path)
        class FakeEncoder:
            def encode(self,texts,**kwargs):return np.ones((len(texts),3),dtype=np.float32)/np.sqrt(3)
        old_model=b._model;b._model=FakeEncoder()
        b.search('RecreateCaseNo',mode='hybrid')
        assert b.status()['chunks']==b.status()['vector_chunks']
        source.write_text('Nueva nota aprendeautomaticamente',encoding='utf-8')
        assert b.search('aprendeautomaticamente',mode='hybrid')['results']
        assert b.status()['chunks']==b.status()['vector_chunks']
        b._model=old_model
        assert p.read_bytes()==before,'La base fuente cambió' 
    b.ROOT,b.CACHE=old_root,old_cache
    print('OK: exactitud de IDs, novedades, cobertura, cambios/borrados, relaciones, lectura segura y base intacta')
if __name__=='__main__':main()

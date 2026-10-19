"""Prueba aislada de secretos, afirmaciones, versiones, filtro de hechos y grounding.
Corre sobre una carpeta temporal; nunca abre la base real."""
import sqlite3, tempfile
import numpy as np
from pathlib import Path
import cerebro_motor as b
import grounding as g
import secretos, afirmaciones as af


class FakeEncoder:
    def encode(self, texts, **kwargs):
        return np.ones((len(texts), 3), dtype=np.float32) / np.sqrt(3)


def main():
    old = b.ROOT, b.CACHE, b._model
    with tempfile.TemporaryDirectory() as td:
        b.ROOT = Path(td).resolve(); b.CACHE = b.ROOT / '.cerebro'; b._model = FakeEncoder(); b._dense.clear(); b._qcache.clear()
        for d in ('brain', 'inbox', 'investigaciones', 'tickets'): (b.ROOT / d).mkdir()
        db = b.ROOT / 'brain/sessions.db'
        with sqlite3.connect(db) as c:
            c.executescript('CREATE TABLE knowledge_chunks(id INTEGER,title TEXT,body TEXT,created_at INTEGER); CREATE TABLE items(id INTEGER,title TEXT,body TEXT,status TEXT);')
            c.execute('INSERT INTO knowledge_chunks VALUES(1,?,?,0)', ('Conexion', 'Server=x;Password=Sup3rS3cr3t9;'))
        antes = db.read_bytes()
        pat = 'abcdefghijklmnopqrstuvwxyz234567abcdefghijklmnopqrst'
        (b.ROOT / 'inbox/2026-10-01-rcs-10001.md').write_text(
            f'# Hallazgos\nHIPOTESIS. El job zorbalox quedó detenido por el lock.\nPAT pegado: {pat}\n'
            'CONFIRMADA. La tabla quarkmeter tiene 1,922,680 filas.\nEl ticket quedó en Under Customer Review.\n', encoding='utf-8')
        (b.ROOT / 'inbox/2026-10-01-rcs-10001-comentario-interno.md').write_text('Primera versión: zorbalox viejo', encoding='utf-8')
        (b.ROOT / 'inbox/2026-10-02-rcs-10001-comentario-interno-v2.md').write_text('Segunda versión: zorbalox nuevo', encoding='utf-8')
        (b.ROOT / 'investigaciones/solo-hipotesis.md').write_text('HIPOTESIS. flumbrix causa el corte, sin verificar.', encoding='utf-8')
        (b.ROOT / 'adjuntos/RCS-10001').mkdir(parents=True)
        (b.ROOT / 'adjuntos/RCS-10001/conteo.csv').write_text('minuto,h20,h21,h22\n0,1500,0,0\n1,1490,0,0\n2,1510,0,12\n', encoding='utf-8')
        b.sync()
        # Adjuntos: el csv entra al índice con su ruta original, ligado al ticket, y se lee por MCP.
        assert any(x['path'] == 'adjuntos/RCS-10001/conteo.csv' for x in b.ticket_packet('RCS-10001')['direct_evidence'])
        assert 'ceros=' in b.read_source('adjuntos/RCS-10001/conteo.csv', 1, 40)['text']
        # Secretos: ni el índice ni leer_fuente devuelven el valor.
        assert not b.search(pat, mode='bm25')['results']
        assert pat not in b.read_source('inbox/2026-10-01-rcs-10001.md')['text']
        assert 'Sup3rS3cr3t9' not in b.read_source('db:knowledge_chunks/1')['text']
        assert secretos.redactar('token: expirado') == 'token: expirado'
        assert b.status()['fragmentos_con_secreto_redactado'] >= 2
        # Afirmaciones por oración, con herencia de la etiqueta.
        tipos = {x[1] for x in af.extraer('HIPOTESIS. El job quedó detenido.\nCONFIRMADA. La tabla existe.\nfaltan 3 en cada tramo. DESCARTADO.')}
        assert tipos == {'hipotesis', 'confirmada', 'descartada'}, tipos
        p = b.ticket_packet('RCS-10001')
        assert p['afirmaciones']['hipotesis'] and p['afirmaciones']['confirmada'] and p['afirmaciones']['estados_jira']
        assert p['afirmaciones']['hipotesis'][0].get('posiblemente_superada') is None  # misma fecha que la confirmación
        # Versiones: la v2 reemplaza a la primera y la primera sale penalizada y anotada.
        assert 'inbox/2026-10-01-rcs-10001-comentario-interno.md' in p['versiones_reemplazadas']
        r = b.search('zorbalox', mode='bm25')['results']
        viejo = [x for x in r if x['path'].endswith('10-01-rcs-10001-comentario-interno.md')]
        assert viejo and viejo[0]['reemplazado_por'].endswith('-v2.md')
        # Filtro de hechos: el fragmento solo especulativo desaparece.
        assert any(x['path'] == 'investigaciones/solo-hipotesis.md' for x in b.search('flumbrix', mode='bm25')['results'])
        assert not any(x['path'] == 'investigaciones/solo-hipotesis.md' for x in b.search('flumbrix', mode='bm25', hechos=True)['results'])
        # Grounding: entidad inexistente, fecha futura y estado volátil.
        v = g.verificar('The quarkmeter table has 1,922,680 rows. The quarkmeter table has 7,654,321 rows. '
                        'It will be fixed by next week. The ticket is now in Under Customer Review.', 'cliente', usar_ce=False)
        por = {x['oracion']: x for x in v['oraciones']}
        assert not any(a['tipo'] == 'entidad_inexistente' for a in por['The quarkmeter table has 1,922,680 rows.']['alertas'])
        assert any(a['tipo'] == 'entidad_inexistente' for a in por['The quarkmeter table has 7,654,321 rows.']['alertas'])
        assert any(a['tipo'] == 'fecha_futura' for a in por['It will be fixed by next week.']['alertas'])
        assert v['verificar_en_jira'] and len(v['bloqueantes']) == 2
        assert db.read_bytes() == antes, 'La base fuente cambió'
    b.ROOT, b.CACHE, b._model = old; b._dense.clear(); b._qcache.clear()
    print('OK: secretos redactados, afirmaciones tipadas, versiones, filtro de hechos, grounding y base intacta')


if __name__ == '__main__':
    main()

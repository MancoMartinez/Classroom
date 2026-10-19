"""Regresión: trabajo interno no responde al cliente, orden y visibilidad de Jira."""
import datetime, tempfile
import cola
from pathlib import Path

def main():
    now=datetime.datetime.fromisoformat('2026-09-28T22:00:00+00:00')
    def comment(day,aid,body,public=True,kind='atlassian'):
        return {'created':f'2026-09-{day}T12:00:00+00:00','body':body,'jsdPublic':public,
                'author':{'accountId':aid,'displayName':aid,'accountType':kind}}
    client=comment('25','qm:customer','<p>Can you send the invitation?</p>')
    internal=comment('28',cola.JUAN,'<p>Investigating</p>',False)
    bot=comment('28','new-bot','Completed',True,'app')
    ack=comment('24',cola.JUAN,'I will provide an update')
    issue={'key':'RCS-99999','fields':{'comment':{'comments':[internal,client,bot,ack]},'priority':{'name':'High'}}}
    with tempfile.TemporaryDirectory() as td:
        old=cola.ROOT;cola.ROOT=td
        (Path(td)/'bitacora').mkdir()
        (Path(td)/'bitacora/RCS-99999.md').write_text('## 2026-09-28\nDraft prepared (17:00)')
        result,bit=cola.clasificar_final(issue,now)
        assert result['nivel']==1 and result['ultimo']['cliente'] and bit
        issue['fields']['comment']['comments'].append(comment('28',cola.JUAN,'<p>Could you confirm access?</p>'))
        assert cola.clasificar_final(issue,now)[0]['nivel']==3
        cola.ROOT=old
    print('OK: visibilidad, bots, cronología y borradores sin ocultar deuda pública')

def test_sla_por_estado():
    """15 oct 2026, regla de Juan: Under Customer Review pausa el SLA; el riesgo es cadencia
    sin comentario publico de Appriss con el reloj activo; una fecha comprometida manda."""
    def c(ts, aid, body):
        return {'created': ts, 'body': body, 'jsdPublic': True,
                'author': {'accountId': aid, 'displayName': aid, 'accountType': 'atlassian'}}
    jue = datetime.datetime.fromisoformat('2026-10-15T11:00:00-05:00')
    # Fin de semana no cuenta: viernes 17:00 a lunes 09:00 son 16 h habiles, 7 del viernes y 9 del lunes.
    assert round(cola.horas_habiles(datetime.datetime.fromisoformat('2026-10-09T17:00:00-05:00'),
                                    datetime.datetime.fromisoformat('2026-10-12T09:00:00-05:00'))) == 16
    preg = c('2026-10-05T11:00:00-05:00', cola.JUAN, 'Could you let me know whether your team still sees it?')
    pausado = {'key': 'RCS-1', 'fields': {'comment': {'comments': [preg]}, 'priority': {'name': 'High'},
               'status': {'name': 'Under Customer Review'}}}
    r = cola.clasificar(pausado, jue)
    assert r['sla']['reloj'] == 'pausado' and r['sla']['riesgo'] is None
    assert r['sla']['seguimiento'] and not any(a.startswith('SLA') for a in r['alertas'])
    activo = {'key': 'RCS-2', 'fields': {'comment': {'comments': [
        c('2026-10-14T10:00:00-05:00', cola.JUAN, 'The correction has been approved and is being put in place.')]},
        'priority': {'name': 'High'}, 'status': {'name': 'Work in progress'}}}
    r = cola.clasificar(activo, jue)
    assert r['sla']['riesgo'] == 'vencido' and r['nivel'] == 2
    sesion = {'key': 'RCS-3', 'fields': {'comment': {'comments': [
        c('2026-10-09T13:25:00-05:00', cola.JUAN, 'Our next session will take place on October 13th from 12:00 PM.')]},
        'priority': {'name': 'Medium'}, 'status': {'name': 'Work in progress'}}}
    r = cola.clasificar(sesion, jue)
    assert r['sla']['fecha_comprometida'] == '2026-10-13' and r['nivel'] == 2 and r['etiqueta'] == 'UPDATE VENCIDO'
    # Fecha pasada en el texto es historia, no compromiso.
    assert cola.fecha_comprometida('it came in through the file load on October 13', jue) is None
    # El cliente que sigue gestionando internamente cede la pelota.
    assert cola.cliente_devuelve_pelota("Greetings Juan, apologies for the delay, I'm still trying to get help internally on this matter.")[0]
    print('OK: SLA por estado, cadencia, fecha comprometida y fin de semana')

if __name__=='__main__':
    main()
    test_sla_por_estado()

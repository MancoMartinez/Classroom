"""Prueba del servidor real por stdio, con el mismo comando de ambos clientes."""
import asyncio,json,sys
from pathlib import Path
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    root=Path(__file__).resolve().parent.parent
    venv=root/'.venv-cerebro/bin/python'
    params=StdioServerParameters(command=str(venv if venv.exists() else sys.executable),args=[str(root/'bin/cerebro_mcp.py')])
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            ts=await session.list_tools()
            assert {t.name for t in ts.tools}=={'buscar_conocimiento','contexto_ticket','leer_fuente','estado_cerebro','verificar_borrador','consultar_relaciones'}
            assert all(t.annotations.readOnlyHint for t in ts.tools)
            ticket=await session.call_tool('contexto_ticket',{'ticket':'RCS-28671'})
            assert not ticket.isError
            data=ticket.structuredContent or json.loads(ticket.content[0].text)
            assert data['found'] and any('2026-09-28' in p for p in data['source_paths'])
            assert 'sqlmi-prd-wus2-arp-001' in data.get('accesos_juan',''), 'contexto_ticket sin accesos de Juan'
            source=await session.call_tool('leer_fuente',{'ruta':'AGENTS.md','linea':1,'cantidad':8})
            assert not source.isError
            found=await session.call_tool('buscar_conocimiento',{'consulta':'SSO Response Log','variantes':['registro de respuesta SSO','SAML claims log'],'limite':5})
            assert not found.isError
            payload=found.structuredContent or json.loads(found.content[0].text)
            degradado=[w for w in payload['warnings'] if w.startswith(('Canal vectorial','No se actualizaron','Sin vectores','Reranker no disponible'))]
            assert payload['results'] and not degradado,payload.get('warnings')
            assert any('SSO' in r['body'] for r in payload['results'])
            assert 'accesos_juan' not in payload
            check=await session.call_tool('verificar_borrador',{'texto':'Ticket RCS-99999999 has 7,654,321 rows. It will be fixed by next week.','destino':'cliente'})
            assert not check.isError
            v=check.structuredContent or json.loads(check.content[0].text)
            assert v['bloqueantes'],v
            rel=await session.call_tool('consultar_relaciones',{'entidad':'smart alerts no salen','hacia':'cliente'})
            assert not rel.isError
            rd=rel.structuredContent or json.loads(rel.content[0].text)
            assert rd['tickets']>0 and rd['cliente'],rd
            stats=await session.call_tool('estado_cerebro',{})
            assert not stats.isError
            print('OK: MCP stdio, seis herramientas, contexto reciente, lectura y búsqueda híbrida sin degradación')
if __name__=='__main__':asyncio.run(main())

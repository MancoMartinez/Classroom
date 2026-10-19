# Atajos de Cerebro para PowerShell. Cargalo una vez por sesion, desde la raiz de la carpeta:
#
#     . .\cerebro.ps1
#
# Despues los comandos son cortos:
#
#     buscar "izenda export"
#     buscar RCS-28535
#     carpetas
#     guardar 16 "Titulo del hallazgo" "cuerpo de la nota"
#     guardar-archivo 16 "Titulo" inbox\2026-09-08-tema.md
#     anotar RCS-28482 "pegue el comentario, quedo en Work in progress"
#     ingerir            ensayo, muestra que va a entrar a la base
#     ingerir-aplicar    escribe en la base
#     indexar            regenera tickets/
#     evaluar            mide el clasificador de la cola
#     estado             cifras de la base y chequeo de integridad

$Global:CerebroRoot = $PSScriptRoot

# Windows trae 'python' o el lanzador 'py'. Mac y Linux traen python3.
$Global:CerebroPy = $null
foreach ($c in @('python', 'py', 'python3')) {
    if (Get-Command $c -ErrorAction SilentlyContinue) { $Global:CerebroPy = $c; break }
}
if (-not $Global:CerebroPy) {
    Write-Host "No encuentro Python. Instalalo desde python.org o con 'winget install Python.Python.3.12'" -ForegroundColor Red
    return
}

function Invoke-Cerebro {
    param([string]$Script, [string[]]$Rest)
    Push-Location $Global:CerebroRoot
    try { & $Global:CerebroPy (Join-Path 'bin' $Script) @Rest }
    finally { Pop-Location }
}

function buscar          { Invoke-Cerebro 'buscar'            $args }
function carpetas        { Invoke-Cerebro 'guardar.py'        @('--carpetas') }
function anotar          { Invoke-Cerebro 'anotar.py'         $args }
function indexar         { Invoke-Cerebro 'indexar_tickets.py' $args }
function evaluar         { Invoke-Cerebro 'eval_cola.py'      $args }
function ingerir         { Invoke-Cerebro 'ingerir_inbox.py'  $args }
function ingerir-aplicar { Invoke-Cerebro 'ingerir_inbox.py'  (@('--aplicar') + $args) }
function cola            { Invoke-Cerebro 'cola.py'           (@('cola/jira-dump.json') + $args) }

function guardar {
    param([Parameter(Mandatory)][int]$Carpeta,
          [Parameter(Mandatory)][string]$Titulo,
          [Parameter(Mandatory)][string]$Cuerpo)
    Invoke-Cerebro 'guardar.py' @("$Carpeta", $Titulo, '--texto', $Cuerpo)
}

function guardar-archivo {
    param([Parameter(Mandatory)][int]$Carpeta,
          [Parameter(Mandatory)][string]$Titulo,
          [Parameter(Mandatory)][string]$Archivo)
    Invoke-Cerebro 'guardar.py' @("$Carpeta", $Titulo, '--archivo', $Archivo)
}

function estado {
    Push-Location $Global:CerebroRoot
    try {
        & $Global:CerebroPy -c @"
import sqlite3, os, glob
db = os.path.join('brain', 'sessions.db')
c = sqlite3.connect(db)
q = lambda s: c.execute(s).fetchone()[0]
print('chunks     ', q('select count(*) from knowledge_chunks'))
print('fts        ', q('select count(*) from chunks_fts'))
print('carpetas   ', q('select count(*) from knowledge_folders'))
print('items      ', q('select count(*) from items'))
print('integridad ', q('pragma integrity_check'))
print('ultimo     ', c.execute("select date(max(created_at),'unixepoch') from knowledge_chunks").fetchone()[0])
print('backups    ', len(glob.glob(db + '.bak-*')))
print('journal    ', 'SI, cuidado' if os.path.exists(db + '-journal') else 'no')
print('tickets    ', len(glob.glob(os.path.join('tickets', '*.md'))))
print('inbox      ', len(glob.glob(os.path.join('inbox', '*.md'))))
"@
    } finally { Pop-Location }
}

Write-Host "Cerebro cargado. Python: $Global:CerebroPy. Raiz: $Global:CerebroRoot" -ForegroundColor Green
Write-Host "Comandos: buscar, carpetas, guardar, guardar-archivo, anotar, ingerir, ingerir-aplicar, indexar, evaluar, cola, estado" -ForegroundColor DarkGray

# Montar Cerebro en una máquina. Paso a paso

Orden de lectura: este archivo para montar, `ESTADO.md` para saber qué hay y qué está roto.

Todo lo de abajo está probado. El Mac se montó el 8 sep 2026 y las cuatro comprobaciones del paso 6
pasaron con las cifras exactas. Solo necesitas Python 3. Nada de pip, ni entorno virtual, ni
dependencias.

Esta carpeta vive hoy en `~/Cerebro` en el Mac de Juan. El apéndice de Windows está al final, porque
la carpeta puede volver a viajar.

---

## Regla que evita el desastre

**El cerebro viaja, no se bifurca.** `brain/sessions.db` es un archivo SQLite. Dos máquinas
escribiendo en dos copias producen dos cerebros distintos y no hay forma de fusionarlos sin perder
trabajo.

Trabaja siempre en una sola máquina a la vez. Cuando cambies de máquina, lleva el zip completo y
reemplaza la carpeta entera. Nunca copies solo `inbox/` de un lado al otro esperando que se junten.

Si un día trabajaste en las dos por error, la máquina con el `sessions.db` más reciente manda.
Lo de la otra se recupera a mano desde `inbox/`, que es texto plano y sí se puede leer.

---

## Paso 1. Llevar el zip

El zip pesa cerca de 75MB. USB, OneDrive, Drive o Dropbox. Los tres sirven. Por correo no pasa.

No lo metas en git. La base de 33MB y los 21MB de adjuntos no van en un repo. Si quieres versionar,
versiona `bin/`, `flujos/`, `investigaciones/`, `brain/memoria/` y los `.md` de la raíz.

---

## Paso 2. Descomprimir

```bash
cd ~ && unzip ~/Downloads/Cerebro-2026-09-08.zip && cd ~/Cerebro
chmod +x cerebro.sh bin/buscar bin/guardar bin/anotar bin/exportar.sh
ls
```

Tienen que aparecer `ESTADO.md`, `CLAUDE.md`, `cerebro.sh`, y las carpetas `brain`, `bin`,
`tickets`, `inbox`, `skills`.

La carpeta va en `~/Cerebro`, no en `~/Downloads`. Downloads es carpeta de paso: las herramientas de
limpieza de macOS la vacían y iCloud puede tocarla. Todos los documentos asumen `~/Cerebro`.

---

## Paso 3. Confirmar que hay Python

```bash
python3 --version
```

Si responde con un número de versión, sigue. Si no existe:

```bash
brew install python3
```

Probado con Python 3.14.3. Nada más hace falta.

---

## Paso 4. Instalar las skills

Hay **dos sitios distintos** y no se hablan entre sí. Copiar en uno no las pone en el otro.

| Dónde | Quién lo lee | Cómo se instala |
|---|---|---|
| `~/.claude/skills/` | Claude Code en terminal | Copiando la carpeta, paso de abajo |
| Tu cuenta de Claude | Cowork y la app de escritorio | Subiéndolas desde Capacidades, Skills |

**Las skills de la cuenta no viajan con el zip.** Si cambias de máquina y además de cuenta de Claude,
Cowork no va a ver las cinco de Cerebro aunque la carpeta esté adjunta. Pasó el 9 sep 2026 al montar
esta Mac: `/cerebro` no autocompletaba nada porque esta cuenta es distinta a la del PC anterior.

Para subirlas, empaqueta una por una y súbelas desde la configuración de la cuenta:

```bash
cd ~/Cerebro/skills
for s in cerebro-cola cerebro-ticket cerebro-comentario cerebro-respuesta-cliente cerebro-asignacion; do
  zip -qr ~/Desktop/$s.zip "$s" -x "*.DS_Store"
done
```

Dos de las cinco funcionan a medias en Cowork, y conviene saberlo. `cerebro-ticket` dice que devuelve
el hallazgo a la base, y desde Cowork no puede escribir: deja el archivo en `inbox/` y ahí se queda
hasta que corras `cerrar`. `cerebro-asignacion` cosecha hacia `inbox/` con la misma limitación. Las
otras tres solo leen y redactan, así que funcionan completas.

Respalda primero lo que ya tengas instalado, porque las versiones del zip son las acortadas del
8 sep 2026 y pisan las viejas:

```bash
mkdir -p ~/.claude/skills-backup-$(date +%Y%m%d) && cp -R ~/.claude/skills/* ~/.claude/skills-backup-$(date +%Y%m%d)/ 2>/dev/null
mkdir -p ~/.claude/skills && cp -R ~/Cerebro/skills/* ~/.claude/skills/
ls ~/.claude/skills | wc -l
```

Van 29 skills en el zip. Las cinco de Cerebro son `cerebro-cola`, `cerebro-ticket`,
`cerebro-comentario`, `cerebro-respuesta-cliente` y `cerebro-asignacion`. El resto son las de Appriss
y las de formato, sirven igual.

Verifica que las cinco llegaron:

```bash
for s in cerebro-cola cerebro-ticket cerebro-comentario cerebro-respuesta-cliente cerebro-asignacion; do
  [ -f ~/.claude/skills/$s/SKILL.md ] && echo "ok $s" || echo "FALTA $s"
done
```

---

## Paso 5. Cargar los atajos de terminal

`cerebro.sh` te deja los comandos cortos. Resuelve la raíz solo, así que lo puedes cargar desde
cualquier directorio:

```bash
source ~/Cerebro/cerebro.sh
```

Tiene que imprimir `Cerebro cargado` en verde y la lista de comandos.

Para no repetirlo cada vez, agrégalo al perfil de zsh:

```bash
printf '\nsource "$HOME/Cerebro/cerebro.sh"\n' >> ~/.zshrc
```

Comandos que quedan cargados:

| Comando | Qué hace |
|---|---|
| `buscar "término"` | busca en conocimiento, mesa, memorias, tickets e inbox |
| `buscar RCS-28535` | imprime la ficha del ticket |
| `carpetas` | lista los IDs de carpeta con su conteo |
| `guardar 16 "Título" "cuerpo"` | escribe un chunk en la base |
| `guardar-archivo 16 "Título" inbox/archivo.md` | lo mismo desde un archivo |
| `anotar RCS-28482 "lo que hiciste"` | append a la bitácora del ticket |
| `ingerir` | ensayo, dice qué va a entrar y qué descarta |
| `ingerir-aplicar` | escribe el inbox consolidado en la base |
| `indexar` | regenera `tickets/` |
| `evaluar` | mide el clasificador de la cola |
| `refrescar` | dice qué etiquetas del eval vencieron |
| `cola` | recalcula la cola desde el volcado de Jira |
| `estado` | cifras de la base y chequeo de integridad |
| `cerrar` | `ingerir-aplicar` más `indexar` más `estado`, la rutina de cierre |
| `cerebro` | te para en la raíz de la carpeta |

---

## Paso 6. Verificar que llegó completo

Cuatro comprobaciones. Si las cuatro pasan, la migración salió bien.

```bash
estado
```

Espera exactamente esto:

```
chunks      1745
fts         1745
carpetas    27
items       491
integridad  ok
ultimo      2026-09-08
backups     1
journal     no
tickets     532
inbox       320
```

`chunks`, `tickets` e `inbox` crecen cada vez que ingieres. Lo que se verifica en una migración es
que las cifras de la máquina nueva sean iguales a las de la máquina de la que saliste, y que
`integridad` diga `ok`. Estas son las del Mac al 8 sep 2026, después de ingerir la nota de la propia
migración.

`chunks` igual a `fts` significa que el índice de búsqueda está sincronizado. Si difieren, la
búsqueda va a devolver menos de lo que hay y hay que reconstruir el índice, ver
`cola/INFORME-recuperacion.md`.

`journal` tiene que decir `no`. Si dice `SI, cuidado`, no borres el archivo a mano. Abre la base una
vez con Python y deja que haga rollback:
`python3 -c "import sqlite3; sqlite3.connect('brain/sessions.db').execute('select 1')"`.

```bash
buscar "izenda export"
```

Tiene que devolver resultados en CONOCIMIENTO, en MESA DE TRABAJO, en MEMORIAS y en TICKETS. Si
CONOCIMIENTO sale vacío y los otros traen cosas, el índice FTS5 se rompió en el traslado.

```bash
buscar RCS-28535
```

Tiene que imprimir la ficha del ticket. Es el atajo para cualquier identificador.

```bash
indexar
evaluar
```

`indexar` regenera `tickets/` y debe decir 530 fichas. `estado` cuenta 532 porque suma
`INDICE.md` y `DUDOSOS.md`, que no son fichas. `evaluar` mide el clasificador de la cola y
hoy da 100%, 15 de 15. Si da menos, corre `refrescar` primero: casi siempre son etiquetas vencidas,
no léxico roto. El detalle está en `ESTADO.md`.

Comprobación extra que vale la pena en máquina nueva. Prueba que SQLite sí puede escribir, sobre una
copia, para no meter basura en la base real:

```bash
cp brain/sessions.db brain/_prueba.db
echo "prueba" | CEREBRO_DB="$PWD/brain/_prueba.db" ./bin/guardar 27 "PRUEBA"
rm -f brain/_prueba.db brain/_prueba.db.bak-*
```

Si imprime `guardado, chunk NNNN`, el disco acepta el bloqueo y el cerebro puede aprender aquí.

---

## Paso 7. Abrir Claude en la carpeta

```bash
cd ~/Cerebro
claude
```

`CLAUDE.md` se carga solo y trae el contrato completo: dónde está cada cosa, las reglas que no se
negocian, y el techo de 2500 caracteres por entregable.

Primera frase útil para arrancar, para confirmar que Claude ve la carpeta y la base:

```
Lee ESTADO.md y dime en cinco líneas qué está roto hoy y qué falta ingerir.
```

Si Claude te contesta sin haber leído nada, o inventa cifras, la carpeta no está montada como
directorio de trabajo. Sal, vuelve a entrar desde `~/Cerebro`, y verifica con `ls CLAUDE.md`.

---

## Paso 8. Lo que falta cubrir, en orden

Esto es la deuda real que queda. Está en `ESTADO.md` con el detalle.

**1. Ingerir lo que se acumule.** Al cerrar cada día basta con `cerrar`, que encadena los tres
pasos. Sin esto el cerebro no aprende. Ya pasó: 289 notas en `inbox/` y un solo chunk en la base
entre el 25 de agosto y el 8 de septiembre.

**2. Cosechar las 17 sesiones pendientes.** `cosecha/registro.json` lleva 75 marcadas contra 92
contadas en el proyecto. Las 17 que faltan son chats cuyo hallazgo nunca llegó a la base. Esos chats
viven en la cuenta de Claude que Juan usaba en el otro PC. Desde esta Mac, con otra cuenta, no se
alcanzan. Recupéralos exportando desde esa cuenta, o dalos por perdidos y sigue.

**3. Clasificador de la cola. Cerrado el 8 sep 2026, está en 100%.** Lo que queda es mantenimiento:
cuando `evaluar` baje, corre `refrescar` antes de tocar el léxico. El set de etiquetas caduca solo y
eso ya se diagnosticó mal una vez. Detalle en `ESTADO.md`.

**4. Llenar `flujos/` e `investigaciones/`.** Tres archivos y uno, contra 1744 chunks. Ahí debería
vivir lo que se repite. Es la deuda más grande.

**5. Embeddings locales. Cerrado el 8 sep 2026: no valen, o al menos no todavía.** El set se llevó a
101 preguntas y se corrieron los cinco brazos. FTS5 33%, BM25 38%, LSA 38%, RRF 39%, BM25 más LSA
39%. Ninguna pareja se separa. Añadir el canal semántico a un ranking léxico bueno mueve cinco
preguntas con p igual a 1.00. No instales torch para arreglar el recall.

Lo que sí queda abierto es por qué cinco recuperadores distintos fallan en las mismas dos terceras
partes. Eso apunta al tamaño de los fragmentos o a los títulos, no al ranking. Detalle en
`cola/INFORME-recuperacion.md`.

---

## Paso 9. Rutina diaria, ya montado

Mañana, con `cerebro.sh` ya en el perfil, los atajos están cargados al abrir la terminal:

```bash
cd ~/Cerebro
claude
```

Y dentro de Claude, según lo que necesites: la cola del día, un ticket concreto, o el reparto al
equipo. Las skills se disparan solas por lo que pidas.

Antes de investigar cualquier cosa, busca. Casi siempre ya hay algo escrito:

```bash
buscar "el síntoma concreto"
```

Al cerrar el día:

```bash
anotar RCS-28482 "pegué el comentario interno, quedó en Under Support Review"
cerrar
```

Una nota puntual entra a mano:

```bash
carpetas
guardar 16 "Título del hallazgo" "el cuerpo de la nota"
guardar-archivo 16 "Título del hallazgo" inbox/2026-09-08-tema.md
```

Carpetas útiles: 16 RCS Soluciones, 19 RCS Procesos, 26 ADUSA, 17 Reuniones, 27 Cerebro.

---

## Paso 10. Cowork, en modo consulta

Decisión de Juan del 8 sep 2026. Cowork sirve para buscar, leer fichas, redactar comentarios y armar
entregables de Office. La base no acepta escritura desde ahí. La carpeta se monta por FUSE y SQLite
no puede tomar el bloqueo.

Adjunta `~/Cerebro` al proyecto de Cowork. Todo lo que Cowork produzca se escribe a
`inbox/AAAA-MM-DD-tema.md`, y entra a la base después, desde esta terminal, con `cerrar`. La regla
ya está escrita en `CLAUDE.md`, así que Cowork la lee sola.

### Cómo se conectan Cowork y la terminal

No hay sincronización ni copia. Es la misma carpeta en el mismo disco. Cowork escribe archivos de
texto en `inbox/`, y la terminal los mete a la base. Ese es todo el mecanismo.

```
Cowork  ──escribe──>  ~/Cerebro/inbox/2026-09-09-tema.md
                              │
Terminal  ──cerrar──>  ingerir-aplicar, indexar, espejo
                              │
                      brain/sessions.db
```

Lo que Cowork sí puede hacer sobre la base: leerla. `bin/buscar` cae a `immutable=1` y funciona.
Lo que no puede: escribir. Por eso todo lo que produzca va a `inbox/` y espera a la terminal.

### La prueba de una sola vez, para confirmar que el circuito cierra

La primera vez que uses Cowork con la carpeta adjunta, pídele esto:

```
Busca "izenda export" en Cerebro y escribe lo que encuentres en
inbox/2026-09-09-prueba-cowork.md
```

Después, en la terminal:

```bash
ls -l ~/Cerebro/inbox/2026-09-09-prueba-cowork.md
cerrar
```

Si el archivo aparece con la fecha de hoy y `cerrar` lo ingiere, el circuito está cerrado y no hay
que volver a comprobarlo. Si el archivo no aparece, Cowork no tiene permiso de escritura sobre la
carpeta y hay que revisar cómo quedó adjuntada.

Nunca abras la carpeta en Cowork en una máquina y en terminal en otra el mismo día. Eso bifurca el
cerebro.

---

## Paso 11. Volver a empacar cuando cambies de máquina

```bash
cd ~/Cerebro && cerrar
cd ~ && zip -r ~/Cerebro-$(date +%Y-%m-%d).zip Cerebro
```

`cerrar` va primero. Un zip con `inbox/` sin ingerir se lleva el trabajo en texto plano y deja la
base atrasada.

---

## Si algo falla

| Síntoma | Causa y qué hacer |
|---|---|
| `disk I/O error` al escribir en la base | Estás en el sandbox de Cowork, no en terminal. La carpeta se monta por FUSE y SQLite no puede tomar el bloqueo. Deja la nota en `inbox/` e ingiere desde la terminal |
| `buscar: command not found` | Falta cargar `cerebro.sh`. Corre `source ~/Cerebro/cerebro.sh`, o llama al script crudo con `python3 ~/Cerebro/bin/buscar "término"` |
| `buscar` no imprime nada | El término no está en la base. Prueba con una palabra sola antes de dar el índice por roto |
| CONOCIMIENTO vacío y el resto con resultados | El índice FTS5 se rompió. Reconstruir según `cola/INFORME-recuperacion.md` |
| `chunks` distinto de `fts` en `estado` | Lo mismo de arriba. La búsqueda está devolviendo menos de lo que hay |
| `journal SI, cuidado` | Escritura interrumpida. Abre la base con Python y deja que haga rollback. No borres el archivo |
| Claude no ve la carpeta | Abriste `claude` fuera de `~/Cerebro`. Sal y entra desde la raíz |
| `evaluar` da menos de 100% | Corre `refrescar`. Si nombra etiquetas vencidas, el problema es el calendario, no el léxico: refréscalas y vuelve a medir. Si no hay vencidas, el léxico se movió y la cola puede estar mal ordenada |
| Moscú abierta al escribir | Ciérrala. `bin/guardar` la detecta en Mac y se detiene antes de tocar la base |
| `permission denied` al correr `bin/guardar` | Falta el bit de ejecución. `chmod +x cerebro.sh bin/buscar bin/guardar bin/anotar bin/exportar.sh` |

---

## Apéndice. Windows

La carpeta trae `cerebro.ps1`, el equivalente de `cerebro.sh` para PowerShell. Los scripts
`bin/guardar` y `bin/anotar` están escritos en bash y PowerShell no los ejecuta, por eso existen
`bin/guardar.py` y `bin/anotar.py`.

```powershell
cd $HOME
Expand-Archive -Path "$HOME\Downloads\Cerebro-2026-09-08.zip" -DestinationPath $HOME -Force
cd $HOME\Cerebro
. .\cerebro.ps1
```

El punto y el espacio del principio importan. Sin ellos las funciones no quedan cargadas.

Para dejarlo en el perfil: `Add-Content $PROFILE "`n. $HOME\Cerebro\cerebro.ps1"`.

Si Python no existe: `winget install Python.Python.3.12`, y reabre PowerShell.

Si la política de ejecución bloquea el `.ps1`:
`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

Skills: `Copy-Item -Recurse -Force "$HOME\Cerebro\skills\*" "$HOME\.claude\skills\"`.

Empacar: `Compress-Archive -Path "$HOME\Cerebro" -DestinationPath "$HOME\Cerebro-$(Get-Date -Format yyyy-MM-dd).zip" -Force`.

En Windows `bin/guardar.py` no verifica si Moscú está abierta. Ciérrala tú antes de escribir.

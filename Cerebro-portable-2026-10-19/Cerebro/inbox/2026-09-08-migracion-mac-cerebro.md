# Migracion de Cerebro al Mac, 8 sep 2026

## Que pasa

Cerebro volvio al Mac desde el PC donde se trabajo en Cowork las ultimas semanas. Quedo montado en
`~/Cerebro`, con terminal como casa y Cowork en modo consulta.

## Causa de la ineficiencia anterior, confirmada

El sandbox de Cowork monta la carpeta por FUSE y SQLite no puede tomar el bloqueo. Escritura da
`disk I/O error` siempre. Por eso la base se congelo entre el 25 ago y el 8 sep: 289 notas en
`inbox/` y un solo chunk escrito. Trabajar solo en Cowork impide que el cerebro aprenda.

## Evidencia

Las cuatro comprobaciones del paso 6 pasaron con las cifras exactas en el Mac: chunks 1744 igual a
fts 1744, integridad ok, sin journal, `evaluar` 73% con los mismos cuatro fallos nombrados,
`indexar` 530 fichas.

La escritura en SQLite se probo sobre una copia de la base y funciono. El disco del Mac acepta el
bloqueo, asi que el cerebro si puede aprender aqui.

`ingerir` en ensayo dio 0 pendientes. El inbox estaba al dia al llegar.

## Que se hizo

Carpeta movida de `~/Downloads/Cerebro` a `~/Cerebro`. Downloads es carpeta de paso que macOS
limpia, y todos los documentos asumen `~/Cerebro`.

Se escribio `cerebro.sh`, equivalente de `cerebro.ps1` para zsh y bash. `cerebro.ps1` es PowerShell
y no corre en Mac, asi que el Mac no tenia atajos. Resuelve su raiz solo y carga desde cualquier
directorio. Quedo en `~/.zshrc`. Trae `cerrar`, que encadena `ingerir-aplicar`, `indexar` y
`estado`.

Las 29 skills quedaron en `~/.claude/skills`. Las versiones viejas de `appriss-hr-question` y
`appriss-jira-support` se respaldaron antes de pisarlas.

`CLAUDE.md` apuntaba a `_MIGRACION-2026-09-08/ESTADO.md`, carpeta inexistente. Corregido a
`ESTADO.md` en la raiz. Toda sesion que siguiera esa ruta arrancaba sin el estado del sistema.

`PASOS.md` se reescribio con Mac primero y Windows en apendice. Antes era solo PowerShell.

## Que sigue

La deuda del paso 8 no cambio. Las 17 sesiones sin cosechar viven en la cuenta de Claude del PC
anterior y desde esta Mac no se alcanzan. O se exportan desde esa cuenta, o se dan por perdidas.

El clasificador de la cola sigue en 73% y espera dos decisiones de Juan: quien cuenta como cliente
mas alla de las cuentas `qm:`, y si un acuse de recibo del cliente sube un ticket a nivel 1.

`flujos/` con tres archivos e `investigaciones/` con uno siguen siendo la deuda mas grande.

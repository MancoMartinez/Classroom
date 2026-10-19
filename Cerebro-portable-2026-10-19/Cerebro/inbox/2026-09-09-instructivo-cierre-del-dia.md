# Instructivo, cierre del dia en terminal

Verificado el 9 sep 2026 leyendo `cerebro.sh` y `bin/ingerir_inbox.py`.

## Que pasa

La rutina de cierre existe y es `anotar` mas `cerrar`. El inbox llego a 342 archivos, 18 de hoy,
porque `cerrar` nunca archiva lo que ya ingirio. Cada cierre relee los 342.

## Causa

CONFIRMADA. `cerrar` corre `ingerir-aplicar` sin `--archivar`. El flag existe en
`bin/ingerir_inbox.py` linea 230 y mueve lo ingerido a `inbox/archivo/`. La funcion `cerrar` de
`cerebro.sh` no lo pasa. Los archivos descartados por nombre nunca se mueven, ni con el flag.

## Evidencia

- `cerebro.sh`: `cerrar() { ingerir-aplicar; indexar; espejo; estado; }`, sin `--archivar`.
- `ingerir_inbox.py` linea 336: solo mueve los archivos de chunks nuevos, no los descartados.
- `ls inbox/*.md | wc -l` devuelve 342 el 9 sep.

## Que hago hoy

Secuencia completa, en este orden:

```
source ~/Cerebro/cerebro.sh
anotar RCS-28756 "que hiciste, una frase"
ingerir --desde 2026-09-09
ingerir-aplicar --desde 2026-09-09 --archivar
indexar
espejo
estado
```

El ensayo va primero siempre. Lee el conteo de descartes antes de aplicar. Si un archivo que
importa aparece como descarte, el problema es el nombre, no el contenido.

Reglas de nombrado, porque el clasificador decide por nombre de archivo:

- Entra: informe, instructivo, causa, analisis, verificacion, fix, rca, investigacion,
  hallazgo, diagnostico, cosecha.
- No entra: comentario, respuesta, teams, correo, pegar, email, mensaje, cola, reparto,
  refresco, plan, pasos, prompt, borrador, draft, checklist.
- Sin palabra clave, entra igual. El default es consolidar.

El ticket sale del nombre del archivo primero, y si no hay, del primer ticket que aparezca en
los primeros 1500 caracteres del texto. Nombra el archivo con el ticket cuando la nota es de un
ticket, o la nota termina archivada bajo el primer ticket que menciones de paso.

## Precedentes

Entre el 25 ago y el 8 sep entraron 289 notas al inbox y un solo chunk a la base. Por eso existe
`ingerir_inbox.py`. Sin `--archivar` el inbox vuelve a crecer igual.

## Compromisos

Ninguno. Queda pendiente decidir si `cerrar` en `cerebro.sh` incorpora `--archivar`.

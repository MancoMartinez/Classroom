# RCS-27991 · Engage Analytics Not Populating Sections · avance del 26 ago 2026

Estado verificado en Jira hoy: **Work in progress**, High, assignee Juan Martinez, reporter Paul
Marderosian, interno de Appriss. Creado 27 jul 2026, ultimo update 19 ago 2026. **30 dias abierto,
7 dias de silencio, cero comentarios de ingenieria en todo el ticket.**

Textos para pegar, en archivos aparte:

- `inbox/2026-08-26-rcs-27991-comentario-interno.md` · comentario de escalacion y mensaje de Teams
- `inbox/2026-08-26-rcs-27991-respuesta-paul.md` · respuesta al reporter

---

## 1. El hallazgo que desatasca el ticket

**RCS-28068, lululemon, esta en `Accepted into Development` desde el 18 de agosto con Shandana
Khan.** Mismo sintoma, palabra por palabra:

> "the Top 10 SKUs and Top 10 Consumers tables are not displaying any data. I tried adjusting the
> date ranges, but the issue persists and the tables remain empty."
> Sindhura Arakala, lululemon, 30 jul 2026

Carl Costelow lo mando a bug el 5 de agosto:

> "After speaking to Jon he thinks this is a code issue. Can we create a bug please"

Ingenieria ya acepto este defecto y esta trabajandolo. RCS-27991 lleva 30 dias esperando a Amy
Tsushima por un canal que nunca contesto. **No hay nada nuevo que investigar. Hay que colgar el
27991 del trabajo que ya corre.**

RCS-28068 no tiene remote link a Azure DevOps. El numero de bug hay que pedirselo a Shandana.

## 2. El defecto ya se arreglo una vez. Puede ser regresion

Confirmado en Confluence, pagina **November 2025 Sprint**, espacio R&D. La fila, literal:

```
66220 | Bug | Engage Analytics dashboard Top 10 lists not populating | RCS-23643 | Foot Locker | Secure EBR | Priority 1
```

https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/476530868980/November+2025+Sprint

Azure DevOps 66220, entregado en el primer release de noviembre 2025, ramas `release/5.4/5.4136` y
`release/5.4/5.4137`.

Causa raiz registrada en RCS-23643 por Mohammed Mutahhar, 22 oct 2025:

```
The Hierarchy Filter is not being applied.
The reference data backload task is failing with:
The given value '44_00001138_NAVY/WHITE/GUM' of type String from the data source
cannot be converted to type nvarchar for Column 7 [ProductHierarchy4].
```

Cerrado como `Engineer Resolved - Data Corrected`.

Mismo componente, mismos dos paneles, titulo casi identico. Esa es la hipotesis fuerte y son dos
chequeos baratos contra HFT y FAD: estado del reference data backload, y aplicacion del Hierarchy
Filter.

## 3. Confluence confirma el descarte de RCS-27586

El link `relates to RCS-27586` viene mal desde el 28 de julio y desvio la investigacion cuatro
semanas. Juan ya lo descarto el 13 de agosto dentro del ticket. Confluence lo respalda por dos vias:

**Runbook: Kohl's**, espacio RTS, clasifica el 27586 como otra cosa:

> "| Engage dashboard missing / timeouts | Engage dashboard blank or 500/timeout | RCS-27586 |"

https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478008508421/Runbook+Kohl+s

**Release Notes Secure July 2026 Release 2/2.** El unico item de Kohl's mas Insights de ese release
es `ENG-6184 | KHL | Insights Return Metrics Error`. Return metrics, no paneles Top 10.

https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/478084988936

Cronologia que lo cierra: release a produccion el 23 jul, cliente confirma funcionando el 24 jul,
Paul reporta el 27 jul contra un dashboard que si renderiza.

## 4. Evidencia tecnica: que falla exactamente

Captura en `adjuntos/RCS-27991/2026-08-26-harbor-freight-engage-analytics-tiles-error.png`. Juan
confirmo que es del momento del reporte, 27 jul 2026, y que el adjunto `Engage Analytics Issue.docx`
del ticket es la misma imagen dentro de un documento. **No hay que descargar el docx, no aporta
nada nuevo.**

Portal Harbor Freight, pestana Engage Analytics:

| Elemento | Resultado |
|---|---|
| Calls to Appriss | 179 · carga |
| Calls Per Action | 5.31% · carga |
| Activity Reports | 126 · carga |
| No ID (NR) | control View presente |
| Manual ID Entry | control View presente |
| Boris Return Amount | $0 · carga |
| Panel inferior izquierdo | triangulo de advertencia, sin datos |
| Panel inferior derecho | triangulo de advertencia, sin datos |

**Los seis tiles agregados cargan. Solo fallan los dos paneles de detalle SKU.** Descarta
autenticacion, permisos, sesion y el dashboard como conjunto. El fallo vive en la capa de datos de
SKU.

Que la captura sea del 27 jul resuelve la contradiccion aparente con lo que dijo Paul el 14 de
agosto. Harbor Freight todavia tenia Engage Analytics ese dia y migro a Insights despues.

## 5. Alcance real: tres tenants, todos en GP3

| Tenant | ABBR | Ticket | Estado |
|---|---|---|---|
| Harbor Freight | HFT | RCS-27991 | Work in progress, 30 dias |
| Floor & Decor | FAD | RCS-27991 | reproducido por Paul, rango 08/08 a 08/14 |
| lululemon | LLU | RCS-28068 | Accepted into Development |

Los tres comparten cluster GP3 segun la tabla de clientes del cerebro.

## 6. El tercer ticket huerfano

**RCS-28004, Engage Insights UPC missing, Harbor Freight y DSW.** Reportado por Paul el 28 jul, un
dia despues del 27991. Assignee Jon Morgan. **Sigue en `Under Support Review` con cero comentarios
desde el 28 de julio.**

Juan le pregunto a Paul el 13 de agosto si era el mismo problema. Paul contesto las otras tres
preguntas y omitio esta. La pregunta se repite en la respuesta de hoy.

Jon Morgan es quien dictamino que el 28068 es bug de codigo, y es el assignee del 28004.

## 7. Ruta de escalacion, verificada

`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md`, handoff de Kristin, 28 jul 2026:

> "Insights (antes Engage Analytics) -> VP Kenny Vu -> Ian -> Shirude/Hal."

`brain/memoria/reference_escalacion_l3_procedimiento.md`:

> "| Engage Engineering | Under Engineering Review | Ian Williams + mensaje de Teams | ENG |"
> "En los demas se reasigna."

Backups si Ian no esta: Shruti Golwalkar o Kenny Vu.

## 8. Transicion sugerida

`Work in progress` → **`Under Engineering Review`**, assignee **Ian Williams**, mensaje de Teams
obligatorio. Juan se desasigna, la regla lo exige para Engineering.

Orden de ejecucion:

1. Quitar el link `relates to RCS-27586`. Agregar `relates to RCS-28068`
2. Pegar el comentario interno
3. Hacer la transicion y reasignar a Ian Williams
4. Mandar el mensaje de Teams
5. Pegar la respuesta a Paul

## 9. Lo que Confluence NO tiene

Vale registrarlo porque cierra lineas de busqueda:

- Ninguna pagina documenta el defecto de 2026. RCS-27991, RCS-28068 y RCS-28004 no aparecen en
  Confluence
- No existe evidencia de un fix de los paneles Top 10 desplegado el 23 de julio de 2026
- El unico ADO ligado a este sintoma es el 66220 de noviembre de 2025
- No hay pagina sobre ProductHierarchy ni sobre reference data backload ligada a Engage Insights

## 10. Pendientes despues de la escalacion

1. Pedirle a Shandana Khan el numero de bug de Azure DevOps del 28068
2. RCS-28004 lleva 29 dias sin un comentario con Jon Morgan. Va aparte
3. Cuando ingenieria confirme la causa raiz, escribir la investigacion en `investigaciones/`. El
   cerebro no tiene ninguna sobre Engage Analytics ni sobre la migracion a Engage Insights

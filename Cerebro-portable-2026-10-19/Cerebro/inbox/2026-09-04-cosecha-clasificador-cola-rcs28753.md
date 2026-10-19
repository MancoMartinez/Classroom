# Cosecha 4 sep 2026 — Falla del clasificador de cola, RCS-28753

Sesión fuente: "Cerebro cola manana" (local_27334dae), transcripción del 3 sep 2026.

## Hallazgo verificado

En la corrida de la mañana del 3 de septiembre, la exactitud del clasificador de `bin/cola.py` cayó a 94 por ciento. RCS-28753 se clasificó en nivel 4 y le correspondía nivel 2. Causa: el léxico de promesas no reconoce el triage automático como respuesta de Appriss.

La cola creció de 17 a 19 tickets ese día. RCS-28342 entró en nivel 1, Ahold-Delhaize llevaba 8 días sin oír nada de Appriss y volvió a escribir. RCS-28482 entró en nivel 3 porque Mohammed Mutahhar mencionó directamente a Juan con una explicación técnica.

## Acción pendiente

Revisar el léxico de `bin/cola.py` para que el triage automático cuente como respuesta de Appriss. Mientras no se corrija, la exactitud contra el set de `bin/eval_cola.py` queda por debajo de 100 por ciento y la cola puede estar mal ordenada en casos similares a RCS-28753.

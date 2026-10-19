---
tema: tickets RCS creados en septiembre 2026 por equipo y estado
fecha: 2026-09-25
---

Conteo de tickets RCS con created >= 2026-09-01, agrupados por team Colombia y team India,
desglosados por estado: Complete, Closed, Under Customer Review (UCR), Under Support Review (USR),
Work in progress (WIP). Roster usado es el corregido de 14 personas en
brain/memoria/project_appriss_support_team.md (25 sep 2026).

## Totales por equipo, solo septiembre

| Equipo   | Complete | Closed | UCR | USR | WIP | Total |
|----------|----------|--------|-----|-----|-----|-------|
| Colombia | 0        | 57     | 23  | 9   | 21  | 110   |
| India    | 0        | 50     | 25  | 3   | 24  | 102   |

## Detalle por persona, solo septiembre

### Team Colombia

| Persona            | Complete | Closed | UCR | USR | WIP | Total |
|--------------------|----------|--------|-----|-----|-----|-------|
| Juan Martinez      | 0        | 2      | 3   | 2   | 2   | 9     |
| Diego Buelvas      | 0        | 17     | 5   | 0   | 0   | 22    |
| Sebastian Rueda    | 0        | 6      | 2   | 3   | 3   | 14    |
| Edwin Garzon       | 0        | 19     | 2   | 3   | 3   | 27    |
| Luis Hernandez     | 0        | 6      | 1   | 1   | 4   | 12    |
| Sebastian Garces   | 0        | 7      | 9   | 0   | 4   | 20    |
| Enrique Jimenez    | 0        | 0      | 1   | 0   | 5   | 6     |

### Team India

| Persona                  | Complete | Closed | UCR | USR | WIP | Total |
|---------------------------|----------|--------|-----|-----|-----|-------|
| Viraj Kansara             | 0        | 15     | 4   | 0   | 0   | 19    |
| Nikita Rathore            | 0        | 7      | 4   | 0   | 4   | 15    |
| Vedant Shirude            | 0        | 10     | 6   | 2   | 7   | 25    |
| Bikash Kumar              | 0        | 5      | 4   | 1   | 5   | 15    |
| Gulshan Kumar             | 0        | 1      | 0   | 0   | 0   | 1     |
| Megha Rathi               | 0        | 5      | 4   | 0   | 6   | 15    |
| Harini Shankarakrishnan   | 0        | 7      | 3   | 0   | 2   | 12    |

Nadie del equipo tiene tickets en estado Complete en septiembre.

Fuente: JQL project = RCS AND assignee = "<nombre>" AND created >= "2026-09-01" AND status in
(Complete, Closed, Under Customer Review, Under Support Review, Work in progress), corrida el
25 sep 2026 para las 14 personas del roster corregido. Ver
inbox/2026-09-25-tickets-por-estado-equipo-colombia-india.md para los totales sin filtro de fecha
y para la nota sobre la correccion del roster.

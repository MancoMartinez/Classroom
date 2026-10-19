# Flag: Sebastian Garces y el roster oficial de Colombia

La sesion "RCS-28621 file upload process" del 28 ago 2026 dejo esta afirmacion sin verificar
contra la fuente: "Sebastian Garces tampoco es del roster oficial de Colombia, es de otro equipo."

`brain/memoria/project_appriss_support_team.md`, tomado de la pestana Miembros de Teams el 3 ago
2026, lista once miembros del equipo Support Appriss y Sebastian Garces no aparece en esa lista.
`bin/asignar.py` si lo trae en el diccionario EQUIPO, nivel nuevo, techo 5, desde antes del 25 ago
2026.

Dos lecturas posibles. Garces entro al equipo despues del 3 de agosto y el roster de Teams quedo
desactualizado. O Garces pertenece a otro equipo y curriculum en el reparto diario es un error que
ya lleva semanas repitiendose, tickets asignados a alguien fuera del roster de Colombia.

Verificar la pestana Miembros de Teams de Support Appriss hoy decide cual de las dos es. Mientras
no se verifique, el reparto de hoy sigue tratando a Garces como nuevo de Colombia porque asi esta en
`bin/asignar.py`, que es lo que corrio en las ultimas corridas. Si la verificacion confirma que no
pertenece, hay que sacarlo de EQUIPO y revisar los tickets que ya le cayeron: RCS-28621, RCS-28634,
RCS-28618, RCS-28612, RCS-28582, RCS-28556, RCS-28552.

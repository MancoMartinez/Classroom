# RCS-29054 Big 5, por qué piden la llamada

Qué pasa
Nancy pidió la llamada el 1 oct, nueve días después de tu respuesta del 22 sep. Tú preguntaste quién administra el feed y ella contesta con Peter Chang, quien en RCS-27342 mandó el storemaster.txt de Big 5. El xlsx trae 382 tiendas, 32 distritos, 6 regiones y 3 RLPM. No trae columna con el valor anterior, así que nadie ve qué filas cambian.

Causa
Hipótesis: Peter es el dueño del archivo y Nancy lo trae para que tú le expliques qué archivo cambiar y en qué formato. Confirmada: la regla de Peyman Motlagh del 22 sep, soporte no edita reference_location por ticket.

Evidencia
RCS-27342, nota interna de Dean Korbakis: x_rlpm sale de lp_manager en parsed_sso_location, unido por número de tienda con storemaster. El RLPM viaja en el CSV de SSO location, no solo en storemaster.
RCS-28576: Big 5 pasó a Snow Time el 25 ago y el RLPM ya se rompió dos veces este año.
Xlsx: los distritos 112, 123 y 135 tienen dos RLPM. El RLPM es atributo de tienda, no nivel de jerarquía.

Qué hago hoy
1. Pregunta a Peter qué sistema genera storemaster.txt y el CSV de SSO location, y quién los edita.
2. Pregunta si lp_manager lleva iniciales (JZ, MI, PH) o nombre completo. El xlsx trae iniciales.
3. Pide la fecha en que el feed llevará los valores nuevos y cuáles son las 2 tiendas que cierran, nota del xlsx.
4. Corre un SELECT de ardm_147.reference_location y compáralo con el xlsx. La diferencia es la lista de cambios.
5. Tras el feed, valida las tiendas 7 y 87 en el distrito 235.

Precedentes
RCS-27342 y RCS-28576, Big 5 RLPM. RCS-28763, CTC: el cliente manda el Appriss_LocationFile por ticket, solo filas nuevas o cambiadas. Confluence PD, Reference_Location Hierarchy: un distrito no puede pertenecer a dos regiones.

Compromisos
Ofreciste comprobar los distritos cuando el feed se actualice. Paul Marderosian pidió el invite el 2 oct y Jira no muestra respuesta. No prometas fecha de carga.

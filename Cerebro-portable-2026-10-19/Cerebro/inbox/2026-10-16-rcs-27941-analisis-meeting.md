Qué pasa
Jira en vivo: Closed, Juan Martinez. ENG-7824 Done, sin cambio de código. Colton validó búsquedas de ambas usuarias el 15 sep.
Causa
Configuración y asignación de acceso. Kiran corrigió grupos de Ramos; los niveles de las usuarias no tenían acceso a los tipos buscados. Beverly todavía aparecía Corporate User cuando Francesca ya tenía HR Corporate User el 10 sep.
Evidencia
Kiran 3323851 del 1 sep y ENG-7824 del 3 sep. Colton 3347270 del 15 sep confirma resultado. https://trebuco.atlassian.net/browse/RCS-27941
Capturas 1414961, 1414958, 1414960: permisos por tipo de caso. 1420026 y 1420027: niveles diferentes; 1420452: Beverly ajustada a HR Corporate User.
Qué hago hoy
Presentarlo como antecedente resuelto. Preguntar por consistencia histórica si surge HR, sin atribuir una regresión de código. La ausencia en LPUser2 no explica por sí sola estas altas.
Precedentes
RCS-26584 ya documentaba HR Corporate User en mayo. Leer correcciones de bitacora/RCS-27941.md; análisis en investigaciones/2026-10-16-tailored-incident-id-analisis.md.
Compromisos
Cierre tras validación del cliente. No confundirlo con el defecto actual de primer ingreso.

Facteus, para qué es la reunión con Santhosh y guión para llevarla

Fecha 2026-10-07. Retomando después de una semana en otras cosas, esto es el hilo completo de por qué esta reunión existe y qué tiene que salir de ahí.

Por qué existe esta reunión

Data Engineering, con Chris Howard, ya armó todo el proceso de soporte de Facteus y ya confirmó los puntos pendientes, SLA de 1 día hábil con expectativa de 24 horas salvo fines de semana, ruta de escalación por Jira Operations hacia todo el equipo de Data Engineering, y los dos dashboards ya enlazados en cada sección de triage de los documentos. Eso quedó cerrado en el correo del 26 y las dos respuestas de Chris del 29, en inbox/2026-09-26-facteus-correo-final-chris.md y inbox/2026-09-29-facteus-respuesta-chris-updates.md.

Lo único que falta para que Support acepte el handover completo es decidir quién monitorea las alertas día a día. En la llamada del 25 con Viraj salió que no tiene sentido que lo monitoree Support directamente, porque L1 ya monitorea todo lo demás con un modelo rotacional 24 por 7, y meter a L1 desde el inicio es mejor que involucrarlos después y que pregunten por qué no los avisaron antes. Esa es la razón de fondo por la que le escribiste a Santhosh.

Qué tiene que salir resuelto de la reunión

Si L1 suma Facteus a lo que ya monitorea. Cuál de los dos dashboards usan, el de Grafana o el de consola que hizo Saddam. Cómo lo validan contra una alerta real antes de confiar en él. Con eso resuelto, le avisas a Chris que L1 está listo y se pone fecha al handover completo.

Sobre el wiki que te mandó Santhosh

Esa página, Facteus Support, es la más vieja de todas, del 28 de junio, la escribió Saddam antes de que existiera todo el proceso detallado. Sirve como contexto general, pero no tiene el SLA confirmado ni la ruta de escalación ni los dashboards, eso se armó después en otras páginas. Vale la pena que la revise, pero mándale también los links de las páginas que sí tienen el estado actual, para que su equipo no llegue con información vieja.

Guión para la llamada, 30 minutos

Primeros 5 minutos, contexto. Facteus es el único cliente al que le enviamos datos en vez de recibirlos, y quiere que les avisemos si no llega el envío diario. Data Engineering ya cerró el SLA, la escalación y los dashboards de su lado, lo único abierto es quién mira las alertas todos los días.

Siguientes 10 minutos, la pregunta central. Preguntar directo si L1 puede sumar esto a la rotación que ya tienen para todo lo demás, dejando que ellos mismos digan si les cabe en la carga actual. No es una decisión que les estás imponiendo, es una pregunta abierta.

Siguientes 10 minutos, si dicen que sí. Revisar juntos los dos dashboards, Grafana en https://apprissretail.grafana.net/goto/svsg2j y el de Saddam en https://prd-datacloud-console-app-wus2.azurewebsites.net/, y decidir cuál usan como fuente única. Preguntar cómo probarían cualquiera de los dos contra una alerta real antes de confiar en él en producción, nadie lo ha hecho todavía.

Últimos 5 minutos, cierre. Acordar quién de su equipo revisa la documentación, y qué le llevas de vuelta a Chris para fijar la fecha del handover completo.

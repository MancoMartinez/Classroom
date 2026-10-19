RCS-29351 AAP, Smart Track Cashier Refunding to Own Card sin resultados
Jira en vivo 16 oct: Under Customer Review, Enrique, esperando respuesta a sus tres preguntas del 14 oct.

QUE PASA
Cathryn Garcia, AAP cliente 21, editó una query. El link desde Store SRA Activity Lookup abre la query 1d vacía.

LO QUE MUESTRA EL VIDEO, 17 SEGUNDOS
0 a 3 s: hace clic en el valor -123.29 de Bruce Wood, tienda 7655, cajero 947878. Se abre el menú "Select Where To Go" y elige Cashier Refunding to Own Card. Ese menú es la opción que Enrique no ve.
5 s: abre /system/ebr/smarttracksearches/1d - Cashier Refunding to Own Card.search con storeno y cashierno en la URL. Parameters muestra Trans Date Within "The last 0 Days".
9 s: pone 7 Days en Set input value. A los 12 s sigue "No Results Found".

CAUSA
Hipótesis, ninguna confirmada.
A. El link pasa solo tienda y cajero y Trans Date queda en 0 días.
B. La edición de Cathryn a la copia pública de 1d cambió algo que el link necesita.
C. La conversión de AAP a SnowTime del 2 oct, PR 58545, dejó 1d sin datos. Cathryn dice que el link funcionaba antes de su cambio, lo que debilita C.

EVIDENCIA
1. Captura del ticket: la copia pública 1d, en Admin Reports > SRA Smart Tracks, tiene Last Changed 10/08/26 11:41:55. Las demás son de mayo.
2. arpfiles: el link abre la copia del sistema. Ese archivo y smarttracks/secure_Repo.json no cambian desde el 5 jun.
3. Video: con 7 días sigue vacío y la fuente muestra 5 reembolsos del mismo cajero.

QUE HAGO HOY
1. En AAP ejecuta 1d directo desde Composer con 30 días, tienda 7655 y cajero 947878. Con datos, el fallo está en el mapeo del link. Vacío, el fallo está en la query o en los datos tras SnowTime.
2. Compara la copia de Admin Reports > SRA Smart Tracks que editó Cathryn con el 1d del sistema. Son dos queries y el link apunta a la del sistema.
3. Revisa el atributo search-name de 1d. Dice "1c" y el archivo es 1d.

PRECEDENTES
RCS-28982 TSC: Composer renombró el token del parámetro y rompió el link. Se arregló con PR 58842. RCS-29268 Watsco: PR 58674. Los dos fixes pasaron por arpfiles.

SIGUIENTE PASO
Carl Costelow, autor de PR 58545 y 58554: ¿la conversión de AAP cambia el resultado de 1d? Falta el resultado del paso 1.
Cathryn: sin mensaje hasta tener el paso 1.

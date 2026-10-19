# RCS-28911, lo que aporto Ryan Barlow en Teams el 15 sep 17:38 a 17:43

Cosecha del hilo de Teams. Corrige tres cosas que el ticket y el tracker daban por buenas.

## Lo que dijo, textual en lo que importa

"We don't typically set ANC_ExpectedDaily so that any other files that are received are processed
(no relation to ticket RCS-28093). If it was something critical, we might set it, or have that file
as a standalone job."

"If no files are found, the job fails and alerts L1 - always."

"It does appear that we usually receive both files. If the file came later on Monday, it would have
processed Tuesday morning. The customer delivers the files with the same name to the same folder
(on the LPMS SFTP). If they resend another file, there is a chance it overwrites what is sitting on
the SFTP waiting for the next scheduled run."

"A missing store file 99% of the time isn't critical. This customer just happens to modify the file
manually and then places it in a location for an internal process to pick up and deliver. They
missed the timing, or the file got process the following day. Given the circumstances though, I'm
assuming they are saying that some of the changes aren't reflected."

"In my opinion, the file they sent yesterday just sat around until it processed this morning. I
didn't see any comments from the customer yet indicating it hasnt."

## Las tres correcciones

1. ANC_EXPECTEDDAILE en FALSE no es un descuido ni tiene que ver con RCS-28093. Es el modo normal,
   para que cualquier otro archivo que llegue se procese igual. Se pone en TRUE solo si el archivo
   es critico, o el archivo se saca a un job aparte. La recomendacion que quedo pendiente el 15 sep
   de "activar la alerta" cae. Ryan ya la respondio.

2. El job no es un fallo silencioso. Si no encuentra ningun archivo, falla y alerta a L1, siempre.
   Lo que paso el 14 fue distinto: el archivo de empleados si estaba, asi que el job tenia trabajo,
   corrio y salio en 0. La lectura de "fallo silencioso" que venia de RCS-28093 no aplica aca.

3. Pedir el reenvio era contraproducente. El cliente entrega con el mismo nombre a la misma
   carpeta, asi que un segundo archivo puede sobrescribir uno que este esperando la proxima corrida.
   Juan ya habia pedido el reenvio en el ticket el 15 sep 18:11. Hay que corregirlo.

## Lectura que queda en pie

El archivo del lunes probablemente quedo en el SFTP y se proceso en la corrida del martes 10:00 GMT.
Los 440 registros de esa corrida encajan con eso. La pregunta real no es si el archivo llego, es si
los cambios que el cliente esperaba ya estan reflejados en LPMS. Eso solo lo puede decir el cliente.

Por eso RCS-28911 sigue en Awaiting Ahold input y la peticion cambia de "reenvia el archivo" a
"confirma si los cambios ya se ven, y no reenvies mientras tanto".

## Compromiso que Juan dejo en Teams

Documentar este proceso para referencia futura. Este archivo lo cubre. Candidato a subirlo a
flujos/ como la ficha del job Refloader Prod Delhaize.

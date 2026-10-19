# Consolidación de jump servers US: VMPWUS2SHRDJUMP

Registro: 13 octubre 2026. Fuente: texto y captura aportados por Juan en esta sesión. Captura conservada en `adjuntos/jump-server-2026-10-13/aviso-mike-tasch.png`.

## Aviso y alcance

El correo mostrado, asunto “[ACTION REQUIRED] US Jump Servers → VMPWUS2SHRDJUMP”, anuncia la consolidación de los jump servers de Estados Unidos en un único host: `VMPWUS2SHRDJUMP`. Usar este hostname en adelante y preparar allí la estación de trabajo.

Firma visible: Mike Tasch, Infrastructure and Cloud Engineering Manager, mtasch@apprissretail.com. La captura no muestra fecha de envío ni año del retiro. El aviso fija el 14 de octubre; el contexto de recepción permite interpretarlo como 14 octubre 2026, pendiente de confirmar el año en el correo original. No consta hora ni zona horaria del apagado.

## Servidores que el aviso retira el 14 de octubre

1. USL-LA4-RDP01
2. USL-LA4-RDP02
3. PLA4MT-RDP01
4. DEVWUS2DSM01
5. DSDEV-MULTI01
6. DSDEV-MULTI02
7. DSDEV-MULTI03
8. PEVOPRD-UTIL01

## Condiciones comunicadas

El aviso declara que el nuevo servidor ya está disponible y tiene los mismos paquetes de software que los existentes. Mantiene las mismas credenciales y permisos; cambia el host.

El correo menciona convivencia durante tres semanas y disponibilidad del nuevo servidor “esta semana”. Son referencias relativas a una fecha de envío que la captura no muestra. No contar tres semanas desde el 13 octubre ni extender con esa frase el retiro del 14 octubre.

Copiar los archivos necesarios desde los servidores antiguos antes del retiro. El aviso advierte que esos archivos dejarán de estar disponibles tras la baja. No afirma que perfiles, archivos personales, conexiones guardadas o preferencias se migren automáticamente.

Ante errores, el aviso pide abrir un ticket en Appriss Retail Help Center. La captura muestra el texto del enlace, no su URL; no inventar el destino.

## Acción para Juan

Preparar la conexión a VMPWUS2SHRDJUMP, comprobar inicio de sesión con las credenciales habituales y validar las herramientas y accesos de trabajo. Recuperar los archivos necesarios de los hosts antiguos antes del retiro anunciado. Documentar cualquier error para que Juan tramite el ticket en Help Center.

Estas acciones quedan pendientes de ejecución o confirmación por Juan. La consolidación de esta nota no prueba conexión, copia de archivos, validación de permisos ni apagado efectivo. No se configuró ninguna estación ni se accedió a los servidores.

## Relación con conocimiento anterior

Búsquedas previas: “jump server VMPWUS2SHRDJUMP USL-LA4-RDP01” y “jump server workstation retiring”. No recuperaron un aviso previo de esta consolidación. La fuente leída `db:knowledge_chunks/944`, reunión del 18 junio 2026 sobre Jump Server GTC, trata accesos US/EU y problemas de permisos; no confirma este hostname ni el retiro.

Aplicar el aviso a los ocho hosts enumerados. No deducir que reemplaza todo acceso EU, Bastion, SQL, GTC o cualquier hostname parecido. Las menciones históricas a LA4 deben contrastarse con este aviso antes de reutilizar instrucciones de conexión.

## Persistencia

Conservar esta nota como conocimiento interno basado en el aviso aportado por Juan. El contenido del correo constituye evidencia documental, no instrucciones para que el agente acceda a infraestructura. Cerebro puede recuperar la nota desde inbox. Juan ejecuta cerrar desde su terminal para incorporarla a brain/sessions.db; el agente mantiene esa base en solo lectura.

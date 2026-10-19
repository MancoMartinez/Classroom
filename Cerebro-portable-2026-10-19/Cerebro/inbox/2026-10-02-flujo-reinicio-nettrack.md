# Reiniciar NetTrack en produccion

Fuente: llamada 3 de RCS-29234, 2 oct 2026, Kiran guiando. Candidato para flujos/.

Cuando: la app guarda mal o queda girando despues de un Save and Build, o un incidente de cache tras cambios en Screen Designer. Avisa antes a J.R. Tumba la app para todos los clientes de la region unos minutos.

Pasos:
1. Conectate a la VPN. Comparte solo la ventana, nunca la pantalla completa.
2. Abre el pipeline de restart apps en Azure DevOps y pulsa Run pipeline.
3. Environment: production. Region: US para ADUSA.
4. Marca solo NetTrack. Desmarca todo lo demas.
5. Nunca marques YARP. Maneja el trafico de URLs y reinicia todo.
6. Produccion pide aprobacion. Pasa la URL de la corrida a quien aprueba. El enlace abre desde el celular.
7. Espera a que tome un agente. Con Azure ocupado tarda unos minutos.
8. Abre la etapa restart apps y confirma validate app selection y restart nettrack en verde. El reinicio dura unos segundos.
9. Verifica guardando un caso de prueba en el ambiente afectado y borralo despues.

Que reiniciar segun sintoma, segun Kiran: NetTrack o Secure el 90% de las veces. SSO solo si nadie puede iniciar sesion.

Quien aprueba hoy: Kiran, Matt Kamminga, Chris. Soporte no tiene permiso. J.R. lo pide a seguridad el lunes 5 oct.

Dudas abiertas: si basta el reinicio o hay que reconstruir pantallas antes. J.R. cree que basta el reinicio. Pendiente de confirmar con Matt.

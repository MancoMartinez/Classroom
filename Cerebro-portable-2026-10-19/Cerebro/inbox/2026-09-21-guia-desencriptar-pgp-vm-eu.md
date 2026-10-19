# Guia setup desencriptar PGP en VM (via Sebastian Rueda, Teams)

Fuente: chat de Teams con Sebastian Rueda, no Confluence. Confirmado 21 sep 2026.
Contexto: Juan ya tenia la VM de EU seteada, path OK, gpg4win instalado y el repo appriss_pipeline clonado.
Sebastian aporto el archivo gpg_looper.sh corregido (el compartido se llamaba "gpg_looper 2.sh", hay que renombrarlo a gpg_looper.sh) y confirmo el flujo completo.

## Prerequisito

Tener el PAT de Azure DevOps. Se pide en uno de los pasos del setup, sin el, el script de instalacion no avanza.

## Instalar el pipeline (una sola vez por VM/region)

1. Clonar el repo dentro de la VM, en Users, carpeta CODE:
   git clone https://apprissdevops@dev.azure.com/apprissdevops/DataOps%20Platform/_git/appriss_pipeline
2. Correr el script de setup (env_setup.ps1) para que PowerShell reconozca apprissgpg como comando. Sin este paso, apprissgpg no se reconoce como comando conocido.

## Importar la clave del cliente

En PowerShell:
apprissgpg i [clientID+abreviacion]
ejemplo: apprissgpg i c171seg

## Desencriptar

Colocar el archivo gpg_looper.sh en la misma carpeta donde estan los archivos .pgp del cliente.
Correrlo y usar el mismo codigo de cliente que se importo arriba.

El archivo original compartido por Sebastian se llama "gpg_looper 2.sh", hay que corregir el nombre a gpg_looper.sh antes de usarlo.

## Nota de Juan

El punto donde se traba la gente la primera vez es que apprissgpg no se reconoce como comando hasta correr el setup del pipeline (clonar repo + correr el script). Una vez hecho eso, el resto es tedioso pero no complejo: importar clave, correr el .sh con el codigo de cliente.

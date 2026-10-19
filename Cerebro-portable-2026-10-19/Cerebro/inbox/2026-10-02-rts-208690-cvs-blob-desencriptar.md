# RTS-208690. CVS C037 STREAM_TRUNCATED. Cómo bajar y desencriptar desde la VM

Qué pasa: tres CVS_Txn_*.JSON.PGP del 1 oct fallan con STREAM_TRUNCATED en raw_tlog. Edwin los verifica. Daniel quiere ver el JSON desencriptado en pantalla.
Causa: hipótesis. Export incompleto de CVS. Los reenvíos cargan bien: 202609302223_00 pasó de 2,079 a 10,000 filas.

Ruta reusada de RCS-28281, ver inbox/2026-09-24-rcs-28281-desencriptar-pasos.md y donde-consultar.md.

1. VM DEVWUS2DSM01. Storage Explorer, buscar stprdwus2shrdtlog. Contenedor de Ahold era 112ahl. Para CVS se espera 037cvs, sin verificar. Ruta Archive/Prod/2026/10/01/.
2. Si pide permisos: clic derecho en la cuenta, conectar con Microsoft Entra ID.
3. Copiar los .PGP a C:\temp\rts208690. Nunca tocar el original.
4. Si apprissgpg no existe en su usuario: clonar appriss_pipeline en C:\Users\<usuario>\CODE, Set-ExecutionPolicy -Scope Process Bypass, correr powershell\env_setup.ps1 con el PAT az-artifact-svc-pat de dev-wus2-dataops-kv, reabrir PowerShell.
5. apprissgpg i c037cvs. Código sin verificar, la llave es gpg-<codigo>-prv en el Key Vault de prod.
6. apprissgpg d c037cvs <archivo.PGP> <archivo.json>
7. Verificar: tamaño, conteo de bytes en cero, últimos 200 bytes, json.load.
8. Borrar C:\temp\rts208690.

Precedente: en RCS-28281 los XML que fallaban estaban llenos de bytes en cero, no cortados. Revisar ambas cosas.

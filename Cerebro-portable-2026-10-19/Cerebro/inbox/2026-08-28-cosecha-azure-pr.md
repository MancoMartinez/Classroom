# Cosecha azure-pr — 2026-08-28
Fuente: sesion local_19ba3b08-1343-4154-940d-76ecfee6008b, "Azure links y PR"

## Hallazgos verificados

Organizacion unica de Azure DevOps: `dev.azure.com/apprissdevops`.

Rutas de PR y builds:

```
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/Secure/pullrequest/<ID>
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/Secure/pullrequests?_a=all
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_build?definitionScope=\Azure\Builds
https://dev.azure.com/apprissdevops/DataOps/_git/c026kro/pullrequest/56772
https://apprissretail.visualstudio.com/VerifyDatabase/_build?definitionId=209
```

DataOps ordena los repos de datos por cliente con el patron `c[ClientID][abrev]`. La branch de
trabajo es `Production`, nunca `master`.

Repos clave: `Secure`, que es el mono repo, `arpfiles`, que guarda configuracion por cliente y se
clona en `C:\arpfiles`, y `Tools`.

Los numeros de PR corren en una sola secuencia para toda la organizacion. El numero no identifica
el repo. El 55297 vive en `c001adm` y el 55640 en `Secure`, y quedan pegados en el mismo rango.
Abrir la URL con el repo equivocado devuelve error, ADO no redirige. Entra por la vista de PRs del
proyecto cuando no sepas de donde salio el numero.

PR 56323 y PR 55640 de Sysrepublic Secure ya estan citados en
`brain/memoria/project_teams_unificacion_2026_08_12.md`.

Paginas de Confluence localizadas:
- Raising a Pull Request (PR), espacio ARPDT, pagina `474635763949`, actualizada jul 2026.
- Code Review for Pull Requests, ARPDT, `474707591321`.
- Azure DevOps Permissions, ARPDT, `475770847254`. Define los grupos Secure y Approval y quien
  puede aprobar PRs.
- Azure DevOps, ARPDT, `1172807180`. Variable groups por entorno.
- Pull Request Review Checklist, espacio DO, `475092680745`. Version DataOps para SQL y Python.
- AI Use Case: Connecting Claude to Azure DevOps via MCP, espacio RTS, `477499654145`. Chenuka
  monto un MCP de ADO para leer PRs desde Claude.

## Decisiones

Ninguna cerrada. La sesion ofrecio guardar la tabla de links en `inbox/` y Juan no respondio. Este
archivo cubre esa oferta.

## Pendiente de verificar

Si Juan quiere el MCP de ADO montado para leer PRs directo en vez de pegar links. La pagina de
Chenuka describe el montaje y nadie lo probo en esta sesion.

Los grupos de permisos de Juan en ADO. La pagina existe, nadie verifico en cual grupo esta.

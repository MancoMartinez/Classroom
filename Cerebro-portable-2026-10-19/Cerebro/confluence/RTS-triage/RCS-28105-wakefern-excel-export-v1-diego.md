---
ticket: RCS-28105
cliente: Wakefern / Village Super Market (VSM-LPMS)
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS
sintoma: la descarga de reportes a Excel nunca completa despues de la migracion
causa: TaskExportController.Index devuelve el archivo con MIME text/csv hardcodeado y sin Content-Disposition, mas posible cambio de ruta de blob storage
fix: derivar el MIME de la extension y revisar GetRepoRootLocation("searchresultsexport")
version: 1 (la ficha del 5 de agosto firmada por Matthew Kamminga es RCS-28105-wakefern-excel-export-v2-kamminga.md)
pendiente_extra: el ticket original tambien reportaba errores subiendo .exe y no poder entrar al sitio, sin confirmar si siguen
confluence_id: 478143086594
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143086594
---

# RCS-28105 — Wakefern: VSM-LPMS Errors — Excel Download Failure

Prepared: 04 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28105 |
| Customer | Wakefern / Village Super Market |
| Issue Type | Incident |
| Priority | Medium |
| Status | WORK IN PROGRESS |
| Opened | 31 July 2026 |
| Reporter | Michael Marasco (michael.marasco@wakefern.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28105 |

## 2. Problem Statement

Wakefern / Village Super Market users are unable to download reports to Excel. When attempting to export, the browser shows a downloading indicator but the file never completes. This issue began following a recent platform migration. The ticket originally also included errors uploading `.exe` files and inability to access the site.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Wakefern / Village Super Market |
| Product | VSM-LPMS |
| Contact | Michael Marasco, LP Coordinator |
| Client ID | Not Available |
| Active Products | LPMS |

## 4. Investigation

### 4.1 Local Reproduction Attempt

PASS — Export completed successfully locally (non-Azure PlatformUI). The failure is specific to the Azure production deployment path.

### 4.2 Code Path Analysis — Azure Export Flow

POINT OF FAILURE FOUND — `TaskExportController.Index()` returns Excel file bytes with hardcoded MIME type `text/csv` (comment: `// hard code to csv for now`). No `Content-Disposition` filename header. Affects both PlatformUI (line 38) and legacy UI (line 44).

### 4.3 Cross-Client Scope Check

FAIL — Multiple clients affected with the same symptom post-migration. Framework-level issue in the download endpoint.

### 4.4 App Insights / Server-Side Log Check

FAIL — No access to production App Insights logs. Requires Engineering access.

## 5. Root Cause Statement

| Field | Value |
| --- | --- |
| What broke | `TaskExportController.Index()` — the file download endpoint for Excel exports |
| Why | MIME type hardcoded as `text/csv` for all file types; additionally, post-migration Azure blob storage path resolution may have changed |
| Scope | All clients on Azure deployment using the Excel export feature |
| Business impact | Admin users cannot download any Excel reports — a weekly workflow broken |
| Evidence | Code-confirmed hardcoded MIME in both UI versions; local test passed, prod-only failure |

## 6. Additional Findings

The original ticket description (2026-07-31) reported two separate issues also attributed to the migration: errors uploading `.exe` files to LPMS, and inability to access the site at all. Neither has been confirmed as resolved; the client's 2026-08-04 update focused exclusively on the Excel download failure.

## 7. Recommended Fix

### Option A — Fix MIME type in TaskExportController (Engineering required)

```
// BEFORE:
return this.File(content, "text/csv");
// AFTER:
string mimeType = Path.GetExtension(filePath).ToLowerInvariant() switch
{
    ".xlsx" => "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".xls"  => "application/vnd.ms-excel",
    _       => "application/octet-stream"
};
return this.File(content, mimeType, Path.GetFileName(filePath));
```

### Option B — Investigate Azure Blob Storage Path Post-Migration

Check App Insights for `/cpf/ssrexport/` errors, verify `GetRepoRootLocation("searchresultsexport")` resolves post-migration, confirm the file exists at download time, audit migrated tenants.

## 8. Open Questions

1. Does `/cpf/ssrexport/` throw an exception in production or return HTTP 200 with wrong MIME type?
2. Were the original `.exe` upload errors and site-inaccessibility issues resolved?
3. Is `GetRepoRootLocation("searchresultsexport")` correctly configured post-migration?
4. Which other clients are affected?

## 9. Queries Run

| # | Description | Result |
| --- | --- | --- |
| 1 | Traced the export code path | MIME type `text/csv` hardcoded confirmed |
| 2 | Local export test non-Azure | Passed — Azure-specific |
| 3 | Codebase search | Both UI and PlatformUI have the same bug |
| 4 | `GlobalConfigurationService.RunningInAzure` detection logic | Via entry assembly name or `SecureInAzure` env/config var |

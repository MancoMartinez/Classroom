---
ticket: RCS-28105
cliente: Wakefern / Village Super Market (VSM-LPMS)
analista: Matthew Kamminga
estado_ficha: WORK IN PROGRESS
sintoma: la descarga de reportes a Excel nunca completa despues de la migracion a Azure
causa: TaskExportController.Index devuelve el archivo con MIME text/csv hardcodeado y sin Content-Disposition, mas posible cambio de la ruta de blob storage post migracion
fix: derivar el MIME de la extension y devolver el nombre de archivo, y revisar GetRepoRootLocation("searchresultsexport") en Azure
version: 2 (hay otra ficha del mismo ticket firmada por Diego el 4 de agosto)
confluence_id: 478143283209
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143283209
---

# RCS-28105 — Wakefern / Village Super Market: VSM-LPMS Excel Export Download Failure

Prepared: 05 August 2026 | Analyst: Matthew Kamminga | Status: WORK IN PROGRESS

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
| Assignee | Matthew Kamminga (mkamminga@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28105 |

## 2. Problem Statement

Wakefern / Village Super Market admin users are unable to download reports to Excel from LPMS. When attempting to export, the browser shows a downloading indicator but the file never completes. This issue began following a recent platform migration to Azure. Client confirmed (2026-08-04) that the export originates from Izenda reports / standard search results. Prior to the migration, the admin performed this export weekly without issues.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Wakefern / Village Super Market |
| Product | VSM-LPMS (Loss Prevention Management System) |
| Contact | Michael Marasco, LP Coordinator |
| Client ID | NOT AVAILABLE |
| ARDM Version | NOT AVAILABLE |
| Active Products | LPMS |

## 4. Investigation

### 4.1 Local Reproduction Attempt

PASS — Export completed successfully in local environment (non-Azure PlatformUI). Issue is not reproducible outside Azure.

### 4.2 Code Path Analysis — Azure Export Flow

POINT OF FAILURE FOUND — Traced `ResultsController.ExportSearchAsync` to HATR task to `AzureExcelFileWriter` to `TaskExportController` under `RunningInAzure=true`. `TaskExportController.Index()` returns Excel file bytes with hardcoded MIME type `text/csv`. Code comment reads literally: `// hard code to csv for now`. No `Content-Disposition` filename header is set. Both versions are affected:

* `Sources\UI\PlatformUI\Areas\Cpf\Controllers\TaskExportController.cs` line 38
* `Sources\UI\UI\Areas\Cpf\Controllers\TaskExportController.cs` line 44

### 4.3 Cross-Client Scope Check

FAIL — Multiple clients affected with the same symptom after the Azure migration. Pattern is consistent with a framework-level issue in the download endpoint, not a Wakefern-specific misconfiguration.

### 4.4 Export Type Confirmation

PASS — Client confirmed export attempted from standard searches / Izenda reports.

### 4.5 App Insights / Server-Side Log Check

FAIL — No access to production App Insights logs. Cannot determine whether the endpoint throws an exception (e.g., blob storage path not found post-migration) or returns HTTP 200 with the wrong MIME type. Requires Engineering escalation.

## 5. Root Cause Statement

| Field | Value |
| --- | --- |
| What broke | `TaskExportController.Index()` — the file download endpoint for Excel search exports |
| Why | MIME type hardcoded as `text/csv` for all file types; additionally, post-migration Azure blob storage path resolution (`GetRepoRootLocation("searchresultsexport")`) may have changed, causing read failures before the response is written |
| Scope | All clients on Azure deployment using the Excel export feature; surfaced after the recent platform migration |
| Business impact | Admin users cannot download Excel reports — a previously weekly workflow completely broken |
| Evidence | Code-confirmed: `return this.File(content, "text/csv")` with comment `// hard code to csv for now` in both `UI` and `PlatformUI`. Local test passed; prod-only failure indicates an additional Azure-specific factor |

## 7. Recommended Fix

### Option A — Fix MIME type in TaskExportController (Engineering required)

```
// BEFORE (bug):
return this.File(content, "text/csv");
// AFTER (fix):
string mimeType = Path.GetExtension(filePath).ToLowerInvariant() switch
{
    ".xlsx" => "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".xls"  => "application/vnd.ms-excel",
    _       => "application/octet-stream"
};
return this.File(content, mimeType, Path.GetFileName(filePath));
```

### Option B — Investigate Azure Blob Storage Path Post-Migration (Engineering required)

1. Check App Insights for the Wakefern tenant — errors on `/cpf/ssrexport/`.
2. Verify `GetRepoRootLocation("searchresultsexport")` resolves correctly in Azure post-migration.
3. Confirm `AzureExcelFileWriter` writes files to blob storage and the file exists at download time.
4. Audit all affected migrated tenants.

## 8. Open Questions

1. Does `/cpf/ssrexport/` throw an exception in production or return HTTP 200 with wrong MIME type?
2. Is `GetRepoRootLocation("searchresultsexport")` correctly configured post-migration?
3. Which other clients are affected?
4. Does the failure affect all export types or only Excel/Izenda?

## 9. Queries Run

| # | Description | Result |
| --- | --- | --- |
| 1 | Traced the export code path | MIME type `text/csv` hardcoded confirmed |
| 2 | Local export test (non-Azure mode) | Passed — issue is Azure-specific |
| 3 | Codebase search for TaskExportController / ssrexport | Both `UI` and `PlatformUI` have the same MIME type bug |

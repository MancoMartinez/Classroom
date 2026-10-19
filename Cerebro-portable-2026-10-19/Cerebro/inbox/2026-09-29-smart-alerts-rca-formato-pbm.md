# Smart Alerts RCA adaptado a la plantilla PBM

Borrador PBM: https://trebuco.atlassian.net/wiki/spaces/PBM/pages/edit-v2/478256037890
Fuente: inbox/2026-09-29-smart-alerts-rca-internal.docx
Cada bloque va en su celda de la plantilla. Juan pega, el agente no escribe en Confluence.

## Encabezado

Root Cause Analysis Report    September 29, 2026

Smart Alerts Processing Failure, September 2026. Secure Incident Smart Alerts, cohesion mode.

## Campos

Incident start time
September 24, 2026 04:06AM PT. Last confirmed completed ADUSA run. Exact onset is unconfirmed.

Incident end time
September 28, 2026 11:30AM PT. ADUSA reported alerts arriving again. Vitamin Shoppe confirmed a test alert at 01:42PM PT.

Duration
4 days, 7 hours. Approximate reference window, not a verified continuous outage.

Ticket #
PBM-____. Related: RCS-29123, RCS-29145, RCS-29026, ENG-9486.

## Incident Description

ADUSA and Vitamin Shoppe reported missing Smart Alert notifications and missing alert history in Secure Incident, cohesion mode. Some emails reached recipients while application processing failed to finish. Affected cases stayed flagged as in process, which blocked later alert attempts on those cases. The September 28 correction restored processing for new activity in the validated examples.

This report covers the shared regression introduced by the September release. A September 20 nonreceipt report for Food Lion case 0619-27 is tracked separately. That run completed and recorded history, and current evidence does not tie it to this regression.

## Timeline. Time column in PT. September dates fall in PDT, UTC-7.

Sep 20, 2026 | 07:12AM PT approx. | Food Lion case 0619-27 records completed alert processing. The reported nonreceipt remains a separate open item.
Sep 24, 2026 | 04:06AM PT | Last confirmed completed ADUSA alert run. Exact onset is unconfirmed. The configuration change from PR 57544 reached production around this date.
Sep 24, 2026 | 01:20PM PT approx. | Support identifies the first missing-history example.
Sep 25, 2026 | 05:47PM PT | Support publishes log analysis: 89 Begin entries, zero End entries and 76 in-process exits in the sampled window. Queue count rises from 217 to 222.
Sep 27, 2026 | 04:17AM PT | RCS-29123 escalated from Medium to High. On-call acknowledges at 04:28AM PT.
Sep 27, 2026 | 11:33AM PT | ADUSA reports its workaround: extra staff run reports and send manual leadership emails. One alert reportedly arrived five times.
Sep 27, 2026 | 03:30PM PT | Infrastructure finds eight of nine listed subjects in provider logs. Case 0143-14 is absent. This rules out a full email transport outage.
Sep 27, 2026 | 06:39PM PT | Engineering records the fix in ENG-9486: ConfigureAwait(False) on both Await calls.
Sep 28, 2026 | 07:38AM PT | Manual QA task ENG-9533 moves to Done.
Sep 28, 2026 | 09:43AM PT | Engineering starts deployment.
Sep 28, 2026 | 11:30AM PT approx. | ADUSA reports alerts arriving again.
Sep 28, 2026 | 12:36PM PT | ADUSA case 1600434 completes processing with step 13b, a SmartAlertProcess row and an End entry.
Sep 28, 2026 | 01:42PM PT | Vitamin Shoppe confirms receipt of a test alert.

## Business Impact

ADUSA reported disruption to critical incident communications across Asset Protection, Operations and Legal for at least two brands, and covered the gap with manual reports and emails. Vitamin Shoppe reported failed incident notifications. Engineering identifies exposure across all cohesion-mode customers with active Smart Alerts. The confirmed customer examples do not measure that full population.

The count of missed, duplicate and delivered notifications is still unknown. Missing SmartAlertProcess rows do not equal undelivered mail. No evidence shows loss of underlying incident records. Confirm data integrity and the unrecovered notification backlog before any no-data-loss statement.

## Resolution Provided

Immediate: Engineering manually retriggered selected ADUSA cases and Infrastructure checked provider delivery. This recovered some notifications and left the defect in place.

Short term: PR 58273 adds ConfigureAwait(False) to both Await calls in the email routine. Engineering confirms deployment to EU and US. ADUSA case 1600434 shows step 13b, a SmartAlertProcess row and an End entry at 12:36PM PT on September 28. Vitamin Shoppe confirmed a received test alert. Neither result validates every tenant or the EU environment.

Long term: QA automation ENG-9589 is in Backlog with a Q4 2026 planning field. No delivery date or preventive monitoring is committed yet.

Historical records: the fix works forward only. ADUSA asked on September 28 not to resend its backlog. Engineering confirmed that historical recovery is manual and that saving a case with InProcess = 1 does not trigger an alert. Behavior after a flag reset or a later edit needs its own recovery decision.

## Root Cause Analysis

PR 57544 for ENG-7181 set targetFramework="4.8" in the ASP.NET httpRuntime configuration around September 24. That setting enabled the modern ASP.NET synchronization context. SendGridEmail.vb awaited the provider call without ConfigureAwait(False), so its continuation captured that context. SmartAlert.vb blocked the request thread synchronously through GetAwaiter().GetResult(), and the continuation could not re-enter the blocked context. The result was a deadlock.

The provider could send the email before the deadlock. Execution then never reached step 13b or the SmartAlertProcess insert, and IIS could return HTTP 500. The fix lets both continuations resume without capturing the blocked context. It does not serialize alert runs or address an ADUSA capacity limit. Earlier internal and customer explanations that described those mechanisms need correction.

Oversized emails, malformed recipient addresses, duplicate recipients and incorrect alert filter assumptions are tracked separately. None of them explains the shared post-release deadlock.

Systemic cause, open for the retrospective: why release validation and monitoring did not catch this interaction before customers did.

## Next Steps

1. Confirm rollout completion times per environment and validate representative EU and US tenants end to end. Owner: Engineering and Support. Target: retrospective.
2. Reconcile eligible alerts, provider delivery and stuck processing states before any customer-approved recovery. Owner: Support and Engineering. Target: retrospective.
3. Add regression checks for runtime configuration changes, email completion, history insertion and flag cleanup. Owner: QA, ENG-9589. Target: Q4 2026, commitment pending.
4. Add monitoring for stalled completion, separate from delivery failure, and retain provider evidence. Include the size-error follow-up with Vlad and Russ. Owner: Engineering and Infrastructure. Target: retrospective.
5. Hold the retrospective by October 1, 2026 06:52AM PT and deliver the final RCA by October 2, 2026. Owner: Juan Martinez.

## Lo que quedó fuera de la plantilla

La plantilla no tiene worksheet de 5 Whys, proceso PBM ni registro de fuentes S1 a S6 y P1 a P4. Siguen en el docx de origen para la reunión.

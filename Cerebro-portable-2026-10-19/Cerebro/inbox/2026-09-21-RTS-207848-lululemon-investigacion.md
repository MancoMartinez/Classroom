RTS-207848 | 2026-09-21 | Investigación y email draft
Borrador no enviado. Sin ETA ni verificación operativa en vivo. Recuperación no implica prevención definitiva. Juan ingiere con cerrar.
Fuentes: comentarios 3352388/3352399 de https://trebuco.atlassian.net/browse/RTS-207848; fix en https://trebuco.atlassian.net/browse/RTS-207427; antecedentes RTS-206318, RTS-206749, RTS-206998 y RTS-207875.
Pendientes: prevención GP3/timeout y reproceso JSON. SAS y fix SQL confirmados; ver notas en inbox.

Subject: lululemon data delays: findings and next steps

Hi team,

We understand your concern about repeated data delays and the need for a lasting resolution.

Our review shows that several recent incidents affected the same data processing pipeline, ARDMTRK, but involved different failures. These included a processing step failing to execute, a timeout when retrieving exchange rates, a SQL processing limit, and the September 18–19 GP3 database infrastructure incident affecting multiple customers.

The alerts use a common format, including “Active Alerts: N,” which identifies the number of active alerts rather than the underlying cause. Similar subjects therefore do not establish that the same defect has returned. We will match your notifications to the incident records to ensure full coverage.

For the latest incident, RTS-207848, the recovery records confirm that database service and processing were restored, and lululemon data had loaded through September 18. For the September 11 SQL error, the fix succeeded and its author confirms it applies to every subsequent run. These confirm recovery of those incidents; we cannot yet confirm that all causes of recurrence have been permanently eliminated.

Peyman confirms that SAS licenses expired on August 21 and all SAS scripts have since been removed from the current code. He also confirms that the issues associated with moving processing from LA4 to Azure have been addressed and are not expected to recur in the current setup.

Processing resumed from the exchange-rate step once connectivity returned. Earlier ecom files failed JSON validation and may still need correction and reprocessing. We are verifying the affected files before requesting any resend. GP3 preventive actions remain under review.

We will consolidate confirmed causes, completed and outstanding actions, owners, target dates and validation criteria. Timelines will follow confirmation from the technical owners.

Best regards,
Juan

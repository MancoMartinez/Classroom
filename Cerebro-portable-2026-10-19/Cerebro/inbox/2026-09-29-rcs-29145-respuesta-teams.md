Hi Colleen,

Here is the confirmed update on [RCS-29145](https://trebuco.atlassian.net/browse/RCS-29145) for Vitamin Shoppe.

- **Status: Resolved.** Vitamin Shoppe opened the High priority ticket on September 28, and we resolved it that same day after Joe confirmed his test alert was working. I also shared the cause with him in the ticket.

- **Root cause:** [ENG-9486](https://trebuco.atlassian.net/browse/ENG-9486) identifies an interaction between the September release’s .NET 4.8 configuration change and the email code. The code could send an email, then hang before recording completion. This left alert processing incomplete and could block subsequent attempts. Vitamin Shoppe showed the same failure pattern as the related investigation in RCS-29123.

- **Corrective action:** Engineering added ConfigureAwait(False) to the email code to prevent this deadlock. The fix, [PR 58273](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/Secure/pullrequest/58273), reached US production on September 28. The linked manual QA task, [ENG-9533](https://trebuco.atlassian.net/browse/ENG-9533), is Done.

- **Timeline:** On September 28, the ticket opened at 12:20 PM EDT. Support acknowledged it at 12:21 PM, and I took ownership at 1:05 PM. After deployment, I requested validation at 4:34 PM; Joe confirmed his test at 4:42 PM.

- **Reported impact:** In his September 28 report, Joe estimated that the issue began around September 23. The exact onset remains unconfirmed in logs. The fix does not automatically resend missed alerts or clear previously stuck cases; any recovery requires a separate manual review and reprocessing.

- **Prevention and follow-up:** The code fix addresses this deadlock, and manual QA is complete. The automation follow-up, [ENG-9589](https://trebuco.atlassian.net/browse/ENG-9589), is in Backlog. Its implementation date and the formal RCA delivery date still need confirmation.

Colleen, this gives you the confirmed cause, recovery and remaining follow-up for your conversation with Joe.

<!-- Borrador, no enviado. Verificado 2026-09-29: RCS 7/7 comentarios; tres ENG sin comentarios. ENG-9486 Development Complete. Sustituye explicación previa de serialización. Vista copiable: adjuntos/RCS-29145/teams.html. -->

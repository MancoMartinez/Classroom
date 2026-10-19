Facteus, correo consolidado para Chris y Sadam, seis preguntas de la llamada con L1

Fecha 2026-10-07. L1, con Santhosh y Shreyas, tuvo su primera sesión hoy con Viraj para asumir el monitoreo diario de Facteus. Salieron estas preguntas, las juntamos en un solo correo para no mandarlas sueltas.

Texto para el hilo:

```
Hi Chris, Sadam,

We had our first walkthrough with L1 today, Santhosh and Shreyas plus Viraj, to get them set up to
monitor Facteus alerts day to day. A handful of questions came out of it, bundling them here instead
of sending them one at a time.

The Missing Clients alert template references a customer label and a drop_ratio value, but we never
got the actual threshold that triggers the alert, both the drop_ratio number and how far past the 26
hour staleness window counts as a real issue. This one's been open since our first review in
September, L1 needs it to tell a real alert from noise.

L1 asked for a short article per alert type, how to confirm the alert is real, which monitoring tool
to check, whether L1 can resolve it on their own or needs to escalate, who to escalate to, within
what timeframe, how often to follow up if there's no response, and what SLA applies. Right now that
doesn't exist anywhere, would help a lot for L1 to have it before they're handling this live.

If a client hasn't sent data for a day or two, when L1 notifies the team, should they name which
client it is or keep it generic, just flag that there's an issue? Wasn't obvious from the docs.

Is there a specific named point of contact for escalating to Data Engineering, rather than the team
in general? L1 wants to know who to reach out to directly.

Which Teams channel actually receives the Facteus alerts, Data Issues or Data Engineering Alerts?
L1 doesn't currently have access to the Data Engineering channel, so whichever one it is, we may need
that sorted out too.

Last one, the documentation mentions this was supposed to go live end of September, we haven't seen
any RCS or RTS tickets come through yet. Just checking whether that's expected or if something's
holding it up.

Thanks,
Juan
```

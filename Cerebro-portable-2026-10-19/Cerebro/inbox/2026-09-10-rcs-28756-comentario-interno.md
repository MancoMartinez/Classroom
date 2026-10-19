Madhuraj, Ayesha, here is the answer for Nike. The text to send them is below the line, ready to go as is.

On what is safe to share: their endpoint and OAuth credential are already theirs from onboarding, so confirming the delivery method adds no exposure. Keep the Event Hub namespace, the hub name, the numeric client ID, blob paths and config keys internal. Those are ours and add nothing for them.

One thing to fix in how the question was framed. Nike assumes we consume a stream on their side. We do not, they publish to us. The consumer client ID they are asking about is their own.

Still open on our side: whether their posts reached our ingestion API after 2026-08-27 19:02 UTC. Event Hub incoming and captured messages are both at zero since then, which rules out anything downstream of the hub. It does not tell us whether their calls were rejected at the API. The API returns 401 resultCode 12 on an OAuth identity mismatch and 400 resultCode 11 on a data type not in the allowed list, and either case looks exactly like this from the hub metrics. I have asked Data Engineering for the inbound logs for that window. That is also why the reply asks Nike for the response codes their side received.

Send the text below as is. Do not add the timestamp in any other timezone, we agreed on a single one.

--------------------------------------------------

[pegar aqui el contenido de inbox/2026-09-10-rcs-28756-respuesta-nike.md]

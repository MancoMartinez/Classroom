# INTERNAL NOTE. NOT FOR CUSTOMER

Environment: production, on-prem NEXCOM tenant, APIS 270 UI. Repro steps on record in this ticket, 10 and 16 Sep. Live working session with the customer, 30 September, recording and HAR attached to the ticket at 15:34.

## Findings

- verified by me, live session, 30 Sep, from the HAR. The request for admin_config_form.asp?recID=576 got a response in 3.64s, then the server took **1268.2s, about 21.1 minutes**, to stream the 1.19MB body. Total 1271.9s, status 200, not an error.
- verified by me, same HAR. Two unrelated requests on the same browser session, evidence_download.asp and fetch_custom_css.asp, independently waited about 1268s for a server response and both resolved within seconds of the 576 request finishing.
- verified by me, watching live. The browser stayed responsive, DevTools and Network kept updating. Server side stall, not browser render thread blocking as my earlier note assumed.
- verified by me, live. Carlo mentioned he has a larger audit coming and expects the same behavior past some size threshold.

## Troubleshooting performed

Claude parsed the HAR after the call and flagged the pattern across the three stalled requests. I ran the working session myself with the customer on 30 Sep and watched DevTools directly. Could someone evaluate whether admin_config_form.asp holds a session level lock while generating output for large templates, classic ASP serializes requests sharing a session, and whether that explains why unrelated requests from the same session stalled together. Also check whether the missing AUDIT.STATUS.1 and .3 labels from my 22 Sep note add a per field delay in a large combined form.

## Ruled out

| Hypothesis | Refutation |
|---|---|
| Browser render thread blocking | TTFB was 3.6s, the delay is server side receive, DevTools stayed responsive |
| Session cookie lost | Fresh incognito login straight to 576 still hung the same way, 23 Sep |
| Edge timeout at 100s | Holds over 21 minutes, ends in 200, no 504 or 524 |

## Still open

1. Does admin_config_form.asp hold a session lock while streaming, explaining why unrelated requests from the same session stall together.
2. Why does generating this template take over 21 minutes server side when the first byte arrives in 3.6s.
3. Does the missing AUDIT.STATUS label pair add per field delay here.

Customer asked for an ETA today, over two weeks since opened, flags a bigger audit that may hit the same wall. **Priority review requested.**

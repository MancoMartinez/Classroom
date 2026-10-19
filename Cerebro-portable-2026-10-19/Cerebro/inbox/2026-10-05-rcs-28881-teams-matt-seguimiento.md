Hey Matt, yes. Server side stall, not a browser hang. HAR from the live session shows admin_config_form.asp taking 21 minutes to stream its response, and two unrelated requests from the same browser session stall in sync with it, points to a session lock in classic ASP, still unconfirmed. Full writeup and the HAR are on RCS-28881, assigned to you since Oct 2.

https://trebuco.atlassian.net/browse/RCS-28881

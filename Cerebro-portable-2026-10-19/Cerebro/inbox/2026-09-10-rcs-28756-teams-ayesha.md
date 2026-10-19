Hi Ayesha, here is what we can safely share and what we should keep internal.

Safe to share: that they deliver over an authenticated POST to our ingestion API, that routing on our side depends on payload size, that we apply no content filters, and the response codes their side receives. They already hold their endpoint and their OAuth credential from onboarding, so none of that is new to them.

Keep internal: the Event Hub namespace and hub name, their numeric client ID, blob paths, config keys and log code names. Those are our infrastructure and add nothing for them.

One correction worth making in the reply. Their question assumes we consume from a stream of theirs. We do not, they publish to us. The consumer client ID they are asking about is their own OAuth client ID, not ours.

I am putting the full five-point answer together now and will post it on the ticket.

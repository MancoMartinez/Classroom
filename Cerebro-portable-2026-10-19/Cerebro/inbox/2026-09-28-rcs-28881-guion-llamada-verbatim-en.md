Hi Carlo, thanks for making time for this. Before we get started, I want to record this call and also record your screen, so I have full evidence to hand to engineering. Are you okay with that?

[wait for yes]

Great. Could you share your full screen for me, not just one tab? I want to be able to see the whole browser and anything Chrome pops up.

[wait]

Perfect. First thing, could you open a new Chrome incognito window? On Windows that is Control, Shift, N at the same time. On Mac it is Command, Shift, N.

[wait]

Now, from that incognito window, go ahead and sign in to APIS like you normally would.

[wait]

Before you click into form 576, I need you to open Chrome's developer tools. You can press F12, or right click anywhere on the page and choose Inspect.

[wait]

You should see a panel open, usually on the right or the bottom. At the top of that panel there are tabs. Click on the one that says Network.

[wait]

In that Network tab, look for two checkboxes, one says Preserve log and the other says Disable cache. If you see them, go ahead and check both.

[wait]

Now click on the tab next to it that says Console.

[wait]

I am going to send you a line of code in the chat right now. Could you paste that into that Console box for me?

[send the snippet in chat, wait for him to paste it]

setInterval(() => { document.querySelectorAll('frameset').forEach(f => { if (f.getAttribute('rows') && f.getAttribute('rows').startsWith('90')) f.setAttribute('rows', '50%,10%,10%,10%,10%,10%'); }); }, 500);

Go ahead and press Enter after you paste it. Chrome might ask you to type the words allow pasting first, if it does, just type that and press Enter, then paste the code again.

[wait, confirm it ran]

Perfect, that is going to keep some hidden parts of the page visible for us the whole time, so we can see if anything shows up there while the page is stuck.

Now, whenever you are ready, could you start recording your own screen too? Whatever tool you normally use is fine. Once that is rolling, go ahead and click into Audit Center, then Templates, then Annual Ops Slash Services Review, and click on form 576.

[wait]

Once you click it, please do not click anything else. Do not refresh, do not click the audit again, even if it looks completely frozen. I know that is going to feel strange, but touching it resets what we are trying to capture.

This is going to take between eight and ten minutes before anything happens, either the page finally loads or Chrome shows you a message that the page is not responding. So we are just going to sit here quietly for a bit, and that is completely normal, do not worry about the silence.

[wait 8 to 10 minutes]

Okay, now that it has loaded, or now that Chrome is showing the not responding message, go ahead and stop your recording.

One last thing. Go back to that Network tab, right click anywhere in the list of requests, and look for an option that says Save all as HAR with content. Click that and save the file.

Once you have that, could you send me three things whenever you get a chance? The recording, that HAR file, and one screenshot of whatever is showing in that thin strip at the bottom of the page from the developer tools.

Thank you so much for walking through this with me, Carlo, this is going to help a lot when I hand this to engineering.

If that strip disappears on its own at any point, just have him run that same command one more time from the Console tab, not by editing the code directly. That is what worked last time.

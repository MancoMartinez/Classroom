# Before you start

Ask permission to record the call, and let Carlo know you will also need him to share his full screen, not just one tab, so any Chrome popup stays visible. State the goal in one line: getting video, network, and console together so engineering can act without another round of tests.

# Step by step for Carlo, in order

1. Share full screen.
2. Open a new Chrome incognito window, Ctrl+Shift+N, or Cmd+Shift+N on Mac. That rules out any leftover session cookie.
3. Sign in to APIS production from that window.
4. Before clicking into form 576, open DevTools, F12 or right click, Inspect.
5. Go to the Network tab and check Preserve log and Disable cache if you see them.
6. Go to the Console tab, so any error in red stays visible.
7. In Console, paste this and press Enter. It may ask you to type "allow pasting" first, that is normal:

setInterval(() => { document.querySelectorAll('frameset').forEach(f => { if (f.getAttribute('rows') && f.getAttribute('rows').startsWith('90')) f.setAttribute('rows', '50%,10%,10%,10%,10%,10%'); }); }, 500);

This keeps the hidden strips visible from the start and stops them from reverting on their own, which happened last time when edited directly in Elements.

8. Start screen recording, or confirm you are recording the call yourself.
9. Navigate to Audit Center, Templates, ANNUAL OPS/SERVICES REVIEW, and click form 576.
10. Do not touch anything else. No re-clicking, no refreshing, even if it looks stuck.
11. Let it run until one of two things happens, the page loads or Chrome shows the page as not responding. That is 8 to 10 minutes, so let Carlo know that stretch of the call will be quiet.
12. Do not minimize or switch tabs while waiting, so the DevTools strip stays in the recording.

# When it is done

13. Stop the recording.
14. In Network, right click any row, Save all as HAR with content. That file is the strongest evidence for engineering.
15. Have him send the HAR, the video, and one final screenshot of the bottom strip in DevTools.

# If step 7 does not hold

If the value snaps back to 90 percent right after changing it, have him run the same command again from Console, not by editing the attribute directly in Elements. It held last time through Console, it reverted on its own through Elements.

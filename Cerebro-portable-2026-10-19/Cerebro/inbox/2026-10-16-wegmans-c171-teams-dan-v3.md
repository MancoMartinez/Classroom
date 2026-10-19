# Mensaje de Teams para Dan y Shireesh, C171_WEG, v3

Sustituye a inbox/2026-10-16-wegmans-c171-teams-dan-v2.md, que queda obsoleto. Agrega promedio por día y mensuales, y baja "no defect" a lo verificado. Formato markdown de Teams. Cifras verificadas con SELECT el 16 oct.

---

Hi Dan, Shireesh,

Short answer: the Oct 15 duplicates come from one definition that re-scans the last 10 days on every run, and they match how it is built. No failures.

**Last month vs this month**, from the Platform DB, matches Shireesh's table:
- September, 30 days: 129 results, 57 generated, 72 duplicates, 2.4 per day
- October 1 to 15: 76 results, 35 generated, 41 duplicates, 2.7 per day
- Duplicate share: 56% and 54%. Failures: 0 in both

**Monthly work items:** September had 2 monthly runs, 0 failures, 1 work item generated, 0 duplicates. There is no October monthly run yet. I assume it runs once the month closes, is that right?

**Why Oct 15 reached 9 duplicates**
- *gift cards purchased with lower trans amount* looks back 10 days on every run, so a flagged ticket returns as a duplicate on each run until it leaves the window
- On Oct 14 it created 5 new work items. On Oct 15 those 5 came back as duplicates, plus 3 older ones, which gives 8. One more comes from *8020 coupons with trans less than 5 by cc*, which repeats 1 per day

**Is it an outlier?** It is the highest day since Sep 1, the September maximum was 4. It follows the 5 new items of Oct 14, not a change in behavior.

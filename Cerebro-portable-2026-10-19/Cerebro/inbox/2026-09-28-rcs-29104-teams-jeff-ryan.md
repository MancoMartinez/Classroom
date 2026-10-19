Sure. Summary for RCS-29104, GPC 356:

What happened: GPC sends each order as a set of 3 files: order, line items and tender. Since 5/4 they often re-send an order a day later with only order and line items, and that replaces the complete one without its tender. About 40% of GPC transactions since 5/4 have no tender in Secure. Example: the 9/18 tender file has 545,902 lines and only 318,705 ended up loaded. GPC found it while investigating refund fraud they could not see in Secure.

What needs to be done:
1. GPC needs to go back to sending the full set of 3 files every time, as agreed at onboarding. Kristen Dyer is checking with them.
2. The data since 5/4 needs a reload from Archive. Przemysław outlined the approach: load several days together, drop incomplete orders before the rest of the scripts, and process week by week. Peyman offered to support whoever takes it.

Przemysław also mentioned he is leaving at the end of October, so it would help if the person who takes this could get a quick walkthrough from him before then.

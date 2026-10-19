# SnowTime RCS Root Cause Review

Fuente: PDF SnowTime_RCS_Root_Cause_Review.pdf, preparado por Adarsh Kumar con Sumeet Jain, 42 tickets RCS de 15 clientes migrados, verificado contra Jira el 18 sep 2026. Compartido al equipo de Support el 15 oct 2026. Texto extraido del PDF, sin cambios.

SnowTime RCS Root Cause Review
42 RCS tickets across 15 migrated clients, collected from the SnowTime engineers and verified against Jira comments on 18 Sep 2026. 41 of 42 tickets
verified (RTS-207681 sits in a tenant we could not open). Two internal migration stories (AZO, DSG) are excluded because they are not support tickets.
Prepared by Adarsh Kumar for review with Sumeet Jain.

1. What is common across clients
Four patterns explain all 42 tickets. The first two are ours to prevent; the third needs the client; the fourth is not a SnowTime issue.
 Root cause              Tickets       What went wrong                                  How it was resolved                       What support can try next time
 pattern
 1. Migration            19 of 42      Logic that the legacy load (pyardm) had          dbt mapping or enrichment fix,            If a field is blank or a count is zero
 mapping gap-            ALA 7,        was not carried into SnowTime, or was            deployed going-forward. History           for every row since the cutover
 SAME                    WCO 2,        wired to the wrong column. Examples:             repaired by a targeted repair script      date, treat it as a mapping gap.
 CATEGORY                BFV, FAD,     Cancel transactions never built for              or a backfill. In 8 cases the first fix   Say it as: legacy showed X,
                         KFC, WTR      Simphony (ALA), header split-item totals         was going-forward only and the            Secure does not, since <date>.
                         3, ICA,       left at zero (ALA), Penny Rounding               customer came back for history.           Check the value in ARDM before
                         TGJ, THD      tender code not mapped so it showed as                                                     the report. For a client with repeat
                                       Unknown (WCO), customer number                                                             gaps (ALA had 6), ask
                                       written to an extension column instead of                                                  engineering for one full flag and
                                       the standard one (FAD), RLPM                                                               count coverage audit instead of
                                       hardcoded to null (BFV).                                                                   fixing one field per ticket.
 2. Feed timing          7 of 42       A column needs two feeds that land at            Persist the slower feed into a            Ask which feeds fill the field and
 mismatch- SAME          TJE 2,        different times (daily token file vs hourly      reference table or use lookback           when each one lands. A column
 CATEGORY                KFC 2,        POS, loyalty file 1 to 2 days after the          enrichment, add a self-healing            that is partly or intermittently blank
                         MKS, OLS,     transaction, hierarchy file vs store             predicate so late rows get re-            (not 100%) usually points here.
                         BFV           master). The hourly build window only            enrolled, then backfill. TJE residual     Put the feed name and its arrival
                                       sees one side, so the join returns               work is still open (PR 57102, 68 of       time in the ticket.
                                       nothing and the row is never revisited.          123 stores still affected on 16 Sep).
                                       TJE card numbers showed as 9 on 67%
                                       of tenders; KFC loyalty ID was 100% null
                                       since go-live.
 3. Client source        10 of 42      Either the client file is wrong (double          Client-side issues routed back to         Trace the field back to the raw file
 data or unusual         ALA 2,        hyphens in item IDs, duplicate ticket            the client (hyphens, GUIDs, card          first. If the anomaly is in the file as
 format                  SBY, KFC,     numbers, 3 days of empty staff-discount          token). Format issues fixed with a        delivered, it is a client fix. Known
                         GUE, BFV,     stubs, GUIDs where a transaction                 guard: TRY_TO_DATE,                       signatures: a 1970 date means a
                         ICA 3, TGJ    number should be, one corrupt XML file)          CONTAINS check for prefixed               numeric string cast as epoch; a
                                       or the format tricked the parser (6-digit        XML, per-row parse safeguard,             suspended task with a
                                       date read as a Unix epoch so every row           drop empty stub rows, plus history        PARSE_XML error means one
                                       became 1970, XML tags with a                     cleanup.                                  bad file; a flag-rate spike on
                                       namespace prefix that XMLGET cannot                                                        specific dates means a POS-side
                                       see).                                                                                      change.
 4. Outside              6 of 42       Data was complete in ARDM but the                Routed to the platform or app team; Confirm the data exists in ARDM
 SnowTime scope          THD 3,        issue sat elsewhere: platform work items         requests handled as                 first. If it does, route to platform or
                         FAD, ALA      generated before data existed, hierarchy         enhancements.                       app. Display labels and receipt
                         2             configured with an extra level, Secure                                               templates in Secure are platform-
                                       app filter bug, receipt template pointing                                            side, not pipeline.
                                       at the wrong model field, or a new-
                                       feature request (add a column, new
                                       BNPL tender group).


2. Per client
 Client             Tickets        Common root cause                                     How it was resolved                            Status (Jira, 18 Sep)
 ALA Alshaya        14             Mapping gaps in header flags and counts on            Fixes in ff_ardm_header_items,                 9 resolved, 5 open (KD rate,
                                   Micros and Simphony feeds (6 tickets: split-          int_header_base and map_ardm_item,             duplicates, EC backfill,
                                   sale flag, split totals, error-correct count, void    deployed going-forward; customer               BNPL, article ID column)
                                   count, cancel transactions). Tender reference         confirmed. Backfill still pending on 3
                                   gaps (Unknown tender type, new BNPL                   tickets. Discount fix (PR 56654) in prod,
                                   group). Two source-data issues (hyphens,              history rebuild pending.
                                   duplicate tickets). One discount netting bug
                                   (rolled discount on one line, 466%).
 GUE Guess          1              Same Tender Card link matches on a masked Options under engineering review; not a                    Open
                                   last-4 fallback, so unrelated cards collapse   SnowTime regression.
                                   together. Same behaviour as legacy; real fix
                                   needs a stable card token from the client POS.
 TJE TJX            2 (+1          Adyen token file lands daily, ahead of the POS Tokens persisted to a reference table,                1 closed, 1 open
 Europe             ENG)           tenders; hourly window read an empty flat      overlay fixed (99% of 1.19M rows). Self-
                                   table, so card numbers stayed as 9.            healing PR 57102 and backfill still
                                                                                  pending.
 KNY Kinney         1              INVENTORY_DOCUMENT history missing                    Full history reloaded, key fixed.              Customer review
                                   after an Aug schema change with only a
                                   partial backfill, so vendor and invoice fields
                                   were blank on old records.
Client         Tickets    Common root cause                                   How it was resolved                         Status (Jira, 18 Sep)
TGJ TG Jones   1          Price-override annotation used a catalogue     PR 57385 released 10 Sep, verified 15            Customer review
                          price whenever a tax field was zero, so 82% of Sep. Historical rebuild not scheduled.
                          override notes were phantom. Money cast
                          rounded to whole pounds.
BFV Big 5      2          Date string YYMMDD cast as epoch, every             TRY_TO_DATE fix plus repair of 10,414 Both closed
                          inventory adjustment landed on 1970-01-04.          rows. RLPM populated from SSO
                          RLPM column hardcoded null at onboarding.           master, history repaired.
FAD Floor &    1          Customer number written to extension column         Data side fixed and 515K rows patched.      Open
Decor                     only; receipt template also read the wrong          Receipt fix waiting for the 24 Sep
                          field.                                              platform release.
MKS M&S        1          Hierarchy file and store-master file arrive on      Hierarchy-only UNION arm added,             Open
                          different cadences; 86% of hierarchy                repair script ready; extract load with
                          deliveries were dropped.                            ingestion team in progress.
OLS Ollie's    1          Refund-with-receipt flags stuck false because       Lookback enrichment plus history            Open
                          the original receipt arrives in a later batch.      correction; remaining Secure 5 items
                                                                              split into 5 new tickets.
WCO WinCo      2          Emerald tender id 999 had no CASE branch            999 branch added (going-forward only        Both closed
                          (Unknown). Gift-card decline mapping and            per Jira). Gift-card mapping PR 57197,
                          stale receipt JSON.                                 219 receipts re-synced.
SBY            1          POS sent empty staff-discount stubs for 3           Guard drops all-null stubs; 4.7M stub       Closed
Sainsbury's               days; every stub flipped the staff-discount flag    rows removed and headers rebuilt.
                          (1% to 34%).
KFC            3          Loyalty and card feeds land after the POS file      Loyalty moved to lookback enrichment,       1 closed, 2 open
                          (feed timing). Manager voids never                  backlog repaired. Refund
                          reclassified as refunds. Client sends GUIDs in      reclassification fixed with history. Card
                          the transaction number field (client-side,          data repaired for clean days.
                          open).
WTR Waitrose   4          Post-cutover gaps: dump-code and                    Closed by support in Jun and Jul as         All closed
                          department-sale lines, unfinished-trip status,      configuration and datatype fixes.
                          reduced-reason field.                               Engineering notes describe mapping
                                                                              PRs 53567 and 53717; Jira does not
                                                                              record them (see note below).
ICA            4          XML tags with a namespace prefix not visible        CONTAINS-based detection, corrected         1 closed, 2 open, 1 not in
                          to XMLGET (bank deposit, post-registered            XML depth, per-row parse safeguard;         Jira scope
                          bonus). Bottle-refund lines collapsed. One          bottle-refund rows kept per line. Two
                          corrupt XML file suspended the client task.         fixes in prod under validation.
THD Home       4          3 outside SnowTime (platform work items,            Platform and app fixes confirmed by         3 closed, 1 open (platform)
Depot                     hierarchy config, app filter). 1 ours: split-file   customer. Cleanup step disabled, days
                          cleanup step dropped lines and receipts went        reloaded, 1.31M receipts rebuilt.
                          stale.


3. What the support team can do before escalating (asked for on almost every ticket)
 • Send 2 or 3 transaction IDs with expected vs actual values, plus one receipt image. Engineers asked for this on 30 of 42
   tickets; it removes the first day of every investigation.
 • State the cutover date and whether legacy showed the value. Legacy had it, Secure does not, since <date> is the single most
   useful sentence in a ticket.
 • Classify the blank before raising it. Blank on every row since cutover = mapping gap. Blank on old rows only = missing rows,
   ask for a backfill. Blank on some rows = feed timing, ask which feed fills it and when it lands.
 • Check the raw file first. If the bad value is in the file as delivered, it is a client fix, not a pipeline fix.
 • Verify the data exists in ARDM before routing to platform. If it is there, the issue is platform, app, or template; SnowTime does
   not need to reload.
 • Ask whether the fix is going-forward only. If yes, request the backfill and the receipt JSON refresh in the same ticket. 8 tickets
   were reopened or extended because history was left as is.

4. Two things on our side
 • Going-forward fixes without backfill are the biggest cause of repeat contact. Every mapping fix should ship with a decision
   on history (repair script, backfill, or a written reason not to).
 • Jira does not carry the technical root cause on 11 of 41 tickets, and on 6 tickets (WTR 3, WCO 1, KFC 1, TJE 1) the engineer
   notes and the Jira closing comment describe different fixes. Support cannot learn from a ticket that says fixed, please confirm.
   The root cause and the fix should be written into the Jira comment at closure, in plain language, by the engineer.

Resolution summary, 9/28.

Issue:
Case 2026-FOOD LION ,LLC-0619-27, ShopliftingID 1596525, 9/20 around 14:12 UTC. Smart Alert History shows two alerts as Success: External Case with Value over $1,000 to james.cosseboom, and Defrauded Customer-Food Lion to the full list. Dawn Hendry and Asset Protection did not receive the Defrauded Customer alert. btatum came from the store manager assignments for store 0619, not the alert list. Answered to the customer 9/24.

What we found:
1. Grafana 9/20: the run completed, 13 Begin, 12 End, inserted into SmartAlertProcess.
2. SmartAlert.vb writes Success without checking the SendGrid result. Success does not prove delivery.
3. Chris Rippingale checked SendGrid on 9/25 and did not find the send. Russ confirmed SendGrid keeps 7 days, so 9/20 can no longer be checked. The exact cause for 0619-27 cannot be reconstructed.
4. Duplicate recipients. Silvana.Baxter and bj.robinson were on both the alert list and the store manager CC, and Kimberly Williams appeared twice on the 0619-27 send. Kiran removed Silvana and BJ from alert config 218 on 9/27.
5. From 9/24 all ADUSA alerts stopped. Handled on RCS-29123, PR 58273.

Verification after the fix, 9/28:
Defrauded Customer-Food Lion: 9/27 SendGrid delivered to all 26 recipients, including dawn.hendry, storepayments and RETFLAssetProtectionDivisionalMgrsALL. 9/28 ShopliftingID 1600434 at 19:36 UTC: 13b, SmartAlertProcess config 197 Success, End, no duplicate addresses.
External Case with Value over $1,000: 13b to james.cosseboom at 19:04 and 20:09 UTC.
Impersonation/Social Engineering on Food Lion goes out through Defrauded Customer-Food Lion, which covers both case types. The TGC Impersonation alert filters on the Giant/Martins division, so Rows Returned=0 on Food Lion is configuration.

Remaining, outside this ticket:
Alerts over 25MB are now rejected by SMTP. Russ found a size bounce to james.cosseboom on 9/21 08:24 UTC.
SendGrid dropped some addresses as Invalid on other alerts because they contain line breaks: jamie.holland, bj.robinson, johnna.krachinski and the RETFL list. Cleanup with Kiran.

Next: customer confirmation, then close.
Related: RCS-29123, RETAILIT-20901.

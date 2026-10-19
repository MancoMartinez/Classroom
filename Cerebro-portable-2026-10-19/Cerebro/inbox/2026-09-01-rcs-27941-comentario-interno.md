# INTERNAL NOTE. NOT FOR CUSTOMER

## Root cause

Access to case records is granted per incident type through Manage Case Type, Security tab. Beverly Wright and Francesca Ramos hold security levels that are not granted on the incident types holding the records they searched for. The search runs, applies the case type security filter and returns zero rows.

**This is configuration. No defect exists.**

## Environment

Production. Tenant 209-tbi. `sqldb-prd-wus2-arp-production-209-tbi-platform`.

## Steps to reproduce

### Tailored Brands (TBI), reported 2026-08-20

1. Sign in to Incident as `beverly.wright@tailoredbrands.com`.
2. Open Search For Incident, People Filters tab.
3. Set Search On to `Suspect`. Enter Last Name `Peters`. Leave every other field empty.
4. Click Search. Read the LPMS Default Case View grid.

**Expected:** four suspect records returned.
**Actual:** `No data to display`. No error raised.

Repeat as `francesca.ramos@tailoredbrands.com`. Same result.
Repeat as `dexter.monroe@tailoredbrands.com`. Records returned, Edit action available.

Screenshots attached to this ticket, dated 2026-08-20 and 2026-08-25.

## Evidence

The four Peters records traced from `incident.Suspect` through `incident.Shoplifting` to `incident.MasterCase`:

```sql
SELECT * FROM incident.MasterCase WHERE MasterCaseId IN (
  SELECT MasterCaseID FROM incident.Shoplifting WHERE ShopliftingID IN (
    SELECT SuspectID FROM incident.Suspect WHERE LastName = 'peters'));
```

| MasterCaseId | StoreIdent | CaseType |
|---|---|---|
| 671 | 5361 | Refund Fraud |
| 11990 | 6665 | Recovery - Legacy ThinkLP |
| 15353 | 3902 | Employee Work Injury |
| 20549 | 5076 | Refund Fraud |

Manage Case Type, Security tab, read in production on 2026-09-01 at `/tailoredbrands/nettrack/Admin/CaseTypeConfig.aspx`:

| Incident Type | Security levels granted |
|---|---|
| Refund Fraud | Field Loss Prevention, Support, Administrators, Risk Management |
| Recovery - Legacy ThinkLP | Support |
| Employee Work Injury | Support, Administrators, Risk Management |

**Corporate User and Location Manager are granted on none of the three.**

| User | Security level | Result |
|---|---|---|
| Beverly Wright | Corporate User | zero rows |
| Francesca Ramos | Location Manager | zero rows |
| Dexter Monroe | Administrators | records returned |

Dexter resolves to Administrators, granted on Refund Fraud and Employee Work Injury. That accounts for the difference in behaviour across all three users.

## Ownership of the change

Tailored Brands decides which security levels access each incident type. Their own administrator applies the change. Dexter Monroe holds access to both screens involved.

Two paths, confirmed with Kiran Vadday on 2026-09-01.

Grant Corporate User or Location Manager on Manage Case Type, Security tab. This grants every user holding that level in the tenant, not only Beverly and Francesca.

Create a new security level on Manage Security, using the Add Security Level button, assign it to the two affected users, and grant that level on the incident types needed. No blast radius beyond the two users.

Support has presented both options to the customer.

## Next steps

1. Tailored Brands confirms which incident types Corporate User and Location Manager should access.
2. Their administrator applies the change.
3. Beverly and Francesca retest and confirm.

No engineering work required. Returning to Support ownership pending the customer's decision.

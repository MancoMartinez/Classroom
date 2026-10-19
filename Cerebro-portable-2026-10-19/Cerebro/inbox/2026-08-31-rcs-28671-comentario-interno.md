# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Retest result: PASS

Environment: USPROD, client 85, C085_THD.

Search retested: `/public/internal investigation lookups/line item void/line item void - general search.search`

Display name: Line Item Void - General Search. Last Changed 08/31/26 11:04:47.

Steps:

1. Sign in to the THD tenant from Control Panel USPROD, table Customers in USPROD, Click logo to sign in.
2. Explorer, public, internal investigation lookups, line item void.
3. Select Line Item Void - General Search, then View results.
4. Apply the reporter's parameters from his screenshot. Transaction Date between 2026-06-01 and 2026-08-31. Store Number 2605. Cashier LDAP UBMKVT7. Every other toggle left off, including Tender Type Group.
5. Run.

Expected: a result set, no error.

Actual: 216 results returned at 12:57 EDT. No error, no tracking code.

## 2. The Tender Type column resolves

The output column Tender Type is populated. It returns Charge and Debit.

That column is fed by the join that was failing:

```sql
LEFT JOIN secure_EnumerationReferenceData AS T6
    ON (T6.EnumerationType = 'tendertypegroup' AND T6.Culture = 'en-GB' AND T6.KeyAsInt = T3.TenderTypeGroup)
```

The join now resolves and returns values. The repair corrected the binding. It did not sidestep the error by dropping the field from the definition.

## 3. Scope still open

I retested one search out of the roughly 150 you repaired. That is one data point. It is not coverage.

By your own count, 50 searches remain uninvestigated in the public folder and user searches have not been touched. Corey's 11:54 comment states the issue may be expanding to additional users, across field and office.

I am holding this ticket in Escalated. I will not tell Corey the matter is resolved on the strength of one search.

## 4. What I need from you

1. How many definitions still reference the old column, public and user folders combined. Your repair pass produces that number and it is the one that tells us when this ticket can close.
2. Whether the repair edits the saved search definition or the underlying field metadata. RCS-28543, Kinney Drugs KNY/179, is the same defect class on the same SnowTime path. There, deleting and re-adding the field through Composer re-copied the stale binding and widened the failure count from 3 of 30 to 11 of 30. That ticket sits in Under Engineering Review.
3. Send me paths from the batch you already fixed and I will retest them. Give me the ones your users hit most.

## 5. Troubleshooting notes

All work was performed in USPROD with read only access. No definition was opened for editing and nothing was saved. The Composer banner on this search reads "Current search is being used in different application. Please contact Administrator before editing it."

AI assistance was used to review the ticket history and to correlate this ticket with DO-12041 and RCS-28543.

No conversations about this ticket took place outside the ticket.

## 6. Related

DO-12041 SnowTime C085_THD Testing and Verification, In Development. Its description reads "Verify searches still work and receipts render as expected."

RCS-28543 Kinney Drugs KNY/179, Under Engineering Review. Same defect class, different column.

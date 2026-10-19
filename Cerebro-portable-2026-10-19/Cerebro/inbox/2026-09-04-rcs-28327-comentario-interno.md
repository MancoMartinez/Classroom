INTERNAL NOTE. NOT FOR CUSTOMER

Root cause investigation on this ticket, comment by Edwin Garzon on August 20, found that the reported symptom is not a data pipeline defect. Fifteen days passed since that finding with no action taken on it.

Environment. Production, Secure 5.4, client c046dhz, ARDMPROD.ARDM_046, Delhaize banner Food Lion.

Findings confirmed by Edwin Garzon on August 20. Transaction 2608025570789970641 carries CODE equal to loyalty discount in ARDM_ITEMDISCOUNT. TYPE for the same row is other. The parser sets these values intentionally in pyardm/us/c046dhz/ardm/python/pd_pos_parser.py at lines 777 and 842 when it detects an AdvancedFrequentShopper or FrequentShopper POS event. The transaction data is correct.

Client 46 runs ARDM V3 with a text based itemdiscount schema. The Item Discount Description field in Composer resolves its text through Platform.GetExcelReferenceData pointed at /system/ebr/crdm/store/2_0/enumerations/crdm pos enumerations.xlsx. A SELECT against secure.Repo for that exact VirtualFilePath on client 46's Platform DB returned zero rows.

Validation completed today. Composer confirms Item Discount Description is a single computed field, not user selectable between type, code or reason. A SELECT against EnumerationReferenceData for client 46 confirms the itemdiscounttype enumeration already exists there, with keys employee, free, loyalty, manual_price and other.

Conclusion, first point. The itemdiscounttype enumeration for client 46 already exists in EnumerationReferenceData. The field definition still calls the CRDM 2.0 xlsx path instead of that table. This definition was left behind in the V2 to V3 migration and it can affect every client migrated the same way, not only client 46.

Conclusion, second point. Redirecting the definition to EnumerationReferenceData does not close this ticket by itself. TYPE for this transaction is other, and other maps to OTHER in EnumerationReferenceData, not to Loyalty Discount. The legacy 3.5 receipt for the same transaction prints Reason: Loyalty Discount. Confirm whether AdvancedFrequentShopper and FrequentShopper POS events should set TYPE to loyalty instead of other in the parser. Without that second fix the column stops being blank and shows OTHER, which does not match what the customer saw before the upgrade.

Precedent. RCS-27761, same client 46, same reporter, Tender Check Amount blank on Payroll Check tender. Nikita Rathore found MediaNo 4 was missing because it originally mapped to paper Food Stamps. Engineering fixed it with a PR adding MediaNo 4. Same symptom family, an enumeration value missing at the platform level, resolved by Engineering.

Scope. Edwin states this is not isolated to loyalty discounts or to one store. It affects every item discount on this client where the type field renders through this same lookup.

Troubleshooting performed. Edwin Garzon queried ARDM_ITEMDISCOUNT and secure.Repo directly against production, read only, on August 20. I confirmed the EnumerationReferenceData content and the Composer field structure today, also read only. AI assisted in interpreting the EnumerationReferenceData output and the Composer field structure, cross referencing them against Edwin's August 20 findings, before this comment was drafted. No conversation with Engineering happened outside this ticket before this comment.

What I need. Update the Item Discount Description definition to resolve against EnumerationReferenceData instead of the CRDM 2.0 xlsx path for client 46. Confirm whether the same stale definition exists on other clients migrated from V2 to V3. Confirm whether TYPE should be loyalty instead of other for AdvancedFrequentShopper and FrequentShopper events in the client 46 parser.

Hi @Vito Zona,

Thank you for the screenshot. It showed me that my earlier answer was incomplete, and I want to correct it.

The over short amount is received per store, register and day, without a cashier attached. Cashier 0 is the register level record, so it carries the full over short amount for each register once per day. That is why Cashier 0 adds up to the total over short for the store.

The rows for individual cashiers work differently. Each cashier who worked on a register that day shows that same register amount in full, as a way to connect them to the register result. The amount is not divided between them. If three cashiers worked on a register that was 5.00 short, each of the three shows 5.00, and Cashier 0 shows 5.00 once.

This is what you are seeing as duplicates. In practice:

For store level totals, use the Cashier 0 rows only.
For cashier analysis, filter out Cashier 0 and read each cashier value as the result of the registers they worked on. Adding those values together will overstate the total.

My earlier note that Cashier 0 carries no dollar value was wrong for this data. I apologize for the confusion.

Kind regards,

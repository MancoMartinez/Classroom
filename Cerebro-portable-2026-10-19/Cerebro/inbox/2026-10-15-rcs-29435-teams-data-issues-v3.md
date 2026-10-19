Subject: RCS-29435 Starbucks NA: Home Store Dept Name shows several stores for one partner

**Issue**
Partner Lookup shows several Home Store Dept Name values for one partner.

**Evidence, partner 37045592 in C166_SBX.REFERENCE_EMPLOYEE**
- 5 rows, one per store, with 3 different X_HOMESTOREDEPTNAME values
- 00559 AGOURA & WESTLAKE on 3 rows
- 10109 CAMPUS PARK & COLLINS, inserted 6 Oct
- 06609 SYCAMORE & COCHRAN, inserted 7 Oct and updated 15 Oct
- C166_SBX_SNOWTIME.FLAT_EMPLOYEE, file of 15 Oct: one row for this partner, 06609
- Partner 32164302 looks correct: all 10 rows carry 18869 MULHOLLAND & CALABASAS

**Scope**
14018 of 2446272 partners in that table have more than one name. That may include renamed stores or inactive partners.

**Questions**
1. Did the load before the 27 Aug cutover update the name on every row of the partner?
2. Can the current load do the same and the stale rows be corrected? Please clone the table first.

**Note**
The source feed has one current store per partner, so I am not asking the customer to change data.

Thanks.

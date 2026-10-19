Hi Daniel, RCS-29224: https://trebuco.atlassian.net/browse/RCS-29224

A correction on my last message: most rows are zero on healthy days too. The signal is the sum. totalsalesquantity adds up to 0 for Oct 2 to 4 and Oct 7 to 13, against about 900K in ARDM_ITEM. Sep 15 to 27 match at about 97%.

The code points to timing. pyardm rebuilt the whole day on every run, while SnowTime writes the row when STRINVDT lands and does not update it when POS arrives later. Does that match what you see, and who should own a fix and a repair run for the zero days?

Thank you!

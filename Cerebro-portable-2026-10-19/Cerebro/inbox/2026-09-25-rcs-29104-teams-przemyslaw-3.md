Thanks Przemysław, it is the same order: the header has order_id 600006266~533653~N~20260915. The tender row came in the 9/18 tender file, line 240047, and its header came one day later in the 9/19 orders file. The tender never reached ardm_tender.

The 9/18 tender file has 545,902 lines and 318,705 loaded, 58.4%, the same ratio I see for GPC since 5/4. I checked 7 rows around line 240047. The 3 that loaded had their header in the same day orders file. The 3 that did not had their header in the next day file, and one has no header yet.

At scale, for 9/14 to 9/18 no loaded tender has a header from a later file. For 4/20 to 4/30 there are 1,961 of those. So it looks like a tender that arrives before its header used to be kept and now is dropped. I may be missing something from the historical load in April.

Could the loader be dropping tender rows when the header is not there yet? And since the tender files are in Archive, could 5/4 onward be reloaded once the headers are in?

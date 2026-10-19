Hi Corey, Ericka, thank you for your patience on this one.

Engineering confirmed the cause of the stuck work item. It was generated before the underlying event data was available in our source system, and that data is available now.

Fixing it requires removing the affected work item and regenerating it against the data that is now present. Support checked every part of the Portal that could do that and found no such action available there.

I raised that gap directly with engineering today and reproduced the same error again this morning to confirm the item is still stuck, which supports their read on the cause.

I need nothing further from you on this one.

I will update this ticket once engineering confirms how we move forward with regenerating the affected items.

Thank you.

Internal note. Taking this one over from here.

Carlo came back this morning. The template is not deleted and not expired, it reads Template deleted.0, so that line is closed.

The template editor opens for him. What does not open are the forms hanging off it. Thirteen forms sit under ANNUAL OPS/SERVICES REVIEW, one per year since 2019 plus four created for 2026, and only three of them load, IDs 577, 575 and 341. Another large template, 2026 Annual Safety Compliance Audit, opens normally for him.

Carlo raised size himself. That fits the shape we have seen elsewhere, a form rendering synchronously and running past the edge timeout, same as RCS-28139 at Sportsman's Warehouse. One of the forms that does load is named Pt1, so someone has already split that form into parts at some point.

Still a working read, not a cause. I have asked him how long the page holds before it goes blank, which is what separates a timeout from an immediate failure, and which form he needs for this year.

I told him I would confirm this with engineering before naming it, so that commitment is on the ticket. If the timing comes back anywhere near one hundred seconds this goes to AALPS through Matthew Kamminga, with the caveat that APIS carries no ongoing development and the realistic outcome may be splitting the form rather than a code change.

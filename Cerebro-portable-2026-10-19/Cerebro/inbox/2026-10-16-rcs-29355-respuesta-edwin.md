OBSOLETO: reemplazado por 2026-10-16-rcs-29355-respuesta-edwin-v2.md (mensaje en espanol, mas corto, con RCS-28125 y RCS-29347).
RCS-29355 respuesta a Edwin (Teams, interno). Hipotesis: nadie ha confirmado que staging cargue c046.

Hey Edwin, good digging. I can't see the repo from here, so I'm going on what you found. Cerebro has nothing written about a staging load for c046, so nobody has told us it's supposed to work. I'd treat it as unknown for now.

Your three questions land on the same person, whoever runs the ingest. Ryan Barlow has been answering on the other Delhaize tickets, like RCS-28911, so I'd ping him first. I don't know if he owns staging, so ask him that too, and if it's not him, who is.

Is staging ingest expected to run for c046, and is the staging RDL slot running? RAW_DATA looks empty for almost every US client, so maybe the slot is just idle. Does that match what you see?

Also ask what SnowflakeTargetArdmDatabase says in the Delhaize QA seed manifest. If it says ARDM_STAGING, the QA instance reads the schema you checked. If it says something else, we may be looking at the wrong one.

On RecallExtract, before anyone edits the pattern, can we ask Rodney if the Test sender can deliver it as zip.pgp like prod? If prod and Test share the same _sources.yml, an edit there touches prod too, so I'd let the owner decide.

Same for POS_Navistore, I'd leave the ignore rule as is for now. Rodney says his file is separate from the Storeline zip that goes to prod, and he's working the mapping with the POS EX team. Maybe the ignore rule is there for the Storeline file, so ask the owner. For the QA test itself, ask if they can load the files Rodney attached by hand, since that's what the ticket asked for.

Don't give Rodney a date until the owner answers. Want me to write the ping for Ryan?

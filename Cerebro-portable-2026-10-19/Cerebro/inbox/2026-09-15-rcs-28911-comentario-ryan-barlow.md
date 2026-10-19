Ryan, thanks for checking the 15th, that run looks fine. The gap is specific to the 14th.

FTP task history and JobLog.log for the 14th 10:00 AM run show only the employee file came in. No store file was on the SFTP at that time, JobLog logs STORE as source file not found, and the job still exits 0.

Looks like a delivery gap on ADUSA's side that morning, not a job issue. I am asking Jim and April to confirm and resend.

When you get a chance, worth checking if STORE has ANC_EXPECTEDDAILY set FALSE like EMPLOYEE, same blind spot as RCS-28093.

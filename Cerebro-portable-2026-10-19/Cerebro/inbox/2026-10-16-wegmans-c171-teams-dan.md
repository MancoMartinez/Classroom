# Mensaje de Teams para Dan y Shireesh, C171_WEG

Un borrador vivo. Va en el hilo de R&D, 2026 SnowTime. Cifras verificadas con SELECT el 16 oct. Pasó verificar_borrador sin bloqueantes. Si Q5 y Q6 confirman la ventana de la definición, cambia el penúltimo párrafo por el hallazgo.

---

Hi Dan, Shireesh,

I pulled the C171_WEG work item counts straight from the Platform database for September and October. They match Shireesh's wisc2 table day by day.

September, 30 days: 129 results, 57 generated, 72 duplicates, 0 failures. Duplicates were 56% of results. October 1 to 15: 76 results, 35 generated, 41 duplicates, 0 failures. Duplicates were 54%. Per day that is 2.4 duplicates in September and 2.7 in October, so the overall rate holds steady.

On the spike: October 15 has 9 duplicates out of 14 results, the highest day since September 1. The highest September day had 4. The rise did not start on the 15th. October 11 to 15 shows 5, 5, 5, 4 and 9 duplicates, and total results per day went from 3.1 on October 1 to 10 to 9.0 on October 11 to 15. September had a smaller stretch from the 13th to the 20th, with 3 or 4 duplicates every day at normal volume.

Almost all of it comes from one definition, gift cards purchased with lower trans amount. It accounts for 96 of the 113 duplicates across both periods. Nothing failed and nothing was skipped.

My read so far is that this definition flags the same transactions again on following days and the duplicate check discards them. I have not confirmed that yet, I am reading the definition's time window. The jump in total results from October 11 may also be related to the data load Ayesha mentioned. Do you know which dates that load covered, or am I reading this wrong?

# RCS-28389 GUESS, lista de desbloqueo ordenada

11 sep 2026. Fuentes: tabla del comentario del cliente del 4 sep (trae los GUID) y captura
`image-20260911-152725.png` del 11 sep 11:27. Orden: ultimo login descendente. Arriba estan
las cuentas que alguien esta usando de verdad y no puede entrar hoy.

| # | Email | Nombre | Ultimo login | TZ | GUID de membership.Users | Fuente |
|---|---|---|---|---|---|---|
| 1 | 04021@guess.com | Store 4021 | 9/9/2026 5:12:11 PM | New_York | pendiente | captura 11 sep |
| 2 | 00156@guess.com | Store 3156 | 9/3/2026 8:54:39 PM | New_York | pendiente | captura 11 sep |
| 3 | 03964@guess.com | Store Manager | 9/2/2026 12:31:42 PM | New_York | pendiente | captura 11 sep |
| 4 | 07146@guess.com | Store Manager | 9/1/2026 9:01:57 AM | New_York | aca73e90-c633-4b92-a470-f747ca1a39a4 | tabla 4 sep |
| 5 | mbustamante@guess.com | Michael Bustamante | 8/31/2026 5:08:01 PM | Los_Angeles | pendiente | captura 11 sep |
| 6 | mmandaglio@guess.com | Maria Mandaglio | 8/29/2026 1:04:40 PM | New_York | b86a979f-705a-46f9-974a-296c3d95320f | las dos |
| 7 | 03280@guess.com | Store 3280 | 8/26/2026 5:38:46 PM | Los_Angeles | ba8e207e-aaae-4ee9-9ccf-f29b635a0acb | tabla 4 sep |
| 8 | 00112@guess.com | Store 3112 | 8/25/2026 12:20:52 PM | Chicago | de1970ce-f0ac-46d9-a3b3-45dec65d9c4a | las dos |
| 9 | 05934@guess.com | Store 5934 | 8/21/2026 9:35:51 PM | New_York | 05359a6c-bfef-4c67-a903-de1b301d7d14 | tabla 4 sep |
| 10 | 03292@guess.com | Store 3292 | 8/16/2026 11:05:35 PM | Phoenix | b36b4ba6-004a-47c8-90c7-91ff46ae91e0 | las dos |
| 11 | 03998@guess.com | Store 3998 | 8/14/2026 7:55:51 PM | Toronto | b1c48071-1d19-4329-b217-a46fb9fdb7db | tabla 4 sep |
| 12 | 03226@guess.com | Store 3226 | 7/14/2026 4:10:47 PM | New_York | d7408a20-ad0d-4105-b9f4-1c3deaacc847 | las dos |
| 13 | 05647@guess.com | Store Manager | 6/28/2026 5:44:35 PM | Los_Angeles | 77bac419-1ef6-4dce-b3fd-ac506ec7605c | las dos |

03263@guess.com no entra. Viraj lo confirmo desbloqueado el 24 ago con login del 21 ago.

CORREGIDO con el SELECT del 11 sep. La captura no estaba cortada, mostraba las nueve que siguen
bloqueadas. Las cuatro que faltaban (03280, 03998, 05934, 07146) ya estaban en `Locked = 0`.
Los trece de esta tabla son la union de dos fotos con una semana de diferencia, o sea la lista
de consulta. Los nueve del SELECT son el estado real.

Rotacion medida entre el 4 y el 11 sep: salieron 03280, 03998, 05934 y 07146. Entraron 04021,
00156, 03964 y mbustamante. Cuatro y cuatro. El total se queda en nueve.

## Lote uno, atender hoy
04021, 00156, 03964, 07146, mbustamante. Cinco cuentas con login en los ultimos diez dias.
Se bloquearon estando en uso, que es lo que le duele al cliente ahora mismo.

## Lote dos
El resto. Ninguna entro desde el 31 ago. Verifica que sigan activas antes de tocarlas.

## Despues de desbloquear
Anota hora y metodo por cuenta. Si alguna vuelve a Locked True en menos de una semana, eso
confirma el umbral de intentos fallidos y no un defecto de la migracion.

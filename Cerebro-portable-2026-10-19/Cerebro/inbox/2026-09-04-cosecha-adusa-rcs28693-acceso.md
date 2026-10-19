# Cosecha 4 sep 2026 — RCS-28693 ADUSA, defecto de control de acceso

Sesión fuente: "ADUSA tickets analysis" (local_1b94d0d4), transcripción del 3 sep 2026.

## Hallazgo verificado

RCS-28693 lleva dos defectos separados y en direcciones opuestas.

Defecto 1, Harrison Xu. No puede autenticar. Giant Food store 233, Asset Protection para Giant District 104, grupo AP Level 2 Ahold. Usuario de control provisto por ADUSA es Kyle Moses. Vlad Bogus compara los claims SSO entre los dos. No se ha descartado membresía de grupo Azure del lado cliente. Leigh Ann Stubbs envía el link de prueba a Harrison.

Defecto 2, Paula Dotson. Un usuario sin ningún aprovisionamiento LPMS en Azure, y sin historial de aprovisionamiento, autenticó con éxito y recibió el rol Store Reporter. ADUSA verificó el estado de Azure de su lado y adjuntó capturas de la sesión abierta. No hay grupo del lado cliente que lo explique. La lógica de fallback está otorgando un rol por defecto a una identidad que debería rechazarse en la autenticación.

Pasos de reproducción del defecto 2, confirmados contra Producción y Test por Leigh Ann Stubbs el 2 de septiembre:
1. Seleccionar cualquier usuario del tenant sin aprovisionamiento LPMS en Azure.
2. Ir a la URL de sign in. Producción `https://apps.apprissretail.com/adusa/signin`. Test `https://test.apprissretail.com/adusa/signin`.
3. Autenticar con ese usuario.
4. Observado: la sesión abre y el usuario recibe el rol Store Reporter.
5. Esperado: la autenticación se rechaza y no se otorga ningún rol.

Vlad Bogus confirmó el 2 de septiembre que las configuraciones SSO de Test y Producción coinciden, salvo identity provider y certificado.

## Estado al cierre de la sesión

El ticket es de Vlad Bogus, no de Juan. La duda de enrutar a Security Review en vez de Engineering Review viene de una nota del 1 de septiembre y ya no aplica, J.R. no pidió nada sobre este ticket el 3 de septiembre. Sin acción pendiente de Juan aquí.

## Cierre de RCS-28123

Se cerró como Completed, resolución Bug - Resolved w/ Release. ENG-557, el error "Assigned to can't be blank" del 8/19, se cierra como duplicado dentro del trabajo de unificación, confirmado por Matthew Kamminga. El síntoma del correo de notificación se separó en RCS-28766, que quedó asignado a Diego Buelvas con la respuesta a Leigh Ann pendiente de pegar.

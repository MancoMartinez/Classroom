# RCS-28153 · Respuesta a Ashley

27 ago 2026, jueves. Reporter verificado: Ashley, ashley.mcfarlane@bigy.com.
Estado en Jira: `Under Customer Review`, assignee Juan Martinez, High. El ticket es tuyo.
Como ya está en Under Customer Review, no hay transición que hacer. Pega y queda.

## Lo que encontré en el hilo y cambia el mensaje

El 10 de agosto le ofreciste subir el timeout de 60 a 240 minutos. Ella aceptó el 11:

> "Raising the timeout from 60 minutes to 240 would be helpful."

Ese mismo día le escribiste:

> "the increased timeout will prevent this. Please let me know how your team gets on over the next
> few days."

**El bug de ENG-7184 es precisamente que el valor configurado del tenant se ignoraba y el sistema
caía siempre a 60 minutos.** Subiste el número a 240 el 11 de agosto y el sistema siguió usando 60.
Tu cambio no surtió efecto durante 16 días.

Eso convierte la verificación en algo más simple y le da un motivo real al mensaje. Ya no estás
avisando de un fix genérico. Estás corrigiendo algo que le afirmaste y que no se cumplió.

## La verificación, ahora concreta

Control Panel, USPROD, Engineering, Config Items, cliente 362 Big Y Foods,
`CPF.Core.LogOnTimeoutMinutes`. Solo lectura.

- **Si el valor del cliente es 240:** todo encaja. Usa el texto A.
- **Si el valor sigue en 60 o está vacío:** el cambio del 11 de agosto nunca se guardó. Eso es
  trabajo tuyo antes de escribirle. Aplica el 240, verifica, y después usa el texto A.
- **Si el valor es otro número:** usa el texto B, que no cita cifras.

## Texto A. Para pegar en Jira

```
Hi Ashley,

Update on this one.

On the 11th I set your user timeout to 240 minutes and told you that would cover the logouts. The system kept applying the old 60 minute limit instead, so your users were still being signed out early.

We have corrected that and the correction is live on your environment.

Could you have your team work as normal and confirm on this ticket whether the logouts and the errors have stopped. I am leaving this with you until you confirm.

Thank you.
```

## Texto B. Si el valor configurado no es 240

```
Hi Ashley,

Update on this one.

On the 11th I raised your user timeout and told you that would cover the logouts. The system kept applying the old limit instead, so your users were still being signed out early.

We have corrected that and the correction is live on your environment.

Could you have your team work as normal and confirm on this ticket whether the logouts and the errors have stopped. I am leaving this with you until you confirm.

Thank you.
```

## Por qué se cayó lo que te di antes

El texto anterior rompía cuatro reglas.

Contaba la investigación. "We traced the errors and the unexpected logouts to a session timeout
issue rather than to the attachments themselves. The session refresh was falling back to a default
timeout instead of reading the one configured for your environment." Eso es hallazgo técnico y no va
al cliente.

Decía "developed, tested and released". "Tested" es resultado de QA. Fuera.

Decía "over the next few days". Referencia relativa de tiempo. Prohibida.

Omitía la corrección. Le afirmaste el 11 de agosto que el aumento del timeout iba a prevenir el
problema y durante 16 días no se aplicó. Eso se corrige de frente, en una oración, sin disculpa
extendida.

## Compromisos que crea este texto

1. Dejas el ticket esperando la confirmación de Ashley. No prometiste fecha, así que la deuda es de
   ella. Persíguela si no contesta en una semana.
2. Cuando confirme, cierras: comentario al cliente, comentario interno con la trazabilidad de
   ENG-7184, Resolve transición 111 a `Completed`, después Close transición 91.
3. El aviso de cierre automático arrancó el 25 de agosto. Este comentario reinicia ese reloj.
4. Queda pendiente confirmar el valor del config item antes de pegar cualquiera de los dos textos.

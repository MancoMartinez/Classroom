# RCS-29465 respuesta a Patricia (cliente, ingles). Borrador vivo. Reemplaza cualquier texto anterior.
Estado de verificar_borrador cliente: sin bloqueantes salvo la oracion del join, marcada por una linea vieja de la bitacora, ya superada (ver pasos.md, Confirmacion del join). Confirmar en Jira estado y SLA antes de pegar.

Hi Patricia,

Thank you for your patience on this request. You can show the employee location in Order Refund Categories- SP and RS by referencing 1b - Emp HR Info with User ID V2. Here is the sequence that returned results in our test.

1. In the Composer, add Cashier No to the Display Fields.
2. Open References and add 1b - Emp HR Info with User ID V2.
3. Set the join option to "A or B".
4. Link Cashier No to User ID in Lower Case.
5. In Add Display Field, open Referenced Searches and add Employee location. Use the field that carries the name of the reference. The field labeled EMPLOYEE returned blank in our test.

Some employees have more than one location row in the reference. In our test those cashiers were counted more than once in Sum of Ticket Amount and in Count. Run the search once without the reference and compare totals before you use them in a report.

Do you need totals by cashier, or only the location next to each transaction?

Best regards,
Juan

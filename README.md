**PARTE 1**

**CONTEXTO DEL CASO PRÁCTICO**

La Librería del Centro quiere un módulo para calcular el precio final de sus productos. El administrador entregó estas tres reglas:

**Regla 1:** Un producto tiene nombre y precio base. El precio base debe ser mayor que cero. Si se intenta crear un producto con precio cero o negativo, el sistema debe rechazarlo con un mensaje claro.

**Regla 2:** Se puede aplicar un descuento porcentual al producto. El descuento debe estar entre 0% y 40%. Un descuento mayor al 40% debe ser rechazado. Un descuento del 0% es válido.

**Regla 3:** El precio final se calcula aplicando primero el descuento y luego el IVA del 19% sobre el resultado. El precio final nunca puede ser negativo.

Para la Regla 1 y la Regla 2, una tabla de particiones de equivalencia con todas las particiones válidas e inválidas, el valor representativo de cada una y el resultado esperado.
Para la Regla 2, una tabla de análisis de valores límite con los valores críticos en los bordes del rango 0%-40%.


nombre Partición | rango | valor prueba | resultado 

precio aceptado - mayor a cero| > 0 | 1000 | se acepta el precio 
precio rechazado - precio igual a cero | > 0 | 0 | se lanza una exception porque el valor no puede ser cero
precio rechazado - precio menor a cero | > 0 | -1000 | se lanza una exception porque el valor no puede ser menor a cero

descuento aceptado - dentro del rango | 0%<=x<=40% | 30% | se acepta el descuento
descuento rechazado - fuera del limite inferior | 0%<=x<=40% | -1% | se lanza una exception porque el valor no puede ser menor a cero
descuento rechazado - fuera del limite superior | 0%<=x<=40% | 41% | se lanza una exception porque el valor no puede ser mayor a 40% 

descuento aceptado - en el limite superior | 0%<=x<=40% | 40% | se acepta el descuento
descuento aceptado - en el limite inferior | 0%<=x<=40% | 0% | se acepta el valor aunque como es 0 no habría descuento

Para la Regla 2, una tabla de análisis de valores límite con los valores críticos en los bordes del rango 0%-40%.

Borde inferior (0%) | -1 % | Justo antes | Fuera | Falla: Error de validación
Borde inferior (0%) | 0% | Exacto | Dentro | Exitoso: registra el descuento
Borde inferior (0%) | 1% | Justo déspues | Dentro | Exitoso: registra el descuento


Borde superior (40%) | 39%| Justo antes | Dentro | Exitoso: registra el descuento y lo aplica
Borde superior (40%|) | 40% | Exacto | Dentro | Exitoso: registra el descuento y lo aplica
Borde superior (40%) | 41% | Justo déspues | Fuera | Falla: Error de validación

Para la Regla 3, una pregunta concreta que le harías al administrador antes de diseñar las pruebas, con su justificación en una línea.

¿El sistema debe redondear el precio final (por ejemplo, a pesos enteros o a dos decimales)?

Justificación:
Esto ayudaría a evitar diferencias por calculos decimales en iva y descuentos 




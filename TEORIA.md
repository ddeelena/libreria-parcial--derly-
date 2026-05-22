## SECCIÓN TEÓRICA

**SM-1** Respuestaa corecta C

Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

A. Shift-left testing. El problema es que las pruebas se vuelven demasiado técnicas para que el cliente las entienda.

este concepto nos dice lo contrario, y es que las pruebas se diseñan e integran desde etapas tempranas del desarrollo.

B. Shift-right testing. El problema es que las pruebas solo se pueden ejecutar en producción.

se enfoca en pruebas tardías o incluso en producción, 

**C. Desarrollo tradicional con pruebas al final. El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas.**

**Respuesta correcta, cuando se utiliza metodologias tradicionales se espera a terminar todo para finalmente probar.**

D. Integración continua. El problema es que requiere un pipeline de CI/CD que el equipo no tiene configurado.

Cuando se hace integración continua, las pruebas se ejecutan cada vez que se hace un pull request o push y no necesariamente al terminar todo el modulo, por lo cual esta opcion no corresponderia con lo que se dice de que se espero a terminar 


**SM-2** Respuesta B 

Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

A. La regla del refactor, porque debería mejorar el código antes de escribir tests.

Falso, el codigo se mejora despues de la fase green, y para ese entonces ya deben estar los tests

**B. La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera.**

**Esta es la respuesta correcta puesto que el TDD establece que primero se deben establecar los tests y luego hacer el codigo minimo para que no falle**

C. La regla del Green, porque el código debería ser mínimo y no cubrir todos los casos desde el inicio.

Porque para eso existe una fase refactor en donde, ya se establecen todas las mejores y optimizaciones necesarias

D. No está violando ninguna regla. TDD permite escribir el código primero siempre que los tests se escriban inmediatamente después.

TDD no establece eso, establece lo contrario primero pruebas y luego codigo


**PA-1**

Durante la semana 4 implementamos el carrito de compras con TDD y en el primer ciclo, el paso GREEN consistió en escribir el código más simple posible aunque fuera "feo". Explica por qué TDD obliga a hacer esto en el GREEN y qué pasaría con el proceso si el desarrollador aprovecha ese paso para escribir código "limpio y completo" desde el inicio.

Con TDD se establece una fase de refactor, porque en la fase GREEN lo que se busca que es que pase con lo minimo garantizando que ya se cumpla con el requisito que es un parte muy importante del sistema, si el desarrollador escribe todo el codido de una sola vez se corre  el riesgo de que no se cumpla con los requisitos y todas las condiciones asociadas por centrarse en hacer todo limpio desde el inicio. 

**PA-2**

Explica con tus propias palabras la diferencia entre TDD y BDD. No es suficiente decir que uno usa código y el otro usa Gherkin. Explica qué problema resuelve cada uno, a quién está dirigido y por qué se complementan en lugar de reemplazarse.

TDD -> Lo que hace se hace es que establece primero los test y luego el codigo pasando primero una etapa simple y luego de refactorizacion para que quede mas limpio el codigo. Hace que se tenga que pensar primero en todo lo que puede salir mal y todas las condiciones para luego enfocarse en darle solucion. 

BDD -> Utiliza lenguaje natural va dirigo a todo tipo de stakeholders. Al hacerse con lenguaje se busca que todos puedan entender que es lo que se busca probar. 

Estos se complementan porque uno ayuda a hacer un codigo enfocado en que se cumplan todas las condiciones y luego al hacerlo tambien en lenguaje natural todos entienden que se esta probando y pueden comprobar que se estan cumpliendo las condiciones necesarias para el sistema 

**PA-3**

Un compañero te muestra su suite de pruebas y dice: "Tengo 95% de cobertura de código, así que mi sistema no tiene bugs." Explica por qué esa afirmación es incorrecta. Usa un ejemplo concreto que demuestre que cobertura alta no garantiza ausencia de defectos.

Esta afirmación es falsa porque una cobertura del 95% solo esta diciendo que lso test ejecutados fueron correctos y esas partes del codigo que se estan midiendo son validas pero esta cobertura no nos dice si se estan contemplando efectivamente todos los casos de prueba posibles o si el compartamiento completo del sistema es correcto, solo sabemos que lo que se abarco si lo es.


**PA-4**

En el contexto de la Regla 2 del examen (descuento entre 0% y 40%), un compañero dice que basta con probar el descuento del 20% porque "si funciona con ese valor, funciona con todos". Explica por qué esa lógica es incorrecta y qué valores concretos deberías probar tú y por qué.

Es incorrecto porque hay limites en los cuales la prueba puede fallar y es necesario establecer que condiciones hay en estos limites, por ejemplo se debe probar

0% limite inferior - probar que aun estando en el limite funciona 
20% valor dentro del rango - probando que un valor dentro del rango funciona
40% limite superior - probar que estando en el limite superior aun funciona 
-1% por fuera del limite inferior - probar que con un valor fuera del rango da un error
41% pro fuera del limite superior - probar que en este caso no se puede aplicar el descuento y se rechaza

**PA-5**

Mirando el planeador de la asignatura, las semanas 3 y 4 cubren pruebas ágiles, TDD y BDD. Explica cómo estas prácticas se conectan con el concepto de CI/CD que veremos en la semana 6. ¿Qué pasaría con un pipeline de CI/CD si el equipo no tiene una suite de tests automatizados sólida?

Para que haya un despliegue continuo e integración correcta es fundamental que se ejecueten pruebas a  lo largo de todo el ciclo, garantizando que todo funciona de la mejor manera, TDD y BDD aportan de una manera fundamental en la forma en como se desarrolla y apunta a la calidad del desarrollo. Estas aportan validaciones continuas de los requisitos durante todo el ciclo.  Si no se tiene una suite de test automatizados solida podría generar que el despliegue e implementacion se lleven de una manera mas lenta, además se perderían los beneificios del CI/CD sin hablar del riesgo que se corre al no ejecutar correctamente las pruebas necesarias antes de hacer un despliegue. 


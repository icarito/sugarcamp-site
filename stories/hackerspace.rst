Hacker Space
============

.. raw:: html
    
    <div class="pull-right">
    <div class="span-one-third">
    <div id="cc-btn-sc" class="cc-btn-camp"> 
        <div class='cc-spacer'></div> 
        <span time="1321570800" class="kkcount-down"></span>
        </div> 
        <h3 style="text-align:center">La entrada es libre</h3>
        <p>
        Tenemos cupos limitados por lo que será necesario registrarse con anticipación.
        </p>
        <p style="font-size:14pt; text-align:center">
        <a href="registro.html">Regístrate aquí</a>.
        </p>
    </div>
    </div>

Notables hackers, locales y extranjeros, se concentrarán durante el encuentro en la conformación y testeo de la nueva imagen de SUGAR para Puno-Perú. El equipo técnico estará liderado por Sebastian Silva, quien tendrá a su cargo coordinar en vivo la integración de las traducciones de Quechua y Aymara, junto con los contenidos relacionados a "ciudadanía digital". Contaremos tambien con la participación confirmada de:

* Chris Leonard PhD, Localization Team Coordinator - SugarLabs Global
* Aleksey Lim, Platform Team Coordinator - SugarLabs Global
* Bernie Innocenti, Infrastructure Team Coordinator - SugarLabs Global
* Rubén Rodriguez, Trisquel GNU/Linux founder

Viernes 18 y sábado 19 de Noviembre 
9 am a 6:00 pm

La Metodología
--------------

Cada Hacker podrá contar con un espacio en el Hacker Space. Su ubicación preferentemente será cercano a quienes estén trabajando en lo mismo, para facilitar la colaboración y la concentración. Al entrar al espacio se le pedirá elegir su reto a resolver.

Durante el evento se llevará a cabo **integración continua** de la imagen para que el equipo pueda ir probando la experiencia de usuario a medida que esta se va desarrollando.

.. raw:: html

    <h3>Estas son las directrices que tendremos en mente para la confección de la imagen Hexoquinasa, que se distribuirá inicialmente en Puno. El producto final será una Live-USB capaz de levantar e instalar Sugar 0.94 en una computadora convencional (Edición Trisquel). Contendrá también las imágenes para instalar laptops XO1 (Edición Dextrose).</h3>
    <div class="pull-right">
    <img src="_static/images/hexokinase.png"/>
    </div>

Las Restricciones y los Retos
-----------------------------

El despliegue de Perú tiene características que lo hacen único tanto en su escala como en su distribución geográfica.

**Restricción 1: Un despliegue Offline/Online**

El despliegue en Perú consta de .5M de laptops (.8M en 2012), las cuales están distribuídas en su gran mayoría en los lugares más apartados del país, sin conectividad. Se necesita una estrategia para "conectar" a estos usuarios mediante el transporte de memorias USB, mediante nexos conectados a la Red (cabinas o "CRT - Centros de Recursos Tecnológicos").


**Restricción 2: Hardware limitado**

La gran mayoría de laptops son modelo XO1, las cuales tienen limitaciones importantes de rendimiento, y un *touchpad* de mala calidad. Sin embargo son computadoras durables y potencialmente muy útiles. Generalmente no se cuenta con un servidor.

Los Retos Estratégicos
----------------------

Todo hacker es libre de trabajar en lo que lo apasione. De todos modos hemos identificado los siguientes retos cuya solución estaremos priorizando y documentando: 

**Reto 1: Integrar traducciones a Quechua y Aymara**

Dos equipos estarán traduciendo a estas lenguas nativas. Se requiere integrar estas traducciones en forma continua durante el evento para que ellos vayan viendo el resultado de su trabajo.

**Reto 2: Recolección de Métricas**

El ciclo de mejoramiento de Sugar necesita de información y métricas de uso del sistema. Se requiere integrar la recolección de métricas de uso y diseñar una metodología para recolectar y publicar esta data de una manera que facilite la investigación y el desarrollo (open data).

**Reto 3: Distribución de Contenidos**

Se cuenta con unos 50MB de espacio en cada laptop disponible para contenidos y software. Se requiere implementar forma de presentarlos al usuario. 

**Reto 4: Chaski USB User Network**

Dadas las condiciones del piloto se priorizarán soluciones que faciliten el trabajo colaborativo descentralizado y asincrónico, el cual pueda sincronizarse mediante "mensajeros" encargados de enviar y recibir actualizaciones, información y mensajes de los usuarios entre sí y con el mundo.

.. title: Proponer un taller
.. slug: proponer
.. date: 06/04/2014 01:07:56 AM UTC-05:00
.. tags:
.. link:
.. description:
.. type: text

.. raw:: html

    <script>
    function validateForm()
    {
        var titulo=$('#titulo').val();
        var descripcion=$('#descripcion').val();
        var tiempo=$('#tiempo').val();
        var horario=$('#horario').val();
        var nombre=$('#nombre').val();
        var email=$('#email').val();
        var telefono=$('#telefono').val();
        var origen=$('#origen').val();
        if (  titulo=="" ||
              descripcion=="" ||
              tiempo=="" ||
              horario=="" ||
              nombre=="" ||
              email=="" ||
              telefono=="" ||
              origen=="" )
        {
            $('#flash').css('display', 'inline');
            return false;
        }
    }
    </script>

    <div class="col-md-5 pull-right">
    <div id="cc-btn-sc" class="cc-btn-camp center-block">
        <div class='cc-spacer'></div>
        <span time="1405630800" class="kkcount-down"></span>
    </div>
    </div>

    <form action="/assets/form/registro_chia_talleres.php" method="post" onsubmit="return validateForm()">
     <div class="fieldcontainer">
     <label for="titulo">Título de tu taller:</label>
     <input id="titulo" type="text" size="50" name="titulo" />
     </div>
     <div class="fieldcontainer">
     <label for="descripcion">Breve descripción:</label>
     <textarea id="descripcion" rows="5" name="descripcion"></textarea>
     </div>
     <div class="fieldcontainer">
     <label for="tiempo">Tiempo estimado:</label>
     <input id="tiempo" type="text" size="50" name="tiempo" />
     </div>
     <div class="fieldcontainer">
     <label for="horario">En qué horarios <br/>podrías realizarlo:</label>
     <textarea id="horario" rows="5" name="horario"></textarea>
     </div>
     <hr>
     <div class="fieldcontainer">
     <label for="nombre">Tu nombre:</label>
     <input id="nombre" type="text" size="50" name="nombre" />
     </div>
     <div class="fieldcontainer">
     <label for="email">Tu email:</label>
     <input id="email" type="text" size="50" name="email" />
     </div>
     <div class="fieldcontainer">
     <label for="telefono">Tu teléfono:</label>
     <input id="telefono" type="text" size="50" name="telefono" />
     </div>
     <div class="fieldcontainer">
     <label for="origen">De dónde vienes:</label>
     <input id="origen" type="text" size="50" name="origen" />
     </div>
     <div style="color:red;display:none" id="flash">
     Debes completar todos los campos.
     </div>
     <div style="margin-left:140px;" class="fieldcontainer">
     <input class="btn" style="background-color:red; color:white;" type="submit" value="Enviar propuesta" />
     </div>
    </form>

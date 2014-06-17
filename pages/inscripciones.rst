.. title: Inscríbete para participar
.. slug: inscripciones
.. date: 06/04/2014 01:07:56 AM UTC-05:00
.. tags:
.. link:
.. description:
.. type: text

.. raw:: html

    <script>
    function validateForm()
    {
      var nombre=$('#nombre').val();
      var email=$('#email').val();
      var telefono=$('#telefono').val();
      var actividad=$('#actividad').val();
      var origen=$('#origen').val();
      var contribucion=$('#contribucion').val();
      var sobreti=$('#sobreti').val();
      var presencia=$('#presencia').val();
      if (  nombre=="" ||
            email=="" ||
            telefono=="" ||
            actividad=="" ||
            origen=="" ||
            contribucion=="" ||
            sobreti=="" ||
            presencia=="" )
      {
          $('#flash').css('display', 'inline');
          return false;
      }
    }
    </script>

    <div class="col-md-3 pull-right">
    <div id="cc-btn-sc" class="cc-btn-camp center-block">
        <div class='cc-spacer'></div>
        <span time="1405609200" class="kkcount-down"></span>
    </div>
    </div>

    <form action="/assets/form/registro_chia.php" method="post" onsubmit="return validateForm()">
     <div class="fieldcontainer">
     <label for="nombre">Tu nombre:</label>
     <input id="nombre" type="text" size="35" name="nombre" />
     </div>
     <div class="fieldcontainer">
     <label for="email">Tu email:</label>
     <input id="email" type="text" size="35" name="email" />
     </div>
     <div class="fieldcontainer">
     <label for="telefono">Tu teléfono:</label>
     <input id="telefono" type="text" size="35" name="telefono" />
     </div>
     <div class="fieldcontainer">
     <label for="origen">De dónde vienes:</label>
     <input id="origen" type="text" size="35" name="origen" />
     </div>
     <div class="fieldcontainer">
     <label for="contribucion">Puedes contribuír:</label>
     <select id="contribucion" name="contribucion">
     <option></option>
     <option>Patrocinando</option>
     <option>Diseñando/Programando</option>
     <option>Lo que sea necesario</option>
     <option>Difundiendo</option>
     </select>
     </div>
     <div class="fieldcontainer">
     <label for="sobreti">Cuéntanos algo <br/>sobre tí:</label>
     <textarea id="sobreti" rows="5" name="sobreti"></textarea>
     </div>
     <div class="fieldcontainer">
     <label for="presencia">Tu presencia será:</label>
     <select id="presencia" name="presencia">
     <option></option>
     <option>Física</option>
     <option>Virtual</option>
     </select>
     </div>
     <div style="color:red;display:none" id="flash">
     Debes completar todos los campos.
     </div>
     <div style="margin-left:140px;" class="fieldcontainer">
     <input class="btn" style="background-color:red; color:white;" type="submit" value="Proceder con el Registro" />
     </div>
    </form>

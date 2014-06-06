<?php
$titulo=$_POST['titulo'];
$descripcion=$_POST['descripcion'];
$tiempo=$_POST['tiempo'];
$horario=$_POST['horario'];
$nombre=$_POST['nombre'];
$telefono=$_POST['telefono'];
$email=$_POST['email'];
$origen=$_POST['origen'];

$data = '"'.addslashes($titulo).
			'","'.addslashes($tiempo).
			'","'.addslashes($nombre).
			'","'.addslashes($email).
			'","'.addslashes($telefono).
			'","'.addslashes($origen).
			'","'.addslashes($horario).
			'","'.addslashes($descripcion).'"'."\n";
file_put_contents('reg_chia_talleres.csv', $data, FILE_APPEND);

$cc = "sebastian@somosazucar.org,laura@somosazucar.org,aura@laptop.org";
#$cc = "sebastian@somosazucar.org,laura@somosazucar.org";
$subject = "$nombre : Gracias por proponer un taller para Sugar Camp Chia 2014";

$message = "Hola!
    Hemos recibido tu ofrecimiento de taller con éxito. ¡Muchas gracias!

    Nos pondremos en contacto contigo para confirmar la aceptación de tu propuesta.

    Los datos registrados son los siguientes:
    Nombre: $nombre
    Email: $email
    Telefono: $telefono
    Origen: $origen

    Taller propuesto: $title
    Descripción: $descripcion
    Duración: $tiempo
    Horario disponible: $horario

    No dudes en responder a este correo con cualquier duda que tengas.

    Cordial Saludo,

    Comite Organizador
    Sugar Camp Chia 2014
    Sugar Labs Colombia - Somos Azúcar- OLPC Colombia";

mail($email, $subject, $message, "From: Comite Organizador <equipo@somosazucar.org>\r\n".
                                 "BCC: $cc\r\n");

header( 'Location: http://pe.sugarlabs.org/ir/SugarCampChia2014/taller' ) ;
?>

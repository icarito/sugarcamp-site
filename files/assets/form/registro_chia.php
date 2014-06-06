<?php
$nombre=$_POST['nombre'];
$telefono=$_POST['telefono'];
$email=$_POST['email'];
$actividad=$_POST['actividad'];
$origen=$_POST['origen'];
$contribucion=$_POST['contribucion'];
$sobreti=$_POST['sobreti'];
$presencia=$_POST['presencia'];

$data = '"'.addslashes($nombre).
	'","'.addslashes($email).
	'","'.addslashes($telefono).
	'","'.addslashes($actividad).
	'","'.addslashes($origen).
	'","'.addslashes($contribucion).
    '","'.addslashes($sobreti).
    '","'.addslashes($presencia).'"'."\n";
file_put_contents('reg_chia.csv', $data, FILE_APPEND);

$cc = "sebastian@somosazucar.org,laura@somosazucar.org,aura@laptop.org";
#$cc = "sebastian@somosazucar.org,laura@somosazucar.org";
$subject = "$nombre : Bienvenido a Sugar Camp Chia 2014";

$message = "Hola!
    A nombre del comite organizador de Sugar Camp Chia 2014, 
    te damos una calurosa bienvenida y desde ya agradecemos 
    tu valiosa contribucion.

    Tus datos de contacto registrados son:
    Nombre: $nombre
    Email: $email
    Telefono: $telefono

    No dudes en responder este correo con tus inquietudes o sugerencias.

    Cordial Saludo,

    Comite Organizador
    Sugar Camp Chia 2014
    Sugar Labs Colombia - Somos Azúcar- OLPC Colombia";

mail($email, $subject, $message, "From: Comite Organizador <equipo@somosazucar.org>\r\n".
                                 "BCC: $cc\r\n");

header( 'Location: http://pe.sugarlabs.org/ir/SugarCampChia2014/inscrito' ) ;
?>

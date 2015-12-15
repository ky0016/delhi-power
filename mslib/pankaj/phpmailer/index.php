<?php

include("class.phpmailer.php");
include("class.smtp.php"); // note, this is optional - gets called from main class if not already loaded

$mail             = new PHPMailer();

$body             = "Hello,, Mailer Working.. :-)";

$mail->IsSMTP();
$mail->SMTPAuth   = true;                  // enable SMTP authentication
$mail->SMTPSecure = "ssl";                 // sets the prefix to the servier
$mail->Host       = "smtp.gmail.com";      // sets GMAIL as the SMTP server
$mail->Port       = 465;                   // set the SMTP port

$mail->Username   = "getiitians@gmail.com";  // GMAIL username
$mail->Password   = "iitdelhi1984";            // GMAIL password, Some times if two step varification enabled in this mail id, Mail will not be sent.

$mail->From       = "getiitians@gmail.com";
$mail->FromName   = "Himanshu";
$mail->Subject    = "This is the subject";
$mail->AltBody    = ""; //Text Body
$mail->WordWrap   = 50; // set word wrap

$mail->MsgHTML($body);

$mail->AddReplyTo("pankaj.arora1994@gmail.com","Pankaj");

//$mail->AddAttachment("/path/to/file.zip");             // attachment
//$mail->AddAttachment("/path/to/image.jpg", "new.jpg"); // attachment

$mail->AddAddress("gitikaarora30@gmail.com","Pankaj");

$mail->IsHTML(true); // send as HTML

if(!$mail->Send()) {
  echo "Mailer Error: " . $mail->ErrorInfo;
} else {
  echo "Message has been sent";
}

?>

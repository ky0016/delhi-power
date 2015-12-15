<?php
abstract class Funs{
	public static function sendmsg($phone,$msg){
		$phone=urlencode($phone);
		$msg=urlencode($msg);
		$url="http://216.245.209.132/rest/services/sendSMS/sendGroupSms?AUTH_KEY=14e4de84f23c84d81f24b8fb69d1e0&message=".$msg."&senderId=GETIIT&routeId=1&mobileNos=".$phone."&smsContentType=english";
		return shell_exec("curl '".$url."'");
	}

	public static function sendmail($to, $subject, $body) {
		$mail             = new PHPMailer();
		$mail->IsSMTP();
		$mail->SMTPAuth   = true;                  // enable SMTP authentication
		$mail->SMTPSecure = "ssl";                 // sets the prefix to the servier
		$mail->Host       = "smtp.gmail.com";      // sets GMAIL as the SMTP server
		$mail->Port       = 465;                   // set the SMTP port

		$mail->Username   = "getiitians@gmail.com";  // GMAIL username
		$mail->Password   = "iitdelhi1984";            // GMAIL password, Some times if two step varification enabled in this mail id, Mail will not be sent.

		$mail->From       = "getiitians@gmail.com";
		$mail->FromName   = "Himanshu";
		$mail->Subject    = $subject;
		$mail->AltBody    = ""; //Text Body
		$mail->WordWrap   = 5000; // set word wrap
		$mail->MsgHTML($body);
		$mail->AddReplyTo("himanshu@getiitians.com","Himanshu Jain");
		$mail->AddAddress($to, "");
		$mail->IsHTML(true); // send as HTML
		return $mail->Send();
	}

}
?>
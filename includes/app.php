<?php

function ptime(){ 
	echo microtime(true)."<br>";
}


$pyfile = "mainpy.py";

function tojson($a) {
	if($a == array())
		return "{}";
	else
		return json_encode($a);
}

function replall($s, $a) {
	foreach ($a as $key => $value) {
		$s = str_replace($key, $value, $s);
	}
	return $s;
}






@session_start();

function resizeimg($filename,$tosave, $max_width, $max_height) {
	$imginfo=getimagesize($filename);
	list($orig_width, $orig_height) = $imginfo;
	$type = $imginfo[2];


	$crop_width = $orig_width;
	$crop_height = $orig_height;
	if($orig_width*$max_height <= $orig_height*$max_width){
		$crop_height = $orig_width*$max_height/$max_width;
	}
	else{
		$crop_width = $orig_height*$max_width/$max_height;
	}

	$image_p = imagecreatetruecolor($max_width, $max_height);
	switch($type){
		case "1": 
			$image = imagecreatefromgif($filename); 
			$transparent = imagecolorallocatealpha($image_p, 0, 0, 0, 127);
			imagefill($image_p, 0, 0, $transparent);
			imagealphablending($image_p, true);         
			break;
		case "2": $image = imagecreatefromjpeg($filename);break;
		case "3": 
			$image = imagecreatefrompng($filename);
			imagealphablending($image_p, false);
			imagesavealpha($image_p, true);
			break;
		default:  $image = imagecreatefromjpeg($filename);
	}
	imagecopyresampled($image_p, $image, 0, 0, ($orig_width-$crop_width)/2, ($orig_height-$crop_height)/2, $max_width, $max_height, $crop_width, $crop_height);

	$ext=pathinfo($tosave, PATHINFO_EXTENSION);

	switch($ext){
		case "gif": imagegif($image_p,$tosave); break;
		case "jpg": imagejpeg($image_p,$tosave,100); break;
		case "jpeg": imagejpeg($image_p,$tosave,100); break;
		case "png": imagepng($image_p,$tosave,0);break;
		default: imagejpeg($image_p,$tosave,100);
	}
	chmod($tosave,0777);
}


function curpathinfo() {
	return $_SERVER['PHP_SELF'];
	// if(array_key_exists("PATH_INFO", $_SERVER)) {
	// 	return substr($_SERVER["PATH_INFO"], 1);
	// } else
	// 	return "";
}

//print_r($_SERVER);

$_GET[""] = "mohit";
$_POST[""] = "mohit";
$_SESSION[""] = "mohit";
$_FILES[""] = "mohit";

$addinfo = array("ip" => $_SERVER['REMOTE_ADDR']);

$pydata = array("get"=> $_GET, "post"=> $_POST, "session"=> $_SESSION, "url"=> curpathinfo(), "file" => $_FILES, "addinfo" => $addinfo);


$cmd = "cd ".$root.";"."python ".$pyfile." \"".replall(tojson($pydata), array('\\' => '\\\\', "\t" => "\\t", "\n" => "\\n", '"' => "\\\""))."\" 2>&1";

//echo $cmd."<br>";

$pyoutp = shell_exec($cmd);

$pyoutp1 = json_decode( $pyoutp, true );
if($pyoutp1 == null)
	echo str_replace("\n", "<br>", $pyoutp);
else{
	$_SESSION = $pyoutp1["_SESSION"];
	if($pyoutp1["_header"] != "" )
		header($pyoutp1["_header"]);
	else
		echo $pyoutp1["printout"];
	foreach($pyoutp1["toresize"] as $name=>$valp) {
		resizeimg($name, $valp[0], $valp[1], $valp[2]);
	}
//	print_r( $pyoutp1["toresize"] );
}


?>
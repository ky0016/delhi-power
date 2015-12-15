<?php

$convert = array();
$convert["todb"] = array(
	"strtotime" => f('strtotime($inp)'),
);


$convert["todisp"] = array(
	"timetostr" => 	f('date("M d Y h:i a",$inp)'),
);


?>
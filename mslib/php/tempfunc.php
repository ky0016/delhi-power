<?php

$_ginfo["funcs"] = array();

$_ginfo["funcs"]["getname"] = function($data){
	$data['name'] = $data["fname"]." ".$data["lname"];
	return $data;
};

$_ginfo["funcs"]["getr"] = "getr";

$_ginfo["funcs"]["gettable"] = function($inp) {
	return array("rows" => $inp, "sqlo" => true);
}

	
?>
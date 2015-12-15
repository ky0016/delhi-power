<?php

$_ginfo["page"]=curfilename();
$_ginfo["query"]=array();


$formconv = array(
	"dob" => array(//first element is db => disp conv & second is converse
		function($inp, $add = array()) {
			mergeifunset($add, array('format' => null));
			if(isset($inp["dob"])) {
				$inp["dob"] = Fun::timetostr_t3( $inp["dob"], $add["format"]);
			}
			return $inp;
		},
		function($inp, $add = array()) {
			mergeifunset($add, array('format' => null));
			if(isset($inp["dob"])) {
				$inp["dob"] = Fun::strtotime_t3( $inp["dob"], $add["format"]);
			}
			return $inp;
		}
	),
	"name" => array(
		function($inp, $add = array()) {
			if(isset($inp["name"])){
				$msvar = explode(" ", $inp["name"]." ", 2);
				mergeifunset($inp, map(array("fname", "lname"), f('$msvar[$ind]'), array("isindexed" => true) ));
			}
			return $inp;
		}, function($inp) {
			if(isallset( array("fname", "lname"), $inp )) {
				$inp["name"] = $inp["fname"]." ".$inp["lname"];
			}
			return $inp;
		}
	)
);



?>
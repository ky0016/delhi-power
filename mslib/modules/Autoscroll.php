<?php
class Autoscroll{
	function loadchat($inp){
		foreach($inp["qresult"] as $i=>$row ){
			$row["isleft"]=($row["aid"]==$row["sid"]);

			$inp["qresult"][$i]=$row;
		}
		return $inp;
	}
}
?>
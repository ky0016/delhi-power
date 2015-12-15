<?php
class Actiondisp{
	function conv($data){
		$need=array("aid");
		$ec=1;
		$odata=0;
		if(!Fun::isAllSet($need,$data))
			$ec=-9;
		else if(!User::islogin())
			$ec=-8;
		else{
			$odata=122;
		}
		echo json_encode(array('ec'=>$ec,'data'=>$odata))."\n";
		if($ec<0){
			return;
		}
		Disps::disp_assign_conv($data["aid"]);
	}
	function chatting($data){
		$need=array("msgid");
		$ec=1;
		$odata=0;
		if(!Fun::isAllSet($need,$data))
			$ec=-9;
		echo json_encode(array('ec'=>$ec,'data'=>$odata))."\n";
		if($ec<0){
			return;
		}
		Disps::disp_chat_list($data["msgid"]);
	}
	function getgrouplist($data,$printjson=true){
		$ec=1;
		$odata=0;
		if($printjson)
			echo json_encode(array('ec'=>$ec,'data'=>$odata))."\n";
		$mymsggroup = Sqle::getA(gtable("mymsggroupdispordered", false), array("uid"=>User::loginId()));
		load_view("template/msggroup.php",array("msggroup"=> $mymsggroup ));
	}

	function profile_aboutdisp($data, $printjson = true) {
		$outp = ao();
		if($printjson)
			echo json_encode($outp)."\n";
		load_view("template/profile_aboutdisp.php", Funs::getprofile_about($data["uid"]));
	}
}
?>

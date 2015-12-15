<?php
class Actions{
	function sendchatmsg($data){
		$need=array( 'msg');
		$ec=1;
		$odata=0;
		if(!Fun::isAllSet($need,$data))
			$ec=-9;
		else if($data["msg"]!=""){
			if(!($_SESSION["chatthid"]>0)){
				$_SESSION["chatthid"]=Sqle::insertVal("chattingthread",array("ip"=>$_SERVER['REMOTE_ADDR'],"time"=>time(),"uid"=>User::loginId(),"isclosed"=>"f"));
			}
			$odata=array("msgid"=>Help::sendchatmsg($data["msg"],$_SESSION["chatthid"]) );
		}
		return array('ec'=>$ec,'data'=>$odata);
	}
	function signup($data) {
		global $_ginfo;
		$outp=array("ec"=>1,"data"=>0);
		$temp=User::signUp(Fun::getflds($_ginfo["action_constrain"]["signup"]["need"],$data));
		if($temp>0)
			$outp["data"]=$temp;
		else
			$outp["ec"]=$temp;
		return $outp;
	}
	function login($data){
		global $_ginfo;
		$outp=array("ec"=>1,"data"=>0);
		$temp=User::signIn($data["email"],$data["password"]);
		if($temp>0)
			$outp["data"]=$temp;
		else
			$outp["ec"]=$temp;
		return $outp;
	}
	function logout($data){
		User::logout();
		return array("ec"=>1,"data"=>1);
	}
	function getlogin($data){
		$outp=array("ec"=>1,"data"=>0);
		if(User::islogin()){
			$outp["data"]=gets("login");
		}
		else
			$outp["ec"]=-22;
		return $outp;
	}
	function sendmsg($data){
		$outp=array("ec"=>1,"data"=>0);
		$recvlist=intexplode("-",$data["rid"]);
		$msgdata=Fun::getflds(array("msg"),$data);
		$msgdata["msg"] = trim($msgdata["msg"]);
		if($data["msg"]!=""){
			$msgdata["time"]=time();
			$msgid=Sqle::insertVal("msgdata",$msgdata);
			$msg_table_arr=array();
			foreach($recvlist as $i=>$rid){
				$msg_table_arr[]=array(User::loginId(),$rid,User::loginId(),$msgid,'u');//u for unseen
				$msg_table_arr[]=array(User::loginId(),$rid,$rid,$msgid,'u');
			}
			$outp["data"]=Sql::query("insert into msg (sid,rid,aid,msgid,isseen) ".Fun::makeDummyTableColumns($msg_table_arr,array("sid","rid","aid","msgid","isseen"),'iiiis'));
		}
		return $outp;
	}
	function loadmsg($data){
		$loginid=User::loginId();
		$query=array("select users.name,users.profilepic, msgdata.msg, msgdata.type, msgdata.formid, msgdata.time, msg.* from msg left join msgdata on msg.msgid=msgdata.id left join users on users.id=(case when msg.aid=msg.sid then msg.rid else msg.sid end) where aid=? AND rid=? order by msg.id desc",'ii',array(&$loginid,&$data["uid"]));
		return array("ec"=>1,"data"=>Sqle::loadtables($query,'id'));
	}
	function changepassword($data){
		$outp=array("ec"=>1,"data"=>0);
		if(!User::changePassword($data["opassword"],$data["npassword"]))
			$outp["ec"]=-26;
		return $outp;
	}
	function saveuserdetails($data) {
		$outp=array("ec"=>1,"data"=>0);
		if(User::loginType()=='a' || User::loginId()==$data["uid"]){
			$data = applyconv($data, false);
			$canneed=array("name", "sign", "lang", "news", "address", "fbid", "skypeid", "email", "phone", "dob");
			$toupdate=Fun::getflds($canneed, $data);
			$myf=User::userProfile(null, array("email"=>getval("email",$toupdate,'')));
			if(isset($toupdate["email"]) && !( $myf==null || $myf["id"]==$data["uid"] )){
				$outp["ec"] = -16;
			} else{
				$outp["data"] = Sqle::updateVal("users",$toupdate,array("id"=>$data["uid"]));
			}
		} else
			$outp["ec"]=-2;
		return $outp;
	}

	function contactus($data) {
		$outp = ao();
		$outp["data"] = msmail("contactus.txt", $data);
		return $outp;
	}

	function forgotpass($data) {
		$outp = array("ec"=>1,"data"=>0);
		if(!(User::passreset($data["email"]))) {
			$outp["ec"] = -6;
		}
		return $outp;
	}


}
?>
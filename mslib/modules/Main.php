<?php
class Main{
	function v(){
		$args =func_get_args();
		if(count($args) > 0) {
			Fun::runmain($args[0], array_slice($args, 1));
		} else{
			echo "Need more Arguments.";
		}
	}

	function index(){
		if(isget("logout")) {
			User::logout();
			Fun::redirect(HOST);
		}
		load_view("index.php");
	}

	function aboutus(){
		load_view("aboutus.php");
	}

	function contactus(){
		$pageinfo = array();
		$pageinfo["msg"] = "";
		if(ispost("contactus")) {
			$ho = handle_request($_POST, "contactus");
			$pageinfo["msg"] = rit("Thank you for contacting us.", $ho["ec"]>0 );
		}
		load_view("contactus.php", $pageinfo);
	}

	function login(){
		$pageinfo = emptyarr(a("loginmsg"));
		if(ispost("login")) {
			$ho = handle_request($_POST, "login");
			$pageinfo["loginmsg"] = errormsg($ho["ec"]);
			Fun::redirect(BASE."profile", $ho["ec"] > 0);
		}
		load_view("login.php", $pageinfo);
	}

	function signup() {
		$pageinfo = emptyarr(a("signupmsg"));
		if(ispost("signup")) {
			$ho = handle_request($_POST, "signup");
			$pageinfo["signupmsg"] = errormsg($ho["ec"]);
			Fun::redirect(BASE."profile", $ho["ec"] > 0);
		}
		load_view("signup.php", $pageinfo);
	}

	function profile($uid = 0 ) {
		$uid = Fun::profileid($uid);
		Fun::redirect(HOST, $uid == 0);
		if(isset($_FILES["profilepic"]) && User::islogin() ) {
			Fun::uploadpic($_FILES["profilepic"], "profilepic", "profilepicbig", 300);
		}

		$uinfo = Funs::getprofile_about($uid);
		$pageinfo = $uinfo;

		if( $uinfo["type"] == "f" ) {
		} else if( $uinfo["type"] == "u") {
		} else if( $uinfo["type"] == "a") {
		}

		load_view("profile.php", $pageinfo);
	}

	function chat() {
		Fun::redirect(HOST, lid()==0);
		$pageinfo = array();
		$pageinfo['cansendlist'] = Fun::dbarrtooption(Funs::cansend(),"id","name");

		load_view("chat.php", $pageinfo);
	}
}
?>








# 	function load_view($view, $inp = array()) {
# 		global $view_default,$_ginfo;
# 		if(isset($view_default[$view]))
# 			$inp=Fun::mergeifunset($inp,$view_default[$view]);
# 		$inp=Fun::setifunset($inp,"page", getNameFromUrl(Fun::getcururl()));
# 		$inp=Fun::setifunset($inp,"islogin",User::loginType());
# 		$tem_name=Fun::getloadviewname($view);
# 		$templates=new Templates();
# 		if(method_exists($templates,$tem_name )){
# 			$templates->$tem_name($inp);
# 			return true;
# 		}
# 		else{
# 			$view = gi("loadviewfile").$view;
# 			if(file_exists($view)){
# 				foreach($inp as $key=>$val){
# 					$$key=$val;
# 				}
# 				include $view;
# 				return true;
# 			}
# 			else{
# 				echo "MM Error : Unable to load view ".$view." Line ".__LINE__." in file ".__FILE__ ;
# 				return false;
# 			}
# 		}
# 	}


# 	function curfilename(){
# 		$cfname=firstelm(explode(".",lastelm(explode("/",$_SERVER['SCRIPT_FILENAME']))));
# 		if($cfname==='')
# 			$cfname="index";
# 		return $cfname;
# 	}

# 	function getmyneed($fname) {
# 		global $_ginfo;
# 		return $_ginfo["action_constrain"][$fname]["need"];
# 	}


# 	function handle_request($post_data, $action=null, $isdisp = false) {
# 		$a=new Actions();
# 		$outp=array("ec"=>-7);
# 		setift($post_data["action"], $action, $action!==null);
# 		$req = null;
# 		if(isset($post_data["action"]) ){
# 			$func=$post_data["action"];
# 			if( getval($post_data["action"], gi("action_constrain") ) !== null ) {
# 				$spec = mius( getval($post_data["action"], gi("action_constrain")) , f_action_constrain_default() );
# 				setift($spec["users"], gi("users"), $spec["users"] === "all");
# 				$spec["action"] = $post_data["action"];
# 				$post_data = f_deletekeys($post_data, array("action"));
# 				$isvalid = f_isvalid_action($post_data, $spec);
# 				if(!($isvalid>0))
# 					$outp["ec"]=$isvalid;
# 				else{
# 					$req = f_setinput($post_data, $spec);
# 					$outp["data"] = f_handle_db_request($req);
# 					$outp["ec"] = 1;
# 					if( method_exists($a, $func) )
# 						$outp = $a->$func($req["data"]);
# 				}
# 			} else {
# 				if(method_exists($a, $func))
# 					$outp = $a->$func($post_data);
# 			}
# 		}
# 		if(!$isdisp )
# 			return $outp;
# 		else {
# 			echo json_encode($outp)."\n";
# //			msprint($req);
# 			if($req === null || $req["view"] === null || $outp["ec"] < 0 )
# 				return;
# 			f_disp_action($req);
# 		}
# 	}

# 	function resizeimg($filename,$tosave, $max_width, $max_height){
# 		$imginfo=getimagesize($filename);
# 		list($orig_width, $orig_height) = $imginfo;
# 		$type = $imginfo[2];


# 		$crop_width = $orig_width;
# 		$crop_height = $orig_height;
# 		if($orig_width*$max_height <= $orig_height*$max_width){
# 			$crop_height = $orig_width*$max_height/$max_width;
# 		}
# 		else{
# 			$crop_width = $orig_height*$max_width/$max_height;
# 		}

# 		$image_p = imagecreatetruecolor($max_width, $max_height);
# 		switch($type){
# 			case "1": 
# 				$image = imagecreatefromgif($filename); 
# 				$transparent = imagecolorallocatealpha($image_p, 0, 0, 0, 127);
# 				imagefill($image_p, 0, 0, $transparent);
# 				imagealphablending($image_p, true);         
# 				break;
# 			case "2": $image = imagecreatefromjpeg($filename);break;
# 			case "3": 
# 				$image = imagecreatefrompng($filename);
# 				imagealphablending($image_p, false);
# 				imagesavealpha($image_p, true);
# 				break;
# 			default:  $image = imagecreatefromjpeg($filename);
# 		}
# 		imagecopyresampled($image_p, $image, 0, 0, ($orig_width-$crop_width)/2, ($orig_height-$crop_height)/2, $max_width, $max_height, $crop_width, $crop_height);

# 		$ext=pathinfo($tosave, PATHINFO_EXTENSION);

# 		switch($ext){
# 			case "gif": imagegif($image_p,$tosave); break;
# 			case "jpg": imagejpeg($image_p,$tosave,100); break;
# 			case "jpeg": imagejpeg($image_p,$tosave,100); break;
# 			case "png": imagepng($image_p,$tosave,0);break;
# 			default: imagejpeg($image_p,$tosave,100);
# 		}
# 		chmod($tosave,0777);
# 	}
# 	function getrefarr(&$inp){
# 		$outp=array();
# 		foreach($inp as $i=>$val){
# 			$outp[] = &$inp[$i];
# 		}
# 		return $outp;
# 	}

# 	function gtable($name, $alias=true) {
# 		global $_ginfo;
# 		return ($alias ? ("(".$_ginfo["query"][$name].") ".$name) : $_ginfo["query"][$name]);
# 	}

# 	function errormsg($ec, $cnd=true) {
# 		global $_ginfo;
# 		return (($ec<0 && $cnd) ?getval($ec, $_ginfo["error"], "Error : ".$ec):"");
# 	}

# 	function autoscroll($post_data){
# 		global $_ginfo;
# 		$action_spec=$_ginfo["autoscroll"][$post_data["action"]];
# 		mergeifunset($action_spec, array('sort'=>'', 'maxl'=>null, 'minl'=>null, "filterfunc"=>null, "load_view"=>"template/".$post_data["action"].".php" ));
# 		$fixed=array("uid"=>User::loginId(), "time"=>time());
# 		$post_data=Fun::mergeforce($post_data, $fixed);
# 		$qoutput=Sqle::autoscroll($action_spec["query"], $post_data, $action_spec["key"], $action_spec["sort"], $post_data["isloadold"], $action_spec["minl"], $action_spec["maxl"]);
# 		if($action_spec["filterfunc"]!==null){
# 			$autos=new Autoscroll();
# 			$funcname=$action_spec["filterfunc"];
# 			if(method_exists($autos, $funcname))
# 				$qoutput=$autos->$funcname($qoutput);
# 		}
# 		$qoutput["load_view"]=$action_spec["load_view"];
# 		return $qoutput;
# 	}

# 	function isvalid_action($post_data) {//to be deleted
# 	/*Checks whether all the fields in post data are set or not according to g_info["action_constraint"] requirements
# 	 Arguments: $post_data: Input data array
# 	*/
# 		global $_ginfo;
# 		if(isset($_ginfo["action_constrain"][$post_data["action"]])){
# 			$sarr=$_ginfo["action_constrain"][$post_data["action"]];
# 			$sarr=Fun::mergeifunset($sarr,array("users"=>"","need"=>array()));
# 			if(!(($sarr["users"]=="all" && User::islogin()) || $sarr["users"]=="" || ($sarr["users"] != "all" && in_array(User::loginType(), $sarr["users"])) ))
# 				return -2;
# 			if(!Fun::isAllSet($sarr["need"], $post_data))
# 				return -9;
# 		}
# 		return true;
# 	}

# 	function handle_disp($post_data,$actionarg=null){
# 		global $_ginfo;
# 		if($actionarg!=null)
# 			$post_data["action"]=$actionarg;
# 		$a=new Actiondisp();
# 		$outp=array("ec"=>-7);
# 		if(isset($post_data["action"])  ){
# 			$isvalid=isvalid_action($post_data);
# 			if(!($isvalid>0))
# 				$outp["ec"]=$isvalid;
# 			else{
# 				$func=$post_data["action"];
# 				if( method_exists($a,$post_data["action"])){
# 					$a->$func($post_data,$actionarg==null);
# 					return;
# 				}
# 				else if(islset($_ginfo,array("autoscroll",$post_data["action"]))) {
# 					$as_handle = autoscroll($post_data);
# 					$outp["data"]=Fun::getflds(array("min", "max", "minl", "maxl", "qresultlen"), $as_handle);
# 					$outp["ec"]=1;
# 					if($actionarg==null)
# 						echo json_encode($outp)."\n";
# 					load_view($as_handle["load_view"], $as_handle);
# 					return;
# 				}
# 			}
# 		}
# 		if($actionarg==null)
# 			echo json_encode($outp)."\n";
# 	}

# 	function getNameFromUrl($url) {
# 		$arr=Fun::myexplode('/',$url);
# 		$index=array_search('welcome', $arr)+1;
# 		if(!(isset($arr[$index])) || $arr[$index]==='' || $arr[$index]==='#')
# 			return 'index';
# 		else if(strpos($arr[$index],'?')!==false) {
# 			$ok=Fun::myexplode('?',$arr[$index]);
# 			return $ok[0];
# 		}
# 		return $arr[$index];
# 	}

# 	function g($inp) {
# 		global $$inp;
# 		return $$inp;
# 	}

# 	function s($inp, $val=null) {
# 		global $$inp;
# 		$$inp = $val;
# 	}

# 	function gi($inp) {
# 		return getval($inp, g("_ginfo"));
# 	}

# 	function listget() {
# 		$args = func_get_args();
# 		$inplist = array_slice($args, 1);
# 		$outp = getval(0,$args);
# 		foreach($inplist as $i => $val) {
# 			$outp = getval( $val, $outp );
# 		}
# 		return $outp;
# 	}

# 	function gget() {
# 		$args = func_get_args();
# 		$args[0] = g(getval(0, $args));
# 		return call_user_func_array("listget", $args);
# 	}

# 	function giget() {
# 		$args = func_get_args();
# 		$args[0] = gi(getval(0, $args));
# 		return call_user_func_array("listget", $args);
# 	}
	
# 	function filter($list, $boolfunc) {
# 		$outp = array();
# 		foreach($list as $i => $val) {
# 			if($boolfunc($val, $i) === true) {
# 				$outp[] = $val;
# 			}
# 		}
# 		return $outp;
# 	}

# 	function map($list ,$func, $custom=array()) {
# 		mergeifunset($custom, array("isindexed" => false, "ismapkey"=>false));
# 		$outp = array();
# 		foreach($list as $i => $val) {
# 			if($custom["ismapkey"] )
# 				$outp[ $func($i) ] = $val;
# 			else
# 				$outp[($custom["isindexed"]?$val:$i)] = $func($val, $i);
# 		}
# 		return $outp;
# 	}

# 	function add($a, $b) {
# 		if(gettype($a) === "array" && gettype($b) === "array" ) {
# 			return Fun::array_append($a, $b);
# 		} else if (gettype($a) === "array" && gettype($b) === "integer") {
# 			return Fun::array_addinall($a, $b);
# 		}
# 	}

# 	function rem($a, $b) {
# 		if(gettype($a) === 'array' && gettype($b) === 'array') {
# 			return f_array_a_minus_b($a, $b);
# 		}
# 	}

# 	function msvalprint($inp) {//recursive function.
# 		if(gettype($inp) === "array") {
# 			$isnindex = (array_keys($inp) === Fun::oneToN(count($inp)-1, 0));//is natural indexed
# 			$otext = map(array_keys($inp), function($ind) use($isnindex, $inp) {
# 				return ($isnindex?"":"'".$ind."'=>").msvalprint($inp[$ind]);
# 			});
# 			return "array(".implode(", ", $otext).")";
# 		} else if(gettype($inp) === 'integer') {
# 			return $inp;
# 		} else if(gettype($inp) === 'boolean') {
# 			return tf($inp);
# 		} else if($inp === null) {
# 			return "null";
# 		} else {
# 			$inp = str_replace("'", "\\'", "".$inp);
# 			return "'".$inp."'";
# 		}
# 	}

# 	function msimplode($glue, $inp, $defval=null) {
# 		 return (count($inp) === 0 && $defval !== null ) ? $defval : implode($glue, $inp);
# 	}

# 	function f($content) {
# 		global $msvar;
# 		$af = function($inp, $ind=0) use ($content, $msvar) {
# 			$content = '$foutput  = '.$content.';';
# 			eval($content);
# 			return $foutput;
# 		};
# 		return $af;
# 	}

# 	function ao() {
# 		return array("ec" => 1, "data" => 0);
# 	}

# 	function msmail($file, $data = array(), $to=null) {
# 		setifnn($to, gi("adminmail"));
# 		Fun::mailfromfile($to, gi("mailfile").$file, $data);
# 	}

# 	function emptyarr($inp) {
# 		return map($inp, f('""'), array("isindexed" => true));
# 	}

# 	function a() {
# 		return func_get_args();
# 	}

# 	function da() {
# 		$args = func_get_args();
# 		$outp = a();
# 		for($i = 0; $i < count($args)-1; $i+=2) {
# 			$outp[$args[$i]] = $args[$i+1];
# 		}
# 		return $outp;
# 	}

# 	function fixedlen($inp, $len=20) {
# 		return Fun::limitlen($len, Fun::inclen($len, $inp));
# 	}

# 	function mystr_repeat($str, $len) {
# 		if($len>0)
# 			return str_repeat($str, $len);
# 		else
# 			return "";
# 	}

# 	function lid() {
# 		return (0+User::loginId());
# 	}

# 	function applyconv($inp, $isdbtodisp = true, $onlythese = null, $conva = null) {
# 		setifnn($conva, g("formconv"));
# 		setifnn($onlythese, array_keys($conva));
# 		foreach($onlythese as $i => $key) {
# 			$conv = $conva[$key][(1-$isdbtodisp)];
# 			$inp = $conv($inp);
# 		}
# 		return $inp;
# 	}

# 	function isallset($alist, $data){
# 		for($i=0;$i<count($alist);$i++)
# 			if( ! isset($data[ $alist[$i] ]) )
# 				return false;
# 		return true;
# 	}

# 	function in($elm, $arr) {
# 		return in_array($elm, $arr, true);
# 	}

# 	function getA($query, $param = array()) {
# 		if(gettype($query) == 'array') {
# 			siu(&$query, 1, array());
# 			return Sqle::getA($query[0], $query[1]);
# 		} else {
# 			return Sqle::getA($query, $param);
# 		}
# 	}

# 	function q($query, $param = array()) {
# 		if(gettype($query) == 'array') {
# 			siu(&$query, 1, array());
# 			return Sqle::q($query[0], $query[1]);
# 		} else {
# 			return Sqle::q($query, $param);
# 		}
# 	}

# 	function t($tablename) {
# 		$tf = gi("table_prifix");
# 		return $tf.rit("_", $tf!==null).$tablename;
# 	}

# 	function getr($inp) {//get one row of sql.
# 		return (count($inp)>0) ? $inp[0]:null;
# 	}
























# 	function sessm($key, $val) {
# 		return (isset($_SESSION[$key]) && $_SESSION[$key]===$val);
# 	}

# 	function init_db() {
# 		global $DB,$db_data;
# 		if($DB===null){
# 			$DB = new mysqli( $db_data['host'] , $db_data['user'] , $db_data['pass'] , $db_data['db']);
# 			Sql::init($DB);
# 		}
# 	}

# 	function closedb() {
# 		global $DB;
# 		if($DB!==null)
# 			$DB->close();
# 	}
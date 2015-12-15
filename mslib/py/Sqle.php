<?php
class Sqle extends Sql{

	public static function autoscroll($query, $param, $key, $sort='', $isloadold=true ,$minl=null, $maxl=null){
		setifnn($minl, $param["minl"]);
		setifnn($maxl, $param["maxl"]);
		if($key!=null){
			if($isloadold)
				$querylimit = "select * from (".gtable($query, false).") outpquery where ($key<{min} OR {min}=-1) ".($param["minl"]==-1?'':"limit {minl} ");
			else
				$querylimit = "select * from (".gtable($query, false).") outpquery where $key>{max} ".($param["maxl"]==-1?'':"limit {maxl} ");
		} else{//max,maxl must be +ve int
			$querylimit="select * from (".$query.") outpquery limit {maxl} offset {max} ";
		}
		if($key!=null)
			$querysort="select * from (".$querylimit.") sortquery ".$sort;
		else
			$querysort=$querylimit;
		$qresult=Sqle::getA($querysort,$param);
		$outp["qresult"]=$qresult;
		$outp["maxl"]=$maxl;
		$outp["minl"]=$minl;
		$outp["qresultlen"]=count($qresult);
		if($key==null){
			$outp["max"]=$param["max"]+$param["maxl"];
		} else{
			if(count($qresult)==0){
				$outp["min"] = $param["min"];
				$outp["max"] = $param["max"];
			} else{
				$e1=$qresult[0][$key];
				$e2=$qresult[count($qresult)-1][$key];
				$s=new Special();
				$outp["min"] = $s->min($e1, $e2, $param["min"]);
				$outp["max"] = $s->max($e1, $e2, $param["max"]);
			}
		}
		return $outp;
	}
}
?>
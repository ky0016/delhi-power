<?php
class Templates{
  function input($inp){
    foreach($inp as $key=>$val)
      $$key=$val;
    if($id==null)
      $id=$name;
    $inpattr=Fun::mergeifunset($inpattr,array("name"=>$name,"type"=>$type,"class"=>"validate","dc"=>$dc,"onkeyup"=>"checkValid(this,event);","id"=>$id));
    mergeifunset($divattr,array("class"=>"row"));
?>
            <div <?php echo param2str($divattr); ?>  >
              <div class="input-field col s12 m12">
                <input <?php echo param2str($inpattr); ?> >
                <label for='<?php echo $id; ?>' ><?php echo $label; ?></label>
              </div>
            </div>
<?php
  }

	function input1($inp){
		foreach($inp as $key=>$val)
			$$key=$val;
		$inpattr=Fun::mergeifunset($inpattr,array("name"=>$name,"type"=>$type,"class"=>"form-control","dc"=>$dc,"onkeyup"=>"checkValid(this,event);"));
		mergeifunset($divattr,array("class"=>"form-group"));
?>
              <div <?php echo param2str($divattr); ?> >
               <label class="col-md-2 control-label">
                <?php echo $label; ?>
               </label>
               <div class="col-md-10">
                <input <?php echo param2str($inpattr); ?> />
               </div>
              </div>
<?php
	}
  function check1($inp){
    foreach($inp as $key=>$val)
      $$key=$val;
    mergeifunset($inpattr,array("class"=>$class.'filled-in',"id"=>$id==''?'':"check_".$id,"onchange"=>$onchange,"type"=>"checkbox", "value"=>$value, 'checked'=>'',"name"=>$name ));
?>
             <input <?php echo param2str($inpattr); ?>  />
             <label for="<?php echo $inpattr["id"]; ?>" >
              <?php echo $label; ?>
             </label><br>
<?php    
  }

  function input3($inp) {
    foreach($inp as $key=>$val)
      $$key=$val;
    mergeifunset($inpattr,array("name"=>$name,"type"=>$type, "dc"=>$dc, "id" =>rit("input3_".$id, $id!='') ));
    mergeifunset($divattr,array("class"=>$divclass));
?>
  <div <?php echo param2str($divattr); ?> >
    <input <?php echo param2str($inpattr); ?> >
    <label for="<?php echo $inpattr["id"]; ?>" ><?php echo $label; ?></label>
  </div>
<?php
  }
}
?>
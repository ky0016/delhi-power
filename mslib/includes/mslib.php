<?php
include "includes/app.php";

$config = array("needprofile" => true );

Fun::runmain(curfilename(), Fun::geturlargs());

closedb();
?>
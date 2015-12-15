<?php

mysql_connect("localhost", "root", "");
mysql_select_db("power");


$table=  mysql_query("select * from tbl_coal_gen");
$list=array();
        while($row=  mysql_fetch_array($table)){
    $obj=new stdClass();
   
        $obj->date=$row[0];
        $obj->target=$row[1];
         $obj->actual=$row[2];
         
        
        
        
    $list[]=$obj;
        }
        echo json_encode($list);
        mysql_close();

?>

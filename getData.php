<?php 

// This is just an example of reading server side data and sending it to the client.
// It reads a json formatted text file and outputs it.
$json = file_get_contents('check.json');
//$obj = json_decode($json);
echo $json;

//$string = file_get_contents("check.json");
//echo $string;

// Instead you can query your database and parse into JSON etc etc

?>
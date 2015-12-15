
<?php

//include 'json.php';
//echo file_get_contents('json.php',TRUE);
$date = "2015-12-12";
ini_set("display_errors", 0);
mysql_connect("localhost", "root", "");
mysql_select_db("power");

if (count($_POST) > 0) {
   // $date = $_POST['date'];
    $d = date_parse_from_format("Y-m-dd", $date);
    $month = $d["month"];
    $year = $d["year"];
    $day = $d["day"];
    $queries = array(); //total queries to be done
    $sumYTD = new SplFixedArray(10); //
    $sumMTD = new SplFixedArray(10);
    $valueToday = new SplFixedArray(10);
    $queries['target_power'] = mysql_query("SELECT date  , target FROM  tbl_total_power ");
    $queries['actual_power'] = mysql_query("SELECT date  , actual FROM  tbl_total_power ");
    $queries['target_coal'] = mysql_query("SELECT date  , target FROM  tbl_coal_gen ");
    $queries['actual_coal'] = mysql_query("SELECT date  , actual FROM  tbl_coal_gen ");
    $queries['target_ntpc'] = mysql_query("SELECT date  , target FROM  tbl_ntpc_gen ");
    $queries['actual_ntpc'] = mysql_query("SELECT date  , actual FROM  tbl_ntpc_gen ");
    $queries['target_gas'] = mysql_query("SELECT date  , target FROM  tbl_gas_gen ");
    $queries['actual_gas'] = mysql_query("SELECT date  , actual FROM  tbl_gas_gen ");
    $queries['target_hydro'] = mysql_query("SELECT date  , target FROM  tbl_hydro_gen ");
    $queries['actual_hydro'] = mysql_query("SELECT date  , actual FROM  tbl_hydro_gen ");
    $ind = array_keys($queries);
    $allQueries = array();
    $efficiency = array();
    $i = 0;
    foreach ($queries as $query) {
        if (!$query) {
            echo mysql_error();
            die;
        }
        $data = array();
        $sumYTD[$i] = 0;
        $sumMTD[$i] = 0;
        $valueToday[$i] = 0;
        for ($x = 0; $x < mysql_num_rows($query); $x++) {
            $data[] = mysql_fetch_assoc($query);
            if ($data[$x]["date"] <= $date && date('Y', strtotime($data[$x]["date"])) == $year) {
                if ($i % 2 == 0) {
                    $sumYTD[$i]+=$data[$x]["target"];
                }
                if ($i % 2 == 1) {
                    $sumYTD[$i]+=$data[$x]["actual"];
                }
                if (date('m', strtotime($data[$x]["date"])) == $month) {
                    if ($i % 2 == 0) {
                        $sumMTD[$i]+=$data[$x]["target"];
                    } else {
                        $sumMTD[$i]+=$data[$x]["actual"];
                    }
                }
                if ($data[$x]["date"] == $date) {
                    if ($i % 2 == 0) {
                        $valueToday[$i]+=$data[$x]["target"];
                    } else {
                        $valueToday[$i]+=$data[$x]["actual"];
                    }
                }
            }
        }
        $allQueries[$ind[$i]] = array('valueToday' => $valueToday[$i], 'sumMTD' => $sumMTD[$i], 'sumYTD' => $sumYTD[$i], 'date' => $date);
        $i++;
    }
    //print_r($sumMTD);
    $efficiency['power'] = array('valueTodayEff' => 0, 'sumMTD_eff' => 0, 'sumYTD_eff' => 0);
    $efficiency['coal'] = array('valueTodayEff' => 0, 'sumMTD_eff' => 0, 'sumYTD_eff' => 0);
    $efficiency['ntpc'] = array('valueTodayEff' => 0, 'sumMTD_eff' => 0, 'sumYTD_eff' => 0);
    $efficiency['gas'] = array('valueTodayEff' => 0, 'sumMTD_eff' => 0, 'sumYTD_eff' => 0);
    $efficiency['hydro'] = array('valueTodayEff' => 0, 'sumMTD_eff' => 0, 'sumYTD_eff' => 0);
    $keys = array_keys($efficiency);
    for ($i = 0; $i < 10; $i = $i + 2) {
        if ($valueToday[$i] != 0 && $sumMTD[$i] != 0 && $sumYTD[$i] != 0) {
            $efficiency[$keys[$i / 2]] = array('valueTodayEff' => ($valueToday[$i + 1] / $valueToday[$i]) * 100, 'sumMTD_eff' => ($sumMTD[$i + 1] / $sumMTD[$i]) * 100, 'sumYTD_eff' => $sumYTD[$i + 1] / $sumYTD[$i] * 100);
        } else {
            $efficiency[$keys[$i / 2]] = array('valueTodayEff' => 0, 'sumMTD_eff' => ($sumMTD[$i + 1] / $sumMTD[$i]) * 100, 'sumYTD_eff' => ($sumYTD[$i + 1] / $sumYTD[$i]) * 100);
        }
    }
    $json_str = json_encode($efficiency);
    //echo $json_str;
   // print_r($efficiency);
    
    $fp = fopen('test.json', 'w');
    fwrite($fp, $json_str);
    fclose($fp);
}
?>

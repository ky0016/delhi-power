<html>
    <head>
        <title>Form</title>
        <link rel="stylesheet" type="text/css" href="styles.css" />
    </head>
    <body>
        <form name="frmUser" method="post" action="" >
            <div style="width:500px;">
                <div class="message"><?php
if (isset($message)) {
    $mess = explode(":", $message);
    if ($mess[0] == "Coal") {
        echo $message;
    } else {
        
    }
}
?>  </div>
                <div class="heading">  Date </div>
                <table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">
                    <tr>
                        <td><label></label></td>
                        <td><input type="text" name="id" class="txtField" value="date" hidden="true"></td>
                    </tr>
                    <tr>
                        <td><label>Date</label></td>
                        <td><input type="date" name="date" class="txtField" value=""></td>
                    </tr>
                    <tr>
                        <td colspan="2"><input type="submit" name="submit1" value="Submit" class="btnSubmit"></td>
                    </tr>
                </table>
            </div>
        </form>

        <br />

    </body></html>
<?php
mysql_connect("localhost", "root", "");
mysql_select_db("power");
if (count($_POST) > 0) {
    $date = $_POST['date'];
    $d = date_parse_from_format("Y-m-dd", $date);
    $month = $d["month"];
    $year = $d["year"];
    $day = $d["day"];
    $queries = new SplFixedArray(10); //total queries to be done
    $sumYTD = new SplFixedArray(10); //
    $sumMTD = new SplFixedArray(10);
    $valueToday = new SplFixedArray(10);
    $queries[0] = mysql_query("SELECT date  , target FROM  tbl_total_power ");
    $queries[1] = mysql_query("SELECT date  , actual FROM  tbl_total_power ");
    $queries[2] = mysql_query("SELECT date  , target FROM  tbl_coal_gen ");
    $queries[3] = mysql_query("SELECT date  , actual FROM  tbl_coal_gen ");
    $queries[4] = mysql_query("SELECT date  , target FROM  tbl_ntpc_gen ");
    $queries[5] = mysql_query("SELECT date  , actual FROM  tbl_ntpc_gen ");
    $queries[6] = mysql_query("SELECT date  , target FROM  tbl_gas_gen ");
    $queries[7] = mysql_query("SELECT date  , actual FROM  tbl_gas_gen ");
    $queries[8] = mysql_query("SELECT date  , target FROM  tbl_hydro_gen ");
    $queries[9] = mysql_query("SELECT date  , actual FROM  tbl_hydro_gen ");
    for ($i = 0; $i < 10; $i++) {
        if (!$queries[$i]) {
            echo mysql_error();
            die;
        }
        $data = array();
        $sumYTD[$i] = 0;
        $sumMTD[$i] = 0;
        $valueToday[$i] = 0;
        for ($x = 0; $x < mysql_num_rows($queries[$i]); $x++) {
            $data[] = mysql_fetch_assoc($query[$i]);
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
                    $valueToday[$i] = 0;
                }
            }
        }
    }
}
?>






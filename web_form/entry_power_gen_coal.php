<?php
mysql_connect("localhost", "root", "");
mysql_select_db("power");



if (count($_POST) > 0) {

    $date = $_POST['date'];
    $target_power = $_POST['target_power'];
    $actual_power = $_POST['actual_power'];
    $id = $_POST['id'];

    if ($id == "coal") {


        $query = mysql_query("insert into tbl_coal_gen values ('{$date}','{$target_power}','{$actual_power}')");


        if ($query) {
            $message = "Total:" . "Record Added Successfully";
        } else {
            $message = "Coal:" . mysql_error();
        }
    }

    if ($id == "total") {
       /* $d = date_parse_from_format("Y-m-d", $date);
        $month= $d["month"];
        $year= $d["year"];
        */
        $query = mysql_query("insert into tbl_total_power values ('{$date}','{$target_power}','{$actual_power}')");        

        if ($query) {

            $message = "Total:" . "Record Added Successfully";
        } else {
            $message = "Total:" . mysql_error();
        }
    }


    if ($id == "ntpc") {
        $query = mysql_query("insert into tbl_ntpc_gen values ('{$date}','{$target_power}','{$actual_power}')");


        if ($query) {

            $message = "NTPC:" . "Record Added Successfully";
        } else {
            $message = "NTPC:" . mysql_error();
        }
    }


    if ($id == "gas") {
        $query = mysql_query("insert into tbl_gas_gen values ('{$date}','{$target_power}','{$actual_power}')");


        if ($query) {

            $message = "Gas:" . "Record Added Successfully";
        } else {
            $message = "Gas:" . mysql_error();
        }
    }

    if ($id == "hydro") {
        $query = mysql_query("insert into tbl_hydro_gen values ('{$date}','{$target_power}','{$actual_power}')");


        if ($query) {

            $message = "Hydro:" . "Record Added Successfully";
        } else {
            $message = "Hydro:" . mysql_error();
        }
    }
}
?>
<html>
    <head>


        <title>Entry Form</title>


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
?></div>

                <div class="heading">  Coal Entry </div>
                <table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">


                    <tr>
                        <td><label></label></td>
                        <td><input type="text" name="id" class="txtField" value="coal" hidden="true"></td>
                    </tr>

                    <tr>
                        <td><label>Date</label></td>
                        <td><input type="date" name="date" class="txtField" value=""></td>
                    </tr>


                    <tr>
                        <td><label>Target Power</label></td>
                        <td><input type="text" name="target_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td><label>Actual Power</label></td>
                        <td><input type="text" name="actual_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td colspan="2"><input type="submit" name="submit" value="Submit" class="btnSubmit"></td>
                    </tr>
                </table>
            </div>
        </form>

        <br />

        <form name="frmUser1" method="post" action="" style="  display: inline; ">
            <div style="width:500px;">
                <div class="message"><?php
                    if (isset($message)) {



                        $mess = explode(":", $message);

                        if ($mess[0] == "Total") {
                            echo $message;
                        } else {
                            
                        }
                    }
?></div>

                <div class="heading">  Total Entry </div>
                <table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">


                    <tr>
                        <td><label></label></td>
                        <td><input type="text" name="id" class="txtField" value="total" hidden="true"></td>
                    </tr>

                    <tr>
                        <td><label>Date</label></td>
                        <td><input type="date" name="date" class="txtField" value=""></td>
                    </tr>


                    <tr>
                        <td><label>Target Power</label></td>
                        <td><input type="text" name="target_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td><label>Actual Power</label></td>
                        <td><input type="text" name="actual_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td colspan="2"><input type="submit" name="submit1" value="Submit" class="btnSubmit"></td>
                    </tr>
                </table>
            </div>
        </form>


        <form name="frmUser2" method="post" action="">
            <div style="width:500px;">
                <div class="message"><?php
                    if (isset($message)) {



                        $mess = explode(":", $message);

                        if ($mess[0] == "ntpc") {
                            echo $message;
                        } else {
                            
                        }
                    }
?></div>

                <div class="heading">  NTPC Entry </div>
                <table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">


                    <tr>
                        <td><label></label></td>
                        <td><input type="text" name="id" class="txtField" value="ntpc" hidden="true"></td>
                    </tr>

                    <tr>
                        <td><label>Date</label></td>
                        <td><input type="date" name="date" class="txtField" value=""></td>
                    </tr>


                    <tr>
                        <td><label>Target Power</label></td>
                        <td><input type="text" name="target_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td><label>Actual Power</label></td>
                        <td><input type="text" name="actual_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td colspan="2"><input type="submit" name="submit1" value="Submit" class="btnSubmit"></td>
                    </tr>
                </table>
            </div>
        </form>


        <form name="frmUser3" method="post" action="">
            <div style="width:500px;">
                <div class="message"><?php
                    if (isset($message)) {



                        $mess = explode(":", $message);

                        if ($mess[0] == "Gas") {
                            echo $message;
                        } else {
                            
                        }
                    }
?></div>

                <div class="heading">  Gas Entry </div>
                <table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">


                    <tr>
                        <td><label></label></td>
                        <td><input type="text" name="id" class="txtField" value="gas" hidden="true"></td>
                    </tr>

                    <tr>
                        <td><label>Date</label></td>
                        <td><input type="date" name="date" class="txtField" value=""></td>
                    </tr>


                    <tr>
                        <td><label>Target Power</label></td>
                        <td><input type="text" name="target_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td><label>Actual Power</label></td>
                        <td><input type="text" name="actual_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td colspan="2"><input type="submit" name="submit1" value="Submit" class="btnSubmit"></td>
                    </tr>
                </table>
            </div>
        </form>   



        <form name="frmUser4" method="post" action="">
            <div style="width:500px;">
                <div class="message"><?php
                    if (isset($message)) {



                        $mess = explode(":", $message);

                        if ($mess[0] == "hydro") {
                            echo $message;
                        } else {
                            
                        }
                    }
?></div>

                <div class="heading">  Hydro Entry </div>
                <table border="0" cellpadding="10" cellspacing="0" width="500" align="center" class="tblSaveForm">


                    <tr>
                        <td><label></label></td>
                        <td><input type="text" name="id" class="txtField" value="hydro" hidden="true"></td>
                    </tr>

                    <tr>
                        <td><label>Date</label></td>
                        <td><input type="date" name="date" class="txtField" value=""></td>
                    </tr>


                    <tr>
                        <td><label>Target Power</label></td>
                        <td><input type="text" name="target_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td><label>Actual Power</label></td>
                        <td><input type="text" name="actual_power" class="txtField" value=""></td>
                    </tr>

                    <tr>
                        <td colspan="2"><input type="submit" name="submit1" value="Submit" class="btnSubmit"></td>
                    </tr>
                </table>
            </div>
        </form>


    </body></html>






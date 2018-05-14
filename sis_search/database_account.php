<?php
    //Connect to database.
    $database_address = "localhost";
    $account = "root";
    $password = "root";
    $con = mysqli_connect($database_address,$account,$password);
    mysqli_select_db($con,"sis");
?>
<?php
include_once "functions.php";
dbConnect();

$username = $_POST['user'];
$password = $_POST['pass'];

if (loginValidate($username, $password))
{
    echo "1";
}
else
{
    echo "0";
}
mysql_close();
?>
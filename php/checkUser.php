<?php
include_once "functions.php";

dbConnect();

$username = $_POST['username'];
$count = queryMysql("select count(username) from Users where username='$username'");

if (mysql_result($count, 0) <= 0)	
{
	echo '0';
}
else
{
	echo '1';
}

//mysql_free_result($count);
//mysql_close();
?>

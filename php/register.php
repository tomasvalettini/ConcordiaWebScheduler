<?php
include_once "functions.php";

dbConnect();

$username = $_POST['user'];
$password = $_POST['pwd'];

$count = queryMysql("select count(username) from Users where username='$username'");

if (mysql_result($count, 0) <= 0)	
{
	mysql_free_result($count);
	$result = queryMysql("insert into Users (username, password) values('$username', '$password')");
	mysql_free_result($result);
	echo '0';
}
else
{
	echo '1';
}

mysql_close();
?>

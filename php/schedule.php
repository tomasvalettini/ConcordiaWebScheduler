<?php
$course = trim($_REQUEST["courseStr"]);
//echo $course;

$blah = exec("python ../python/mainController.py $course");
echo "$blah";
?>



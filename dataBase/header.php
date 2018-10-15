<?php
$dbServername = "localhost"; //these lines are the variables needed to connect to the database
$dbUsername = "root";
$dbPassword = "root";
$dbName = "synth";
$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName); // this function and the tuple will actually connect to the database


<?php

$dbServername = "localhost"; //these lines are the variables needed to connect to the database
$dbUsername = "root";
$dbPassword = "root";
$dbName = "synth";

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName); // this function and the tuple will actually connect to the database

if (!$conn) {
  die("connection failed: " . mysqli_connect_error());
  echo "Fail!";
}else
{
  echo "Connected!";
}
$userid = htmlspecialchars($_GET["u_id"]);
$username = htmlspecialchars($_GET["u_name"]);
$password = htmlspecialchars($_GET["u_pass"]);
$email = htmlspecialchars($_GET["email"]);


$createNewUser = "INSERT INTO users (u_id, u_name, u_pass, email) VALUES('$userid', '$username', '$password', '$email')";
if($userid){
  $createNewProfile = " INSERT INTO profiles(u_id) VALUES ('$userid')";
}

mysqli_query($conn,$createNewUser);
mysqli_query($conn, $createNewProfile);

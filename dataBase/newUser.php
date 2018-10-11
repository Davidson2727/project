<?php
include 'header.php';

function createUser($_conn,$_username,$_password,$_email)
  {
    if(!$_conn){
      $returnVal -> message = 'no $conn';
      $returnVal -> username = $_email;
      $jsonObj = json_encode($returnVal);
      echo json_encode($jsonObj);
    }

    else
    {
      $newUser = "INSERT INTO users(userName, password, email) VALUES('$_username', '$_password', '$_email')";
      mysqli_query($_conn,$newUser);
      $returnVal -> message = '$conn';
      $returnVal -> username = $_username;
      $jsonObj = json_encode($returnVal);
      echo json_encode($jsonObj);
    }


  }


$function = $_GET["function"];
$username = ($_GET["userName"]);
$password = ($_GET["password"]);
$email = ($_GET["email"]);

if ($function == 'create')
  {
    createUser($conn,$username,$password,$email);
  }

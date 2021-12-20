<?php 
$user = 'root';
$password = ''; 
$database = 'creditcard'; 
$servername='localhost';
$mysqli = new mysqli($servername, $user, 
                $password, $database);
  
$sql = "SELECT * FROM creditcard";
$result = $mysqli->query($sql);
$mysqli->close(); 
?>
<!DOCTYPE html>
<html lang="en">
<head>
<style>
  .center {
  margin-left: auto;
  margin-right: auto;
}
table, th, td {
  border: 1px solid black;
}
</style>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table class="center">
        <tr>
            <th>id</th>
            <th>Amount</th>
            <th>Time</th>
            <th>Status</th>
        </tr>
        <?php    
                while($rows=$result->fetch_assoc())
                {
             ?>
             <tr>
                
                <td><?php echo $rows['id'];?></td>
                <td><?php echo $rows['Amount'];?></td>
                <td><?php echo $rows['Time'];?></td>
                <td><?php echo $rows['Status'];?></td>
            </tr>
            <?php
                }
             ?>
    </table>

</body>
</html>
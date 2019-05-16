<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}
fieldset{
  border: 1px solid rgb(255,232,57);
  width: 480px;
  margin:auto;
}
.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
<body>

<div class="topnav">
  <a class="active" href="mainPage.jsp">Home</a>

  <a href="mainPage.jsp">Contact</a>
  <a href="attendance.jsp">About</a>
  <a href="loginMain.jsp">Login</a>
  <a href="newTeacher.jsp">Sign-up</a>
</div>

<div style="padding-left:16px">
  <!-- <h2>Top Navigation Example</h2>
  <p>Some content..</p> -->
</div>

</body>
</html>

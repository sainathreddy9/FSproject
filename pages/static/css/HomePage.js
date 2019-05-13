{% load staticfiles %}
{% block content %}
var image1 = new Image();
image1.src = "/pages/static/images/1.jpg";
// image1.src = "/pages/static/images/1.jpg";
var image2 = new Image();
image2.src = "/pages/static/images/2.jpg";
//image2.src = "/pages/static/images/2.jpg";
var image3 = new Image();
image3.src = "/pages/static/images/3.jpg";
//image3.src = "/pages/static/images/3.jpg";
var image4 = new Image();
image4.src = "/pages/static/images/4.jpg";
//image3.src = "/pages/static/images/4.jpg";
var image5 = new Image();
image5.src = "/pages/static/images/5.jpg";
//image3.src = "/pages/static/images/5.jpg";

var step = 1;
function slideit() {
	document.getElementById("slide").src = eval("image" + step + ".src");
	step++;
	if (step > 5)
		step = 1;
	setTimeout("slideit()", 4000);
}
slideit();

//Ask ma'am whether to use inline script or find out other way to fetch the below msg from db

function msgBox() {
	document.getElementById("msgBox").innerHTML = "<p id='box'><b>Sorry , We regret to inform you that, you did not clear the interview attended on 12th May 2014.</b></p>";
}

function validateLoginCredentials() {
	var A = document.adminLoginPage.loginID;
	var B = document.adminLoginPage.loginPassword;

	if ((A.value == "") && (B.value == "")) {
		alert("All the fields are mandatory")
		return false;
	} else if (A.value == "" || A.value == null) {
		alert("Enter Login ID");
		return false;
	} else if (B.value == "" || B.value == null) {
		alert("Enter Password");
		return false;
	} else {
		return true;
	}
}

function clearLoginIDAlert() {
	document.getElementById("loginIDAlert").innerHTML = "";
}

function clearPasswordAlert() {
	document.getElementById("passwordAlert").innerHTML = "";
}

function validateLoginId(loginID) {
	var loginIDPattern = /^([A-Za-z]{2}[0-9]{6})$/;
	if (loginID.value == "" || loginID.value == null) {
		document.getElementById("loginIDAlert").innerHTML = "*Login ID mandatory";
		return 1;
	} else if (!loginID.value.match(loginIDPattern)) {

		document.getElementById("loginIDAlert").innerHTML = "*Please enter the Login ID in the specified format {AA123456}";
		return 1;
	} else {
		document.getElementById("loginIDAlert").innerHTML = "";
		return 0;
	}

}

function validatePassword(loginPassword) {
	var loginPasswordPattern = /^[A-Za-z0-9]{8}$/;

	if (loginPassword.value.length > 7) {
		if (loginPassword.value == "" || loginPassword.value == null) {
			document.getElementById("passwordAlert").innerHTML = "*Password field mandatory";
			return 1;
		} else if (!loginPassword.value.matchwd(loginPasswordPattern)) {
			document.getElementById("passwordAlert").innerHTML = "*Password must be 8 characters";
			return 1;
		} else {
			document.getElementById("passwordAlert").innerHTML = "";
			return 0;
		}
	} else {
		document.getElementById("passwordAlert").innerHTML = "*Password must be 8 characters";
		return 0;
	}
}
{% endblock %}
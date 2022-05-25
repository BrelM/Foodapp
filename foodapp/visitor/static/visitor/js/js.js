

function chargement()
{
	var Obj = document.createElement("div");
	
	Obj.setAttribute("class","main");
	var Obj1 = document.createElement("div");
	Obj1.setAttribute("class","contenue");
	Obj.appendChild(Obj1);
	document.getElementsByTagName('body')[0].appendChild(Obj);
}


function unhidePassword(pwd){
	
	pwdTag = document.getElementById(pwd);
	if (pwdTag.type=="password"){
		pwdTag.type = 'text';
		if(pwd=='pwd')
			document.getElementById('hide').innerHTML = "Hide";
		else
			document.getElementById('hideConf').innerHTML = "Hide";
		}
	else{
		pwdTag.type = 'password';
		if(pwd=='pwd')
			document.getElementById('hide').innerHTML = "Display";
		else
		document.getElementById('hideConf').innerHTML = "Display";
	}

}


function logInFirst()
{
	alert("You have to log in first!");
}

function checkPwd()
{
	form = document.getElementById('form');

	if(form.password.value!=form.password_conf.value)
	{
		alert('UOOI');
		form.password_conf.value = "";
		form.password_conf.focus();
		document.getElementById('errorPwdConf').innerHTML = "Passwords does not seem to be the same.<br>Please re-enter your password properly.";
		document.getElementById('errorPwdConf').style.color = 'red';
		document.getElementById('errorPwdConf').style.textAlign = 'center';
		return false;
	}
	else
		return true;
}


/*/This function checks if informations are correct before submiting the registration form.
function checkAll(form)
{
	form = document.getElementById(form);
	isCorrect = true;

	//Check the mail address
	const mail = /^[a-zA-Z0-9.-]+@[a-zA-Z0-9]+.[a-zA-Z]{3}$/;

	if (!mail.test(Form.mail.value)){
		alert('incorrect');
		document.getElementById('errorMail').innerHTML = "Mail address does not seem to be correct. Please enter another one.";
		document.getElementById('errorMail').style.color = 'red';
		isCorrect = false;
	}


	//Verify if a password contains at least six characters, has anx uppercase letter and a special character
	const pwd1 = /[A-Z]+/;
	const pwd2 = /[a-zA-Z0-9,.;?]{6,}/;
	const pwd3 = /[.,;?]+/;
	if(!(pwd1.test(Form.password.value) && pwd2.test(Form.password.value) && pwd3.test(Form.password.value) && Form.password.value==Form.password_conf.value))
	{
		document.getElementById('errorPwd').innerHTML = "Password does not seem to be correct.<br>Your password must contain at least six characters, an uppercase letter and a special character.";
		document.getElementById('errorPwd').style.color = 'red';
		document.getElementById('errorPwd').style.textAlign = 'center';
		isCorrect = false;
	}

	//Check password confirmation
	if(Form.password.value!=Form.password_conf.value)
	{
		Form.password_conf.value = "";
		Form.password_conf.focus();
		document.getElementById('errorPwdConf').innerHTML = "Passwords does not seem to be the same.<br>Please re-enter your password properly.";
		document.getElementById('errorPwdConf').style.color = 'red';
		document.getElementById('errorPwdConf').style.textAlign = 'center';
		isCorrect = false;
	}

	//Check the username
	const name = /^[a-zA-Z]+$/g;
	if (!(Form.username.value!='' && name.test(Form.username.value)))
	{
		document.getElementById('errorLogin').innerHTML = "Name does not seem to be correct. Please enter another one.";
		document.getElementById('errorLogin').style.color = 'red';
		isCorrect = false;
	}

	if(isCorrect)
		alert("YOOOO");
	else
		alert("NOOO");

	return isCorrect;
}*/
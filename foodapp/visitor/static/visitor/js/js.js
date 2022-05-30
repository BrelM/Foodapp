

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


function likeMeal(id)
{
	nb_like = document.getElementById('nb_like');
	id = document.getElementById('id').value;

	xhttp = new XMLHttpRequest();
	
	xhttp.onreadystatechange = function (){
		
		if(this.readyState==4 && this.status==200){
			if(parseInt(nb_like.innerHTML) > this.responseText)
				document.getElementById('like_image').src = "/static/visitor/images/like.png";
			if(parseInt(nb_like.innerHTML) < this.responseText)
				document.getElementById('like_image').src = "/static/visitor/images/liked.png";
				
			nb_like.innerHTML = this.responseText;
		}
	}

	xhttp.open('GET', '/user/like_content/'+id+'/meal/', true);
	xhttp.send();
}


function likeMenu(id)
{
	nb_like = document.getElementById('nb_like');
	id = document.getElementById('id').value;

	xhttp = new XMLHttpRequest();
	
	xhttp.onreadystatechange = function (){
		
		if(this.readyState==4 && this.status==200){
			if(parseInt(nb_like.innerHTML) > this.responseText)
				document.getElementById('like_image').src = "/static/visitor/images/like.png";
			if(parseInt(nb_like.innerHTML) < this.responseText)
				document.getElementById('like_image').src = "/static/visitor/images/liked.png";
				
			nb_like.innerHTML = this.responseText;
		}
	}

	xhttp.open('GET', '/user/like_content/'+id+'/menu/', true);
	xhttp.send();
}




function commentMeal(id)
{
	nb_comment = document.getElementById('nb_comment');
	id = document.getElementById('id').value;

	xhttp = new XMLHttpRequest();
	
	xhttp.onreadystatechange = function (){
		
		if(this.readyState==4 && this.status==200){
			alert('Your comment has been successfully posted!');
			document.getElementById('comment').value = "";				
			nb_comment.innerHTML = this.responseText;
		}
	}

	xhttp.open('GET', '/user/comment_content/'+id+'/meal/'+document.getElementById('comment').value+'/', true);
	xhttp.send();
}


function commentMenu(id)
{
	nb_comment = document.getElementById('nb_comment');
	id = document.getElementById('id').value;

	xhttp = new XMLHttpRequest();
	
	xhttp.onreadystatechange = function (){
		
		if(this.readyState==4 && this.status==200){
			alert('Your comment has been successfully posted!');
			document.getElementById('comment').value = "";				
			nb_comment.innerHTML = this.responseText;
		}
	}

	xhttp.open('GET', '/user/comment_content/'+id+'/menu/'+document.getElementById('comment').value+'/', true);
	xhttp.send();
}



function logInFirst(ea,edd)
{
	alert("You have to log in first!");
}


function submitForm(form)
{
	document.getElementById('search').submit();
}

/*
//This function checks if informations are correct before submiting the registration form.
function checkAll(form)
{
	
	form = document.getElementById(form);
	isCorrect = true;

	if(!checkLogin(form))
		isCorrect = false
	if(!checkMail(form))
		isCorrect = false;
	if(!checkPwd(form))
		isCorrect = false;
	if(!checkPwdConf(form))
		isCorrect = false;

	if(isCorrect)
		form.submit();
}


//Check the username
function checkLogin(Form)
{
	const name = /^[a-zA-Z]+$/g;
	if (Form.username.value == '' || !name.test(Form.username.value))
	{
		document.getElementById('errorLogin').innerHTML = "Name does not seem to be correct. Please enter another one.";
		document.getElementById('errorLogin').style.color = 'red';
		return false;
	}
	document.getElementById('errorLogin').innerHTML = "";
	return true;
}

//Check the mail address
function checkMail(Form)
{
	const mail = /^[a-zA-Z0-9.-]+@[a-zA-Z0-9]+.[a-zA-Z]{3}$/;

	if (!mail.test(Form.mail.value)){
		document.getElementById('errorMail').innerHTML = "Mail address does not seem to be correct. Please enter another one.";
		document.getElementById('errorMail').style.color = 'red';
		return true
	}
	document.getElementById('errorMail').innerHTML = "";
	return false;
}

//Verify if a password contains at least six characters, has anx uppercase letter and a special character
function checkPwd(Form)
{
	const pwd1 = /[A-Z]+/;
	const pwd2 = /[a-zA-Z0-9,.;?]{4,}/;
	//const pwd3 = /[.,;?]+/;
	if(!(pwd1.test(Form.password.value) && pwd2.test(Form.password.value)/* && pwd3.test(Form.password.value)))
	{
		document.getElementById('errorPwd').innerHTML = "Password does not seem to be correct.<br>Your password must contain at least four characters, an uppercase letter.";
		document.getElementById('errorPwd').style.color = 'red';
		document.getElementById('errorPwd').style.textAlign = 'center';
		Form.password.focus();
		return false;
	}
	document.getElementById('errorPwd').innerHTML = "";
	return true;
}

//Check password confirmation
function checkPwdConf(Form)
{
	if(checkPwd(Form))
	{
		if(Form.password.value != Form.password_conf.value)
		
			Form.password_conf.value = "";
			Form.password_conf.focus();
			document.getElementById('errorPwdConf').innerHTML = "Passwords does not seem to be the same.<br>Please re-enter your password properly.";
			document.getElementById('errorPwdConf').style.color = 'red';
			document.getElementById('errorPwdConf').style.textAlign = 'center';
			return false;
		}
		document.getElementById('errorPwdConf').innerHTML = "";
		return true;
	}
}
*/y


function chargement()
{
	var Obj = document.createElement("div");
	
	Obj.setAttribute("class","main");
	var Obj1 = document.createElement("div");
	Obj1.setAttribute("class","contenue");
	Obj.appendChild(Obj1);
	document.getElementsByTagName('body')[0].appendChild(Obj);
}


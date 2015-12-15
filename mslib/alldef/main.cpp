define main(acss:["css/materialize_mohit.css?reload", "css/lib.css", 'css/custom-stylesheet.css', 'css/jquery.bxslider.css', 'https://fonts.googleapis.com/icon?family=Material+Icons', 'css/lib.css', 'css/main.css', 'css/style.css'], ajs:['mslib/js/jquery-2.1.1.min.js','mslib/js/materialize.min.js','mslib/js/jquery.bxslider.min.js','mslib/js/jquery.easing.1.3.js','mslib/js/jquery.raty.js','mslib/js/lib.js?reload','mslib/js/mohit.js','mslib/js/mohitlib.js?reload','mslib/js/main.js?reload'], title: "Class Pundit", css:[], js:[], bodystyle:{}, htmlstyle:{}) {
	css = acss + css;
	js = ajs + js;
	print("<!DOCTYPE html>");
	html(style:htmlstyle){
		head(){
			base(attr:{href:HOST});
			title(){	print(title); }
			for(i, css) {
				link(attr:{href:i, rel:"stylesheet", type:"text/css"});
			}
		}
		body(style:bodystyle){
			innerHTML();
			script(attr:{type:"text/javascript"}) {
				print("var jsdata = " + jsdata+";");
			}
			script(attr:{type:"text/javascript"}) {
				print("var ec  = jsdata['_ec'] ;");
				print("var ve  = jsdata['_formerror'];");
			}
			for(i, js) {
				script(attr:{type:"text/javascript", src:i});
			}
		}
	}
}


define disptabs(tabname: [], tablink: [], liclass: None, active: None) {
	for(i, j, tabname) {
		li(class: liclass) {
			isactive = ((active == tablink[j]) ? "active" : " ");
			a(attr: { href: tablink[j] }, class: isactive ) {
				print(i);
			}
		}
	}
}

define header1(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down") {
					disptabs(tabname: tabname, tablink: tablink);
				}
			}
		}
	}
}


define header1_cp(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down") {
					disptabs(tabname: tabname, tablink: tablink);
					headertabs_cp();
				}
				ul(id: "nav-mobile", class: "side-nav") {
					headertabs_cp();
				}
				a(attr:{"data-activates": "nav-mobile"}, class: "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}



define icon(aclass: "") {
	i(class: "material-icons "+aclass, style: style){
		print(name);
	}
}

define icon1(class: None) {
	attr["src"] = img;
	img(attr: attr, style:{"margin-bottom": "-5px"}, class: class);
}


define checkbox1(checked: None, label:"Check", aclass:"", labels:{}) {
	span() {
		input(attr:{type: "checkbox", id: id, checked: checked}, class: "filled-in "+aclass, data: data);
		label(attr:{"for": id}, style: labels) {
			print(label);
		}
	}
}


define checkbox2(checked: None, label:"Check", aclass:"", labels:{}) {
	span() {
		input(attr:{type: "radio", id: id, checked: checked}, class: "with-gap "+aclass, data: data);
		label(attr:{"for": id}, style: labels) {
			print(label);
		}
	}
}

define bigf(font: "65px") {
	span(style:{"font-size": font, "text-shadow": "3px 3px 3px #000, 2px 2px 2px blue"}, color: color) {
		print(name);
	}
}

define bigf1(font: "40px") {
	bigf(color: color,font: font, name: name);
}


define height() {
	div(style:{height: val+"px"});
}

define resimg(aclass:"", opacity: None) {
	img(class: "responsive-img "+aclass, attr:{src: src}, style:{"opacity": opacity});
}

define circleimg(opacity: None) {
	resimg(aclass:"circle", src:src, opacity:opacity);
}

define divpedding(text:"", padding:"5px") {
	div(style:{padding: padding}, class: class){
		print(text);
		innerHTML();
	}
}

define textdiv(text:"", fontw: None, font: None, color: None, class: None, id: None) {
	div(style:{"font-size": font, "font-weight": fontw}, color:color, class: class, id: id){
		innerHTML();
		print(text);
	}
}

define textdiv1(font: "20px", fontw: None, color: None, class: None, text: "") {
	textdiv(font: font, fontw: fontw, color: color, class: class, text: text);
}

define a1(class: None, text:None, href: None) {
	a(attr: attr, style: style, class: class) {
		print(text);
	}
}

define starrating(val: 5) {
	for(i, val) {
		img(attr:{src: "photo/rating4.png"}, style:{"margin": "-1px", width: "22px"});
	}
}

define input1(aclass: "col s6",  type: "text", dc: "simple", icon: None, dname: None, value: None, iclass: None, disabled: None) {
	div(class: "input-field "+aclass) {
		if(icon) {
			icon(name: icon, aclass: "prefix");
		}
		data["name"] = label;
		data["dc"] = dc;
		if(dname != None) {
			data["name"] = dname;
		}
		input(attr:{id: id, type:type, value: value, disabled: disabled}, class: iclass, data: data);
		label(attr:{"for": id}) {
			print(label);
		}
	}
}



define input2(aclass: "col s6",  type: "text", iclass: None, label: None, placeholder: None) {
	div(class: "input-field "+aclass) {
		input(attr:{id: id, type:type, name:id, placeholder: placeholder}, class: iclass);
		label(attr:{"for": id}) {
			print(label);
		}
	}
}

define input3(aclass: "col s6",  type: "text", dc: "simple", icon: None, dname: None, value: None, iclass: "", name: None) {
	div(class: "input-field "+aclass) {
		if(icon) {
			icon(name: icon, aclass: "prefix");
		}
		data["name"] = label;
		data["dc"] = dc;
		if(dname != None) {
			data["name"] = dname;
		}
		input(attr:{type:type, value: value, placeholder: label, name: name}, class: "inputph "+iclass, data: data);
	}
}

define textarea1(aclass: "col l12 m12 s12") {
	div(class: "input-field "+aclass) {
		textarea(attr:{id: id, name:id}, class: "materialize-textarea");
		label(attr:{"for": id}) {
			print(label);
		}
	}
}

define button1(aclass: "" ) {
	button(class: "btn waves-effect waves-light btn "+aclass, data: data, attr: attr, datas: datas) {
		print(name);
	}
}

define hidinp(name: None, value: None) {
	input(attr: {type: "hidden", name: name, value: value});
}


define popupmodal(title: "Mohit Saini", body: "Mohit Saini in there in content of this popup. This is actually a real content of mohit saini. don't try to close this content. It may effect your transferive coolness of circuler motional emotions. due to which a pencial may disclose your aggersive argument of chair in fron of public transport within central state of indian government captured by narender modi.") {
	div(attr:{id: id}, class: "modal") {
		div(class: "modal-content container-fluid") {
			div(class: "row") {
				div(class: "col l12 m12 s12 realtexttitle", style: {"font-size": "20px"}) {
					print(title);
				}
			}
			div(class: "row") {
				div(class: "col l12 m12 s12 realtext") {
					print(body);
					innerHTML();
				}
			}
		}
	}
}


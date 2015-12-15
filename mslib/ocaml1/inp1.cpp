define main(acss:["css/materialize.min.css", "css/lib.css", 'css/materialize.min.css', 'css/custom-stylesheet.css', 'css/jquery.bxslider.css', 'https://fonts.googleapis.com/icon?family=Material+Icons', 'css/lib.css', 'css/main.css', 'css/style.css'], ajs:['mslib/js/jquery-2.1.1.min.js','mslib/js/materialize.min.js','mslib/js/jquery.bxslider.min.js','mslib/js/jquery.easing.1.3.js','mslib/js/jquery.raty.js','mslib/js/lib.js','mslib/js/mohit.js','mslib/js/mohitlib.js','mslib/js/main.js'], title: "Class Pundit", css:[], js:[], bodystyle:{}, htmlstyle:{}) {
	css = acss + css;
	js = ajs + js;
	p("<!DOCTYPE html>");
	html(style:htmlstyle){
		head(){
			base(attr:{href:HOST});
			title(){ p(title); }
			for(i, css) {
				link(attr:{href:i, rel:"stylesheet", type:"text/css"});
			}
		}
		body(style:bodystyle){
			innerHTML();
			script(attr:{type:"text/javascript"}) {
				p("var jsdata = " + jsdata+";");
			}
			script(attr:{type:"text/javascript"}) {
				p("var ec  = jsdata['_ec'] ;");
			}
			for(i, js) {
				script(attr:{type:"text/javascript", src:i});
			}
		}
	}
}


define disptabs(tabname: [], tablink: []) {
	for(i, j, tabname) {
		li(class: liclass) {
			isactive = ((active == tablink[j]) ? "active" : " ");
			a(attr: { href: tablink[j] }, class: isactive ) {
				p(i);
			}
		}
	}
}

define header1(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
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
					li() {
						a1(name: "MyFav", attr:{onclick: '$("#myfavlist").openModal();'});
					}
					li() {
						a1(name: "Provider\'s Form", attr:{onclick: '$("#providerform").openModal();'});
					}
				}
			}
		}
	}
}



define header2(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(href:"#loginmodal", class: "modal-trigger", name: "Login");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}


define header2_user(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {

		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"account", name: "Account");
			}
			li() {
				a1(href: BASE+"orders", name: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", name: "Logout");
			}
		}

		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", name: "&nbsp;"*5+"Profile"+"&nbsp;"*10, data:{activates:"dropdown1"});
						//icon(name: "arrow_drop_down", aclass: "right");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}

define header2_chef(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"profile", name: "Profile");
			}
			li() {
				a1(href: BASE+"orders", name: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", name: "Logout");
			}
		}

		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", name: "&nbsp;"*5+"Profile"+"&nbsp;"*10, data:{activates:"dropdown1"});
						//icon(name: "arrow_drop_down", aclass: "right");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}


define header2_admin(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"account", name: "Account");
			}
			li() {
				a1(href: BASE+"orders", name: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", name: "Logout");
			}
		}
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", name: "&nbsp;"*5+"Profile"+"&nbsp;"*10, data:{activates:"dropdown1"});
						//icon(name: "arrow_drop_down", aclass: "right");
					}
				}
				ul(attr:{id: "nav-mobile"}, "class": "side-nav") {
					disptabs(tabname: tabname, tablink: tablink);
				}
				a(attr:{"data-activates": "nav-mobile"}, "class": "button-collapse") {
					icon(name: "menu");
				}
			}
		}
	}
}




define icon(aclass: "") {
	i(class: "material-icons "+aclass, style: style){
		p(name);
	}
}

define icon1() {
	img(attr:{src: img}, style:{"margin-bottom": "-5px"});
}


define checkbox1(checked: None, label:"Check", aclass:"", lstyle: {}) {
	span() {
		input(attr:{type: "checkbox", id: id, checked: checked}, class: "filled-in "+aclass, data: data);
		label(attr:{"for": id}, style: lstyle) {
			p(label);
		}
	}
}


define bigf(font: "65px") {
	span(style:{"font-size": font, "text-shadow": "3px 3px 3px #000, 2px 2px 2px blue"}, color: color) {
		p(name);
	}
}


define height() {
	div(style:{height: val+"px"});
}

define resimg(aclass:"") {
	img(class: "responsive-img "+aclass, attr:{src: src}, style:{"opacity": opacity});
}

define circleimg() {
	resimg(aclass:"circle", src:src, opacity:opacity);
}

define divpedding(text:"", padding:"5px") {
	div(style:{padding: padding}, class: class){
		p(text);
		innerHTML();
	}
}


define textdiv(name:"") {
	div(style:{"font-size": font, "font-weight": fontw}, color:color, class: class){
		innerHTML();
		p(name);
	}
}

define a1(data: {}) {
	attr["href"] = href;
	a(attr: attr, style: style, class: class, data: data) {
		p(name);
	}
}

define starrating(val: 5) {
	for(i, val) {
		img(attr:{src: "photo/rating4.png"}, style:{"margin": "-1px", width: "22px"});
	}
}

define input1(aclass: "col s6",  type: "text") {
	div(class: "input-field "+aclass) {
		if(icon) {
			icon(name: icon, aclass: "prefix");
		}
		input(attr:{id: id, type:type, value: value}, class: iclass, data: data);
		label(attr:{"for": id}) {
			p(label);
		}
	}
}

define input2(aclass: "col s6",  type: "text") {
	div(class: "input-field "+aclass) {
		input(attr:{id: id, type:type, name:id}, class: iclass);
		label(attr:{"for": id}) {
			p(label);
		}
	}
}


define button1(aclass: "" ) {
	button(class: "btn waves-effect waves-light btn "+aclass, data: data, attr: attr) {
		p(name);
	}
}


define main1(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
//		loginmodal();
	}
}


define main2(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "KurryBox") {
	js = ["js/main.js"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle) {
		innerHTML();
		loginmodal();
	}
}



define bigsearch() {
	div(class: "row", style: {"background-color":""}) {
		div(class: "col l1 m1") {
			p("&nbsp;");
		}
		div(class: "col m8 s12 l9", style:{"padding": "0px", "margin": "0px"}) {
			input(attr:{placeholder: ph, id: id, autofocus: autofocus}, class:"bigsearch definput", style:{"border-radius": "0px"});
		}
		div(class: "col m2 s12 l1 ", style:{"padding": "0px", "margin": "0px"}) {
			button(class: "bigsearchbutton waves-effect waves-light btn", style:{"border-radius": "0px"}, attr:{type:"submit"}) {
				p("Go");
				icon(name: "send", aclass: "right");
			}
		}
	}
}

define header4() {
	if(islogin == "") {
		header2(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog", "Be a Chef", "Contact Us"]);
	} elif (islogin == "u") {
		header2_user(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog", "Be a Chef", "Contact Us"]);
	} elif (islogin == "a") {
		header2_admin(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog"]);
	} elif (islogin == "c") {
		header2_chef(tablink:[HOST, "", "", "", "", ""], tabname:["Home", "Our Story", "Blog"]);
	}
}


define header3(tabname:[], tablink:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: BASE}, class: "brand-logo") {
					img(attr:{src: "photo/mylogo1.png"}, class: "circle responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "right hide-on-med-and-down" ) {
					li() {
						a(class: "dropdown-button", attr:{"data-activates": "dropdown2"}) {
							p("&nbsp;"*10+"Today, 28th Oct"+"&nbsp;"*10);
						}
					}
					li() {
						a(class: "dropdown-button", attr:{"data-activates": "dropdown1"}) {
							p("&nbsp;"*5+"All"+"&nbsp;"*20);
						}
					}
					disptabs(tabname: tabname, tablink: tablink);
				}
			}
		}
		ul(attr:{id: "dropdown1"}, class: "dropdown-content") {
			foodtype = ["All", "Veg", "Non-Veg"];
			for(i, ii, foodtype) {
				li() {
					a(attr:{href: ""}) {
						p(i);
					}
				}
			}
		}
		ul(attr:{id: "dropdown2"}, class: "dropdown-content") {
			nextdays = ["Today, 26 Oct", "27 Oct", "28 Oct"];
			for(i, ii, nextdays) {
				li() {
					a(attr:{href: ""}) {
						p(i);
					}
				}
			}
		}
	}
}

define dispfood() {
	div(class: "col s12 l4 m6 ", style:{}) {
		div(class: " card-panel", style:{"margin-bottom":"40px", "padding":"0px"}) {
			div() {
//				resimg(src: "photo/food4.jpg");
				resimg(src: dishinfo["pic"]);
			}
			div(style: {"padding-bottom": "10px"}) {
				div(style:{padding: "10px"}) {
					div(class: "row") {
						div(class: "col l8", attr:{align: "left"}) {
							div() {
								p(dishinfo["title"]);
							}
						}
						div(class: "col l4") {
							icon1(img: "photo/inr1.png");
							span(style:{"font-size": "25px", "font-weight": "600"}){
								p(dishinfo["price"]);
							}
						}
					}
					div(class: "row valign-wrapper", attr:{align: "left"}) {
						div(class: "col l2") {
							// circleimg(src: "photo/chef.jpg");
							circleimg(src: dishinfo["profilepic"]);
						}
						div(class: "col l10"){
							div(style:{"font-weight": "500"}) {
								profilea1(name:"Chef "+dishinfo["name"], uid: dishinfo["cid"]);
							}
							div() {
								starrating(val:3);
//								p("5 Start Rating.");
							}
						}
						// div(class: "col l5") {
						// 	select(class: "browser-default"){
						// 		option(){
						// 			p(1);
						// 		};
						// 		option(){
						// 			p(2);
						// 		};
						// 		option(){
						// 			p(3);
						// 		};
						// 	}
						// }
					}
				}
				// div(class: "row", style:{"padding": "12px", "padding-bottom": "0px"}) {
				// 	div(class: "col l6 grey lighten-1 left", style: {margin: "-1px"}) {
				// 		divpedding(text:"Faveroute", class: "cursp");
				// 	}
				// 	div(class: "col l6 grey lighten-1 right", style: {margin: "-1px"}) {
				// 		divpedding(text: "View", class: "cursp");
				// 	}
				// }

				div(class: "row") {
					if(islogin == "a" ) {
						div(class: "col l4 ") {
							button(class: "btn waves-effect waves-light btn") {
								p("Delete");
							}
						}
						div(class: "col l4 offset-l3") {
							button(class: "btn waves-effect waves-light btn") {
								p("Edit");
							}
						}
					} elif( loginid == dishinfo["cid"] ) {

					} else {
						div(class: "col l4 ") {
							button(class: "btn waves-effect waves-light btn", data:{onclick: "addfav"}, attr:{"id": "mohit"}) {
								p("Favourite");
							}
						}
						div(class: "col l4 offset-l3") {
							button(class: "btn waves-effect waves-light btn") {
								p("Add + ");
							}
						}
					}
				}
			}
		}
	}
}

define l_otp_button() {
	button(class: "btn waves-effect waves-light", attr:{type: "button"}, data:{onclick: "sreq", action: "sendotp", fobj: "$(obj).parent().parent()[0]", restext: "Re-send"}) {
		p("Send OTP");
	}
}




define loginmodal() {
	div(attr:{id: "loginmodal"}, class: "modal") {
		div(class: "modal-content container-fluid") {
			div(class: "row") {
				ul(class: "tabs") {
					disptabs(liclass: "tab col l6", tablink:["#logintab", "#signuptab"], tabname:["Login", "Signup"]);
				}
			}
			div(attr:{id: "logintab"}) {
				form(data:{onsubmit:"sreq", bobj: "", action:"login", res: "ms.reload();"}) {
					div(class: "row") {
						input1(label: "Phone number", icon: "phone", aclass: "col s12 l7 m6", id:"loginphone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input1(label: "Password or OTP", icon: "vpn_key", aclass: "col s12 l12 m12", id: "loginpass");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								p("Login");
							}
						}
					}					
				}
			}

			div(attr:{id: "signuptab"}) {
				form(data:{onsubmit:"sreq", bobj: "", action:"signup", res: "ms.reload();" }) {
					div(class: "row") {
						input1(label: "Phone number", icon: "phone", aclass: "col s12 l7 m6", id:"signupphone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input1(label: "Choose Password", icon: "vpn_key", aclass: "col s12 l6 m6", id: "signuppass", type:"password");
						input1(label: "OTP", icon: "vpn_key", aclass: "col s12 l6 m6", id: "signupotp");
					}
					div(class: "row"){
						input1(label: "Name", icon: "account_circle", aclass: "col s12 l12 m12", id: "signupname");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								p("Signup");
							}
						}
					}
				}
			}

		}
	}
}


define table1(rows:[], thead:[]) {
	table(class: class) {
		thead() {
			for(i, thead) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, rows) {
				tr() {
					for(j, jj, i) {
						td() {
							p(j);
						}
					}
				}
			}
		}
	}
}

define profilea1() {
	a1(name: name, href: BASE+"profile?uid="+uid);
}

define account_admin() {
	div(attr:{align: "center"}) {
		height(val: 20);
		textdiv(name: "Hey Admin,\n you can login/create account of a chef using OTP as 'Admin_Secure432' ", font: "20px");
		height(val: 50);
	}
	form() {

	}
	table(class: "bordered striped centered highlight") {
		thead() {
			for(i, usertable["thead"]) {
				th() {
					p(i);
				}
			}
		}
		tbody() {
			for(i, ii, usertable["rows"]) {
				tr() {
					for(j, jj, i) {
						td() {
							if((jj == 1) && (i[-1] == "Chef" )) {
								profilea1(name:j, uid: i[0]);
							} else {
								p(j);
							}
						}
					}
				}
			}
		}
	}
}


define profile_chef_top2() {
	div(class: "row valign-wrapper") {
		div(class: "col l3", attr:{align: "center"}) {
			div() {
				circleimg(src: uinfo["profilepic"]);
			}
			if(canedit) {
				form(attr:{enctype: "multipart/form-data", method: "post"}) {
					a1(name: "Upload Profile Pic", attr:{onclick: 'uploadfile(this, "profilepic");'});
				}
			}
			div() {
				textdiv(name: "Chef "+uinfo["name"], font: "25px", fontw: "500");
				div(class: "row") {
					div(class: "col l6") {
						textdiv(name:38456, fontw:600);
						textdiv(name: "Plates Delivered");
					}
					div(class: "col l6") {
						textdiv(name: 56, fontw:600);
						textdiv(name: "People reviewed");
					}
				}
			}
		}
		div(class: "col l8 offset-l1") {
			textdiv(font:"25px", name:"About "+uinfo["name"], fontw:600);
			if(canedit) {
				a1(name: "Edit", attr:{"onclick": "ms.showtextarea(this);"});
				div(class: 'edittext', style: {display: "none"}) {
					form(data: {onsubmit:"sreq", bobj: "", action:"saveaboutinfo", res: "ms.reload();"}) {
						input(attr: {type: "hidden", name: "chefid", value: uid});
						textarea(attr:{name: "aboutus"}, class: "materialize-textarea") {
							p(uinfo["aboutus"].gchars);
						}
						button1(name: "Save", attr:{type: "submit"});
					}
				}
			}
			textdiv(font:"16px", name: uinfo["aboutus"].gchars);
		}

	}
}


define profile_chef() {
	div(class: "container-fluid") {
		div(class: "row") {
			div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
				profile_chef_top2();
				div(class: "msdivider");

				div(class: "container-fluid") {
					div(class: "row") {
					}
				}
				if(canedit) {
					div(class: "container-fluid") {
						div(class: "row") {
							div() {
								ul(class: "tabs") {
									disptabs(liclass: "tab col s2", tabname: ["All Dishes"]+ day5times["textl"], tablink: ["#alldishes"]+ day5times["tabkeys1"], active: day5times["tabkeys1"][0]);
								}
							}
							div(class: "") {
								div(attr:{id: "alldishes"}) {
									height(val:20);
									if(viewtype == "a") {
										button1(name: "Add a New Dish", data: {onclick: "slideform"});
										form(style: {display: "none"}, attr:{enctype: "multipart/form-data", method: "post"}) {
											div(class: "row") {
												input(attr:{type:"hidden", name: "cid", value: uid });
												input2(label: "Title of Dish", aclass: "col s12 l6 m6", id:"dishtitle");
												input2(label: "Price of Dish", aclass: "col s12 l6 m6", id:"dishprice");
												// input2(label: "Amount Limit", aclass: "col s12 l3 m6", id:"dishlimit");
											}
											div(class: "row"){
												textarea(class: "materialize-textarea", attr:{name: "descp", placeholder: "Dish Description"});
											}
											div(class: "row") {
												div(class: "file-field input-field") {
													div(class: "btn") {
														span() {
															p("Upload Image");
														}
														input(attr:{type:"file", name: "dishpic"});
													}
													div(class: "file-path-wrapper") {
														input(class: "file-path-validate", attr:{type: "text"});
													}
												}
											}
											div(class: "row") {
												div(class: "col") {
													button(class: "btn waves-effect waves-light", attr:{type: "submit", name:"adddish"}) {
														p("Add");
													}
												}
											}					
										}
									}

									div(class: "row", attr:{align: "center"}) {
										for(i, dispdata) {
											dispfood(dishinfo: i) ;
										}
									}
								}
								for(i, ii, day5times["tabkeys"]) {
									div(attr:{id: i}) {
										div(class: "row") {
											table(class: "bordered") {
												thead() {
													for(j, ["Title", "Price", "Add For Lunch", "Add for Dinner"]) {
														th() {
															p(j);
														}
													}
												}
												for(j, jj, dispdata) {
													tr() {
														th() {
															p((j["title"]+"").gchars);
														}
														th() {
															p(j["price"]);
														}
														th() {
															input1(label: "Plate Limit", id: "lunch_"+jj+"_"+ii, data:{dishid: j["id"], day:ii}, iclass: "numplatelimit", value: j["llimit"+ii]);
														}
														th() {
															input1(label: "Plate Limit", id: "dinner_"+jj+"_"+ii, data:{dishid: j["id"], day: ii}, iclass: "numplatelimit", value: j["dlimit"+ii]);
														}
													}
												}
											}
											div() {
												if(dispdata.len != 0) {
													button1(name: "Save", data:{action: "savedaymenu", "onclick": "sreq", params: "ms.getnumlimit("+ii+")"}, datas:{datetime: day5times["timel"][ii], cid: uid});
												}
											}
										}
									}
								}
							}
						}
					}
				}
				div(attr: {align: "center"}, style:{margin:"20px"}) {
					textdiv(name: "Dishes Serving today", font: "25px");
				}
				div(class: "row", attr:{align: "center"}) {
					for(i, dispdata) {
						if( (i["llimit0"] > 0) || (i["dlimit0"] > 0) ) {
							dispfood(dishinfo: i) ;
						}
					}
				}
			}
		}
	}
}

main2(js:["js/menu.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		if(islogin == "a") {
			div(class: "continer") {
				div(class: "row") {
					div(class: "col l8 offset-l2 m10 offset-m1 s12") {
						account_admin(usertable: users);
					}
				}
			}
		}
	}
}
define header1(){
	div(color:"black") {
		for(i, 6) {
			p("this is my new header"+i);
		}
	}
}

main2(js:["js/index.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"], bodystyle:{"background-image": 'url("photo/slide1.jpg")', "background-size": "auto 100%", "background-position": "center" }) {
	header4();
	div(attr:{id: "googlemap"});
	div() {
		div(attr:{align: "center"}) {
			div(class: "pagecenter container") {
				bigf(name: "Super Hit Meal From Super Hit Chefs", color: "white");
				height(val:40);
				form(attr:{"action": BASE+"menu" }){
					bigsearch(ph:"Enter Your Location", id:"locsearch", autofocus:"");
				}
			}
		}
	}
}
main2(js:["js/menu.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		div() {
			nav(class:"white", attr:{role: "container"}, style:{"border-bottom":"solid #ccc 1px"}) {
				div(class: "nav-wrapper container") {
					ul(class: "" ) {
						li() {
							a(class: "dropdown-button", attr:{"data-activates": "dropdown2", "aria-expanded": "false", "aria-haspopup": "true"}) {
								p("&nbsp;"*20+"Today, 28th Oct"+"&nbsp;"*0);
								icon(name: "arrow_drop_down", aclass:"right");
							}
						}
						li() {
							a(class: "dropdown-button", attr:{"data-activates": "dropdown3"}) {
								p("&nbsp;"*18+"All"+"&nbsp;"*0);
								icon(name: "arrow_drop_down", aclass:"right");
							}
						}
					}
				}
			}
			ul(attr:{id: "dropdown3"}, class: "dropdown-content") {
				foodtype = ["All", "Veg", "Non-Veg"];
				for(i, ii, foodtype) {
					li() {
						a(attr:{href: ""}) {
							p(i);
						}
					}
				}
			}
			ul(attr:{id: "dropdown2"}, class: "dropdown-content") {
				nextdays = ["Today, 26 Oct", "27 Oct", "28 Oct"];
				for(i, ii, day5times["timel"] ) {
					li() {
						a(attr:{href: BASE+"menu?datetime="+i}) {
							p( day5times["textl"][ii] );
						}
					}
				}
			}
		}

		div(class: "container-fluid") {
			div(class: "row") {
				ul(class: "tabs") {
					disptabs(liclass: "tab col s2", tabname: ["Lunch", "Dinner"], tablink: ["#lunch", "#dinner"]);
				}
			}
		}
		div(class: "container-fluid") {
			div(class: "row") {
				div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
					div(attr:{id: "lunch"}) {
						div(class: "row", attr:{align: "center"}) {
							for(i, lunch) {
								dispfood(dishinfo: i);
							}
						}
					}
					div(attr:{id: "dinner"}) {
						div(class: "row", attr:{align: "center"}) {
							for(i, dinner) {
								dispfood(dishinfo: i);
							}
						}
					}
				}
			}
		}
	}
}
main1(js:["js/profile.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		if(uid > 0) {
			profile_chef();
		}
	}
}
main1() {
	p(_session);
	form(attr: {enctype: "multipart/form-data", method: "post"}) {
		input(attr: {type: "file", name:"mohit"});
		button(attr: {type: "submit"}) {
			p("Submit");
		}
		table1(thead: thead, rows: rows, class: "bordered");
	}
}

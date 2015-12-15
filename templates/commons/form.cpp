define main2(css:[], js:[], bodystyle:{}, htmlstyle:{}, title: "Power | Get Real Data online") {
	js = ["js/main.js?reload"] + js;
	main(title: title, css: css, js:js, bodystyle:bodystyle, htmlstyle: htmlstyle, acss: ["css/materialize_mohit.css", "css/lib.css", 'mslib/css/gfont.css', "css/style1.css", "js/owl-carousel/owl.carousel.css","js/owl-carousel/owl.theme.css", "css/main.css" ], ajs: ['mslib/js/jquery-2.1.1.min.js','mslib/js/materialize.min.js','mslib/js/jquery.bxslider.min.js','mslib/js/jquery.easing.1.3.js','mslib/js/jquery.raty.js','mslib/js/lib.js?reload','mslib/js/mohit.js','mslib/js/mohitlib.js?reload', "js/d3.min.js", "js/radialProgress.js", "js/jquery.js", "js/jquery-1.9.1.min.js", "js/owl-carousel/owl.carousel.js", "js/lib1.js", "c3/c3.min.js"]) {
		innerHTML();
		popupmodal(id: "popupmodal");
	}
}



define bigsearch() {
	div(class: "row", style: {"background-color":""}) {
		div(class: "col l1 m1") {
			print("&nbsp;");
		}
		div(class: "col m8 s12 l6", style:{"padding": "0px", "margin": "0px"}) {
			input(attr:{placeholder: ph, id: id, autofocus: autofocus}, class:"bigsearch definput", style:{"border-radius": "0px"});
		}
		select2(tlist: config["foodtype"].values, dclass: "col m8 s12 l3", class: "browser-default", vlist: config["foodtype"].keys, name: "foodtype", style: {"height": "60px"});
		div(class: "col m2 s12 l1 ", style:{"padding": "0px", "margin": "0px"}) {
			button(class: "bigsearchbutton waves-effect waves-light btn", style:{"border-radius": "0px"}, attr:{type:"submit"}) {
				print("Go");
				icon(name: "send", aclass: "right");
			}
		}
	}
}

define header2(tabname:[], tablink:[], tabname1:[], tablink1: []) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo center") {
					img(attr:{src: "photo/logo4.png"}, class: "responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "left hide-on-med-and-down" ) {
					disptabs(tabname: tabname1, tablink: tablink1);
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(href:"#loginmodal", class: "modal-trigger", text: "Login");
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

define header1_power(tabname:[], tablink:[], bgcolors:[], colors:[]) {
	div(class: "navbar-fixed ") {
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container-fluid") {
				ul(class: "left", style: {color: "black"}) {
					for(i, j, tabname) {
						li() {
							a(attr: { href: tablink[j] }, class: bgcolors[j], color: colors[j]) {
								print(i);
							}
						}
					}
				}
			}
		}
	}
}


define header2_user(tabname:[], tablink:[], tabname1:[], tablink1:[]) {
	div(class: "navbar-fixed ") {

		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"account", text: "Account");
			}
			li() {
				a1(href: BASE+"orders", text: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", text: "Logout");
			}
		}

		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo center") {
					img(attr:{src: "photo/logo4.png"}, class: "responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "left hide-on-med-and-down" ) {
					disptabs(tabname: tabname1, tablink: tablink1);
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", text: "&nbsp;"*5+loginname+"&nbsp;"*10, data:{activates:"dropdown1"});
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

define header2_chef(tabname:[], tablink:[], tabname1:[], tablink1:[]) {
	div(class: "navbar-fixed ") {
		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"profile", text: "Profile");
			}
			li() {
				a1(href: BASE+"orders", text: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", text: "Logout");
			}
		}

		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo center") {
					img(attr:{src: "photo/logo4.png"}, class: "responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "left hide-on-med-and-down" ) {
					disptabs(tabname: tabname1, tablink: tablink1);
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", text: "&nbsp;"*5+loginname+"&nbsp;"*10, data:{activates:"dropdown1"});
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


define header2_admin(tabname:[], tablink:[], tabname1:[], tablink1:[]) {
	div(class: "navbar-fixed ") {
		ul(id: "dropdown1", class: "dropdown-content") {
			li() {
				a1(href: BASE+"account", text: "Account");
			}
			li() {
				a1(href: BASE+"orders", text: "Orders");
			}
			li() {
				a1(href: HOST+"?logout", text: "Logout");
			}
		}
		nav(class:"white", attr:{role: "container"}) {
			div(class: "nav-wrapper container") {
				a(attr:{id: "logo-container", href: HOST}, class: "brand-logo center") {
					img(attr:{src: "photo/logo4.png"}, class: "responsive-img", style:{"vertical-align": "middle"});
				}
				ul(class: "left hide-on-med-and-down" ) {
					disptabs(tabname: tabname1, tablink: tablink1);
				}
				ul(class: "right hide-on-med-and-down" ) {
					disptabs(tabname: tabname, tablink: tablink);
					li() {
						a1(class: "dropdown-button", text: "&nbsp;"*5+"Profile"+"&nbsp;"*10, data:{activates:"dropdown1"});
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




define header4() {
	blogurl = "";
	tablink1 = [blogurl];
	tabname1 = ["Blog"];
	if(islogin == None) {
		header2(tablink:[BASE+"chefjoin"], tabname:["Be a Chef"], tablink1: tablink1, tabname1: tabname1);
	} elif (islogin == "u") {
		header2_user(tablink:[BASE+"cart"], tabname:["Cart"], tablink1: tablink1, tabname1: tabname1);
	} elif (islogin == "a") {
		header2_admin(tablink:[], tabname:[], tabname1: tabname1, tablink1: tablink1);
	} elif (islogin == "c") {
		header2_chef(tablink:[], tabname:[], tablink1: tablink1, tabname1: tabname1);
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
							print("&nbsp;"*10+"Today, 28th Oct"+"&nbsp;"*10);
						}
					}
					li() {
						a(class: "dropdown-button", attr:{"data-activates": "dropdown1"}) {
							print("&nbsp;"*5+"All"+"&nbsp;"*20);
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
						print(i);
					}
				}
			}
		}
		ul(attr:{id: "dropdown2"}, class: "dropdown-content") {
			nextdays = ["Today, 26 Oct", "27 Oct", "28 Oct"];
			for(i, ii, nextdays) {
				li() {
					a(attr:{href: ""}) {
						print(i);
					}
				}
			}
		}
	}
}

define dispfood() {
	div(class: "col s12 ll4 l6", id: "mohit") {
		div(class: "card-panel", style:{"margin-bottom":"40px", "padding":"0px", "max-width": "450px"}) {
			div() {
//				resimg(src: "photo/food4.jpg");
				resimg(src: dishinfo["pic"]);
			}
			div(style: {}) {
				div(style:{padding: "10px"}) {
					div(class: "row", style: {"min-height": "70px"}) {
						div(class: "col ll7 l8 s8 m8", attr:{align: "left"}) {
							div() {
								print(dishinfo["title"]);
							}
							div() {
								div(style: {display: "none"}) {
									print(dishinfo["descp"]);
								}
								a1(text: "Details", data: {onclick: "view_dish_details"});
							}
						}
						div(class: "col ll5 l4 m4 s4") {
							icon1(img: "photo/inr1.png");
							span(style:{"font-size": "20px", "font-weight": "600"}){
								print(dishinfo["price"]);
							}
							icon1(img: ["photo/vegfood1.jpg", "photo/nonveg1.png"][dishinfo["isveg"] == 'n']);
						}
					}
					div(class: "row valign-wrapper", attr:{align: "left"}) {
						div(class: "col l2") {
							circleimg(src: dishinfo["profilepic"]);
						}
						div(class: "col l6"){
							div(style:{"font-weight": "500"}) {
								profilea1(text:"Chef "+dishinfo["name"], uid: dishinfo["cid"]);
							}
						}
						div(class: "col l3") {
							if(islogin == "a" ) {
								button(class: "btn waves-effect waves-light btn", datas:{datetime: dishinfo["datetime"], lord: dishinfo["lord"], dishid: dishinfo["id"]}, data:{onclick: "sreq", action: "deletedisp", restext: "Deleted !", res: "ms.reload();"}) {
									print("Delete");
								}
							} elif( loginid == dishinfo["cid"] ) {

							} else {
								button(class: "btn waves-effect waves-light btn", data:{onclick: "sreq", action: "addincart", restext: "Added!"}, datas: {datetime: dishinfo["datetime"], lord: dishinfo["lord"], dishid: dishinfo["id"]}) {
									print("Add + ");
								}
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
		print("Send OTP");
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
				form(data:{onsubmit:"sreq", bobj: "", action:"login", res: "ms.reload();", errorh: "error_login"}) {
					errorbox();
					div(class: "row") {
						input3(label: "Phone", icon: "phone", aclass: "col s12 l7 m6", name:"loginphone", dc: "phone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input3(label: "Password or OTP", icon: "vpn_key", aclass: "col s12 l12 m12", name: "loginpass", type: "password", dc: "password1");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								print("Login");
							}
						}
					}					
				}
			}

			div(attr:{id: "signuptab"}) {
				form(data:{onsubmit:"sreq", bobj: "", action:"signup", res: "ms.reload();", errorh: "error_login"}) {
					errorbox();
					div(class: "row") {
						input3(label: "Phone number", icon: "phone", aclass: "col s12 l7 m6", name:"signupphone", dc: "phone");
						div(class: "col l4 m6") {
							l_otp_button();
						}
					}
					div(class: "row"){
						input3(label: "Choose Password", icon: "vpn_key", aclass: "col s12 l6 m6", name: "signuppass", type:"password", dc: "password1");
						input3(label: "OTP", icon: "vpn_key", aclass: "col s12 l6 m6", name: "signupotp", type: "password", dc: "otp");
					}
					div(class: "row"){
						input3(label: "Name", icon: "account_circle", aclass: "col s12 l12 m12", name: "signupname");
					}
					div(class: "row") {
						div(class: "col") {
							button(class: "btn waves-effect waves-light", attr:{type: "submit"}) {
								print("Signup");
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
					print(i);
				}
			}
		}
		tbody() {
			for(i, ii, rows) {
				tr() {
					for(j, jj, i) {
						td() {
							print(j);
						}
					}
				}
			}
		}
	}
}

define profilea1(uid: None) {
	a1(text: text, href: BASE+"profile?uid="+uid);
}

define account_admin() {
	div(attr:{align: "center"}) {
		height(val: 20);
		textdiv(text: "Hey Admin,\n you are welcome", font: "20px");
		height(val: 50);
	}
	div() {
		height(val: 20);
		textdiv(text: "Add new Admins", font: "20px");
		height(val: 50);
		form(data:{onsubmit: "sreq", bobj: "", action: "createadmin", restext: "Created", res: "ms.reload();", errorh: "error_login"}) {
			errorbox();
			input1(label: "Phone number", id: "phone", dc: "phone");
			input1(label: "Choose password", id: "password", type: "password");
			button1(name: "Create", attr: {type: "submit"});
		}
	}
	br();
	table(class: "bordered striped centered highlight") {
		thead() {
			tr() {
				for(i, ["UserID", "Name", "Email", "Phone", "User Type"]) {
					th() {
						print(i);
					}
				}
			}
		}
		tbody() {
			for(i, ii, users) {
				tr() {
					for(jjj, jj, ["id", "name", "email", "phone", "typetext"]) {
						j = i[jjj];
						td() {
							if( (jjj=="name") && (i["type"] == "c") ) {
								profilea1(text:j, uid: i["id"]);
							} else {
								print(j);
							}
						}
					}
					td() {
						button1(name: (i["conf"] ? "UnBlock": "Block"), datas:{uid: i['id'], isblock: (i["conf"] != None)}, data:{onclick: "sreq", action: "blockunblock", restext: "Done!", res: "ms.reload();"});
					}
					td() {
						button1(name: "Delete", datas:{uid: i['id']}, data:{onclick: "sreq", action: "deleteaccount", restext: "Done!", res: "ms.reload();"});
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
					a1(text: "Upload Profile Pic", attr:{onclick: 'uploadfile(this, "profilepic");'});
				}
			}
			div() {
				textdiv(text: "Chef "+uinfo["name"], font: "25px", fontw: "500");
				div(class: "row") {
					div(class: "col l12 m12 s12") {
						textdiv(text:platedelivered, fontw:600);
						textdiv(text: "Plates Delivered");
					}
					// div(class: "col l6") {
					// 	textdiv(text: 56, fontw:600);
					// 	textdiv(text: "People reviewed");
					// }
				}
			}
		}
		div(class: "col l8 offset-l1") {
			textdiv(font:"25px", text:"About "+uinfo["name"], fontw:600);
			if(canedit) {
				a1(text: "Edit", attr:{"onclick": "ms.showtextarea(this);"});
				div(class: 'edittext', style: {display: "none"}) {
					form(data: {onsubmit:"sreq", bobj: "", action:"saveaboutinfo", res: "ms.reload();"}) {
						input(attr: {type: "hidden", name: "chefid", value: uid});
						textarea(attr:{name: "aboutus"}, class: "materialize-textarea") {
							print(uinfo["aboutus"]);
						}
						button1(name: "Save", attr:{type: "submit"});
					}
				}
			}
			textdiv(font:"16px", text: uinfo["aboutus"]);
			div() {
				if(canedit) {
					b() {
						print("Address: ");
					}
					print(uinfo["address"]);
				}
				if(islogin == 'a') {
					a1(text: "Edit", attr:{"onclick": "ms.shownext(this);"});
					form(data:{onsubmit:"sreq", bobj: "", action:"change_address", res: "ms.reload();", errorh: "error_login"}, style: {display: "none"}) {
						errorbox();
						div(class: "row") {
							hidinp(name: "cid", value: uinfo["id"]);
							input1(label: "Address, Choose from google", id: "gaddress", attr:{onkeydown: "return notenterkey(event);"});
							input1(label: "House number", id: "address");
						}
						div() {
							button1(name: "Submit", attr:{type: "submit"});
						}
					}
				}
			}
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
									disptabs(liclass: "tab col s2", tabname: ["All Dishes"]+ day5times["textl"], tablink: ["#alldishes"]+ day5times["tabkeys1"]);
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
												input2(label: "Title of Dish", aclass: "col s12 l4 m4", id:"dishtitle");
												input2(label: "Price of Dish", aclass: "col s12 l4 m4", id:"dishprice");
												select2(tlist: config["foodtype"].values, dclass: "col l3 s12 m4", class: "browser-default", vlist: config["foodtype"].keys, name: "isveg");
											}
											div(class: "row"){
												textarea(class: "materialize-textarea", attr:{name: "descp", placeholder: "Dish Description"});
											}
											div(class: "row") {
												div(class: "file-field input-field") {
													div(class: "btn") {
														span() {
															print("Upload Image");
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
														print("Add");
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
													for(j, ["Title", "Price", "Booked For Lunch", "Booked for Dinner"]) {
														th() {
															print(j);
														}
													}
												}
												for(j, jj, dispdata) {
													tr() {
														th() {
															print((j["title"]+"").gchars);
														}
														th() {
															print(j["price"]);
														}
														th() {
															input1(label: "Plate Limit ("+j["ollimit"+ii]+" Booked)", id: "lunch_"+jj+"_"+ii, data:{dishid: j["id"], day:ii}, iclass: "numplatelimit", value: j["llimit"+ii], disabled: block_today_menu[ii][0]);
														}
														th() {
															input1(label: "Plate Limit ("+j["odlimit"+ii]+" Booked)", id: "dinner_"+jj+"_"+ii, data:{dishid: j["id"], day: ii}, iclass: "numplatelimit", value: j["dlimit"+ii], disabled: block_today_menu[ii][1]);
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
					textdiv(text: "Dishes Serving today", font: "25px");
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


define select1(tlist:[], class: "browser-default", aclass: "", selected: None, name: None, vlist: None, toptext: None, style: {}) {//class, tlist, vlist, toptext, selected
	select(class: class+" "+aclass, attr:attr, style: style) {
		if(toptext != None) {
			option(attr:{value: ""}) {
				print(toptext);
			}
		}
		for(i, ii, tlist) {
			attrs = {};
			if (vlist != None) {
				attrs["value"] = vlist[ii];
			} else {
				attrs["value"] = (ii+1);
			}
			if( selected == ii ) {
				attrs["selected"] = "";
			}
			option(attr:attrs) {
				print(i);
			}
		}
	}
}

define select2(tlist:[], dclass: "col l3 s12 m6", class: "browser-default", selected: None, toptext: None, vlist: None, name: None, style: {}) {
	div(class: dclass) {
		select1(class: class, tlist: tlist, vlist: vlist, toptext: toptext, selected: selected, name: name, style:style);
	}
}

define mselect(tlist:[], vlist: None, selected: None) {
	for(i, ii, tlist) {
		attrs = {};
		if (vlist != None) {
			attrs["value"] = vlist[ii];
		} else {
			attrs["value"] = (ii+1);
		}
		if( selected == ii ) {
			attrs["selected"] = "";
		}
		checkbox1(label: i, id: id+"_"+ii);
	}
}


define mselect1(tlist:[], vlist: None) {
	div(id: id, class: "dropdown-content p5", tlist:[]) {
		mselect(vlist:vlist, tlist: tlist, id: id);
	}
	a(class: "dropdown-button", data:{activates: id}) {
		print(label);
	}
}

define mselect2(class: "col l3 s12 m6") {
	div(class: class) {
		div(class: "mselect complexinput", data:{complexinput: "ci_checkbox"}, attr: {name: id}) {
			mselect1(id: id, tlist: tlist, label: label, selectall: selectall);
		}
	}
}


define switch1(on: "Yes", off: "No") {
	div(class: "switch") {
		label() {
			print(off);
			input(attr:{type: "checkbox", name: name});
			span(class: "lever");
			print(on);
		}
	}
}


define switch2(class: "col l3 s12 m6") {
	div(class: class) {
		div(class: "m5") {
			print(label);
			switch1(name: name);
		}
	}
}



define orderl_admin(){
	table(class: "bordered") {
		thead() {
			for(i, ["Date of Order", "Delivery Date", "Chef", "User", "Dish", "Price", "Chef Address", "User Address", "Status"]) {
				th() {
					print(i);
				}
			}
		}
		tbody() {
			for(i, ii, orderl) {
				tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
					td() {
						print(i["timetext"]);
					}
					td() {
						print(i["datetimetext"]);
					}
					td() {
						profilea1(text: i["cname"], uid: i["cid"]);
					}
					td() {
						profilea1(text: i["uname"], uid: i["uid"]);
					}
					td() {
						print(i["title"]);
					}
					td() {
						icon1(img: "photo/inr2.png");
						span(class: "itemprice") {
							print(i["price"]+'*'+i["numplate"]+"="+(i["price"]*i["numplate"]));
						}
					}
					td() {
						print("("+i["clat"]+", "+i["clng"]+")<br>"+i["caddress"]);
					}
					td() {
						print("("+i["lat"]+", "+i["lng"]+")<br>"+i["uaddress"]);
					}
					td() {
						print(i["status_text"]);
					}
				}
			}
		}
	}
}


define orderl_user(){
	table(class: "bordered") {
		thead() {
			for(i, ["Date of Order", "Delivery Date", "Chef", "Dish", "Price", "User Address", "Status"]) {
				th() {
					print(i);
				}
			}
		}
		tbody() {
			for(i, ii, orderl) {
				tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
					td() {
						print(i["timetext"]);
					}
					td() {
						print(i["datetimetext"]);
					}
					td() {
						profilea1(text: i["cname"], uid: i["cid"]);
					}
					td() {
						print(i["title"]);
					}
					td() {
						icon1(img: "photo/inr2.png");
						span(class: "itemprice") {
							print(i["price"]+'*'+i["numplate"]+"="+(i["price"]*i["numplate"]));
						}
					}
					td() {
						print("("+i["lat"]+", "+i["lng"]+")<br>"+i["uaddress"]);
					}
					td() {
						print(i["status_text"]);
					}
				}
			}
		}
	}
}


define orderl_chef(){
	table(attr:{"border": "1"}) {
		// thead() {
		// }
		tbody() {
			tr() {
				for(i, ["Date of Order", "Delivery Date", "User", "Dish", "Price", "User Address", "Status"]) {
					td() {
						print(i);
					}
				}
			}
			for(i, ii, orderl) {
				tr(class: "cartitems", datas:{ datetime: i["datetime"], cid: i["cid"], lord: i["lord"], dishid: i["dishid"]}) {
					td() {
						print(i["timetext"]);
					}
					td() {
						print(i["datetimetext"]);
					}
					td() {
						profilea1(text: i["cname"], uid: i["cid"]);
					}
					td() {
						profilea1(text: i["uname"], uid: i["uid"]);
					}
					td() {
						print(i["title"]);
					}
					td() {
						icon1(img: "photo/inr2.png");
						span(class: "itemprice") {
							print(i["price"]+'*'+i["numplate"]+"="+(i["price"]*i["numplate"]));
						}
					}
					td() {
						print("("+i["clat"]+", "+i["clng"]+")<br>"+i["caddress"]);
					}
					td() {
						print("("+i["lat"]+", "+i["lng"]+")<br>"+i["uaddress"]);
					}
					td() {
						print(i["status_text"]);
					}
				}
			}
		}
	}
}


define orderl(utype: islogin) {
	if(utype == 'u') {
		orderl_user(orderl: orderl);
	}
	if(utype == 'c') {
		orderl_chef(orderl: orderl);
	}
	if(utype == 'a') {
		orderl_admin(orderl: orderl);
	}
}



define errorbox() {
	div(class: "row hiddenerror") {
		div(class: "col s12 l12") {
			div(class: "card-panel red white-text center errortext") {
				print("");
			}
		}
	}
}


define menu_nofood() {
	div(class: "col l12 m12 s12") {
		textdiv(text: "No chef is serving in this location. We are trying hard to serve you in this location, will let you know once this location is launched", font: "20px");
	}
}



define kurry_footer() {
	div(class: "page-footer darken-4", style: {"margin-bottom": "0px", "padding-bottom": "0px"}) {
		div(class: "container") {
			div(class: "row", style: {"margin-bottom": "-25px"}) {
				div(class: "col s2 m2 l3 offset-l2 offset-m2") {
					h5() {
						print("Social Media");
					}
					ul(){
						li() {
							a1(text: "Facebook");
						}
						li() {
							a1(text: "Twitter");
						}
						li() {
							a1(text: "Instagram");
						}
					}
				}
				div(class: "col s2 m2 l3") {
					h5() {
						print("Help");
					}
					ul(){
						li() {
							a1(text: "About us", attr:{ "onclick": '$("#aboutus").openModal();'});
						}
						li() {
							a1(text: "Contact us", attr: {onclick: '$("#contactusform").openModal();'});
						}
					}
				}
				div(class: "col s2 m2 l3") {
					h5() {
						print("Legal");
					}
					ul(){
						li() {
							a1(text: "Company Policies, Terms and Conditions", attr:{ "onclick": '$("#policy").openModal();'});
						}
					}
				}
			}
			div(class: "row"){
				div(class: "col l12 center ") {
					print("&copy; Copyright 2015 KurryBox");
				}
			}
		}
	}
}


define kurry_contactus_form() {
	div(class: "row") {
		div(class: "col s12 l12 m12") {
			h3(class: "grey-text text-darken-4") {
				print("Contact US");
			}
		}
		div(class: "col s12 l6 m6") {
			h5(class: "grey-text text-darken-2") {
				print("Mail");
				icon(name: "mail", aclass: "tiny");
			}
			div(class: "grey-text") {
				print("ContactUs@kurrybox.in");
			}
			h5(class: "grey-text text-darken-2") {
				print("Call");
				icon(name: "call", aclass: "tiny");
			}
			div(class: "grey-text") {
				print("+91 9821147004");
			}
		}
	}
}

define kurry_aboutus() {
	div(class: "card-content") {
		h3(class: "card-title") {
			print("About Us");
		}
		div() {
			print(aboutus_content);
		}
	}
}

define kurry_policy() {
	div(class: "card-content") {
		h3(class: "card-title") {
			print("Policy");
		}
		div() {
			print(policy_content);
		}
	}
}


define button2(aclass: "", text: "Submit", data: {}, datas: {}, attr: {}) {
	button(class: "btn waves-effect waves-light btn "+aclass, data: data, attr: attr, datas: datas) {
		print(text);
	}
}

main2(js:["js/menu.js"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		div() {
			nav(class:"white", attr:{role: "container"}, style:{"border-bottom":"solid #ccc 1px"}) {
				div(class: "nav-wrapper container") {
					ul(class: "left hide-on-med-and-down" ) {
						// li() {
						// 	a(class: "dropdown-button", attr:{"data-activates": "dropdown2", "aria-expanded": "false", "aria-haspopup": "true"}) {
						// 		print("&nbsp;"*20+ dayselecttext +"&nbsp;"*0);
						// 		icon(name: "arrow_drop_down", aclass:"right");
						// 	}
						// }
						li() {
							a(class: "dropdown-button", attr:{"data-activates": "dropdown3"}) {
								print("&nbsp;"*18+ foodtypetext +"&nbsp;"*0);
								icon(name: "arrow_drop_down", aclass:"right");
							}
						}
					}
					ul(class: 'right hide-on-med-and-down') {
						for(i, ii, day5times["timel"] ) {
							li(class: [None, "active"][ i == daydatetime ]) {
								a(attr:{href: BASE+"menu?"+daysurls[ii] }) {
									print( day5times["textl"][ii] );
								}
							}
						}
					}
				}
			}
			ul(attr:{id: "dropdown3"}, class: "dropdown-content") {
				foodtype = config["foodtype"].values;
				for(i, ii, foodtype) {
					li() {
						a(attr:{href: BASE+"menu?"+foodtypeurls[ii]}) {
							print(i);
						}
					}
				}
			}
			// ul(attr:{id: "dropdown2"}, class: "dropdown-content") {
			// 	for(i, ii, day5times["timel"] ) {
			// 		li() {
			// 			a(attr:{href: BASE+"menu?"+daysurls[ii] }) {
			// 				print( day5times["textl"][ii] );
			// 			}
			// 		}
			// 	}
			// }
		}

		div(class: "container-fluid") {
			div(class: "row") {
				ul(class: "tabs") {
					disptabs(liclass: "tab col s2", tabname: ["Lunch", "Dinner"], tablink: ["#lunch", "#dinner"]);
				}
			}
		}
		div(class: "slider") {
			imgs = ["http://lorempixel.com/580/250/nature/1", "http://lorempixel.com/580/250/nature/2", "http://lorempixel.com/580/250/nature/3", "http://lorempixel.com/580/250/nature/4"];
			img_align = ["center", "left", "top", "right"];
			ul(class: "slides"){
				for(i, ii, imgs) {
					li() {
						img(attr: {src: i});
						div(class: "caption "+img_align[ii]+"-align") {
							h3() {
								print("Hey, I am offer");
							}
							h5(class: "light grey-text text-lighten-3") {
								print("I am very cool offfer. Buy this token in 3 rupees.");
							}
						}
					}
				}
			}
		}
		div(class: "container-fluid") {
			div(class: "row") {
				div(class: "col l12 s12 m12") {
				// div(class: "col l10 offset-l1 s10 m10 offset-s1 offset-m1") {
					div(attr:{id: "lunch"}) {
						div(class: "row", attr:{align: "center"}) {
							if(lunch.len == 0) {
								menu_nofood();
							}
							for(i, lunch) {
								dispfood(dishinfo: i);
							}
						}
					}
					div(attr:{id: "dinner"}) {
						div(class: "row", attr:{align: "center"}) {
							if(dinner.len == 0) {
								menu_nofood();
							}
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

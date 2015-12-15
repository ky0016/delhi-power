chefjoinjs = ["js/chefjoin.js?reload"];

if(true) {
	chefjoinjs = chefjoinjs + ["https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"];
}

main2(js: chefjoinjs) {
	header4();
	div() {
		div(class: "container") {
			height(val: 100);
			form() {
				errorbox();
				div(class: "row"){
					input1(label: "Name", id: "name");
					input1(label: "Mobile number", id: "mobile", dc: "phone");
					input1(label: "Email Id", id: "email", dc: "email");
					input1(label: "Address [Select your Area from Google Search]", id: "gaddress", attr:{onkeydown: "return notenterkey(event);"});
					input1(label: "Extra Address [Building#/Apartment#/Street Name/Land Mark]", id: "address");
					input1(label: "Choose a password", id: "password", dc: "password1", type: "password");

					select2(tlist: ["Male", "Female"], vlist: ["M", "F"], toptext: "Gender", name: "gender");
					select2(tlist: config["chefagelist"], toptext: "Age", name: "age");
					select2(tlist: config["chefhowmanypeople"], toptext: "How many plates are you comfortable cooking in 1 meal", name: "cookpeople");
					mselect2(id: "languages", tlist: config["cheflanguages"], label: "Select languages", selectall: "Select All");
				}
				div(class: "row"){
					switch2(label: "Do you cook NonVeg Food", name: "isnonveg");
					switch2(label: "Do you have academic degree in cooking ?", class: "col l6", name: "isdegree");
				}
				div(class: "row") {
					textarea1(label: "Please enter few of your signature dishes", class: "materialize-textarea", id: "dishes");
				}
				div() {
					button1(name: "Submit", attr:{type: "button"}, data: {onclick: "sreq", fobj: "", action: "chefjoinus", restext: "Submitted", errorh: "error_login", res: "ms.thanksforapply(obj);"});
				}
			}
		}
	}
}

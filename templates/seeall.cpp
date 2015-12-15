main2() {
	div(class: "container") {
		for(i, allt) {
			div(class: "row") {
				div(class: "") {
					table1(thead: i["data"]["thead"], rows: i["data"]["rows"], class: "bordered");
				}
			}
		}
	}
}



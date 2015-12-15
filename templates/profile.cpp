main2(js:["js/profile.js", "https://maps.googleapis.com/maps/api/js?signed_in=true&libraries=drawing,places&callback=initMap"], htmlstyle:{"overflow-y": "scroll"}) {
	div() {
		header4();
		if(uid > 0) {
			profile_chef();
		}
	}
}

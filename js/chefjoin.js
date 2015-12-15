function initMap() {
	var autocinput = $("#gaddress")[0];
	var autocomplete = new google.maps.places.Autocomplete(autocinput);
	autocomplete.addListener('place_changed', function() {
		var loc = autocomplete.getPlace().geometry.location;
		add_hidden_inps (lookontop(autocinput, function (x) {
			return x[0].tagName == "FORM";
		}), {lat:loc.lat(), lng: loc.lng()});
		return false;
	});
}



ms.thanksforapply = function(obj) {
	$(lookontop_form(obj)).slideUp();
	ms.popup("Submitted Successfully", "Thanks for submitting the form, we will get back to you within one business day.");
};


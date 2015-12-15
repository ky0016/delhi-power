
ms.getnumlimit = function(day) {
	return {"platelimits": append(mapo(function(x,y){ return [dattr(x).dishid, attr(x)["id"][0], x.value ]; }, $(".numplatelimit"), function(x){ return (x.value != "" && dattr(x)["day"] == day ); }), [0]) };
}

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

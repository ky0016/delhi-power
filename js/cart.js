
var itemp = function() {
	return mapo(function (x, y) {
		var parseInt1 = function(x) {
			return x!="" ? parseInt(x): 0;
		};
		return [parseInt($(x).find(".itemprice").html()), parseInt1($(x).find(".numitem")[0].value), $(x).find('[data-iserror=1]').length, dsattr(x), $(x).find(".dslots").val()];
	}, $(".cartitems"));
}

function totalprice() {
	var totalp = fold(function(x, y){
		return x+(y[0]*y[1]);
	} , itemp(), 0);
	return totalp;
}

function settotalprice() {
	$("#totalprice").html(totalprice());
}

$(document).ready(function() {
	settotalprice();
});

function removerow(obj) {
	var rowobj = lookontop(obj, function(x) {
		return x.hasClass("cartitems");
	});
	$(rowobj).remove();
	settotalprice();
}

funcs.order = function () {
	var clist = itemp();
	var latlng = mapp(function(x){ return hvali(x)}, ["lat", "lng"], null, function(x,y) { return y; });
	var flist = mapo(function(x){
		return mifu(mifu(x[3], {dslots: x[4], numplate: x[1], status: 'c'}), latlng);
	}, clist, function (x) {
		return (x[2]==0);
	});
	if(flist.length < clist.length) {
		msg ("Please remove Stupid items");
	} else {
		runf("sreq", mifu({obj: obj, params: {olist: flist}, callback: function(d) {
		}}, dattr(obj) ));
	}
	return false;
}


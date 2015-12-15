mergeforce(funcs, {
	addfav: function() {
		runf("error", {msg: "Oops!! You forgot to login!"});
	},
	slideform: function () {
		$(obj).parent().find("form").slideToggle();
	},
	error_login: function() {//obj, msg
		var errore = $(lookontop_form(obj)).find(".hiddenerror");
		if(msg.length > 0)
			errore.fadeIn(1000);
		else
			errore.hide();
		errore.find(".errortext").html(msg);
	},
	view_dish_details: function() {
		ms.popup("Description", $(obj).prev().html());
	}
});


ms.showtextarea = function(obj) {
	$(obj).parent().find("div.edittext").slideDown();
}

ms.shownext = function(obj) {
	$(obj).next().slideDown();
}


ms.form = function(obj) {
	return lookontop_form(obj);
}

ms.popup = function(title, body) {
	var popup = $("#popupmodal");
	popup.find(".realtexttitle").html(title);
	popup.find(".realtext").html(body);
	popup.openModal();
}

//ms.popup("Saini ji", "Hey mohit Saini");


// (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
// (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
// m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
// })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

// ga('create', 'UA-50390872-2', 'auto');
// ga('send', 'pageview');




// function f() {
// 	return $("body").width();
// }


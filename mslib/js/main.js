$( document ).ready(function(){
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip()
	});
	$('.dropdown-menu').click(function(e) {
		e.stopPropagation();
	});
	$(".dropdown-content").on("click", function(e){
		e.stopPropagation();
	});
	runonload();
	mylib();
});


function hideshowdown(h,s){
	$("#"+h).slideUp();
	$("#"+s).slideDown();
}

function hs_toggle(ids, timetaken) {
	doforall(ids, function(e){
		$("#"+e).slideToggle(timetaken);
	});
}

function uploadfile(obj, name) {
	var formjobj=$(obj).parent();
	if(!(formjobj.find("input[name="+name+"]").length>0)){
		var elm=document.createElement("input");
		elm.setAttribute("type","file");
		elm.setAttribute("name",name);
		elm.setAttribute("style","display:none;");
		elm.onchange=function (){
			formjobj.submit();
		}
		formjobj[0].appendChild(elm);
	}
	else{
		var elm=formjobj.find("input[name="+name+"]")[0];
	}
	elm.click();
}



function runonload(){
	// $('.button-collapse').sideNav();
	// $('.parallax').parallax();
	// $('.materialboxed').materialbox();
	// $('.slider').slider({
	// 	full_width: true,
	// 	height:350,
	// 	transition:400,
	// 	interval:3500
	// });
	// $(".collapsible_sub").collapsible();
 //    $('select').material_select();
	// $(".modal-trigger").leanModal();
}


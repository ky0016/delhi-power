var mohit={
		alerthelp:{
			alertShowButton:null,
			init:function(){
				if(this.alertShowButton!=null){
					this.alertShowButton.setAttribute("data-target","#alertPopupId");
					return;
				}
				var alertShowButton=document.createElement("button");
				alertShowButton.setAttribute("data-toggle","modal");
				alertShowButton.setAttribute("data-target","#alertPopupId");
				alertShowButton.style.display="none";
				document.body.appendChild(alertShowButton);
				this.alertShowButton=alertShowButton;
			},
			isdisplayed:function (){
				var temp=$("#alertPopupId")[0].style.display;
				return (temp!="none" && temp!="" );
			}
		},
		alert:function(text){
			if(this.alerthelp.isdisplayed())
				return;
			this.alerthelp.init();
			this.alerthelp.alertShowButton.click();
			$("#alertText").html(""+text);
		},
		confirmhelp:{
			init:function(){
				mohit.alerthelp.init();
				mohit.alerthelp.alertShowButton.setAttribute("data-target","#confirmPopupId");
			},
			isdisplayed:function (){
				var temp=$("#confirmPopupId")[0].style.display;
				return (temp!="none" && temp!="" );
			}
		},
		confirm:function(text,f,obj){
			if(this.confirmhelp.isdisplayed())
				return;
			this.confirmhelp.init();
			this.alerthelp.alertShowButton.click();
			$("#confirmText").html(""+text);
			$("#confirmconfirm").attr("onclick",f);
		}
	};

var mohit={
	lastclickedinside:0,
	clickoutside:function(obj){
		var delay=50;//ms
		setTimeout(function(){
			if(time("m")-mohit.lastclickedinside>delay*2){
				mohit.closeme(obj);
			}
		},delay);
	},
	clickinside:function(obj){
		mohit.lastclickedinside=time("m");
	},
	popup:function(id,data){
		if(id==null)
			id="";
		if(data==null)
			data={};
		mergeifunset(data,{"title":null,"body":null});
		console.log(data);
		for(i in data){
			if(data[i]!=null)
				$("#"+id+"Popup"+i).html(data[i]);
		}

		var prvvisib=$('#'+id+"Popupmain").css("visibility");
		var animtime=500;
		$('#'+id+"Popupmain").css("visibility","hidden");
		$('#'+id+"Popup").css("visibility","hidden");
		$('#'+id+"Popup").fadeIn(100,function(){
			var anim=["width","left","top"];
			var oldvals={};
			for(var i=0;i<anim.length;i++){
				oldvals[anim[i]]=$("#"+id+"Popuplayer").css(anim[i]);
			}
			oldvals["height"]="auto";
			var defaultvals={"width":"2%","left":"48%","top":"48%"};
			$("#"+id+"Popuplayer").css(defaultvals);
			$('#'+id+"Popup").css("visibility","visible");
			$("#"+id+"Popuplayer").animate(oldvals,animtime,function(){
					$('#'+id+"Popupmain").css("visibility",prvvisib);
			});
		});
	},
	alert:function(msg, timeout){
		// if(timeout == null)
		// 	timeout = 4000;
		// Materialize.toast(msg, timeout);

		mohit.popup("alert",{"title":"Alert","body":msg});
	},
	closeme:function(obj){
		$(obj).fadeOut();
//		$("#"+$(obj).attr("id")+"body").html("");
	},
	popup_close:function(id){
		mohit.closeme( $("#"+id+"Popup")[0] );
	}
};

$(document).keyup(function(e) {
	if(e.keyCode == 27){
		var allpopup=$('.PopupWrapper');
		for(var i=0;i<allpopup.length;i++){
			mohit.closeme(allpopup[i]);
		}
	}
});


function latlandist(lat1, lng1, lat2, lng2) {
	var degtorad = function(x){
		return x*(Math.PI/180);
	}
	var R = 6371000; // metres
	var ph1 = degtorad(lat1);
	var ph2 = degtorad(lat2);
	var dph = degtorad(lat2 - lat1);
	var dlem = degtorad(lng2 - lng1);
	var sin = Math.sin;
	var a = sin(dph/2) * sin(dph/2) + sin(ph1)*sin(ph2)*sin(dlem/2)*sin(dlem/2);
	var c = 2*Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
	return R*c;
}


function cluster_points(plist, f) { //f (p0, p1) -> is p0 friend of p1
	var clusters = [];
	var limit = 100;
	while(plist.length > 0) {
		limit--;
		cluster = filter(function(x) {
			return f(x,plist[0]);
		}, plist);
		plist = listaminusb(plist, cluster);
		clusters.push(cluster);
	}
	return clusters;

}

function geolocgroup(plist, zoom, screen_distance) {
	var scale = 1183315100;//scale on google map when zoom = 0
	return cluster_points(plist, function(x,y) {
		var distance = latlandist(x[0], x[1], y[0], y[1]);//meter
		return (distance*Math.pow(2, zoom) <= screen_distance*scale);
	});
}

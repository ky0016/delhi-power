var data = jsdata.rows;
var d = jsdata.rowExtra2;
var es=data["energy_shortage"][0];
var pps=data["peak_power_shortage"][0];
//console.log("pps is ");
//console.log(pps);
data["energy_shortage"]=null;
data["peak_power_shortage"]=null;
//console.log(data);
esDaily="tbl_energy_shortage_daily";
esMonthly="tbl_energy_shortage_monthly";
//esYTD="tbl_energy_shortage_ytd";
//ppsDaily="tbl_peak_power_shortage_daily";
//ppsMonthly="tbl_peak_power_shortage_monthly";
//ppsYTD="tbl_peak_power_shortage_ytd";
//console.log(en[enDaily]);
var ChartName=jsdata.ChartName;
var energy_shortage=[{"actual":es[esDaily][0]["actual"],"target":es[esDaily][0]["target"],"percent":es[esDaily][0]["percent"]},
		//{"actual":es[esMonthly][0]["actual"],"target":es[esMonthly][0]["target"],"percent":es[esMonthly][0]["percent"]},
		//{"actual":es[esYTD][0]["actual"],"target":es[esYTD][0]["target"],"percent":es[esYTD][0]["percent"]}
		];
var peak_power_shortage=[{"actual":pps[ppsDaily][0]["actual"],"target":pps[ppsDaily][0]["target"],"percent":pps[ppsDaily][0]["percent"]},
		//{"actual":pps[ppsMonthly][0]["actual"],"target":pps[ppsMonthly][0]["target"],"percent":pps[ppsMonthly][0]["percent"]},
		//{"actual":pps[ppsYTD][0]["actual"],"target":pps[ppsYTD][0]["target"],"percent":pps[ppsYTD][0]["percent"]}
		]; 

data["energy_shortage"]=energy_shortage;
//console.log(energy_shortage);
data["peak_power_shortage"]=peak_power_shortage;
var tbl_name = Object.keys(data);
//var tbl_name = Object.keys(data);
//console.log(tbl_name);
var currYear=jsdata.date[2];
var lastYear=(int(jsdata.date[2])-1);
//console.log(currDate+" "+lastYear);
function start() {
	var rows = $(".maindata").children("div");
	//console.log(rows);
	var rps = map(function(rowind, row){
		//console.log(row);
		var owltheme = $( rows[row] ).children("div.owl-theme");

		var mchild = owltheme.find("div.ringdiv");	
		console.log(mchild);
			map(function(onerowd, i) {
				// console.log(onerowd);
				//console.log(owltheme.find(".actualtext"));
				//$(owltheme.find(".actualtext")[i]).html("Actual Generation = "+onerowd["actual"]+" MU<br> Target Generation= "+onerowd["target"]+" MU");
				var outterc = radialProgress(mchild[i])
					.label("idiot")
					.onClick(function(){})
					.diameter(330)
					.value( onerowd["percent"] )
					.render();
				
			}, data[rowind]);
			owltheme.owlCarousel({
				navigation: true, // Show next and prev buttons
				slideSpeed: 300,
				paginationSpeed: 400,
				singleItem: true
			});
	}, array_keys(data));
}
$(document).ready(function() {
	start();
});
for(i=0;i<5;i++){
	y='#'.concat(ChartName[i]);
	var tblData=data[tbl_name[i]];
	ChartName[i] = c3.generate({
	    bindto: y,
	    data: {
	        json: [
	          {Actual:tblData[4]["actual"]/1000.0,Target:tblData[4]["target"]/1000.0,Efficiency: tblData[4]["percent"] ,date:lastYear},
	          {Actual:tblData[2]["actual"]/1000.0,Target: tblData[2]["target"]/1000.0,Efficiency: tblData[2]["percent"],date:currYear}
	        ],
	      keys: {
	        x: 'date', // it's possible to specify 'x' when category axis
	        value: ['Actual', 'Target','Efficiency'],
	      },
	      axes: {
	        Efficiency: 'y2'
	      },
	      types: {
	        Actual: 'bar',
	        Target: 'bar' // ADD
	      }
	    },
	    axis: {
	      y: {
	        label: {
	          text: 'Power(x1000 MU)',
	          position: 'outer-middle'
	        }
	      },
	      y2: {
	        show: true,
	        label: {
	          text: '% Efficiency',
	          position: 'outer-middle'
	        }
	      }
	    },
	    size: {
	      height: 330
	    }
	});
}
for(i=5;i<10;i++){
	y='#'.concat(ChartName[i]);
	var tblData=data[tbl_name[i-5]];
	ChartName[i] = c3.generate({
	    bindto: y,
	    data: {
	        json: [
	          {Actual:tblData[3]["actual"]/1000.0,Target:tblData[3]["target"]/1000.0,Efficiency: tblData[3]["percent"] ,date:lastYear},
	          {Actual:tblData[1]["actual"]/1000.0,Target:tblData[1]["target"]/1000.0,Efficiency: tblData[1]["percent"],date:currYear}
	        ],
	      keys: {
	        x: 'date', // it's possible to specify 'x' when category axis
	        value: ['Actual', 'Target','Efficiency'],
	      },
	      axes: {
	        Efficiency: 'y2'
	      },
	      types: {
	        Actual: 'bar',
	        Target: 'bar' // ADD
	      }
	    },
	    axis: {
	      y: {
	        label: {
	          text: 'Power(x1000 MU)',
	          position: 'outer-middle'
	        }
	      },
	      y2: {
	        show: true,
	        label: {
	          text: '% Efficiency',
	          position: 'outer-middle'
	        }
	      }
	    },
	    size: {
	      height: 330
	    }
	});
}

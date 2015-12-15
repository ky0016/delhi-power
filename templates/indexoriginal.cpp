main2(js: ["js/index.js?reload"]) {
	blogurl = "";
	tablink1 = [blogurl];
	tabname1 = ["Blog"];
	withChart=['Total Power Generation', 'Coal Power Generation', 'Ntpc Power Generation', 'Gas Power Generation', 'Hydro Power Generation'];
//	header2(tablink:[BASE+"chefjoin"], tabname:["Be a Chef"], tablink1: tablink1, tabname1: tabname1);
	//header1_power(ChartName:ChartName,tabname: tabs, tablink: rowkeydef_href, bgcolors:["blue", "blue", "red", "red", "red"], colors:["red", "red", "red", "pink", "pink"]);
	rowkeysdef2 = rowExtra1.keys;
	rowkeysdef = rows.keys;

	//br();
	//print(rows["peak_power_shortage"]);
	//print(rowkeysdef);
	div() {
		div(class: "container", id: "mohitsaini") {
			form() {
				div(class: "row") {
					input2(id: "date", label: "Date", iclass: "datepicker", placeholder: "DD-MM-YYYY");
				}
				div() {
					button1(attr: {type: "submit"}, name: "Submit");
				}
				br();
			}
		}
	}
	//colors=["black","black","red ","green","blue"];
	div(class: "maindata") {
		for(j,jj, withChart) {
			div(id: rowkeysdef[jj],style:{"color":"black"}) {
				div(class: "owl-carousel owl-theme") {
					for(i, 3) {
						div(class: "maindiv1", style: {}, attr: {align: "center"}) {
							div(attr: {align: "center"}) {
								div(style: {"font-size": "40px"}) {
									print(j);
								}
								b() {
									print(labeltext[i]);
									br();
								}
								span(class: "actualtext") {
									//print("kailash");
								}
							}
							br();
							br();
						    div(class: "ringdiv");
						    br();
						}
					}
					div(attr: {align: "center"}) {
						div(style: {"font-size": "40px"}) {
							print(j);
						}
						b() {
							print(compMYTD[0]);
							br();
							
						}
						br();
						br();
						div(id: ChartName[jj]);
						br();
					}
					div(attr: {align: "center"}) {
						div(style: {"font-size": "40px"}) {
							print(j);
						}
						b() {
							print(compMYTD[1]);
							br();
							
						}
						br();
						br();
						div(id: ChartName[jj+5]);
						br();
					}
				}
			}
			hr();
			br();
			
		}
		div(id:"energy_shortage") {
				div(class: "owl-carousel owl-theme") {
					//for(i, 3) {
						div(class: "maindiv1", style: {}, attr: {align: "center"}) {
							div(attr: {align: "center"}) {
								div(style: {"font-size": "40px"}) {
									print("Total Energy Shortage");
								}
								b() {
									print(labeltextExtra1[0]);
									br();
								}
								span(class: "actualtext") {
									print("Actual Shortage =");

									print(rows["energy_shortage"][0]["tbl_energy_shortage_daily"][0]["actual"]+"%");
									br();
									
									print("Target Shortage =");
									print(rows["energy_shortage"][0]["tbl_energy_shortage_daily"][0]["target"]+"%");
									br();
									br();

									//print();
									//print(energy_shortage["percent"]);
									//br();
									//print("target ="+ date );
								}
							}
						    div(class: "ringdiv");
						    br();
						}
					//}
				}
				hr();
				br();
		}
		div(id:"peak_power_shortage") {
				div(class: "owl-carousel owl-theme") {
					//for(i, 3) {
						div(class: "maindiv1", style: {}, attr: {align: "center"}) {
							div(attr: {align: "center"}) {
								div(style: {"font-size": "40px"}) {
									print("Peak Power Shortage");
								}
								b() {
									print(labeltextExtra2[0]);
									br();
								}
								
								span(class: "actualtext") {
									print("Actual Shortage =");
									print(rows["peak_power_shortage"][0]["tbl_peak_power_shortage_daily"][0]["actual"]+"%");
									br();
									print("Target Shortage =");
									print(rows["peak_power_shortage"][0]["tbl_peak_power_shortage_daily"][0]["target"]+"%");
									br();
									br();
								}
							}
						    div(class: "ringdiv");
						    br();
						}
					//}
				}
		}
		hr();
		br();
		
	}
	
		div( style: {}, attr: {align: "center"}) {
							div(attr: {align: "center"}) {
								div(style: {"font-size": "40px","color":"red"}) {
									print("Critical Coal Plants");
								}
								b() {
									print("Number of ");
									print(labeltextcritical[0]);
									//print
									div(style: {"font-size": "200px","color":"green"}) {
									//print(200);
									print(scritical["tbl_super_critical_coal_plant"][0]["number"]);
									br();
									//br();
								}
								}
								}
								//br();
								hr();
								br();
							}   
						
	
	
		div(style: {}, attr: {align: "center"}) {
							div(attr: {align: "center"}) {
								div(style: {"font-size": "40px","color":"red"}) {
									print("Super Critical Coal Plants");
								}
								b() {
									print("Number of Super ");
									print(labeltextcritical[0]);
									//print("Number of Super Critical Plants on   ");
									div(style: {"font-size": "200px","color":"green"}) {
									print(scritical["tbl_super_critical_coal_plant"][0]["number"]);
									//print(200);
									//br();
									
								}
									
								}	
							}
							
						    hr();
						   br();
						}
}


_sql = sqllib(( g(globals(), "_agent") == "poorvi" and (_server == "gcl" or _server == "csc")), db_data);# or (doifcan1(lambda: r1(MySQLdb, 0), 1)), db_data);
#import calender
execfile(ROOT+"py/kurry.py");
_kurry = kurry();
import calendar;
import datetime;
_config["realmsg"] = (_server[:3] == "aws");
_config["realmail"] = False;
_config["users"] = {"a": "Admin", "c": "Chef", "u": "User"};


_config["adminpass"] = "Admin_Secure432";
_config["adminmail"] = "mohitsaini1196@gmail.com";
_config["config"] = {
	"chefagelist": ["18-23 Years", "24-45 Years", "45-60 Years", "Above 60 Years"],
	"chefhowmanypeople": ["5-10", "11-20", "21-30"],
	"cheflanguages": ["Hindi", "English"],
	"deliverydistance": 5, #Km
	"foodtype": cod([
		("", "Meal Type"),
		("v", "Veg"),
		("n", "Non-Veg")
	])
};

mifu(_config, {
	"dslots": {
		"l": range(3600*12, 3600*15, 1800), #12:00 PM to .. half an hour slots... before 3:00 PM (excluding)
		"d": range(3600*20, 3600*23, 1800)
	},
	"ordertimelimit": {
		"l": 3600*10, #10 AM
		"d": 3600*(12+7) # 7 PM
	}
});

_config["status"] = {
	"c": "Order Confirmed",
	"i": "Shipping initiated",
	"d": "Delivered",
	"f": "Failed"
};

init_sql_config();

_config["timef"] = "%I:%M %p";
_config["datef"] = "%a, %b %d %Y";
_config["datef1"] = "%a, %b %d";
_config["timedatef"] = "%a, %b %d %Y, %I:%M %p";


class pagehandler:
	def __init__(self, name):
		self.name = name;
		if(False and _server == "gcl"):
			elc("python client.py 10.208.20.186 ./compile");
		self.jsdata = {"HOST": HOST, "BASE": BASE, "curpage": self.name, "_server": _server, "_ec": _ec, "_formerror": _formerror};
		self.methodmap = eval("{"+", ".join(mappl((lambda x: '"'+x+'": self.'+x), ["index", "seeall"]))+"}");
#		self.methodmap = {"index": self.index, "test": self.test, "account": self.account, "profile": self.profile, "menu": self.menu, "cart": self.cart};

	def call(self):
		runmethod = (rifn(self.methodmap[self.name](), {}) if self.methodmap.has_key(self.name) else {});
		logininfo = { "islogin": islogin(), "loginid": loginid(), "loginname": loginname() };
		mifu(self.jsdata, logininfo);
		return mifu(mifu(runmethod, {"jsdata": json.dumps(self.jsdata), "config": _config["config"]}), logininfo);

	def orders(self):
		return {
			"orderl": mappl(order_convrow, getorderl(islogin(), loginid()))
		};


	def cart(self):
		def convrow(row, rind):
			row["datetimetext"] = t2f(_config["datef"], row['datetime']);
			plate_remaining = intf(row["plimit"])-intf(row["numplatebooked"])
			row["tlist"] = range(1, plate_remaining+1);
			row["distance"] = round(float("0"+str(rifn(row["distance"],0))), 1);
			numbering = lambda xx: mappl(lambda x, y: (str(y+1)+". "+x) if len(xx) > 1 else x, xx);
			row["error"] = "<br>".join(numbering(mappl(idf, ["All plates are Sold!", "Sorry!! Ordering Time has passed", "Your Delivery Location is too far from selected home chef("+str(row["distance"])+"Km)"], lambda y, x: [plate_remaining <= 0, (row["datetime"]+ _config["ordertimelimit"][row["lord"]] < tnow()), (row["distance"] > _config["config"]["deliverydistance"])][x])));
			return row;
		dstime = daystarttime();
		return {
				"cartl": mappl(convrow, _sql.g("select * from "+gtable("cart1"), mifu({"uid": loginid()}, mapp(idf, getloc()[:2], None, lambda x:["lat", "lng"][x])) )), 
				"dslots": dict(mapp(lambda val, lord: mappl(lambda x: t2f(_config["timef"], dstime+x), val),_config["dslots"])),
				"address": getloc()
			};

	def menu(self):
		saveloc();
		daydatetime = intf(g(_get, "datetime", daystarttime()));
		foodtype = g(_get, "foodtype", '');

		outp = mapp(lambda x:_sql.g(gtable("dispdish5", 0), mifu({"datetime": daydatetime, "lord": x, "isveg": ife(foodtype == '', '%', foodtype)}, mapp(idf, getloc()[:2], None, lambda x:["lat", "lng"][x]))), ["l", "d"], None, lambda x: ["lunch", "dinner"][x]);
		day5times = _kurry.day5times();

		outp["foodtypeurls"] = mappl(lambda x: urllib.urlencode({"datetime": daydatetime, "foodtype": x}), _config["config"]["foodtype"].keys());
		outp["daysurls"] = mappl(lambda y: urllib.urlencode({"datetime": y, "foodtype": foodtype}), day5times["timel"]);

		outp["foodtypetext"] = _config["config"]["foodtype"][foodtype];

		#outp["dayselecttext"] = day5times["textl"][(day5times["timel"].index(daydatetime) if (daydatetime in day5times["timel"]) else 0)];
		outp["daydatetime"] = daydatetime;
		outp["day5times"] = day5times;
		return outp;

	def index(self):
		idate = g(_get, 'date', t2f_date());
		int_date = s2t(idate);
		obj_date = timeint2obj(int_date);
		sql_date = t2f("%Y-%m-%d", int_date);
		#print(obj_date.year);
		rnames = ["total_power_generation", "coal_power_generation", "ntpc_power_generation", "gas_power_generation", "hydro_power_generation"];
		rExtra1 = ["tbl_energy_shortage_daily", "tbl_energy_shortage_monthly", "tbl_energy_shortage_ytd"];
		rExtra2=["tbl_peak_power_shortage_daily","tbl_peak_power_shortage_monthly", "tbl_peak_power_shortage_ytd"];
		rCritical=["tbl_critical_coal_plant"];
		rSuperCritical=["tbl_super_critical_coal_plant"];

		row = lambda tname: mappl(lambda x: sifu(x, "percent", ((100*intf(x["actual"]))/intf(x["target"], 1)) ), [
		_sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname+" where date = {date} ", {"date": t2f("%Y-%m-%d", int_date)}),
		_sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname+" where day(date) <= {day} AND (month(date), year(date)) =({month}, {year})", {"day": obj_date.day, "month": obj_date.month, "year": obj_date.year})
		, _sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname+" where date <= {date} AND year(date) ={year}", {"date": sql_date, "year": obj_date.year})
		, _sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname+" where day(date) <= {day} AND (month(date), year(date)) =({month}, {year})", {"day": obj_date.day, "month": obj_date.month, "year": obj_date.year-1})
		, _sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname+" where date <= {date} AND year(date) ={year}", {"date": sql_date, "year": obj_date.year-1})
		]);
		
		
		rowCritical= lambda tname: mappl(lambda x: sifu(x, "number", ((100*intf(x["actual"]))/intf(x["target"], 1)) ) , [
		_sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname+" where date = {date} ", {"date": t2f("%Y-%m-%d", int_date)})]);

		rowExtra= lambda tname2: mappl(lambda x: sifu(x, "percent", ((100*intf(x["actual"]))/intf(x["target"], 1)) ), [
		_sql.g1("select cast(sum(actual) as unsigned) as actual, cast(sum(target) as unsigned) as target from "+tname2+" where date = {date} ", {"date": t2f("%Y-%m-%d", int_date)})]);
		


		self.jsdata["rowExtra1"] = mapp(lambda x: rowExtra(x), rExtra1, None, lambda x: rExtra1[x]);
		self.jsdata["rowExtra2"] = mapp(lambda x: rowExtra(x), rExtra2, None, lambda x: rExtra2[x]);
		self.jsdata["rows"] = mapp(lambda x: row("tbl_"+x), rnames, None, lambda x: rnames[x]);
		self.jsdata["rows"]["energy_shortage"] = [self.jsdata["rowExtra1"]];
		self.jsdata["rows"]["peak_power_shortage"] = [self.jsdata["rowExtra2"]];
		self.jsdata["critical"] = mapp(lambda x: rowCritical(x), rCritical, None, lambda x: rCritical[x]);
		self.jsdata["scritical"] = mapp(lambda x: rowCritical(x), rSuperCritical, None, lambda x: rSuperCritical[x]);

		 

		self.jsdata["ChartName"] = ["TotalYTD","CoalYTD","NtpcYTD","GasYTD","HydroYTD","TotalMTD","CoalMTD","NtpcMTD","GasMTD","HydroMTD","EnergyMTD","EnergyYTD"];
		self.jsdata["date"] = [obj_date.day,obj_date.month,obj_date.year];
		#temp= ["total_power", "coal_gen", "ntpc_gen", "gas_gen", "hydro_gen"];
		outp = {"rows": self.jsdata["rows"]};
		outp ["critical"]= self.jsdata["critical"];
		outp ["scritical"]= self.jsdata["scritical"];
		outp ["rowExtra1"]= self.jsdata["rowExtra1"];
		outp ["date"]= self.jsdata["date"];
		lastYear=str(obj_date.day)+"-"+str(obj_date.month)+"-"+str(int(obj_date.year)-1);
		dateWithStrMonth=datetime.datetime.strptime(idate, "%d-%m-%Y").strftime("%d-%b-%Y");
		LastDateWithStrMonth=datetime.datetime.strptime(lastYear, "%d-%m-%Y").strftime("%d-%b-%Y");

		outp ["rowExtra2"]= self.jsdata["rowExtra2"];
		outp["rowkeydef_href"] = mappl(lambda x: "#"+x, outp["rows"].keys());
		outp["rowkeys"] = mappl(lambda x: x.replace("_", " ").title(), outp["rows"].keys());
		outp["rowExtrakeys1"] = mappl(lambda x: x.replace("_", " ").title(), outp["rowExtra1"].keys());
		outp["rowExtrakeys2"] = mappl(lambda x: x.replace("_", " ").title(), outp["rowExtra2"].keys());
		outp["tabs"] = mappl(lambda x: x.split("_")[0].title(), outp["rows"].keys());
		#jsdata["rowkeys"] = mappl(lambda x: x.replace("_", " ").title(), outp["rows"].keys());
		outp["ChartName"] = ["TotalYTD","CoalYTD","NtpcYTD","GasYTD","HydroYTD","TotalMTD","CoalMTD","NtpcMTD","GasMTD","HydroMTD"];
		outp["labeltext"] = ["Daily Generation:"+dateWithStrMonth, "Month Till "+dateWithStrMonth, "Year Till "+dateWithStrMonth];
		outp["labeltextExtra1"] = ["Energy Shortage on :"+dateWithStrMonth];
		outp["labeltextExtra2"] = ["Peak Energy Shortage on :"+dateWithStrMonth];
		outp["labeltextcritical"] = ["Critical Coal Plants on :"+dateWithStrMonth];
		#outp["labeltextExtra2"] = ["Super Critical Coal plant on :"+dateWithStrMonth];
		
		outp["compMYTD"] = ["MTD "+dateWithStrMonth+" Vs MTD "+LastDateWithStrMonth,"YTD "+dateWithStrMonth+" Vs YTD "+LastDateWithStrMonth];
		
		return outp;

	def ajaxactions(self):
		if( has_key(_actions, g(_post, "action"))):
			return _kurry.handler(_post,  _actions[_post["action"]]);
		else:
			return {"ec": -4};

	def test(self):
		return {"_session": _session};

	def seeall(self):
		return {"allt": mappl(lambda x: {"data": sqlr2table(_sql.sval(x)), "name": x}, ['tbl_coal_gen', 'tbl_critical_coal_plant', 'tbl_energy_shortage_daily', 'tbl_energy_shortage_monthly', 'tbl_energy_shortage_ytd', 'tbl_gas_gen', 'tbl_hydro_gen', 'tbl_list_coal_plant', 'tbl_ntpc_gen', 'tbl_peak_power_shortage_daily', 'tbl_peak_power_shortage_monthly', 'tbl_peak_power_shortage_ytd', 'tbl_super_critical_coal_plant', 'tbl_total_power'])};
		['tbl_coal_gen', 'tbl_critical_coal_plant', 'tbl_energy_shortage_daily', 'tbl_energy_shortage_monthly', 'tbl_energy_shortage_ytd', 'tbl_gas_gen', 'tbl_hydro_gen', 'tbl_list_coal_plant', 'tbl_ntpc_gen', 'tbl_peak_power_shortage_daily', 'tbl_peak_power_shortage_monthly', 'tbl_peak_power_shortage_ytd', 'tbl_super_critical_coal_plant', 'tbl_total_power'];







#"energy shortage month: "+t2f("%m-%Y", int_date),"energy shortage year: "+t2f("%Y", int_date)]
#, "peak energy shortage month: "+t2f("%m-%Y", int_date),"peak energy shortage year: "+t2f("%Y", int_date)
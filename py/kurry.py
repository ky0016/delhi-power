_ec = {
	-1: "Incorrect password or OTP",
	-2: "Phone number is already registered",
	-3: "OTP is Incorrect",
	-4: "Action handler not valid",
	-5: "Insufficient arguments",
	-6: "Invalid Input",
	-7: "Incorrect password",
	-8: "This Phone number is already used",
	-9: "Sorry!! You don't have privileges to perform this action",
	-10: "It is already added",
	-11: " Sorry!!You are Blocked!",
	-12: "Invalid phone number",
	-13: "Sorry!! You need to login first"
};


mifa(_formerror, {
	"idel": "",
	"simple": "Should not Empty",
	"email": "Not valid email format",
	"password": "Didn't matched",
	"phone": "Should be 10 digit",
	"otp": "Should be 8 digit",
	"password1": "Should Be Strong"
});

def init_sql_config():
	global _config;
	_config["sql_help"] = {};

	_config["sql_help"]["latlng"] = lambda lat1='lat',lng1='lng': "(((acos(sin(({lat}*pi()/180)) * sin(("+lat1+"*pi()/180))+cos(({lat}*pi()/180)) * cos(("+lat1+"*pi()/180)) * cos((({lng}- "+lng1+")* pi()/180))))*180/pi())*60*1.1515*1.609344)"

	_config["sql"] = {};

	_config["sql"]["users1"] = "select chef.aboutus, chef.lat, chef.lng, users.* from users left join chef on chef.chefid = users.id"; #Valid for Chef users list

	#_config["sql"]["dishes1"] = "select users.name, users.profilepic, dishes.* from dishes left join users on users.id = dishes.cid";
	_config["sql"]["dishes1"] = "select users1.name, users1.profilepic, users1.lat, users1.lng, users1.address, dishes.* from dishes left join "+gtable("users1")+" on users1.id = dishes.cid";


	_config["sql"]["dishes2"] = "select * from "+gtable("dishes1")+" where cid={cid}";


	_config["sql"]["dispdish0"] = "select cast(IFNULL(sum(orders.numplate),0) as unsigned)as numplatebooked, dispdish.* from dispdish left join orders on (dispdish.datetime = orders.datetime AND dispdish.dishid = orders.dishid AND dispdish.lord = orders.lord) group by dispdish.datetime,dispdish.dishid,dispdish.lord"

	_config["sql"]["dispdish1"] = "select cast(sum((lord='l')*plimit) as unsigned)as llimit, cast(sum((lord='l')*numplatebooked) as unsigned) as ollimit, cast(sum((lord='d')*numplatebooked) as unsigned) as odlimit, cast(sum((lord = 'd')*plimit) as unsigned) as dlimit, cid, datetime, dishid from "+gtable("dispdish0")+" group by cid, datetime, dishid";

	_config["sql"]["dispdish2"] = "select "+ ', '.join(mappl(lambda i:", ".join(mappl(lambda x:" cast(sum((datetime={x"+i+"})*"+x+"limit) as unsigned) as "+x+"limit"+i+"", ["l", "d", "ol", "od"])) , mappl(lambda x:str(x), range(5)))) +", dispdish1.cid, dispdish1.dishid from "+gtable("dispdish1")+" where datetime>={x0} AND datetime<={x4} group by cid, dishid ";

	_config["sql"]["dispdish3"] = "select dishes1.*, "+(", ".join(mixl(mappl(lambda i:mappl(lambda x:"dispdish2."+x+"limit"+str(i), ["l", "d", "ol", "od"]), range(5)))))+" from "+gtable("dishes1")+" left join "+gtable("dispdish2")+" on dishes1.cid = dispdish2.cid AND dishes1.id = dispdish2.dishid";

	_config["sql"]["dispdish4"] = "select * from "+gtable("dispdish0")+" where datetime={datetime} AND plimit > 0 AND lord ={lord} ";

	_config["sql"]["dispdish5"] = "select dispdish4.plimit, dispdish4.numplatebooked, dispdish4.datetime, dispdish4.lord,"+sqlhelp("latlng")+" as distance, dishes1.* from "+gtable("dispdish4")+" left join "+gtable("dishes1")+" on dishes1.id = dispdish4.dishid where ((plimit-numplatebooked > 0 or true) and (isveg like {isveg}))  having distance <= "+str(_config["config"]["deliverydistance"])+"";

	_config["sql"]["cart1"] = "select dispdish0.plimit, dispdish0.numplatebooked, "+sqlhelp("latlng", {"lat1": "chef.lat", "lng1": "chef.lng"})+" as distance, dishes1.cid, dishes1.name, dishes1.title, dishes1.price, cart.* from cart left join "+gtable("dishes1")+" on dishes1.id = cart.dishid left join "+gtable("dispdish0")+" on (dispdish0.datetime = cart.datetime AND dispdish0.dishid = cart.dishid AND dispdish0.lord = cart.lord) left join chef on chef.chefid = dishes1.cid where uid={uid}";

	_config["sql"]["orders1"] = "select users.name as uname, dishes1.name as cname, orders.address as uaddress, dishes1.address as caddress, IFNULL(dishes1.price, 0) as price, dishes1.title, dishes1.lat as clat, dishes1.lng as clng, orders.* from orders left join users on users.id = orders.uid left join "+gtable("dishes1")+" on (dishes1.id=orders.dishid ) order by time desc";
	_sql.uniqc["cart"] = ["datetime", "dishid", "lord", "uid"];



_actions = {
	"login": {
		"need": ["loginphone", "loginpass"],
		"mapping": {"loginphone": "phone", "loginpass": "password"},
	},
	"signup": {
		"need": ["signupphone", "signuppass", "signupotp", "signupname"],
		"mapping": {"signupphone": "phone", "signuppass": "password", "signupname": "name", "signupotp": "otp"}
	},
	"sendotp": {
		"mapping": {"loginphone": "phone", "signupphone": "phone"},
		"ignoreother": False # Don't ignore the arguments, other then which are required.
	},
	"adddish": {
		"need": ["dishprice", "dishtitle", "descp", "cid", "isveg"],
		"mapping": {"dishprice": "price", "dishtitle": "title"}
	},
	"savedaymenu": {
		"need": ["cid", "datetime", "platelimits"],
	},
	"saveaboutinfo": {
		"need": ["aboutus", "chefid"]
	},
	"chefjoinus": {
		"need": ["lat", "lng"],
		"ignoreother": False,
		"mapping": {"mobile": "phone"}
	},
	"addincart": {
		"need": ["dishid", "lord", "datetime"],
		"eadd": ["uid"],
		"whocan": "login" #can be 1. "all", 2. "login", 3. ["a", "c"]
	},
	"delfromcart": {
		"need": ["id"],
		"eadd": ["uid"],
		"whocan": "login",
	},
	"order": {
		"need": ["eaddress", "olist"],
		"whocan": ["u"],
		"eadd": ["time", "uid"],
		"mapping": {"eaddress": "address"}
	},
	"deletedisp": {
		"need": ["dishid"],
		"whocan": ["a"],
		"ignoreother": False
	},
	"blockunblock": {
		"need": ["uid", "isblock"],
		"whocan": "a",
	},
	"change_address": {
		"need": ["lng", "lat", "gaddress", "address", "cid"],
		"whocan": "a"
	},
	"deleteaccount": {
		"need": ["uid"],
		"whocan": "a"
	},
	"createadmin": {
		"need": ["phone", "password"],
		"whocan": "a"
	}
}

class kurry:
	def __init__(self):
		self.ec = None;
		self.mapping = eval("{"+", ".join(mappl((lambda x: '"'+x+'": self.'+x), _actions.keys()))+"}");

	def handler(self, udata, specf):
		self.ec = 1;
		computed = None;

		mifu(specf, {"need": [], "mapping":{}, "ignoreother": True, "eadd": [], "whocan": "all"});

		if(not(set(specf["need"]) <= set(udata.keys()))):
			self.ec = -5;
		elif(not(specf["whocan"] == "all") and not(islogin())):
			self.ec = -13;
		elif(not(specf["whocan"] == "all") and not( specf["whocan"] == "login") and not(islogin() in specf["whocan"])):
			self.ec = -9;
		else:
			udata_f = mapp(idf, udata, lambda x,y: (not(specf["ignoreother"]) or (y in specf["need"])), lambda x,y: g(specf["mapping"], x, x));
			mifu(udata_f, pkey1({"uid": loginid(), "time": tnow()}, specf["eadd"]), True);
			computed = self.mapping[udata["action"]](udata_f);
		return {"ec": self.ec, "data": computed };

	def createadmin(self, data):
		pass

	def deleteaccount(self, data):
		_sql.dval("users", {"id": data["uid"]}, limit=1);
		_sql.dval("chef", {"chefid": data["uid"]}, limit=1);

	def blockunblock(self, data):
		_sql.uval("users", {"conf": ife(data["isblock"] == "1", None, 'b')}, {"id": data['uid']});


	def change_address(self, data):
		_sql.uval("chef", pkey1(data, ["lng", "lat"]), {"chefid": data["cid"]});
		_sql.uval("users", {"address": data["address"]+" "+data["gaddress"]}, {"id": data["cid"]})

	def deletedisp(self, data):
		if(has_key(data, "datetime")):
			_sql.dval("dispdish", dict(pkey1(data, ["dishid", "lord", "datetime"])), 1);
		else:
			_sql.dval("dispdish", {"dishid": data["dishid"]});
			_sql.dval("dishes", {"id": data["dishid"]});

	def order(self, data):
		mappl(lambda x: _sql.ival("orders", mifu(x, pkey1(data, ["uid", "time", "address"]))), data["olist"]);
		_sql.dval("cart", {"uid": loginid()});
		cids = list(set(mappl(lambda x: x["cid"], data["olist"])))+[loginid()];
		cinfos = mapp(lambda x:_sql.sval("users", "name, email, type", {"id": x}, 1), cids, None, lambda x: cids[x]);
		mailinfo = {"uname": rifn(cinfos[loginid()]["name"], "Somebody") };
		mapp(lambda c,i: filemail1(c["email"], "order", mifu({"cname": c["name"]}, mailinfo)), cinfos, lambda x: x["type"] == "c");
		adminmail("order_admin", mailinfo);

	def addincart(self, data):
		if(not intf(_sql.ival("cart", dict(data)), False)):
			self.ec = -10;

	def delfromcart(self, data):
		return _sql.dval("cart", dict(pkey1(data, ["id", "uid"])), 1);

	def chefjoinus(self, data):
		if(isuserexist(data["phone"])):
			self.ec = -8;
		else:
			iid = _sql.ival("users", dict(mifu(pkey1(data, ["phone", "email", "name", "password"]), {"address": data["address"]+" "+data["gaddress"], "type": "c", "profilepic": "photo/chef2.jpg"} )));
			_sql.ival("chef", dict(mifu(pkey1(data, ["gender", "age", "languages", "cookpeople", "isnonveg", "isdegree", "lat", "lng"]), {"aboutus": "", "chefid": iid})));
			adminmail("chefjoinus", {"cname": data["name"]});
			filemail1(data["email"], "chefjoinus_chef", {"cname": data["name"]});
			return iid;

	def saveaboutinfo(self, data):
		return _sql.uval("chef", {"aboutus": data["aboutus"]}, {"chefid": data["chefid"]});

	def savedaymenu(self, data):
		limitdata = data["platelimits"];
		if(limitdata):
			_sql.dval("dispdish", pkey1(data, ["cid", "datetime"]));
			return mappl(lambda x: _sql.ival("dispdish", x), mappl(lambda x: mifu(dict(mapp(idf, x, None, lambda x: ["dishid", "lord", "plimit"][x] )), pkey1(data, ["cid", "datetime"])), limitdata, lambda x: len(x)==3 ));
		else:
			self.ec = -6;


	def sendotp(self, data):
		_session["otp"] = str(random.randint(10000000,99999999));
		filemsg(data["phone"], "datar/msgs/otp.txt", {"otp": _session["otp"]});

	def login(self, data):
		if(data["password"] ==  g(_session, "otp")):
			return self.signup(data);
		else:
			qr = _sql.sval("users", "*", pkey1(data, ["phone"]), 1); #Query Result
			if(qr == None):
				self.ec = -12;
			elif(qr["conf"] == "b"):
				self.ec = -11;
			elif(g(qr, "password") == data["password"]):
				login(qr["id"], qr["type"], pkey1(qr, ["name"]));
				return qr["id"];
			else:
				self.ec = -1;

	def signup(self, data, typ="u"):
		if( data.has_key("otp") and data["otp"] != g(_session, "otp")):
			self.ec = -3;
			return;
		cdata = _sql.sval("users", "*", {"phone": data["phone"]}, 1)
		if(cdata):
			if(cdata["conf"] == "b"):
				self.ec = -11;
			else:
				login(cdata["id"], cdata["type"], pkey1(cdata, ["name"]));
				return cdata["id"];
		else:
			idata = sifu(pkey1(data, ["phone", "password", "email", "name"]), "type", typ, True);
			iid = _sql.ival("users", idata);
			login(iid, typ, pkey1(data, ["name"]));
			return iid;

	def adddish(self, data):
		imgname = "";
		if(_files.has_key("dishpic") and _files["dishpic"]["error"] == 0):
			imgname = uploadimg(_files["dishpic"]["tmp_name"], _files["dishpic"]["name"], [630, 400]);
		_sql.ival("dishes", dict(sifu(data, "pic", imgname)));
		pass


	def day5times(self):
		tnow0 = daystarttime();
		outp = {"textl":["Today"]+list(t2f("%a, %b %d", tnow0+24*3600*i) for i in xrange(1,5)), "timel":list(tnow0+3600*24*i for i in xrange(5)), "tabkeys": mappl(lambda x:"day5_"+str(x), range(5)) };
		outp["tabkeys1"] = mappl(lambda x: "#"+x, outp["tabkeys"]);
		return outp;




# From Chef & Admin


def initloc():
	sifu(_session, "loc", [0, 0, ""]);


def saveloc():
	initloc();
	_session["loc"] = mappl(lambda i,j: g(_get, i, _session["loc"][j]), ["lat", "lng", "address"]);


def getloc():
	initloc();
	stored = _session["loc"]
	return mappl(lambda x,y: g(_get, x, stored[y]), ["lat", "lng", "address"]);


def getorderl(utype, uid=0):
	if(utype == "c"):
		orderl = _sql.g("select * from "+gtable("orders1")+" where cid={cid}", {"cid": uid});
	elif(utype == "u"):
		orderl = _sql.g("select * from "+gtable("orders1")+" where uid={uid}", {"uid": uid});
	elif(utype == "a"):
		orderl = _sql.g("select * from "+gtable("orders1"));
	else:
		orderl = [];
	return orderl;


def order_convrow(row, rind):
	row["datetimetext"] = t2f( r2(_config["datef"]+"<br>"+_config["timef"], _config["timedatef"]), row['datetime'] + _config["dslots"][row["lord"]][row["dslots"]-1])+" ("+{"l": "Lunch", "d": "Dinner"}[row["lord"]]+")";
	row["timetext"] = t2f(_config["timedatef"], row["time"]);
	row["status_text"] = _config["status"][row["status"]]
	return row;


execfile(_mslib+"py/config.py");

def mprint(*x):
	global _printout;
	_printout += (", ".join(str(i) for i in x));


def msgdummy(phone, msg):
	msgfile = "data/msgf";
	writefd(open(msgfile, "a"), "To: {0}\nAt: {1}\n{2}\n{3}\n{4}\n{4}\n\n\n".format(phone, t2f_time(), '-'*20, msg, '-'*20));

def maildummy(email, sub, msg):
	mailfile = "data/mailf";
	writefd(open(mailfile, "a"), "To: {0}\nSubject: {1}\nAt: {2}\n{3}\n{4}\n{5}\n{5}\n\n\n".format(email, sub, t2f_time(), '-'*20, msg, '-'*20));

def msgreal(phone, msg):
#	return msgreal1(phone, msg);
	return curl("http://api.textlocal.in/send/", {"username": "harshaccent@gmail.com", "hash": "Woodwindow62", "numbers": phone, "sender": 'KURYBX', "message": msg});
	url="http://mysms.msgclub.net/rest/services/sendSMS/sendGroupSms?"+ urllib.urlencode({"AUTH_KEY": key, "message": msg, "senderId": "SMSTST", "routeId": "1", "mobileNos": phone, "smsContentType": "english"});
	return s2j(mcurl(url));

def msgreal1(phone, msg):
	url="http://216.245.209.132/rest/services/sendSMS/sendGroupSms?AUTH_KEY=14e4de84f23c84d81f24b8fb69d1e0&senderId=GETIIT&routeId=1&smsContentType=english&"+urllib.urlencode({"message": msg, "mobileNos": phone});
	return s2j(mcurl(url));

def mailreal(email, sub, msg):
	pass
	
def sendmsg(phone, msg):
	msgdummy(phone, msg);
	msgreal(phone, msg) if _config["realmsg"] else None;

def sendmail(email, sub, msg):
	maildummy(email, sub, msg);
	mailreal(email, sub, msg) if _config["realmail"] else None;

def filemsg(phone, fn, data={}):
	return sendmsg(phone, read_file(fn).format(**data));

def filemail(email, fn, data={}):
	msg = read_file(fn).format(**data);
	return sendmail(email, msg.split("\n")[0], msg.split("\n", 1)[1]);

def filemail1(email, fn, data={}):
	return filemail(email, "datar/mails/"+fn+".txt", data);

def adminmail(fn, data={}):
	filemail1(_config["adminmail"], fn, data);

def init_mailmsgsystem():
	elc("mkdir -p data; > data/msgf; > data/mailf; chmod 777 data -R ");

def login(id, typ, ext={}):
	global _session;
	_session["login"] = mifu({"id": id, "type": typ}, ext);

def logininfo():
	return g(_session, "login");

def loginname():
	return doifcan(lambda: logininfo()["name"].title(), (), "Profile");

def islogin():#Also return login type
	return _session["login"]["type"] if (g(g(_session, "login"), "id") > 0) else None;

def isloginas(t):
	if type(t) != list:
		t = [t];
	return (islogin() and (_session["login"]["type"] in t));

def logout():
	global _session;
	_session["login"] = None;

def loginid():
	if(islogin()):
		return _session["login"]["id"];

def redirect(url):
	global _phpheader, _addinfo;
	_addinfo["redirect"] = True;
	_phpheader += "Location: " + url;

def getnewfilename(ext='mohit', extra=''):
	nname = _addinfo["ip"]+"_"+str(tnow())+"_"+str(loginid())+"_"+str(random.randint(1, 100000))+extra+"."+ext
	return "data/files/"+nname;

def getext(name):
	ext = name.split(".")[-1];
	return (ext if ext != name else 'mohit');

def resizeimg(name, nname, width, height):
	_toresize[name] =[nname, width, height];

def uploadimg(tmpname, name, size=None, extra=''):
	nname = getnewfilename(getext(name), extra);
	if(size == None):
		if( _server == "csc"):
			resizeimg(tmpname, nname, -1, -1);
		else:
			write_file(nname, read_file(tmpname));
			os.chmod(nname, 0777);
	else:
		resizeimg(tmpname, nname, size[0], size[1]);
	return nname;

def gtable(name, astable = True):
	return "("+_config["sql"][name]+")"+name if astable else _config["sql"][name];

def sqlhelp(name, args={}):
	return _config["sql_help"][name](**args);

def sqlr2table(r):
	if(len(r) == 0):
		return {"thead": [], "rows": []};
	else:
		thead = r[0].keys();
		rows = mappl(lambda x: x.values() ,r);
		return {"thead": thead, "rows": rows};

def mcurl(url):
	if(_agent == "poorvi" and _server == "gcl" ):
		return elc_virtual('curl -s "'+url+'" ');
	else:
		return curl(url);


def isuserexist(u, umatch = 'phone'):
	return _sql.sval("users", "*", {umatch: u} , 1);


def latlngdist(lat1, lng1, lat2, lng2) :
	degtorad = lambda x: x*(math.pi/180);
	R = 6371000; # metres
	ph1 = degtorad(lat1);
	ph2 = degtorad(lat2);
	dph = degtorad(lat2 - lat1);
	dlem = degtorad(lng2 - lng1);
	sin = math.sin;
	a = sin(dph/2) * sin(dph/2) + sin(ph1)*sin(ph2)*sin(dlem/2)*sin(dlem/2);
	c = 2*math.atan2(a**0.5, (1-a)**0.5);
	return R*c;

def forlist(a, typ):
	if(type(a) == int):
		return range(a);
	else:
		if(typ and type(a) == list):
			return range(len(a))
		else:
			return a;

def extentattrs(a):
	mifu(a, {"style": {}, "attr": {}, "data": {}, "datas": {}});
	fillfroma = lambda arr, impkey: mifa(arr, pkey1(a, impkey));
	fillfroma(a["style"], ["color", "font-size"]);
	fillfroma(a["attr"], ["style", "class", "id", "name", "href"]);
	mifa(a["data"], mapp(idf, a["datas"], None, lambda x: "send"+x));
	mifa(a["attr"], mapp(idf, a["data"], None, lambda x:"data-"+x));
	return a;

def overwriteattrs(a, b): #b is overwritting a
	for i in b:
		if(a.has_key(i) and (type(a[i]) == type(b[i]) == dict)):
			overwriteattrs(a[i], b[i]);
		else:
			a[i] = b[i];
	return a;

def execview(fn, ginp={}):
	sifu(ginp, "page", fn);
	if(0):
		return elc("python todisp.py "+quoted_s(json.dumps(ginp)));
	else:
		write_file("todispdata.json", json.dumps(ginp));
		return elc("python todisp.py");

class htmlnode():
	def __init__(self, tag=None, attrs={}, ptext=None):
		self.tag = tag;
		self.attrs = attrs;
		self.parent = None;
		self.content = [];
		self.ptext = ptext;

		self.fcalldata = {};# List of (method_name-> htmltree)

	def addchild(self, n):
		self.content.append(n);
		n.parent = self;

	def addfcdata(self, fname):
		self.fcalldata[fname] = htmltree();


	def tostr(self):
		if(self.tag == "script"):
			attr = self.attrs["attr"];
			if(isg(attr, "src") and (re.match(".*?reload$", attr["src"]) != None)):
				attr["src"] += ("="+str(tnow()));
		def tagattrs(a):
			a = a["attr"];
			a["style"] = rift("".join(mappl(lambda y,x: x+":"+str(y)+";", a["style"], lambda x: x!=None)), None, lambda x: x=='');
			return " ".join(mappl(lambda y,x: x+"='"+str(y)+"'", a, lambda x: x!=None));
		opentag = lambda : ("<"+self.tag+" "+ tagattrs(self.attrs) + " >") if self.tag != None else "";
		closetag = lambda : ("</"+self.tag+">") if self.tag != None and (self.tag not in _onewaytags) else "";
		if(self.ptext != None):
			return [self.ptext];
		elif (len(self.content) == 0):
			return [opentag()+closetag()]
		elif ( len(self.content) ==1 and self.content[0].ptext != None):
			return [opentag()+self.content[0].ptext+closetag()];
		else:
			return [opentag()]+mappl(lambda x: x.tostr(), self.content)+[closetag()];


class htmltree():
	def __init__(self):
		self.root = htmlnode();
		self.cur = self.root;

	def open(self, hnode):
		self.cur.addchild(hnode);
		if(hnode.tag != None and not(hnode.tag in _onewaytags)):
			self.cur = hnode;

	def close(self):
		self.cur = self.cur.parent;

	def addchilds(self, content):
		mappl(lambda x: self.cur.addchild(x), content);

	def addtext(self, ptext):
		self.open(htmlnode(ptext = str(ptext)));

def create_username(name, alreadyexists=[], maxlen = 25):
	keys = searchkeysplit(name);
	outp = "";
	for i in keys:
		if(len(outp)+len(i) > maxlen):
			break;
		else:
			outp+=(i+"-");
	outp = outp[:-1];
	outp_a = outp;
	count = 1;
	while(outp_a in alreadyexists):
		outp_a = outp+"-"+str(count);
		count+=1;
	return outp_a;

def geturlpath(inpurl):
	uup = urlparse.urlparse;
	return doifcan1(lambda: mappl(lambda x: cleanpath(str(x)), inpurl.split(uup(HOST).path, 1)[1].split("index.php")), (None, None));


def convchars(inp):
	return replaceall(inp, {"&": "&amp;", '"': "&quot;", "'": "&#039;", "<": "&lt;", ">": "&gt;"});


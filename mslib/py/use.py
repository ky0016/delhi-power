#!/usr/bin/env python
# -*- coding: utf-8 -*- 



_localtz = pytz.timezone("Asia/Calcutta") if ("pytz" in _includes) else None;



def fold_l(f, l, a):
	for i in l:
		a = f(a, i) if len(inspect.getargspec(f).args) == 2 else f(a, l[i], i);
	return a;

def timenow():
	return int(mktime(datetime.datetime.now(_localtz).timetuple()));

def time2format(formate, tat = None):#tat: TimeAt
	return datetime.datetime.fromtimestamp(rifn(tat, tnow())).strftime(formate);

def str2time(times, formate = None):
	formates = gen_form(['']+gen_form(['%d-%m-'], ['%y', '%Y']), [' '], ['', '%I:%M:%S %p', '%H:%M:%S', '%I:%M %p', '%H:%M' ])
	return (lambda x: x if type(x) == int else 0 )(fold( lambda x,y: rifn(doifcan(lambda x,y: int(time.mktime(datetime.datetime.strptime(x,y.strip()).timetuple())) , (x, y)), x), formates, re.sub('\s+', ' ', times).strip()));

def daystarttime(tat = None):
	return s2t(t2f_date(tat));

def grouplist(arr, gap=1):
	outp = [];
	for i in arr:
		if (outp == [] or (outp[-1][0] + outp[-1][1]*gap != i)):
			outp.append([i, 1]);
		else:
			outp[-1][1]+=1;
	return outp;

def replaceall(inp, ra):
	return fold(lambda s, ar, br: s.replace(br, ar), ra, inp);

def searchkeysplit(ss):
	return re.split("[^a-zA-Z0-9]+", ss.strip().lower());

def seto(a, b, o='|'):#Set operation, Warning: list order not preserved, a & b should be list of int or str
	return eval('list(set(a) '+o+' set(b) )');

def setol(a, b, o): #set operation on list, Ordered is preserved. a, b may not be set.
	if( o == '|' ): #Union
		return fold(lambda x, y: r1(appenduniq(x, y), x), b, unique(a));
	elif( o == '&' ): #Intersection
		return fold(lambda x,y: r1(appenduniq(x, y) if y in a else None, x), b, []);
	elif( o == '-' ): # a\b
		return fold(lambda x,y: r1(x.append(y) if y not in b else None, x) , a, []);
	else:
		return [];

def pkey(arr, keys):# partial keys
	return (mmap(lambda x, y: arr[x], seto(keys, gkeys(arr), '&'), True));

def pkey1(arr, keys): # partial keys: output is a cod, in same order as key is.
	return mapp(lambda x: arr[x], keys, lambda x: has_key(arr, x), lambda x: keys[x]);

def readfd(fd):
	data=fd.read();
	fd.close();
	return data;

def writefd(fd,data):
	fd.write(data);
	fd.close();

def read_file(fn):
	return readfd(open(fn));

def write_file(fn,data):
	writefd(open(fn,'w'),data);

def elc(c):
	return readfd(os.popen(c));

def elc_virtual(cmd):
	return elc("python client.py 10.208.20.186 '"+ cmd +"'");

def curl(url):
	return elc("curl -s '"+url+"'");

class mnum(int):#Same as int, except it thinks, -1 is infinite
	def __init__(self, ival):
		self.val = ival;
	def __str__(self):
		return str(self.val);
	def __add__(self, x):
		return mnum(-1) if self.val == -1 or mnum(x).val == -1 else mnum(self.val+x)

	def __sub__(self, x):
		return self+mnum(-x);

	def __cmp__(self, x):
		x=mnum(x);
		if(self.val == -1):
			return 1;
		elif(x.val == -1):
			return -1;
		elif(self.val == x.val):
			return 0;
		elif(self.val < x.val):
			return -1;
		else:
			return 1;

class countlimit(int):
	def __init__(self, ival):
		self.val = ival;
	def count(self):
		self.val -= 1;
		return (self.val > 0);



def appenduniq(l, x):
	return r1(l.append(x) if x not in l else None, l.index(x));

def unique(l):
	return fold(lambda x,y: r1(appenduniq(x, y), x), l, []);

def mixl(l):
	return fold(lambda x,y: x+y, l, []);

def mapp_rec(f, l, filt=None, keyf=None, depth = 0):
	if(depth <= 0):
		return mapp(f, l, filt, keyf);
	else:
		return list(mapp_rec(f, i, filt, keyf, depth-1) for i in l);

def allfile_rec(f):
	if(f[-1] != "/"):
		f+="/";
	allff = os.listdir(f);
	return list(f+i for i in allff if os.path.isfile(f+i))+fold(lambda x,y: x+y, list(allfile_rec(f+i) for i in allff if not(os.path.isfile(f+i)) ), [])

def readxlx(fn):
	wb = xlrd.open_workbook(fn);
	return list(list(list(s.cell(i,j) for j in xrange(s.ncols)) for i in xrange(s.nrows)) for s in wb.sheets());
	wb.close();

def catgxlx(data, depth = 0):
	return data if (depth <= 0) else mapp(lambda v: catgxlx(v, depth-1), fold(lambda x,y: r1(sifu(x, y[0], []), x[y[0]].append(y[1:]), x) , data, {}));

def catgxlx1(data, keyl, isuniq = False):
	listorrow = lambda x: x[0] if isuniq else x;
	return data if (len(keyl) == 0) else dict(mapp(lambda v: listorrow(catgxlx1(v, keyl[1:])), fold(lambda x,y: r1(sifu(x, y[keyl[0]], []), x[y[keyl[0]]].append( r1(y.pop(keyl[0]), y) ), x), data, {})));

def readxlx_val(fn):
	return list(list(list(str(x.value.encode('utf-8')) for x in y) for y in z) for z in readxlx(fn));

def readxlx1(fn, depth = 0):
	return catgxlx(readxlx_val(fn)[0][1:], depth);

def readxlx_db(xldata, title, grouping={}): #data: (list of (list of str)), title line removed, Assuming no element is grouped twice
	outp = mapp(lambda: [], cod.fromkeys(grouping.keys()));
	maint = [];
	if(len(xldata) == 0):
		return (maint, outp);
	else:
		rkeys = setol(range(len(xldata[0])), mixl(grouping.values()), '-');
		for row in xldata:
			nrow = pkey1(row, rkeys);
			for i in grouping:
				nrow[i+"_index"] = 1+appenduniq(outp[i], mifu(cod({i+"_id":None}), pkey1(row, grouping[i]) ));
			maint.append(nrow);
		for i in grouping:
			mappl(lambda x,y: sifu(x, i+"_id", y+1, True), outp[i]);
		return (maint, outp);

def readxlx_dbdump(fn, title, coltyp, maintable, grouping={}): #Assuming there is atleast 1 row, other then title.
	(maint, groupt) = readxlx_db(readxlx_val(fn)[0][1:], title, grouping);
	tableattrs = mappl(lambda x,y: x+" "+coltyp[y], title);
	sqlstatement = lambda table, row, isuniqi='': "create table if not exists "+ table+ "("+ ", ".join(mappl(lambda y,x: (tableattrs[x] if type(x) == int else (x+' int'+isuniqi)) , row))+")";
	groupt[maintable] = maint;

	print "Started Executing..";
	createquerys = mappl(lambda x,y: sqlstatement(y, x[0], ' unique' if y != maintable else '' ), groupt);
	groupt = mapp(lambda x, i: mappl(lambda j:mapp(idf, j, None, lambda x: (title[x] if type(x) == int else x)), groupt[i]), groupt);
	list(_sql.q(x) for x in createquerys);
	print "Created All";
	mappl(lambda x,y: mappl(lambda i: _sql.ival(y, dict(i)), x), groupt);


def google_addrtolanlat(addr):
	url ="https://maps.googleapis.com/maps/api/geocode/json?"+urllib.urlencode({"address": addr});
	req = s2j(curl(url));
	if(req):
		return req["results"][0]["geometry"]["location"];

def udicttostr(inp):
	if(type(inp) == unicode):
		return mystr(inp);
	elif(type(inp) == cod):
		return mapp(lambda x: udicttostr(x), inp, None, lambda x: mystr(x));
	elif(type(inp) == list):
		return map(udicttostr, inp);
	else:
		return inp;

def json_action(inp, f):
	if(type(inp) == cod):
		return f["cod"](inp);
	elif(type(inp) == list):
		return f["list"](inp);
	else:
		return f["default"](inp);


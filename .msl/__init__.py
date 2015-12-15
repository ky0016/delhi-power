
import urllib2, urllib, collections, inspect, json, os#, re, time, copy

if(not locals().has_key("exceptionf")):
	exceptionf = ".pyerrors";

cod = collections.OrderedDict;
cod.__str__ = lambda x: json.dumps(x);

fargs = lambda f: inspect.getargspec(f).args;


def fold_l(f, l, a):
	for i in gkeys(l):
		a = f(a, l[i]) if len(fargs(f)) == 2 else f(a, l[i], i);
	return a;

fold = fold_l;

def gkeys(a): #Assuming a is list or have .keys method
	return range(len(a)) if type(a) == list else a.keys();

def runf(f, args):
	numfargs = len(fargs(f))
	largs = list(args);
	sifu(largs, numfargs, None);
	return f(*tuple(largs[:numfargs]));

def idf(x):
	return x;

def mapp(f, l, filt=None, keyf=None):
	return cod((runf(rifn(keyf, idf), (i, l[i])), runf(f, (l[i], i))) for i in gkeys(l) if(runf( rifn(filt, lambda: True), (l[i], i))));

def mappl(f, l, filt=None, keyf=None):
	return mapp(f, l, filt, keyf).values();

def doifcan(fun, inp=(), defaultval = None): #run fun on inp if possible.
	try:
		return fun(*inp) if type(inp) == tuple else fun(inp);
	except:
		return defaultval;

def doifcan1(fun, defaultval=None):
	return doifcan(fun, (), defaultval);

def getitem(arr, key, defaultval = None): #arr can be list or dict | output = arr[key]
	return doifcan(lambda :arr[key], defaultval=defaultval);

g = getitem; #

def has_key(arr, key): #Check is key set in arr ? ( arr: List | Dict  )
	return doifcan(lambda l,i: r1(l[i], True), (arr, key), False);

isg = has_key;


def str2json(inp, errorval = None): #dl = []
	return doifcan(lambda x: udicttostr(json.loads(x, object_pairs_hook=cod)), inp, errorval);

s2j = str2json;

def gl(arr, keys, errorval = None): #apply list of keys ex: gl(arr, ["x", 1, "y"]) = arr["x"][1]["y"]
	return fold(lambda x,y: g(x, y, errorval), keys, arr);

def rift(var, val, checker):
	return val if checker(var) else var;

def rifn(var, val):
	return rift(var, val, lambda var: var == None);

def sifu(arr, key, val, isforce = False):
	if (not isg(arr, key)) or isforce:
		if type(arr) == list and key > len(arr)-1:
			return fold(lambda x, y: r1(x.append(None if len(x)!=key else val), x), range(key-len(arr)+1), arr);
		else:
			arr[key] = val;
	return arr;

def seta(arr, key, val):#Set Array Keys Forcefully
	return sifu(arr, key, val, True);

def r1(*args):
	return args[-1];

def r2(*args):
	return args[-2];

def mifu(a1, a2, isforce = False):# Merge If Unset
	return fold(lambda x1, yval, y1: sifu(x1, y1, yval, isforce), a2, a1);

def mifa(a1, a2): #Merge Forcefully
	return mifu(a1, a2, True);

def rmifu(a1, a2, isforce=False):
	return mifu(cod(a1), a2, isforce);


def msplit(st, spliter = '-'):
	return rift(st.split(spliter), [], lambda x: x==[""]);

def mjoin(glu, l, defaultval=''):
	return glu.join(list(str(x) for x in l)) if len(l) > 0 else defaultval;

def isallone(l):
	return sum(l) == len(list(l));

def isanyone(l):
	return sum(l) >= 1;

def intf(x, defaultval = 0):
	return doifcan1(lambda :int(x), defaultval);

def ife(a,b,c=None):
	return (b if a else c);

def mystr(s):
	return unicode(s).encode('ascii', 'ignore')

def udicttostr(inp):
	if(type(inp) == unicode):
		return mystr(inp);
	elif(type(inp) == cod):
		return mapp(lambda x: udicttostr(x), inp, None, lambda x: mystr(x));
	elif(type(inp) == list):
		return map(udicttostr, inp);
	else:
		return inp;

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

def write_file(fn, data, mode='w'):
	writefd(open(fn, mode),data);

def errorlog(e):
	global exceptionf;
	write_file(exceptionf, str(e)+"\n", 'a');


def elc(c):
	return readfd(os.popen(c));

def replaceall(inp, ra):
	return fold(lambda s, ar, br: s.replace(br, ar), ra, inp);


def setol(a, b, o): #set operation on list, Ordered is preserved. a, b may not be set.
	if( o == '|' ): #Union
		return fold(lambda x, y: appenduniq1(x, y), b, unique(a)); #unique(a) won't go in infite loop.
	elif( o == '&' ): #Intersection
		return fold(lambda x,y: appenduniq1(x, y, y in a), b, []);
	elif( o == '-' ): # a\b
		return fold(lambda x,y: appenduniq1(x, y, y not in b), a, []);
	else:
		return [];

def inlist(l, e, f=None, notfound_index=-1):
	if(f==None):
		f=lambda x,y: x==y;
	return fold(lambda y,x,i: (i if (y==-1 and f(x,e)) else y), l, notfound_index);

def appenduniq(l, x, f=None):
	return r1(l.append(x) if (inlist(l, x, f) == -1) else None, l.index(x));

def appenduniq1(l, x, areyousure=True):
	return r1(appenduniq(l, x) if areyousure else None, l);

def append(l, x):
	return r1(l.append(x), l);

def remove(l, x):
	return r1(doifcan1(lambda:l.remove(x)), l);

def unique(l):
	setol([], l, '|') if l!=[] else [];

def curl(url, postdata='', proxy='', getdata=''):
	postdata = urllib.urlencode(postdata) if type(postdata) != str else postdata;
	if(1):
		return elc(proxy+" curl -s "+(("-d '"+postdata+"'") if postdata !="" else "") +" '"+url+"'");
		lc = proxy+" wget --no-check-certificate  "+ (("--post-data=\""+postdata+"\" ") if postdata != '' else '') +" "+url+" -O- -o /tmp/null1"
		return elc(lc);
	else:
		encodeifneed = lambda x: urllib.urlencode(x) if type(x) != str else x;
		postdata = encodeifneed(postdata);
		getdata = encodeifneed(getdata);
		if(getdata != ''):
			if("?" in url):
				url = ife(url[-1] == "&", url, url+"&");
			else:
				url = url+"?";
			url += getdata
		try:
			if(0):
				proxy = {'http': 'http://proxy22.iitd.ac.in:3128', 'https': 'http://proxy22.iitd.ac.in:3128'}
			return urllib2.urlopen( urllib2.Request(url, postdata), proxies = proxy ).read()
		except Exception as e :
			errorlog(e);
			return "";


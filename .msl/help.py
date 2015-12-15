import itertools, socket,re;

from msl import *
try:
	import xlrd;
except:
	pass


def gen_form(*args):
	return map(lambda x: ''.join(list(str(i) for i in x)), itertools.product(*args));


def getmyip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("www.iitd.ac.in",80))
	myip=s.getsockname()[0];
	s.close()
	return myip;

def my_send(s, msg):
	return s.send(("%010d" % (len(msg),))+msg);

def my_recv(s):
	num_to_recv = doifcan1(lambda: int(s.recv(10)), 0)
	need_to_recv = num_to_recv;
	datasofar = "";
	while(need_to_recv > 0):
		recved = s.recv(need_to_recv);
		need_to_recv-=len(recved);
		datasofar+=recved;
	return datasofar;

def mixl(l):
	return fold(lambda x,y: x+y, l, []);


def quoted_s1(x):
	return replaceall(x, cod([('\\', '\\\\'), ('\t', "\\t"), ('\n', "\\n"), ('"', '\\\"')]));

def quoted_s(x):
	return '"'+quoted_s1(x)+'"';

def myadd(x,y):
	return doifcan1(lambda: x+y, str(x)+str(y));

def printoutp(xl, tabseprate='\t', depth = -1):
	if type(xl) == list :
		return mixl(map(lambda x: printoutp(x, tabseprate, depth+1), xl));
	elif(xl != '') :
		return [tabseprate*depth+xl];
	else:
		return [];

def oslistdir(f, shouldvis=False):
	return filter(lambda x: (not(shouldvis) or g(x,0) != '.'), os.listdir(f));

def allfile_rec(f, shouldvis = False):
	if(f[-1] != "/"):
		f+="/";
	allff = oslistdir(f, shouldvis);
	return list(f+i for i in allff if os.path.isfile(f+i))+fold(lambda x,y: x+y, list(allfile_rec(f+i, shouldvis) for i in allff if not(os.path.isfile(f+i)) ), [])

def alldir(f):
	if(f[-1] != "/"):
		f+="/";
	return list(i for i in os.listdir(f) if not(os.path.isfile(f+i)));

def readxlx(fn, mincol=None):
	wb = xlrd.open_workbook(fn);
	return list(list(list(s.cell(i,j) for j in xrange(s.ncols)) for i in xrange(s.nrows)) for s in wb.sheets());

def google_addrtolanlat(addr):
	url ="https://maps.googleapis.com/maps/api/geocode/json?"+urllib.urlencode({"address": addr});
	req = s2j(curl(url));
	if(req):
		country_code = filter(lambda x: x["types"][0]=="country", req["results"][0]["address_components"])[0]["short_name"];
		return sifu(req["results"][0]["geometry"]["location"], "countrycode", country_code);


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
	return re.sub("[^a-zA-Z0-9]+", " ", ss.lower()).strip().split();
#	return re.split("[^a-zA-Z0-9]+", ss.strip().lower());

def cleanpath(p, typ='se'):
	if('s' in typ and len(p)>0 and p[0]=='/'):
		p=p[1:];
	if('e' in typ and len(p)>0 and p[-1]=='/'):
		p=p[:-1];
	return p;



import os,copy,sys,inspect,collections

class mtmlparser:
	def elc(self, c):
		f = os.popen(c);
		data = filter(lambda x: (x!="\n" and x!="\r") , f.read())
		f.close();
		return data;

	def parsebyocaml(self, f):
		cmd = self.parser+" "+f+" 2> /dev/null"
		a = self.elc(cmd if _server != "gcl" else "python client.py 10.208.20.186 '"+ cmd +"'" );
		return eval("["+a+"]");

	def parsedefn(self):
		path = _mslib+"alldef/";
		alldefn = path+".alldefn";
		modftime = lambda x: self.elc("stat -c %x "+x).split(".")[0];
		if(not( modftime(path) == modftime(alldefn) ) or True):
			write_file(alldefn, "".join(read_file(i)+"\n\n" for i in allfile_rec(path) if i not in [alldefn] ));
		self.datadef = self.parsebyocaml(alldefn);

	def __init__(self):
		self.parser = _mslib+"ocaml/calc";
		self.tabseprate = "  ";
		self.newlj = lambda x: "\n".join(list(str(i) for i in x if i!=""))
		self.compiled = "templates/.compiled/";
		self.compileddefn = self.compiled+"defines";

	def readcompiled(self, name):
		self.data = eval(read_file(self.compileddefn))+eval(read_file(self.compiled+name));

	def readinp(self, fname):
		self.parsedefn();
		self.data = self.datadef + self.parsebyocaml(fname);

	def readonefile(self, fname):
		self.data = self.parsebyocaml(fname);

	def expend(self, t, gamma, funcs, depth = 0):
		expend = self.expend;
		def fold(f, l, a):
			for i in l:
				a = f(a, i) if len(inspect.getargspec(f).args) == 2 else f(a, l[i], i);
			return a;

		def joinarr(a, b):
			for i in b:
				a[i] = b[i];
			return a;

		def mergeifunset(a, b, isforce = False, checknone = False): #Warning: a is overwritten
			for i in b:
				if ((not a.has_key(i)) or isforce) and (not(checknone and b[i] == None)) :
					a[i] = b[i];
			return a;

		def geta(key, arr): #for dict array only.
			if(arr.has_key(key)):
				return arr[key];
			else:
				return None;

		def overwrite(a, b): #overwrite array a , forced by b
			for i in b:
				if(a.has_key(i) and type(a[i]) == dict and type(b[i]) == dict ):
					overwrite(a[i], b[i]);
				else:
					a[i] = b[i];
			return a;

		cod = lambda: collections.OrderedDict();
		def ouradd(x,y):
			try:
				return x+y;
			except:
				return str(x)+str(y);
		if(t[0] == "None"):
			return None;
		elif(t[0] == "Assign"):
			if(t[1][0] == "V"):
				gamma[ t[1][1] ] = expend( t[2], gamma, funcs );
			elif(t[1][0] == "Get"):
				expend(t[1][1], gamma, funcs)[ expend(t[1][2], gamma, funcs) ] = expend( t[2], gamma, funcs );
			return ("", gamma, funcs);
		elif(t[0] == "V" ):
			return geta(t[1], gamma);
		elif(t[0] in ["N", "S"] ):
			return t[1];
		elif(t[0] == "Not" ):
			return int(not(expend(t[1], gamma, funcs)));
		elif(t[0] == "Attr" ):
			a = expend(t[1], gamma, funcs);
			if(t[2] == 'len'):
				return len(a);
			elif(t[2] == 'keys'):
				return a.keys();
			elif(t[2] == 'gchars'):
				return convchars(a);
			else:
				return a;
		elif(t[0] == "Ife"):
			if(expend(t[1], gamma, funcs)):
				return expend(t[2], gamma, funcs);
			else:
				return expend(t[3], gamma, funcs);
		elif(t[0] in ["Add", "Mul", "Sub", "Div", "Mod", "Or", "And", "Get", "Isequal", "Le", "Ge", "Ls", "Gt", "Notequal"] ):
			a1,a2 = expend(t[1], gamma, funcs), expend(t[2], gamma, funcs)
			if(t[0] == "Add"):
				return ouradd(a1, a2);
			elif(t[0] == "Mul"):
				return a1*a2;
			elif(t[0] == "Sub"):
				return a1-a2;
			elif(t[0] == "Div"):
				return a1/a2;
			elif(t[0] == "Mod"):
				return a1%a2;
			elif(t[0] == "And"):
				return int(a1 and a2);
			elif(t[0] == "Or"):
				return int(a1 or a2);
			elif(t[0] == "Get"):
				return g(a1, a2);
			elif(t[0] == "Isequal"):
				return int(a1 == a2);
			elif(t[0]=="Le"):
				return int(a1<=a2);
			elif(t[0]=="Ge"):
				return int(a1>=a2);
			elif(t[0]=="Ls"):
				return int(a1<a2);
			elif(t[0]=="Gt"):
				return int(a1>a2);
			elif(t[0]=="Notequal"):
				return int(a1!=a2);
			else:
				return "";
		elif(t[0] == "Dictle"):
				return {(t[1][1] if t[1][0] == "V" else expend(t[1], gamma, funcs)): expend(t[2], gamma, funcs) };
		elif(t[0] == "Dictl"):
			return fold(lambda x,y: joinarr(x, expend(y, gamma, funcs) ), t[1:], {});
		elif(t[0] == "Listl"):
			return map(lambda x: expend(x, gamma, funcs), t[1:]);
		elif(t[0] == "Listi"):
			outp = [];
			for i in t[1:]:
				(outp1, gamma1, funcs1) = expend(i, gamma, funcs, depth);
				outp.append(outp1);
				gamma = gamma1;
				funcs = funcs1;
			return (outp, gamma, funcs);
		elif(t[0] == "Ifel"):
			for i in t[1:]:
				if(expend(i[1], gamma, funcs)):
					return (self.newlj(expend(i[2], gamma, funcs)[0]), gamma, funcs);
			return ("", gamma, funcs);
		elif(t[0] == "Forl"):
			lt = expend(t[3], gamma, funcs);
			lta = ( range(lt) if type(lt) == int else lt)
			outp = [];
			for i in xrange(len(lta)):
				gamma1 = copy.deepcopy(gamma);
				gamma1[t[1][1]] = lta[i];
				if(t[2][1] != ""):
					gamma1[ t[2][1] ] = i;
				(outp1, gamma2, funcs2) = expend(t[4], gamma1, funcs, depth);
				outp.append(self.newlj(outp1));
			return (self.newlj(outp), gamma, funcs);
		elif(t[0] == "Defn" ):
			funcs[ t[1][1] ] = t;
			return ("", gamma, funcs);
		elif(t[0] == "Tag" ):
			tagname = t[1][1];
			pretext = self.tabseprate*depth;
			if(tagname == "p"):
				return (pretext+str(expend(t[2], gamma, funcs)), gamma, funcs);
			elif(tagname == "innerHTML" and  gamma.has_key("innerHTML")):
				return (self.newlj( gamma["innerHTML"] ), gamma, funcs);
			else:
				onewaytags = ["input", "link", "img", "base"];
				inattr = expend(t[2], gamma, funcs);
				mergeifunset(inattr, {"attr": {}, "style": {}, "data": {}, "datas":{}});
				mergeifunset(inattr["attr"], {"class": geta("class", inattr), "id": geta("id", inattr), "name": geta("name", inattr) }, True, True);
				mergeifunset(inattr["style"], {"color": geta("color", inattr)}, True, True);
				inattr["attr"]["style"] = inattr["style"];

				mifu(inattr["attr"], dict(("data-"+i, inattr["data"][i]) for i in inattr["data"]));
				mifu(inattr["attr"], dict(("data-send"+i, inattr["datas"][i]) for i in inattr["datas"]));

				innerHTML = expend(t[3], gamma, funcs, depth+1)[0];
				if(funcs.has_key(tagname)):
					t1 = funcs[tagname];
					gamma1 = copy.deepcopy(gamma);
					mifu(gamma1, overwrite( expend(t1[2], gamma, funcs), inattr), True);
					gamma1["innerHTML"] = innerHTML;
					return (self.newlj(expend(t1[3], gamma1, funcs, depth)[0]), gamma, funcs);
				else:
					styles = inattr["attr"]["style"];
					attrs = inattr["attr"];
					linstyle = ";".join("{0}:{1}".format(x, styles[x]) for x in styles if styles[x]!=None);
					linattr = "".join( list(" {0}='{1}' ".format(x, attrs[x]) for x in  attrs if (x!="style" and attrs[x]!=None )) + ([" style='"+linstyle+"' "] if linstyle!='' else []) )
					fp1 = [pretext+"<"+tagname+linattr+">"];
					fp2 = ([pretext+"</"+tagname+">"] if (tagname not in onewaytags) else [] );
					return (self.newlj(fp1+innerHTML+fp2 ), gamma, funcs);
		else:
			return "";
	def disp(self, gamma = {}):
		if(gamma == None):
			gamma = {};
		return self.newlj(self.expend( tuple(['Listi']+self.data), gamma, {})[0]);



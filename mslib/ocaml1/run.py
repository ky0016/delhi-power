
class mtmlparser:
	def config(self):
		self.parser = _mslib+"ocaml/calc";
		self.tabseprate = "  ";
		self.newlj = lambda x: "\n".join(list(str(i) for i in x if i!=""))
		self.compiled = "templates/.compiled/";
		self.compileddefn = self.compiled+"defines";
		self.defname = lambda x: "newtag_"+x;

	def runtimevar(self):
		self.returnvardef = "outpvar";
		self.returnvar = self.returnvardef;
		self.ginp = "ginp";
		self.linp = "inp";
		self.scopefun = False;

		self.directvar = [];

	def __init__(self):
		self.config();
		self.runtimevar();

	def varname(self, x):
		if(x in self.directvar):
			return x;
		else:
			return (self.linp if self.scopefun else self.ginp)+"["+quoted_s(x)+"]";


	def expend(self, t):
		expend = self.expend;
		if(t[0] == "None"):
			return t[0];
		elif(t[0] == "Assign"):
			if(t[1][0] == "V"):
				if(not(self.scopefun)):
					self.directvar.append(t[1][1]);
				return ([ expend(t[1]) + " = " + expend(t[2])+";"]);
			elif(t[1][0] == "Get"):
				return ([expend(t[1])+" = " + expend(t[2])+";"])
			return ([""]);
		elif(t[0] == "V"):
			return self.varname(t[1]);
		elif(t[0] in ["S"]):
			return quoted_s(t[1]);
		elif(t[0] ==  "N"):
			return str(t[1]);
		elif(t[0] == "Not"):
			return "not("+expend(t[1])+")"
		elif(t[0] == "Attr"):
			eexpr = expend(t[1]);
			if(t[2] == "len"):
				return "len("+eexpr+")";
			elif(t[2] == 'gchars'):
				return "convchars("+eexpr+")";
			else:
				return eexpr+"."+t[2]+"()";
		elif(t[0] == "Ife"):
			return "("+ expend(t[2]) +" if (" +expend(t[1]) + ") else "+ expend(t[3])+")";
		elif(t[0] in  ["Get", "Add"]):
			a1,a2 = expend(t[1]), expend(t[2])
			if(t[0] == "Get"):
				return a1+"["+a2+"]";
			elif(t[0] == "Add"):
				return "myadd("+a1+", "+a2+")";
		elif(t[0] in ["Mul", "Sub", "Div", "Mod", "Or", "And", "Isequal", "Le", "Ge", "Ls", "Gt", "Notequal"]):
			a1,a2 = expend(t[1]), expend(t[2])
			expr = "("+a1+" "+{"Add": "+", "Mul": "*", "Sub": "-", "Div": "/", "Mod": "%", "Or": "or", "And": "and", "Isequal": "==", "Le": "<=", "Ge": ">=", "Ls": "<", "Gt": ">", "Notequal": "!="}[t[0]]+" "+a2+")";
			if(t[0] in ["Or", "And", "Isequal", "Le", "Ge", "Ls", "Gt", "Notequal"]):
				return "int("+expr+")";
			else:
				return expr;
		elif(t[0] == "Dictle"):
				return "("+(quoted_s(t[1][1]) if t[1][0] == "V" else expend(t[1]) ) +", "+ expend(t[2])+")";
		elif(t[0] == "Dictl"):
			return "cod(["+(", ".join(map(lambda x: expend(x), t[1:][::-1])))+"])"
		elif(t[0] == "Listl"):
			return "["+(", ".join(map(lambda x: expend(x), t[1:])))+"]"
		elif(t[0] == "Listi"):
			outp = [];
			for i in t[1:]:
				(outp1) = expend(i);
				outp+=outp1;
			return (outp);
		elif(t[0] == "Ifel"):
			outp = [];
			for j in range(len(t[1:])):
				i = t[1:][j];
				outp.append(("elif" if j!=0 else "if")+" ("+expend(i[1])+"): " );
				ifcontent = expend(i[2])
				if(len(ifcontent) == 0):
					ifcontent.append("pass");
				outp.append( ifcontent );
			return (outp);
		elif(t[0] == "Forl"):
			lt = expend(t[3]);
			index_var = t[2][1];
			value_var = t[1][1];
			lta = "forlist("+lt+", "+str(index_var != "")+" )";

			outp = ["for "+(index_var if index_var != "" else value_var)+" in " + lta + " :"];
			self.directvar+=[value_var, index_var];
			outp.append([""+value_var+" = "+lt+"["+index_var+"];" if (index_var != "") else "" ]+ rift(expend(t[4]), ["pass"], lambda x: len(x) == 0)) ;
			remove(remove(self.directvar, value_var), index_var);
			return (outp);
		elif(t[0] == "Defn"):
			fname = t[1][1];
			self.scopefun = True;
			innerHTML = expend(t[3]);
			self.scopefun = False;
			return (["def "+self.defname(fname)+"("+self.linp+", "+self.ginp+", innerHTML): "]+[[self.linp+" = overwriteattrs(extentattrs("+expend(t[2])+"), extentattrs("+self.linp+"));"]+["mifu("+self.linp+", "+self.ginp+");"]+[self.returnvar+" = htmltree();"], innerHTML, ["return "+self.returnvar+";"]]+[self.tabseprate]);
		elif(t[0] == "Tag"):
			tname = t[1][1];
			if(tname == "print"):
				return ([ self.returnvar+ ".addtext("+expend(t[2])+");"]);
			elif(tname == "innerHTML"):
				return [self.returnvar+".addchilds(innerHTML);"]
			else:
				inattr = expend(t[2]);
				if(tname not in self.alltags):
					oldrvar = self.returnvar;
					self.returnvar = self.returnvar+".cur.fcalldata["+quoted_s(tname)+"]"
					innerHTML = expend(t[3]);
					self.returnvar = oldrvar;
					return [self.returnvar+".cur.addfcdata("+quoted_s(tname)+");"]+innerHTML+[self.returnvar+".addchilds("+self.defname(tname)+"("+inattr+", "+self.ginp+", "+self.returnvar+".cur.fcalldata["+quoted_s(tname)+"].root.content).root.content);"];
				else:
					innerHTML = expend(t[3]);
					return [self.returnvar+".open(htmlnode("+quoted_s(tname)+", extentattrs("+inattr+")));"]+innerHTML+([self.returnvar+".close();"] if (tname not in _onewaytags) else [])
		else:
			return "";
	def disp(self, data):
		self.alltags = _config["alltags"];
		outp = self.expend(tuple(['Listi'] + data))
		return self.newlj(["#This code is auto generated code, don't Edit it "]+printoutp(outp, self.tabseprate, -1));


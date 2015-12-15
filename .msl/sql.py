from msl import *
from msl.mtime import *;
from msl.help import *;

import re, socket

try:
	import MySQLdb;
except:
	pass

class sqllib:
	# Notes:
	# 	i_* : internal local methods.
	db = None;
	cur = None;
	uniqc = {};
	s = None; #MyQueryServer's socket
	need_to_call_cur = True;
	def __init__(self, isvirtual, db_data):
		self.isreal = not(isvirtual);
		self.db_data = db_data;

	def tabtype(self, inpl):
		def interp(x):
			if(doifcan(lambda x: r1(int(x), True), "0"+x[2:], False)):
				outp="";
				if(g(x, 0) == 'i'):
					outp += "int";
				elif(g(x, 0) == 'r'):
					outp += "real";
				elif(g(x, 0) == 'v'):
					outp += 'varchar({0})'.format(int("0"+re.sub("[^0-9]", "", x)));
				if(g(x, 1) == 'u'):
					outp+=" unique";
				return outp;
			else:
				return x;
		return list(interp(x.strip()) for x in inpl.split(","));

	def init_qs(self):
		db_data = self.db_data;
		if(self.s == None):
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
			self.s.connect((db_data["qs_host"], db_data["qs_port"]));

	def close_qs(self):
		if(self.s != None):
			my_send(self.s, json.dumps({"isclose": True}));
			self.s.close();

	def query(self, cmd, inp=None):
		self.init_qs();
		my_send(self.s, json.dumps({"action": cmd, "inp": inp}));
		whatigot = my_recv(self.s)
		try:
			return s2j(whatigot)["data"];
		except:
			print "Error:", whatigot;

	def init_db(self):
		db_data = self.db_data;
		if(self.db == None and self.cur == None):
			self.db = MySQLdb.connect(host=db_data["host"], user=db_data["user"], passwd=db_data["pass"], db=db_data["db"]);
			self.cur = self.db.cursor(MySQLdb.cursors.DictCursor);

	def close_db(self):
		self.close_qs();
		map(lambda x:x.close() if x!=None else None, [self.cur, self.db]);

	def rquery(self, query, dkeys={}, keys={}):
		return query.format(**mifu(keys, mapp(lambda x,y: "%("+y+")s", dkeys), True));

	def q(self, query, darr={}, arr={}):
		if(not self.isreal):
			return self.query("sql", [query, darr, arr, 'q']);
		self.init_db();
		if(self.need_to_call_cur):
			self.cur = self.db.cursor(MySQLdb.cursors.DictCursor);
		self.cur.execute(self.rquery(query, darr, arr), dict(darr))
		self.db.commit();
		return (self.cur.lastrowid)
		# return (self.cur.lastrowid + self.cur.rowcount)

	def g(self, query, darr={}, arr={}):
		if(not self.isreal): #Warning: It may go to infinite loop. Make sure vertual query handler don't enter in this 'if' block
			return self.query("sql", [query, darr, arr, 'g']);
		self.init_db();
		if(self.need_to_call_cur):
			self.cur = self.db.cursor(MySQLdb.cursors.DictCursor);
		self.cur.execute(self.rquery(query, darr, arr), dict(darr));
		s_feilds = mappl(lambda x: x[0], list(self.cur.description));
		return mappl(lambda x: pkey1(mapp(lambda y: intf(y, str(y)), x), s_feilds), list(self.cur));

	def g1(self, query, darr={}, arr={}):
		return self.i_1row(self.g(query, darr, arr), 1);

	def i_conds(self, arr, glu = ' AND '):
		if(type(arr) == dict or type(arr) == cod ):
			(a,b) = fold(lambda (clist, darr),val,key: r1(clist.append(key+" = {"+key+"}"), (clist, seta(darr, key, val))) , arr, ([],{}));
			return (mjoin(glu, a, "true"), b);
		else:
			return (arr, {});

	def i_1row(self, x, limit):
		return (g(x, 0) if limit == 1 else x);

	def i_limits(self, limit):
		return '' if limit == -1 else 'limit '+str(limit);

	def sval(self, table, flds = '*', conds={}, limit = -1):
		(s_conds, darr) = self.i_conds(conds);
		query = "select {1} from {0} where {2} {3}".format(table, flds, s_conds, self.i_limits(limit) );
		return self.i_1row(self.g(query, darr), limit);

	def uval(self, table, toset, conds={}, limit = -1):
		[(s_conds, darr), (s_set, darr1)] = map(lambda x:self.i_conds(*x), [(conds, ' AND '), (toset, ',')]);
		return self.i_1row(self.q("update {table} set {s_set} where {s_conds} {limit_s}".format( **rmifu(locals(),{"limit_s": self.i_limits(limit)})), mifu(darr, darr1)), limit);

	def dval(self, table, conds={}, limit = -1):
		(s_conds, darr) = self.i_conds(conds);
		return self.i_1row(self.q("delete from {table} where {s_conds} {limit_s}".format( **rmifu(locals(), {"limit_s": self.i_limits(limit)}) ), darr), limit);

	def ival(self, table, toins={}):
		if(has_key(self.uniqc, table)):
			ucols = self.uniqc[table];
			exisrow = self.sval(table, '*', dict(pkey1(toins, ucols)), 1);
			if(exisrow):
				return exisrow;
		return self.q("insert into {0} ({1}) values ({2})".format( *([table]+map(lambda l:','.join(l), (lambda l:[l, list("{"+x+"}" for x in l)])(toins.keys())) )), toins);

	def autoscroll(self, query, darr={}, key = None, sort='', isloadold = True, minl = None, maxl = None, arr={}):
		return;
		(minl, maxl) = tuple(mmap(lambda x, y: rifu(x, [minl, maxl][y])  ,list(pkeys(arr, ["minl", "maxl"]))))



##################This is DustBin below this###############################


	# def rquery(self, query, dkeys={}, keys={}):
	# 	return query.format(**mifu(keys, mapp(lambda x,y: "%("+y+")s", dkeys), True));
	# 	#return fold(lambda q,tr: q.replace("{"+tr+"}", "%("+tr+")s" if isg(dkeys, tr) else g(keys, tr, '{'+tr+"}")), (x[1:-1] for x in re.compile("{[^}]+}").findall(query)), query);


	# def tabtype1(self, inpl):
	# 	def interp(x):
	# 		if(x[0] == "_"):
	# 			return x[1:];
	# 		else:
	# 			#intinx = int("0"+re.sub("[^0-9]", "", x));
	# 			#[{'i': 'int', 'v': 'varchar({0})'.format(intinx), 'r': 'real'}, {'u': 'unique','n': 'not null', 'a': "AUTO_INCREMENT"}]
		# 	if(doifcan(lambda x: r1(int(x), True), "0"+x[2:], False)):
		# 		outp="";
		# 		if(g(x, 0) == 'i'):
		# 			outp += "int";
		# 		elif(g(x, 0) == 'r'):
		# 			outp += "real";
		# 		elif(g(x, 0) == 'v'):
		# 			outp += 'varchar({0})'.format());
		# 		if(g(x, 1) == 'u'):
		# 			outp+=" unique";
		# 		return outp;
		# 	else:
		# 		return x;
		# return list(interp(x.strip()) for x in inpl.split(","));


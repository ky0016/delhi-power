execfile("parse.py");


def parsejson(parsedfile):
	rules = [
		['dicte', ('name', '*'), ':', ('jsonval', '*') , lambda x, y: {x[0][1]: x[2][1]}],
		['jsonval', ('number', '*') , lambda x, y: int(x[0][1])],
		['jsonval', ('name', '*') , lambda x, y: g(y, x[0][1]) ],
		['jsonval', ('string', '*') , lambda x, y: x[0][1][1:-1] ],
		['dictel', ('dicte', '*') , lambda x,y: x[0][1]],
		['dictel', ('dictel', '*'), ',', ('dictel', '*') , lambda x,y: mifu(x[0][1], x[2][1])],
		['jsonvall', ('jsonval', '*'), ',', ('jsonvall', '*') , lambda x,y: [x[0][1]]+x[2][1]],
		['jsonvall', ('jsonval', '*'), ',', ('jsonval', '*') , lambda x,y: [x[0][1], x[2][1]] ],
		['jsonval', '[', ('jsonvall', '*'), ']' , lambda x,y: x[1][1]],
		['jsonval', '[', ('jsonval', '*'), ']' , lambda x,y: [x[1][1]]],
		['jsonval', '[', ']' , lambda x, y: []],
		['jsonval', '{', '}' , lambda x, y: {}],
		['jsonval', '{', ('dictel', '*'), '}', lambda x,y: x[1][1]],
	];
	varlist = {"Saini": 124};#values to be given to variables.
	return leftparse(parsedfile, rules, varlist)[0][1];

def parsehtml(parsedfile):
	rules = [
		['tag_f', ('name', '*'), '(', ('dictel', '*'), ')', lambda x,y: (x[0][1], x[2][1])],
		['tag_f', ('name', '*'), '(', ('jsonval', '*'), ')', lambda x,y: (x[0][1], x[2][1])],
		['tag_f', ('name', '*'), '(', ('jsonvall', '*'), ')', lambda x,y: (x[0][1], x[2][1])],
		['tag_f', ('name', '*'), '(', ')', lambda x,y: (x[0][1], {})],
		['tag', ('tag_f', '*'), ';', lambda x,y: (x[0][1][0], x[0][1][1],[]) ],

		['tagbox', '{', ('tagl', '*'), '}', lambda x,y: x[1][1]],
		['tagbox', '{', ('tagl', '*'), '}', ';', lambda x,y: x[1][1]],

		['tag', ('tag_f', '*'), '{', '}', lambda x,y: (x[0][1][0], x[0][1][1], [])],
		['tag', ('tag_f', '*'), ('tagbox', '*'), lambda x,y: (x[0][1][0], x[0][1][1], x[1][1])],
		['tag', ('tag_f', '*'), ('tagbox', '*'), ';', lambda x,y: (x[0][1][0], x[0][1][1], x[1][1])],

		# ['tagl', ('tag', '*'), ('tag', '*'), lambda x,y: [x[0][1], x[1][1]]],
		# ['tagl', ('tag', '*'), ('tagl', '*'), lambda x,y: [x[0][1]] + x[1][1] ],

		['tagl', ('tag', '*'), lambda x,y: [x[0][1]]],
		['tagl', ('tagl', '*'), ('tagl', '*'), lambda x,y: x[0][1] + x[1][1]],


		['vardeeplist', ('jsonval', '*'), ('jsonval', '*'), lambda x, y: x[0][1]+x[1][1] ],
		['vardeeplist', ('jsonval', '*'), ('vardeeplist', '*'), lambda x, y: x[0][1]+x[1][1] ],
		['jsonval', ('name', '*'), ('vardeeplist', '*'), lambda x, y: [{'val': x[0][1], 'type': 'var'}]+x[1][1] ],
		['jsonval', ('name', '*'), ('jsonval', '*'), lambda x, y: [{'val': x[0][1], 'type': 'var'}]+x[1][1] ],

		['dicte', ('name', '*'), ':', ('jsonval', '*') , lambda x, y: {x[0][1]: x[2][1]}],
		['jsonval', ('number', '*') , lambda x, y: int(x[0][1])],
		['jsonval', ('name', '*') , lambda x, y: {'val': x[0][1], 'type': 'var'} ],
		['jsonval', 'True' , lambda x, y: True ],
		['jsonval', 'False', lambda x, y: False],

		['jsonval', ('jsonval', '*'), '==', ('jsonval', '*'), lambda x, y: {'type': 'eq', 'val': (x[0][1], x[2][1])} ],
		['jsonval', ('jsonval', '*'), '<=', ('jsonval', '*'), lambda x, y: {'type': 'lseq', 'val': (x[0][1], x[2][1])} ],
		['jsonval', ('jsonval', '*'), '>=', ('jsonval', '*'), lambda x, y: {'type': 'gteq', 'val': (x[0][1], x[2][1])} ],
		['jsonval', ('jsonval', '*'), '>', ('jsonval', '*'), lambda x, y: {'type': 'gt', 'val': (x[0][1], x[2][1])} ],
		['jsonval', ('jsonval', '*'), '<', ('jsonval', '*'), lambda x, y: {'type': 'ls', 'val': (x[0][1], x[2][1])} ],
		['jsonval', ('jsonval', '*'), '!=', ('jsonval', '*'), lambda x, y: {'type': 'neq', 'val': (x[0][1], x[2][1])} ],

		['jsonval', ('jsonval', '*'), '+', ('jsonval', '*'), lambda x, y: {'type': 'add', 'val': (x[0][1], x[2][1])} ],


		['jsonval', ('string', '*') , lambda x, y: x[0][1][1:-1] ],
		['dictel', ('dicte', '*') , lambda x,y: x[0][1]],
		['dictel', ('dictel', '*'), ',', ('dictel', '*') , lambda x,y: mifu(x[0][1], x[2][1])],
		['jsonvall', ('jsonval', '*'), ',', ('jsonvall', '*') , lambda x,y: [x[0][1]]+x[2][1]],
		['jsonvall', ('jsonval', '*'), ',', ('jsonval', '*') , lambda x,y: [x[0][1], x[2][1]] ],
		['jsonval', '[', ('jsonvall', '*'), ']' , lambda x,y: x[1][1]],
		['jsonval', '[', ('jsonval', '*'), ']' , lambda x,y: [x[1][1]]],
		['jsonval', '[', ']' , lambda x, y: []],
		['jsonval', '{', '}' , lambda x, y: {}],
		['jsonval', '{', ('dictel', '*'), '}', lambda x,y: x[1][1]],
	];
	varlist = {"Saini": 124, "j": 32};#values to be given to variables.
	return leftparse(parsedfile, rules, varlist);


def genhtml(t, depth=0): 
	sep=" ";
	lines = [];
	if(t[0] == "t"):
		lines.append(str(t[1]));
	else:
		lines.append("<"+str(t[0])+">");
		try:
			map(lambda i: map(lambda x: lines.append(x), genhtml(i, depth+1)), t[2]);
		except:
			lines.append("Failed !");
			pass
		lines.append("</"+str(t[0])+">");
	lines.append("");
	return map(lambda x: sep*depth+x, lines);





a = parsehtml(parsedfile);

for i in a[0][1]:
	print '\n'.join(genhtml(i));



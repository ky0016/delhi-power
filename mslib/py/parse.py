execfile("func.py");

data = read_file("page.html");

from plex import *

letter = Range("AZaz")
digit = Range("09")
name = (letter | Any("_")) + Rep(letter | digit | Any("_") )
number = (Str("-") | Str("")) +Rep1(digit)
space = Any(" \t\n")
linecomment = (Str("#") + Rep(AnyBut("\n")) + Eol )
astring = (Str("'") + Rep( (Str('/')+AnyChar) | AnyBut("'") ) + Str("'"));
dstring = (Str('"') + Rep( (Str('/')+AnyChar) | AnyBut('"') ) + Str('"'));

resword = Str("True", "False", "==", "<=", ">=", "!=") | Any("+-&*()=/[];|:{},.")


phpparser = Lexicon([
	State("comment_started", [
		(Str("*/"), Begin("")),
		(AnyBut(""), IGNORE)
		]),
	(resword, ["resword", TEXT]),
	(number, ["number", TEXT]),
	(name, ["name", TEXT]),
	(astring | dstring, ["string", TEXT]),
	( Str("/*"), Begin("comment_started")),
	(space | linecomment | AnyChar , IGNORE),
]);


filename = "jsonc.json"
filename = "page.html"


scanner = Scanner(phpparser, open(filename), filename)
parsedfile = [];
while 1:
		token = scanner.read()
		if token[0] is None:
				break
		parsedfile.append((token[0][0], token[1]));

def dispcool(parsedfile):
	for i in parsedfile:
		print i[1],

def leftparse(parsedfile, rules, varlist):
	checker = lambda ourdatap, rulep: (rulep == ourdatap[1]) or (rulep[0] == ourdatap[0] and ( rulep[1]=='*' or rulep[1]==ourdatap[1]));
	def ismatch(l1, l2):
		if(len(l1) != len(l2)):
			return False;
		for i in range(len(l1)):
			if( not(checker(l1[i], l2[i]) )):
				return False;
		return True;
#	ismatch = lambda ourdata, rule: ((len(rule) == len(ourdata)) and (isallone( checker(ourdata[i], rule[i]) for i in range(len(rule)) )))
	stake = [];
	count = 50;
	rparsedfile = parsedfile[::-1];
	ii=0;
	while(True):
		count-=1;
		for j in rules:
			jmatch = j[1:-1];
			maymatch = stake[-(len(jmatch)):][::-1];
			if(ismatch(maymatch, jmatch)):
				stake = stake[:-(len(jmatch))]+[(j[0], maymatch if j[-1] == None else j[-1](maymatch, varlist) )];
				break;
		else:
			if(ii<len(parsedfile)):
				i = rparsedfile[ii];
				stake.append(i);
				ii+=1;
			else:
				break;
	return stake;



# dispcool(parsedfile);

# a = leftparse(parsedfile, rules);

# print "\n\n\n\n";
# print "\n".join(str(i) for i in a)
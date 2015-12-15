from msl import *
from msl.help import *

a = s2j(read_file("/tmp/null"));

def quoted_s(x):
	return replaceall(x, cod([('\\', '\\\\'), ('\t', "\\t"), ('\n', "\\n"), ('"', '\\\"')]));

def json2cpptj(j):
	def json2cppjson(j):
		tj = type(j);
		if(tj==int):
			return ["1 "+str(j)];
		elif(tj == str):
			return ["2 "+quoted_s(j)]
		elif(tj == list):
			return ["3 "+str(len(j))]+map(lambda x: "\t"+x, mixl(map(json2cppjson, j)))
		elif(tj == dict or tj == cod):
			return ["4 "+str(len(j))]+map(lambda x: "\t"+x, mixl(mapp(lambda x,y: ["2 "+quoted_s(y)]+json2cppjson(x), j)))
		elif(j == None):
			return ["5"];
		elif(tj == bool):
			return ["6 "+str(int(j))];
		elif(tj == float):
			return ["7 "+("%f"%j)]
		else:
			return "1 0";
	return "\n".join(json2cppjson(j))



#print json.dumps(a);

print json2cpptj(a);


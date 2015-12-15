execfile("includes/setting.py");

_printout = ""

execfile(_mslib+"py/func.py");

try:
	inpdata = udicttostr(json.loads(sys.argv[1]));
	_session = inpdata["session"];
	_get = inpdata["get"];
	_post = inpdata["post"];
	_urlpath = inpdata["url"]
	_files = inpdata["file"];
	_addinfo = inpdata["addinfo"];
except:
	print "Error in reading php vars";
	(_session, _get, _post, _urlpath, _file, _addinfo) = ({}, {}, {}, '', {}, {});

write_file(".datainput.txt", str((_session, _get, _post, _urlpath, _file, _addinfo)));
elc_virtual('python mainpy2.py');
print read_file(".dataoutput.txt");

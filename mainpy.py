_agent = "poorvi";
execfile("includes/setting.py");

import time, sys, random, urllib, urlparse

#import MySQLdb

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;



try:
	inpdata = udicttostr(json.loads(sys.argv[1]));
	_session = inpdata["session"];
	_get = inpdata["get"];
	_post = inpdata["post"];
	_urlpath = inpdata["url"]
	_files = inpdata["file"];
	_addinfo = inpdata["addinfo"];
except Exception as e:
	print "Error in reading php vars"+str(e);
	(_session, _get, _post, _urlpath, _file, _addinfo) = ({}, {}, {}, '', {}, {});
execfile(_mslib+"py/webd.py");

_urlpath = geturlpath(_urlpath);

#mprint("%f"%time.time());



exec(read_file(ROOT+"py/main.py"));

filename = ("index" if _urlpath[1] == "" else _urlpath[1]);

# mprint(_urlpath);

if(filename == "ajaxactions"):
	mprint(json.dumps(pagehandler(filename).ajaxactions()));
else:
	pageh = pagehandler(filename).call();
	if(not(g(_addinfo, "redirect") == True)):
		mprint(execview(filename+".cpp", mifa(pageh, {"HOST": HOST, "CDN": CDN, "BASE":BASE})));


#	maincontent = mtmlparser();
#	maincontent.readcompiled(filename+".cpp");
#	write_file("cache_mainpage.html", maincontent.disp(mifu(pageh, {"HOST": HOST, "CDN": CDN, "BASE":BASE}, True) ));
#	mprint(read_file("cache_mainpage.html"));

#mprint("<br>%f<br>"%time.time());

_sql.close_db();

print json.dumps({"printout": _printout, "_SESSION": _session, "_header": _phpheader, "toresize": _toresize});

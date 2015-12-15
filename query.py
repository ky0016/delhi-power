_agent = "gcl";

execfile("includes/setting.py");

if(_server == "csc"):
	ROOT = "/home/btech/cs1120233/private_html/kurry/";
	_mslib = "/home/btech/cs1120233/private_html/kurry/mslib/";


import time, sys, MySQLdb, random

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;




execfile(_mslib+"py/webd.py");


execfile(ROOT+"py/main.py");

# maincontent = mtmlparser();

# maincontent.readonefile("templates/test.cpp");

# print maincontent.disp() ;


#print sql.sval("users", limit=1);

#print sql.ival("users", {"name": "Mohit#$%^6''", "email": "timepass@mail.com"});

#a = pagehandler("init").init();


if(_server ==  "csc" ):
	elc("scp cs1120233@ssh1.iitd.ac.in:~/private_html/.queryinput.txt .");




[query, darr, arr] = s2j(read_file(".queryinput.txt"));
if(sys.argv[1] == 'g'):
	outp = _sql.g(query, darr, arr);
else:
	outp = _sql.q(query, darr, arr);
write_file(".queryoutput.txt", json.dumps(outp));
_sql.close_db();


if(_server == "csc" ):
	elc("scp .queryoutput.txt cs1120233@ssh1.iitd.ac.in:~/private_html/");

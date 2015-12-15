
#import xlrd, requests, urllib

_agent = "poorvi";


execfile("includes/setting.py");

import time;

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

(_session, _get, _post, _urlpath, _file, _addinfo) = ({}, {}, {}, '', {}, {});

execfile(_mslib+"py/webd.py");
execfile(ROOT+"py/main.py");


#print curl("http://api.textlocal.in/send/", {"username": "mohitsaini1196@gmail.com", "hash": "Mohitsaini1", "numbers": "7503759053", "sender": 'TXTLCL', "message": "Hey, This is just a message"});

print pagehandler("index").db_init();

# maincontent = mtmlparser();

# maincontent.readonefile("templates/test.cpp");

# print maincontent.disp() ;



#print pagehandler("index").db_init();

_sql.close_db();

#a = _sql.sval("users")

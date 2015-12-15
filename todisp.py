execfile("includes/setting.py");
import time, sys;

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

execfile(_mslib+"py/webd.py");

if(len(sys.argv)>1):
	ginp = s2j(sys.argv[1]);
else:
	ginp = s2j(read_file("todispdata.json"));

outpvar = htmltree();
compiledf = ROOT+"templates/.compiled/"

#print("<br>Start1:%f<br>"%time.time());
execfile(compiledf+"defines.py");
#print("<br>Start1.1:%f<br>"%time.time());
execfile(compiledf+ginp["page"]+".py");
#print("<br>Start2:%f<br>"%time.time());

print "\n".join(printoutp(outpvar.root.tostr(), "  ", -2));

#print("<br>Start3:%f<br>"%time.time());

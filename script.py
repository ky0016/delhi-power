import sys, os

execfile("includes/setting.py");
execfile(_mslib+"py/webd.py");

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

execfile(_mslib+"ocaml1/run.py");

def setp():
	print elc("chmod 777 "+_mslib+"alldef -R");


_pushpull_localstore = ".msl/";

def push(ctext):
	os.system("cp "+_msladd+"* "+_pushpull_localstore);
	os.system("git add '*';"+'git commit -m "'+ctext+'"; git push');

def pull():
	os.system("git pull");
	os.system("cp "+_pushpull_localstore+"* "+_msladd);

def compile(): #compile all
	folder = "templates/";
	parser = _mslib+"ocaml/calc";
	compiledf = ".compiled"
	defines = "defines";
	cmd = lambda f: eval("["+ elc(parser+" "+f+" 2> /dev/null") + "]");

	pagefiles = list(i for i in os.listdir(folder) if os.path.isfile(folder+i) and (i not in [compiledf]));

	list(write_file(folder+compiledf+"/"+i, str(cmd(folder+i)) ) for i in pagefiles);
	write_file(folder+compiledf+"/"+defines, str(fold(lambda x,y: x+y, list(cmd(x) for x in allfile_rec(_mslib+"alldef/", True)+allfile_rec(ROOT+"templates/commons/", True)), []) ));

	m = mtmlparser();
	for i in [defines]+pagefiles:
		write_file(folder+compiledf+"/"+i+".py", m.disp(eval(read_file(folder+compiledf+"/"+i))));


if(len(sys.argv) >= 2 ):
	cmd = sys.argv[1]
	if( cmd == "setp" ):
		setp();
	elif( cmd == "compile" ):
		compile();
	elif( cmd == "push" ):
		push(g(sys.argv, 2, "Another Change"));
	elif( cmd == "pull"):
		pull();


execfile("includes/setting.py");

_printout = ""

execfile(_mslib+"py/func.py");
execfile(_mslib+"ocaml/run.py");

_agent = "poorvi";

_toresize = {};
_phpheader = "";

elc("scp cs1120233@ssh1.iitd.ac.in:~/private_html/.datainput.txt .");
(_session, _get, _post, _urlpath, _files, _addinfo) = eval(read_file(".datainput.txt"));

write_file(".dataoutput.txt", "");

execfile(_mslib+"py/webd.py");


exec(read_file(ROOT+"py/main.py"));


filename = ("index" if _urlpath == "" else _urlpath);

if( filename == "ajaxactions" ):
	mprint(json.dumps(pagehandler(filename).ajaxactions()));
else:
	pageh = pagehandler(filename).call();
	maincontent = mtmlparser();
	maincontent.readcompiled(filename+".cpp");
	mprint(maincontent.disp( mifu(pageh, {"HOST": HOST, "CDN": CDN, "BASE":BASE}, True) ));

_sql.close_db();

write_file(".dataoutput.txt", json.dumps({"printout": _printout, "_SESSION": _session, "_header": _phpheader, "toresize": _toresize}));
elc("scp .dataoutput.txt cs1120233@ssh1.iitd.ac.in:~/private_html/");

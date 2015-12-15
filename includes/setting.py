
execfile("includes/password.py");

if(_server == 'gcl'):
	HOST = 'http://poorvi.cse.iitd.ac.in/~cs1120233/power/';
	_hostextrapath = 'power/';
	ROOT = '/home/btech/cs1120233/private_html/power/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = 'msl/'
	db_data["qs_host"] = "10.208.20.185";
	db_data["qs_host"] = "10.208.20.186";

elif(_server == 'csc'):
	HOST = 'http://privateweb.iitd.ac.in/~cs1120233/power/';
#	ROOT = '/home/btech/cs1120233/private_html/power/';
	ROOT = '/home/cse/btech/cs1120233/private_html/power/';
	db_data = {'host': 'poorvi.cse.iitd.ac.in', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = '~/.local/lib/python2.7/site-packages/msl/';
	db_data["qs_host"] = "10.208.20.9";


elif(_server == "aws"):
	HOST = 'http://54.149.49.212/power/';
	ROOT = '/var/www/html/power/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'power'};
	_msladd = '/usr/lib/python2.7/msl/';

elif(_server == "aws_power"):
	HOST = 'http://52.62.43.34/';
	ROOT = '/var/www/html/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'power'};
	_msladd = '/usr/lib/python2.7/msl/';


elif(_server == "solnki"):
	HOST = 'http://localhost/power/';
	ROOT = '/var/www/html/power/';
	db_data = {'host': '10.208.20.8', 'user': 'mohit', 'pass': 'mohitsaini', 'db': 'mohit'};
	_msladd = '/usr/lib/python2.7/msl/';

elif(_server == "mohit"):
	HOST = 'http://localhost/power/';
	ROOT = '/var/www/power/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohitsaini', 'db': 'power'};
	_msladd = '/usr/lib/python2.7/msl/';

elif(_server == "kailash"):
	HOST = 'http://localhost/power/';
	ROOT = '/var/www/html/power/';
	db_data = {'host': 'localhost', 'user': 'root', 'pass': 'mohit', 'db': 'power'};
	_msladd = '/usr/lib/python2.7/msl/';


db_data["qs_port"] = 1136;

CDN = HOST+'photo/'
BASE = HOST+'index.php/'
_mslib = ROOT+"mslib/";
_includes = [];



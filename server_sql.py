import os,sys,time,socket,json,threading,random;

execfile("includes/setting.py");

from msl import *
from msl.help import *
from msl.sql import *
from msl.mtime import *;

listen_port=1136;
cleaner_timeout = 60*15;
_agent = "gcl";


execfile("py/server_action.py");
execfile(_mslib+"py/webd.py");
execfile(ROOT+"py/main.py");



_server_actions = server_action();

def closewithmsg(conn,msg,ec=-30):
	conn.send( json.dumps({"msg":msg,"ec":ec}) );
	conn.close();

def serv():
	global listen_port
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	lock=threading.Lock();
	if(False):
		while(True):
			try:
				sock.bind(('',listen_port))
				write_file("listenport",str(listen_port));
				break;
			except:
				listen_port+=1;
	else:
		os.system("fuser -k "+str(listen_port)+"/tcp");
		sock.bind(('',listen_port))
		#write_file("listenport",str(listen_port));

	sock.listen(1);
	print "I am ",getmyip()," On port ",listen_port;


	def talk(conn,client_address):#talk to each request
		print "a Client connected me ",client_address;
		send_json = lambda x: my_send(conn, json.dumps(x));
		while(True):
			cmd=s2j(my_recv(conn));
			try:
				mifu(cmd, {"isclose": False});
				if(cmd["isclose"]):
					break;
				send_json(_server_actions.handler(cmd));
			except Exception as e :
				send_json({"ec": "-100", "msg": "Error: "+str(e)});
		print "I am done with him"
		conn.close();

	def timer_cleaner():
		while(True):
			time.sleep(cleaner_timeout);
			print "Cleaner Aquired Lock",;
			lock.acquire();
			lock.release();
			print "Cleaner release Lock";
	threading.Thread(target=timer_cleaner).start();
	while True:
		print "Waiting...";
		conn, client_address = sock.accept();
		print "Found Client";
		lock.acquire();
		try:
			talk(conn,client_address);
		except Exception as e:
			print "Error in replying the client:",e;
		lock.release();
	sock.close();

serv();


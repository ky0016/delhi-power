import socket,sys, time

import json
from msl import *
from msl.help import *
from msl.mtime import *;

HOST = sys.argv[1];

PORT=int(read_file("listenport"));


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
	print "Good..", ">>"+HOST+"<<", "<>>"+str(PORT)+"<<";
	s.connect((HOST, PORT))
	for i in range(5):
		print "%f"%time.time();
		my_send(s, json.dumps({"action": "sql", "query": ["select * from users", {}, {}, "g"] }));
		print my_recv(s)+";";
	my_send(s, json.dumps({"isclose": True}));
	s.close()
except Exception as e:
	print e;




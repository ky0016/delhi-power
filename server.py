import thread
import os,sys,time,socket;

def elc(c):
	f=os.popen(c);
	data = f.read();
	f.close();
	return data;


listen_port=1116;

def reg():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("www.iitd.ac.in",80))
	myip=s.getsockname()[0];
	s.close()
	return myip;



def serv():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('',listen_port))
	sock.listen(1);
	def talk(conn,client_address):
		print "a Client connected me ",client_address;
		cmd=conn.recv(1024);
		print "From ",client_address," Received command ",cmd,"....",
		sending_data=elc(cmd);
		conn.send(str(len(sending_data)));
		conf=conn.recv(1);
		if(conf=='y'):
			conn.send(sending_data);
		print "Sent it's executed value ! ";
		conn.close();

	while True:
		print "Waiting...";
		conn, client_address = sock.accept();
		thread.start_new_thread(talk,(conn,client_address));
	sock.close();

print "I am ",reg();
serv();



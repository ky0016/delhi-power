
class server_action:
	def handler(self, cmd):
		self.ec = 1;
		computed = eval("self."+cmd["action"]+"(cmd['inp'])");
		return {"ec": self.ec, "data": computed};

	def tnow(self, cmd):
		return tnow();

	def sql(self, inp):
		if(inp[3] == 'g'):
			return _sql.g(inp[0], inp[1], inp[2])
		elif(inp[3] == 'q'):
			return _sql.q(inp[0], inp[1], inp[2])


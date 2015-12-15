
class json{
public:
	void* data;
	char type;
	json() {
		type = '\0';
		data = NULL;
	}
	json(double x) {
		type = 'f';
		data = new double(x);
	}
	json(string x) {
		type = 's';
		data = new string(x);
	}
	json(char c) {
		type = c;
	}
	json(char c, int num, ...) {
		type = c;
		va_list ap;
		int n_args = num;
		if(c=='i') {
			this->set_int(num);
		}
		else if (c=='l') {
			va_start(ap, num);
			FL(i, n_args) {
				this->pushjsonl(va_arg(ap, json*));
			}
			va_end(ap);
		} else if (c=='m') {
			num*=2;
			va_start(ap, num);
			FL(i, n_args) {
				string *keyp = va_arg(ap, string*);
				this->addkey((*keyp), va_arg(ap, json*));
				delete keyp;
			}
			va_end(ap);
		}
	}

	json (const json & j) {
		this->newcopy(j);
	}

	void newcopy(const json & j) {
		type = j.type;
		if(type == 'i')
			set_int(j.get_int());
		else if(type == 's')
			set_str(j.get_str());
		else if(type == 'f')
			set_float(j.get_float());
		else if(type == 'l')
			this->set_list(j.get_list1());
		else if(type == 'm') 
			this->set_map(j.get_keys1(), j.get_map1());
	}

	json& operator = (const json & v) {
		this->newcopy(v);
		//assert(false && ("Bug: I thought nobody will call this method"));
		return *this;
	}


	~json() {
//		cout<<"I have free the json with type = "<<type<<endl;
		if(data != NULL) {
			if(type == 'i')
				delete (int*)data;
			else if(type == 's') 
				delete (string*)data;
			else if (type == 'l')
				delete get_list();
			else if( type == 'm') {
				delete get_keys();
				delete get_map();
				delete (pair<void*, void*>*)data;
			}
			else if ( type == 'f') 
				delete (double*)data;
		}
	}
	inline void set_int(int x) {
		data = new int(x);
	}
	inline void set_str(string x) {
		data = new string(x);
	}
	inline void set_float(double d) {
		data = new double(d);
	}
	inline void set_list(vector<json>l) {
		this->init_list();
		*get_list() = l;
	}
	inline void set_map(vector<string>keys, map<string, json> jsonm) {
		this->init_map();
		*get_keys() = keys;
		*get_map() = jsonm;
	}

	inline void init_list() {
		data = new vector<json>(0);
	}
	inline void init_map() {
		data = new pair<void*, void*>(new map<string, json>(), new VS());
	}


	inline int get_int() const {
		return *((int*)data);
	}
	inline double get_float() const {
		return *((double*)data);
	}
	inline string get_str() const {
		return *((string*)data);
	}
	inline vector<json>* get_list() const {
		return ((vector<json>*)data);
	}
	inline vector<json> get_list1() const {
		return *(get_list());
	}
	inline map<string, json>* get_map() const {
		return (map<string, json>*)(((pair<void*, void*>*)data)->first);
	}
	inline map<string, json> get_map1() const {
		return *get_map();
	}
	inline VS* get_keys() const {// for map only
		return (VS*)(((pair<void*, void*>*)data)->second);
	}
	inline VS get_keys1() const {// for map only
		return *get_keys();
	}

	void pushjsonl(json*j) {
		get_list()->PUSH(*j);
		delete j;
	}
	void addkey(string s1, json j);
	void addkey(string s1, json* j) {
		addkey(s1, *j);
		delete j;
	}

	string __str__();
	json*copy();
	void parse(istream& fd);
	void self_Not();
	json* op_Get(json j);
	void self_Set(json j, json j1);
	json op_Attr(string s);
	json op_Ife();
	json op_Binary(string, json j1);
};

#define INDEXARR(j) (j.type == 'i' ? j.get_int(): j.get_list()->size())
#define INDEXARRVAL(j, i) (j.type == 'i' ? i: j.get_list()[i])
typedef map<string, json> mapsj;
#define MAPSJL(it, m) for(mapsj::iterator it = m.begin(); it != m.end(); it++) 


json json::op_Binary(string op, json j1) {
	return *this;
}

void json::addkey(string s1, json j) {
	mapsj gmap = *get_map();
	if(!FIND(s1, gmap)) {
		get_keys()->PUSH(s1);
	}
	(*get_map())[s1] = j;
}


void json::self_Not() {
	set_int(!get_int());
}

json* json::copy() {
	return new json(*this);
}

inline json* json::op_Get(json j) {
	if(type == 'l')
		return &(get_list1()[j.get_int()]);
	else if(type == 'm') 
		return &(get_map1()[j.get_str()]);
	else
		return NULL;
}

inline json json::op_Attr(string s) {
	if(s=="len") {
		return json('i', (type == 'l' ? get_list1().size() : get_keys1().size()));
	} else if( s == "keys" ) {
		return *this;
	} else if( s == "gchars" ) {
		return *this;
	}
}




string json::__str__() {
	if (this->type == 'n')
		return "null";
	else if (this->type == 'i') 
		return int2str(this->get_int());
	else if (this->type == 'f') 
		return float2str(this->get_float());
	else if (this->type == 's')
		return quotestring(this->get_str());
	else if (this->type == 'l') {
		string outp = "[";
		vector<json> jlist = this->get_list1();
		FL(i, jlist.size()) {
			outp+=(jlist[i].__str__());
			if(i!=jlist.size()-1) 
				outp+=", ";
		}
		outp+="]";
		return outp;
	}
	else if(this->type == 'm') {
		string outp = "{";
		VS keys = this->get_keys1();
		FL(i, keys.size()) {
			outp+=(quotestring(keys[i])+": "+ this->get_map1()[ keys[i] ].__str__());
			if(i!=keys.size()-1) 
				outp+=", ";
		}
		outp+="}";
		return outp;
	}
	else
		return "0";
	return "Mohit..";
}

void json::parse(istream& fd) {
	int type,temp;
	string temp1;
	double tempf;
	fd>>type;
	if(type == 1 || type == 6 ) {
		this->type = 'i';
		fd>>temp;
		this->set_int(temp);
	} else if(type == 2) {
		this->type = 's';
		getline(fd, temp1);
		this->set_str(invqstring(temp1.substr(1)));
	} else if(type == 3) {
		int listlen;
		fd>>listlen;
		this->type = 'l';
		this->init_list();
		FL(i, listlen) {
			json j;
			j.parse(fd);
			this->get_list()->PUSH(j);
		}
	} else if(type == 4) {
		int listlen;
		fd>>listlen;
		this->type = 'm';
		this->init_map();
		FL(i, listlen) {
			fd>>temp;
			string key;
			getline(fd, key);
			key = invqstring(key.substr(1));
			json j;
			j.parse(fd);
			this->addkey(key, j);
		}
	} else if(type==5) {
		this->type = 'n';
	} else if(type == 7) {
		this->type = 'f';
		fd>>tempf;
		this->set_float(tempf);
	}
}

json parse(istream& fd) {
	try {
		json j;
		j.parse(fd);
		return j;
	} catch (const char* msg) {
		cout<<":(  " <<msg<<endl;
	}
}




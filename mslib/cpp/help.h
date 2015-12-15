#define FL(i,n) for(int i=0; i<n; i++)
#define FLS(i, s, e) for(int i=s; i<e; i++)
#define FLSI(i, s, e, inc) for(int i=s; i<e; i+=inc)
#define RFL(i,n) for(int i=n-1; i>=0; i--)
#define FIND(elm, m) (m.find(elm) != m.end() ) //Warning: m is used twice
#define FINDV(elm, v) find(v.begin(), v.end(), elm) //Warning: v is used twice
#define FINDVB(elm, v) (FINDV(elm, v) != v.end()) //Warning: v is used twice, parent warning

#define FINDVI(elm, v) (FINDV(elm, v)-v.begin()) //Warning: v is used twice, parent warning
#define PRINTS(a, size, sep) FL(cur##__LINE__, size) { cout<<a[cur##__LINE__]<<sep; }
#define PRINTV(a) PRINTS(a, a.size(), ",") //Warning: a is used twice
#define PRINTVL(a) do{PRINTV(a); cout<<endl; }while(false) //Warning: Forward from child

#define LINEFORIF(i, m, expr, cond, outp) FL(i, m) { if(cond) outp.PUSH(expr); }

#define F first
#define S second
#define LL long long
#define VI vector<int>
#define VS vector<string>
#define INF 0x7fffffff
#define PUSH push_back


string int2str(int x) {
	stringstream ss;
	ss<<x;
	string outp;
	ss>>outp;
	return outp;
}

string float2str(float x) {
	stringstream ss;
	ss<<x;
	string outp;
	ss>>outp;
	return outp;
}

string quotestring(string inp) {
	string outp = string("")+'"';
	FL(j, inp.length()) {
		char i=inp[j];
		if(i=='\\')
			outp+="\\\\";
		else if(i=='\"')
			outp+="\\\"";
		else if(i=='\n')
			outp+="\\n";
		else if(i=='\t')
			outp+="\\t";
		else
			outp+=i;
	}
	outp+='"';
	return outp;
}

string invqstring(string inp) {
	string outp = "";
	for(int j=0; j<inp.length(); j+=2) {
		string focus = inp.substr(j, 2);
		if(focus=="\\n")
			outp+="\n";
		else if(focus=="\\\"")
			outp+='\"';
		else if(focus=="\\\\")
			outp+="\\";
		else if(focus=="\\t")
			outp+='\t';
		else {
			outp+=inp[j];
			j--;
		}
	}
	return outp;
}

string join(vector<string>sl, string join_str) {
	string outp = "";
	FL(i, sl.size()) {
		outp+=sl[i];
		if(i!=sl.size()-1)
			outp+=join_str;
	}
	return outp;
}






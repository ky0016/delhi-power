#include <bits/stdc++.h>
using namespace std;

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

#define LINEFORIF(i, m, cond, outp) FL(i, m) { if(cond) outp.PUSH(i); } //This is bkvas. don't use it again
#define LINEFORIF1(i, m, expr, cond, outp) FL(i, m) { if(cond) outp.PUSH(expr); }

#define F first
#define S second
#define LL long long
#define VI vector<int>
#define INF 0x7fffffff
#define PUSH push_back




//Local Definations..
#define mapi map<int, int>
#define mapii map<int, VI>
#define indpair pair3<int, int, int> //(indexval, clique_id, slack) or (labelno., clique id, pixel id) , Warning: Don't use it.

#define pair3i pair3<int, int, int>

#define mapil(c) for(mapi::iterator i=c.begin(); i!=c.end(); ++i )
#define mapiil(c) for(mapii::iterator i=c.begin(); i!=c.end(); ++i )

#include "use.h"


streamer sm;
int n, k, m, nc; //# of Pixels, Clique Size, # of labels, # of cliques
stringstream ss;
vector<VI> allconfig;

class clique{
public:
	int id;
	mapii v;
	VI wclc;
	VI wc_slack;
	VI vkeys; // = v.keys()

	clique(int idd) {
		id = idd ;
	}

	void print(string ext="") {
		printf("C%d: ", id);
		PRINTV(vkeys);
		cout<<ext;
	}
};

vector<class clique> cliques;
vector<class pixel> pixels;

class pixel {
public:
	int id, maxofmin;
	VI heights, dpl, mycliques;
	vector<pair3i> labels; //these are labels which are given as ranking..
	map<int, vector< indpair > > nbrindex;
	VI nbrs;
	pixel(int m, int idd) {
		id = idd;
		heights.resize(m, 0);
		dpl.resize(m, 0);
		labels.resize(m, make_pair3(-1, -1, -1));
	}
	void set_mycliqes(); //Need to do it once only.
	void set_myheights(VI labell);
	void set_maxofmin(); //Assume heights are already set.
	void print(string ext);
	VI get_minballs(); //Assume maxofmin is set
	VI get_maxballs(); //Assume maxofmin is set
	void cal_indexes();
};


VI pixel::get_minballs() {
	VI outp;
	LINEFORIF(i, m, heights[i] == heights[maxofmin], outp);
	return outp;
}

VI pixel::get_maxballs() {
	VI outp;
	LINEFORIF(i, m, heights[i] != heights[maxofmin], outp);
	return outp;
}

void pixel::set_maxofmin() {
	sm.reset(false);
	FL(i, m) {
		sm.fedformin( heights[i], i );
	}
	maxofmin =  sm.minat;
}

void pixel::print(string ext = "") {
	printf("(Pixel%d: heights = [", id);
	FL(i, m) {
		cout<<heights[i]<<",";
	}
	cout<<"])";
	cout<<ext;
}

void pixel::set_mycliqes() {
	mycliques.resize(0);
	FL(i, nc) {
		if(FIND(id, cliques[i].v ))
			mycliques.push_back(i);
	}
}

void pixel::set_myheights(VI labell) {//call it when some of cliques[c].v vars are changed.
	FL(j, labell.size()) {
		sm.reset();
		sm.fedforsum( this->dpl[j] );
		FL(i, mycliques.size()) { //Assuming this loop runs atleast once
			sm.fedforsum(cliques[i].v[id][j] );
		}
		this->heights[j] = sm.sum; //Assuming that pixel belongs to one of pixels. Otherwise sm.sum is bkvas.
	}
}

string readline(istream& fd) {
	string line;
	do{
		getline(fd, line);
	}while(line.length() == 0 || line[0] == '#');

	return line;
}

void readss() {
	string line = readline(cin);
	ss.str("");
	ss<<line<<endl;
}

VI getnbrs(int p) {
	VI outp;
	VI mycliques = pixels[p].mycliques;
	FL(i, mycliques.size()) {
		VI mypixels = cliques[mycliques[i]].vkeys;
		FL(j, mypixels.size()) {
			if( mypixels[j] != p && !FINDVB(mypixels[j], outp)) {
				outp.PUSH(mypixels[j]);
			}
		}
	}
	outp.PUSH(p); //PS: I am not stupid
	return outp;
}

void init_algo() {
	int temp;
	readss();
	ss>>n>>k>>m>>nc;
	FL(i, n) {
		pixel p(m, i);
		readss();
		FL(j, m) {
			ss>>p.dpl[j];
			p.heights[j] = p.dpl[j];
		}
		pixels.push_back(p);
	}
	FL(i, nc) {
		clique c(i);
		readss();
		FL(j, k) {
			VI mm(m, 0);
			ss>>temp;
			c.v[temp] = mm;
		}
		FL(j, pow(m, k)) {
			readss();
			ss>>temp;
			c.wclc.push_back(temp);
			c.wc_slack.push_back(temp);

		}
		c.vkeys = mapiikeys(c.v);
		cliques.push_back(c);
	}
	allconfig = genallconfig(k, n);
	FL(i, n) {
		pixels[i].nbrs = getnbrs(i);
	}
}

void disp(bool once = false) {
	if(once) {
		printf("Number of pixels = %d, Clique size = %d, Number of labels = %d, Number of cliques = %d\n\n\nCliques = \n", n, k, m, nc);
		FL(i, nc) {
			cliques[i].print("\n");
		}
		FL(i, nc) {
			printf("DFC for Clique%d:\n", i);
			FL(config, allconfig.size()) {
				FL(l, k) {
					VI mypixels = cliques[i].vkeys;
					printf("Vc%d,p%d,l%d", i, mypixels[l], allconfig[config][l]);
					if(l!=k-1)
						printf(" + ");
				}
				printf(" <= %d ( Slack = %d )\n", cliques[i].wclc[config], cliques[i].wc_slack[config]);
			}
		}
	}
	printf("\nV Variables: \n");
	FL(i, nc) {
		VI mypixels = cliques[i].vkeys;
		FL(j, k) {
			FL(l, m) {
				printf("Vc%d,p%d,l%d = %d, ", i, j, l, cliques[i].v[mypixels[j]][l] );
			}
			cout<<";"<<endl;
		}
		cout<<endl;
	}
	printf("Pixels = \n");
	FL(i, n) {
		pixels[i].print("\n");
	}
	cout<<repstring("-", 100)<<endl;
}

pair<int, int> ind(int p, int q, int a, int c) { //Assuming {p,q} ⊆ c, a:ball, c:clique
	int pi = FINDVI(p, cliques[c].vkeys); //p index.
	int qi = FINDVI(q, cliques[c].vkeys);
	sm.reset();
	sm.maxima = -1; // This is epsilon label
	FL(config, allconfig.size()) {
		if(allconfig[config][pi] <= a  && cliques[c].wc_slack[config] > 0 ) {
			sm.fedformax(allconfig[config][qi], cliques[c].wc_slack[config]);
		}
	}
	return make_pair(sm.maxima, sm.maxat);
}

indpair ind(int p, int q, int a) { //Assuming ∃ c ∈ ℂ, {p,q} ⊆ c
	sm.reset();
	int slackinclique[nc];
	FL(i, nc) {
		if(FIND(p, cliques[i].v) && FIND(q, cliques[i].v) ) {
			pair<int,int> indcap = ind(p, q, a, i);
			slackinclique[i] = indcap.S;
			sm.fedformin(indcap.F, i);
		}
	}
	return make_pair3(sm.minima, sm.minat, slackinclique[sm.minat]);
}

void pixel::cal_indexes() {
	FL(i, nbrs.size()) {
		nbrindex[nbrs[i]] = (vector<indpair>());
		FL(a, m) {
			nbrindex[nbrs[i]][a] = ind(id, nbrs[i], a);
		}
	}
}

void findpath() {
	FL(i, n) {
		pixels[i].cal_indexes();
	}
	FL(i, n*m) {
		FL(p, n) {
			FL(j, pixels[p].nbrs.size()) {
				int q = pixels[p].nbrs[j];
				FL(a, m) {
					pair3i calind = pixels[p].nbrindex[ q ][a];
					int corlabel = calind.x;
					if( corlabel == -1 || pixels[q].labels[corlabel].x != -1 ) {
						pixels[p].labels[ a ] = make_pair3(i, calind.y, calind.z) ;
					}
				}
			}
		}
	}
}

int main() {
	init_algo();

	disp(true);

	return 0;
}

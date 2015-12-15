

def cluster_points(plist, f): #f (p0, p1) -> is p0 friend of p1
	clusters = [];
	while(len(plist) > 0):
		cluster = filter(plist, lambda x: f(x,plist[0]))
		plist = setol(plist, cluster, '-');
		clusters.append(cluster);
	return clusters;


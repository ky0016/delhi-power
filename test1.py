y=0;
def f(x):
	global y
	y+=1;
	return x+y;


def g(x, z=f(3)):
	return z;


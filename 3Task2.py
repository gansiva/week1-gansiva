import math
def square_root(a,x):
	while True:
		#print(x)
		y=(x+a/x)/2
		if(abs(y-x)<0.0000000000001):
			return x
			break
		x=y

def test_square_root(n):
	col2=square_root(n,n)
	col3=math.sqrt(n)
	col4=abs(col2-col3)
	print(n," ",col2," ",col3," ",col4)

x=1
for x in range(1,10):
	test_square_root(x)



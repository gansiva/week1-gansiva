import turtle
import math

def polygon(t,l,n):
	"""Draws a polygon"""
	for i in range(n):
		t.fd(l)
		t.lt(360/n)
def circle(t,r):
	"""Draws a circle"""
	cir=2*math.pi*r
	polygon(t,int(cir/2),int(cir/2))
radi=int(input("Input radius of circle:"))
bob=turtle.Turtle()
circle(bob,radi)
turtle.mainloop()


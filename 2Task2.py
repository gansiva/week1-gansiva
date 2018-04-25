import turtle

def square(t):
	"""Draws a square"""
	for i in range(4):
		t.fd(100)
		t.lt(90)
bob=turtle.Turtle()
square(bob)
turtle.mainloop()

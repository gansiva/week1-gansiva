import turtle
import math
bob = turtle.Turtle()
def polygon(t, n, angle):
    for i in range(n):
        a = angle / n
        t.fd(25)
        t.lt(a)
def arc(t, angle):
    """Draws a arc"""
    n = int(360 / angle)
    polygon(t, n, angle)
arc(bob,50)
turtle.mainloop()

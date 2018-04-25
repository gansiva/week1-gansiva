import turtle

def polygon(t,l,n):
        """Draws a polygon"""
        for i in range(n):
                t.fd(l)
                t.lt((360/n))
len=int(input("Input the length: "))
sides=int(input("Input sides of polygon:"))
bob=turtle.Turtle()
polygon(bob,len,sides)
turtle.mainloop()



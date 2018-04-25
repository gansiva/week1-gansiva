import turtle

def square(t,l):
        for i in range(4):
                t.fd(l)
                t.lt(90)
len=int(input("Input the length: "))
bob=turtle.Turtle()
square(bob,len) #Draws square with variable length
turtle.mainloop()

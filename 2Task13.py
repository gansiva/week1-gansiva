def is_between(x,y,z):
    """Checks if the entered values satisfies x<=y<=x"""
    if(x<=y):
        if(y<=z):
            return True
    else:
        return False
a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
c=int(input("Enter 3rd num:"))
print("The relation x<=y<=z is ",is_between(a,b,c))

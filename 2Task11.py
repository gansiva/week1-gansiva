def is_triangle(a,b,c):
    """Checks if triangle can be formed"""
    if(a>(b+c)):
        return False
    elif(b>(a+c)):
        return False
    elif(c>(a+b)):
        return False
    return True
def chk_triangle(value):
    """Checks if the formed triangle is a degenerate one"""
    if(value==True):
        if(a==b+c or b==a+c or c==a+b):
            print("Entered values form a degenerate triangle")
        else:
            print("Entered values form a triangle")
    else:
        print("Entered values does not form a triangle")

a=int(input("Enter 1st side of a triangle:"))
b=int(input("Enter 2nd side of a triangle:"))
c=int(input("Enter 3rd side of a triangle:"))
value=is_triangle(a,b,c)
chk_triangle(value)

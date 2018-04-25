# Couldn't understand the logic of the equation

def check_format(a,b,c,n):
    if(n>2 and a**n+b**n==c**n):
        print("Fermat was right")
    else:
        print("Fermat was wrong")
a=int(input("Enter the positive integer for 'a' "))
b=int(input("Enter the positive integer for 'b' "))
c=int(input("Enter the positive integer for 'c' "))
n=int(input("Enter the positive integer for 'n' "))
check_format(a,b,c,n)


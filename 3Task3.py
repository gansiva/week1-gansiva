import math
def estimate_pi():
    a=(2*math.sqrt(2))/9801
    count=0
    fvalue=0
    while True:
        num=int((math.factorial(4*count))*(1103+(26390*count)))
        den=int(((math.factorial(count))**4)*(396**(4*count)))
        value=num/den
        fvalue=value+fvalue
        if(value<pow(10,-15)):
            return a*fvalue
            break
        count=count+1
print("Answer for 1/pie as per given formula is ",estimate_pi())
print("Comparing this answer with math.pi function which is ",1/math.pi)

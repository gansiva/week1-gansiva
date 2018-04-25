def ack(m,n):
    """Ackermann function"""
    if(m==0):
        return n+1
    elif(m>0 and n==0):
        return ack(m-1,1) #recursive function
    elif(m>0 and n>0):
        return ack(m-1,ack(m,n-1)) #recursive function
    return
m=int(input("Enter the value of m ="))
n=int(input("Enter the value of n ="))
print("Ackermann function for values of ",m,"and",n,"is",ack(m,n))


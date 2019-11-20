def gcd(a,b):
    if(b==0):
        return gcd(a,a%b)
    elif(a==0):
        return a
    else:
        return(0)
a=int(input())
b=int(input())
GCD=gcd(a,b)
print("GCD is: ")
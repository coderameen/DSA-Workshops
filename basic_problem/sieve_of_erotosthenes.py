#For given input n, we need to find all the prime number up to that number
#ip n=10 op: 2 3 5 7

def myprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def myprimenumbers(n):
    for i in range(2,n+1):
        if myprime(i):
            print(i, end=" ")
            
print(myprimenumbers(10))
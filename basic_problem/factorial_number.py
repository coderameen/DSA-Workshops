# 5! = 1*2*3*4*5
#ip: n=4 op:24
#ip:n=6 op:720
#ip:n=0 op:1 Bcoz 0! = 1
#ip: n=1 op:1 Boz 1! = 1

def fact(n):
    res = 1 #0!=1 or 1!=1
    for i in range(2,n+1):
        res*=i
    return res
print(fact(5))     

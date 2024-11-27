#Factorial of n nubmer using recursion
'''
input:
ip: n= 4
op: 24


ip: n = 0
op: 1

'''
def fact(n):
    if n>=0:
        #base condition
        if n == 0:
            return 1
        return n*fact(n-1)
print(fact(5))
#5! = 5 *4*3*2*1=120
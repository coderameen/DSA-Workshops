'''
Fibonacci number
ip: n=5
op:5 (0 1 1 2 3 5)


ip:7
op:13  (0 1 1 2 3 5 8 13)

ip: n=4
op: 3 (0 1 1 2 3)


ip: n=0
op: 0
'''

def fab(n):
    if n>=0:
        if n==0:
            return 0
        if n == 1:
            return 1
        return fab(n-1) + fab(n-2)
print(fab(4))
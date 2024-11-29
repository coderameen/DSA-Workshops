'''

ip: n= 5
op: 15

ip:10
op:55

'''
def sumRec(n):
    if n==0:
        return 0
    return n+ sumRec(n-1)

print(sumRec(5))#15
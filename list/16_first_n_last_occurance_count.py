#Index of first Occurance in a sorted array
'''
ip: [1,10,10,10,20,20,40]
x = 20
op: 4


ip: [1,10,10,10,20,20,40,40]
x = 40
op: 6

ip: [1,10,10,10,20,20,40,40]
x = 400
op: -1
'''


#sol 1: lraverse 1 by 1, if we dind the given element return the index of it. esle -1

def firstOccurnace(l,n,x):
    for i in range(0,n):
        if l[i] == x:
            return i
    return -1
    
l = [1,10,10,10,20,20,40,40]
n = len(l)
x = 20

#----
def lastOccurnace(l,n,x):
    for i in range(n-1,0,-1):
        if l[i] == x:
            return i
    return -1
    
l = [1,10,10,10,20,20,40,40]
n = len(l)
x = 40
print(lastOccurnace(l,n,x))


def lastOccurnace2(l,n,x):
    for i in reversed(range(len(l))):
        if l[i] == x:
            return i
    return -1
    
l = [1,10,10,10,20,20,40,40]
n = len(l)
x = 40
print(lastOccurnace2(l,n,x))
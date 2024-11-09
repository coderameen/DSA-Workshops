#Left rote by d places(******)
#Given a list l and given number d, we need to do left rotate the list
'''
C
d = 2
op: [30,40,10,20]


ip:[1,2,3,4,5,6]
d = 3
op: [4,5,6,1,2,3]
'''

#method 1
l = [1,2,3,4,5,6]
d = 3
l = l[d:] + l[:d]
print(l)


#method 2 using deque container
from collections import deque
l = [1,2,3,4,5,6]
d = 2
dq = deque(l)
dq.rotate(-d)#-ve is used for left rotate and +ve is used for right rotate
print(list(dq))


#method 3


def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))
    
    
    return l


l = [1,2,3,4,5,6]
d = 4  
print(leftRotate(l,d))
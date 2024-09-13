''''
ip: [1,2,3,4,5]
d = 2
op: [3,4,5,1,2]


ip: [1,2,3,4]
d = 3
op: [3,1,2,3]
'''

#sol 1
l =[10,20,30,40]
d = 2
print(l[d:]+l[:d])


#sol 2
from collections import deque
l = [10,20,30,40,50]
d = 3
dq = deque(l)
# print(dq)
dq.rotate(-d)#-ve => left rotate, +ve => right rotate
print(list(dq))#[40, 50, 10, 20, 30]

print("-----------------")
#own method

def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))
    return l
l = [10,20,30,40,50]
d = 2
print(leftRotate(l,d))
#l = [10,20,30,40,50]
#l = [20,30,40,50,10], i=0
#l = [30,40,50,10,20], i=1
#l = [40,50,10,20,30], i=2

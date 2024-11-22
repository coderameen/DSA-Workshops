'''
#Rotate a given array in Kth element

input:
arr = [10,20,30,40,50]
k = 2
output:
[30,40,50,10,20]
'''

from collections import deque
#create deque of array
d = deque([10,20,30,40,50])
k = 2
d.rotate(-k)#left rotation of array
print(d)


#[10,20,30,40,50] ==> output: [40,50,10,20,30]
d = deque([10,20,30,40,50])
k = 2
d.rotate(2)
print(d)
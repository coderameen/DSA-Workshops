#Left rotate a list(counter clockwise rotation)
'''
IP: [10,20,30,40]
OP: [20,30,40,10]


ip:[1,2,3]
op: [2,3,1]
'''

l = [10,20,30,40]
l = l[1:] + l[0:]
print(l)



#sol 2
l = [1,2,3,4]
# print(l.pop(0))
l.append(l.pop(0))
print(l)



#shifting technique
#[1,2,3,4,5]


def rotateByOne(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]
    l[n-1] = x
    return l

l = [1,2,3,4]
rotateByOne(l)
print(l)
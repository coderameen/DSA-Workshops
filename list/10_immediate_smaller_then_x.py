#Find the immediate smaller than x 
'''
ip: n=5
arr = [4,67,13,12,15]
x = 16

op: 15



ip: n = 5
arr = [1,2,3,4,5]
x = 1
op: -1
'''

def immediateSmaller(arr,n,x):
    l = []
    for i in arr:
        if i < x:
            l.append(i)#[4,13,12,15]
    if l == []:
        return -1
    return max(l)#15

arr = [4,67,13,12,15]
n = len(arr)
# x = 4 #op: -1
x = 16

print(immediateSmaller(arr,n,x))
#Find if array is sorted or not
'''
ip [10,20,30]
op: YES

ip: [10,5,12]
op: NO

ip:[10]
op: YES

ip:[]
op: YES
'''

#Sol 1
def isSorted(l):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            return False
    return True
    
l = [5,10,20,30,40]
print(isSorted(l))


#sol 2
def isSorted2(l):
    l2 = sorted(l)
    if l == l2:
        return True
    else:
        return False
    

l = [50,10,20,30,40]
# print(isSorted2(l))
if isSorted(l):
    print("YES")
else:
    print("No")


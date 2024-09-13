#Linear search
def linearSearch(l,key):
    for i in range(0,len(l)):
        if l[i]==key:
            return  i
    return -1
l = [10,20,30,40,50]
key = 20
print(linearSearch(l,key))

print("-------------")
#O(n)


#Binary search
'''
ip: l = [10,20,30,40,50]
key = 20
 op: 1



ip: l = [10,20,30,40,50]
key = 20
op: -1
'''

def BinarySearch(l,key):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == key:
            return mid
        elif l[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

l = [10,20,30,40,50]
key = 40
print(BinarySearch(l,key))

#O(log(n))
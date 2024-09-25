'''
arr = [10,20,20,20,30,30]
x = 20
op: 3


arr = [11,11,11]
x =11
op: 2

x = 77
op: -1
'''


#Using Linear Search
def lastOccLS(arr,x):
    for i in reversed(range(len(arr))):
    # for i in range(len(arr)-1,0,-1):
        if arr[i] == x:
            return i
    return -1



arr = [10,20,20,20,30,30]
x = 20
# print(lastOccLS(arr,x))



#using binary Search

def lastOccBS(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid-1
        else:
            if mid==len(arr) - 1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low = mid + 1
    


# arr = [10,20,20,20,30,30]
# x = 30

arr = [11,11,11]
x = 11

print(lastOccBS(arr,x))
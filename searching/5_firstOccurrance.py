'''
arr = [10,20,20,20,30,30]
x = 20
op: 1


arr = [11,11,11]
x =11
op: 0

x = 77
op: -1
'''

#using Linear Search

def firstOccLS(arr,x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [10,20,20,20,30,30]
x = 30

# print(firstOccLS(arr,x))


#using binary Search

def firstOccBS(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid-1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                high = mid -1
    


arr = [10,20,20,20,30,30]
# x = 30
x = 20

print(firstOccBS(arr,x))
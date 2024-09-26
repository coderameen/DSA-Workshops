def firstOcc(arr,x):
    low =0
    high = len(arr) -1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or arr[mid - 1]!=arr[mid]:
                return mid
            else:
                high = mid - 1
    return -1
def lastOcc(arr,x):
    low =0
    high = len(arr) -1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == len(arr) - 1 or arr[mid]!=arr[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1
    
    
def countOccMain(arr,x):
    firstIndex = firstOcc(arr,x)
    lastIndex = lastOcc(arr,x)
    if firstIndex == -1:
        return 0
    else:
        return lastIndex - firstIndex + 1
    
    
arr = [10,20,20,20,30,30]
x = 100
print(countOccMain(arr,x))

#20
# lo = 3
# fo = 1
# res = lo - fo + 1#3-1+1=3


#30
#lo = 5
#fo = 4
#res = lo - fo + 1#5-4+1=2
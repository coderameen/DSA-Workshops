'''
BINARY SEARCH



ip : arr = [10,20,30,40,50]
x = 30
op: 2 (index position of 30)


ip : arr = [10,20,30,40]
x = 55
op : -1

CASES 
mid = (low+high)//2
arr[mid] == x, return mid
arr[mid] > x, high = mid - 1
arr[mid] < x, low = mid + 1
'''
def binarySearch(arr,x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
    
            
arr = [10,20,30,40,50]
# x = 20
x = 40
print(binarySearch(arr,x))


#NOTE: only work for sorted array
#O(log(n))
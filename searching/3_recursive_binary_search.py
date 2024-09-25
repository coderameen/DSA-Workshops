#Recursive Binary Search

def bSearch(arr,x,low,high):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return bSearch(arr,x,low, mid-1)
    else:
        return bSearch(arr,x,mid+1,high)
        
        
def binarySearchMain(arr,x):
    return bSearch(arr,x,0,len(arr)-1)

arr = [10,20,30,40,50]
# x = 20
# x = 40
x = 22
print(binarySearchMain(arr,x))
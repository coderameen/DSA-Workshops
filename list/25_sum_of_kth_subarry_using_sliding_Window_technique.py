def maxKSum(arr,k):
    #first windown
    curr = 0
    for i in range(k):
        curr += arr[i]
    res = curr
    
    #upcoming elements
    for i in range(k,len(arr)):
        curr = curr + arr[i]-arr[i-k]
        res = max(curr,res)
    return res

arr = [1,8,30,-5,20,7]
k = 4
print(maxKSum(arr,k))#53
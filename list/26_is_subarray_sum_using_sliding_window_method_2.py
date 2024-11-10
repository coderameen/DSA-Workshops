def isSubSum(arr,sum):
    s,curr = 0,0
    for e in range(len(arr)):
        curr += arr[e]
        
        if curr > sum:
            curr -= arr[s]
            s+= 1
        if curr == sum:
            return True
    return False        
          
# arr = [1,4,20,3,10,5]
arr = [4,8,12,5]
sum = 17
print(isSubSum(arr,sum))

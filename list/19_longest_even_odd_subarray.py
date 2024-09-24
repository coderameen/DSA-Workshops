# arr = [10,12,14,7,8]
# op: 3
# arr = [7,10,13,14]
# op: 4

# arr = [10,12,8,4]
# op: 1

#arr = [11]
# op: 1
# #arr = [6]
# op:1
def maxEvenOdd(arr,n):
    res = 1
    curr = 1
    for i in range(1,n):
        if (arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i]%2!=0 and arr[i-1]%2==0):
           curr += 1
           res = max(res,curr)
        else:
            curr = 1
    
    return res
    


# arr = [10,12,14,7,8]
# arr = [7,10,13,14]
arr = [10,12,8,4]
n = len(arr)
print(maxEvenOdd(arr,n))
'''
ip: arr[] = [10,12,10,15,10,20,12,12]
op: 10 3
    12 3
    15 1
    20 1
    
ip: l = [10,10,10,10]
op: 10 4
'''
#direct approach
def frequencyCount(arr,n):
    dp = {}#hashset
    for i in range(n):
        if arr[i] in dp.keys():
            dp[arr[i]] += 1
        else:
            dp[arr[i]] = 1
            
    for k,v in dp.items():
        print(k," ",v)
    
    
    
arr = [10,12,10,15,10,20,12,12]
n = len(arr)
print(frequencyCount(arr,n))
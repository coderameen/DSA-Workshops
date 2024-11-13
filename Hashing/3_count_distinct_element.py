'''
ip: [10,20,10,30,30,20]
op: 3
'''
#Direct approach
arr =[10,20,10,30,30,20]
print(set(arr))#Bcoz set is a collection of unique elements


def distinctCount(arr,n):
    dp = {}#hashset
    for i in range(len(arr)):
        if arr[i] in dp.keys():
            dp[arr[i]] += 1
        else:
            dp[arr[i]] = 1
    # print(dp)#{10: 2, 20: 2, 30: 2}
    return len(dp)

# arr =[10,20,10,30,30,20]
arr = [10,10,10,10,10]
n = len(arr)
print(distinctCount(arr,n))
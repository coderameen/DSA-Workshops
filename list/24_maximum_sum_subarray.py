'''
arr = [1,2,3]
subarray are contiguous element picked from the array
subarray are: {1},{2},{3},{1,2},{2,3},{1,2,3}
note:here {1,3} is not subarray Bcaz 1,3 is not contigous



ip: l = [1,2,3]
op: 6

ip:[1,2,3,4]
op: 10

note:Note if we have all +ve elements, sum of all element. if it has -ve element there will be no sum()
'''

#ip: l = [2,3,-8,7,-1,2,3]
#Kadane Algorithms
'''
* travers elment from left to right for every element find the maximum sum of sub array 
'''
#Kadane Alogrithm to solve sum of subarray
def maxSum(arr,n):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1,n):
        maxEnding = max(maxEnding + arr[i],arr[i])
        res = max(maxEnding, res)
    return res
    
# arr = [1,-2,3,-1,2]
arr = [-3,8,-2,4,-5,6]
n = len(arr)
print(maxSum(arr,n))
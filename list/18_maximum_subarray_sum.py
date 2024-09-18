#Maxium subarray sum
'''
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''
# arr = [5,4,-1,7,8]
# arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [1]
res = arr[0]#5->9->9->15->23
maxSum = arr[0]#5->9->8->15->23
for i in range(1,len(arr)):
    maxSum = max(maxSum+arr[i],arr[i])
    res = max(maxSum,res)
print(res)

#https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        res = nums[0]
        maxSum = nums[0]
        for i in range(1,len(nums)):
            maxSum = max(maxSum+nums[i],nums[i])
            res = max(maxSum,res)
        return res
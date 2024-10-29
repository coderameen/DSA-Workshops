def findPeakElement(nums):
    return nums.index(max(nums))

nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))
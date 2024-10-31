# def first_last6(nums):
#   n = len(nums)
#   if n >=1:
#     if nums[0]==6 or nums[-1]==6:
#       return True
#   return False
  
  
  
#2
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return True
  return False
    
#3
def make_pi():
  return [3,1,4]


#4
def common_end(a, b):
  if len(a)>=1 and len(b)>=1:
    if a[0]==b[0] or a[-1]==b[-1]:
      return True
      
  return False

#5
def sum3(nums):
  return sum(nums)
    
#6
def rotate_left3(nums):
  l = []
  n = len(nums)
  first_ele = nums[0]
  for i in range(1,n):
    l.append(nums[i])
  l.append(first_ele)
  return l


#7
def reverse3(nums):
  nums.reverse()
  return nums


#8
def max_end3(nums):
  lg_elen = max(nums[0],nums[-1])
  n = len(nums)
  return n * [lg_elen]


#9
def sum2(nums):
  if len(nums) ==0:
    return 0
  if len(nums) == 1:
    return nums[0]
  if len(nums)>=2:
    return nums[0] + nums[1]


#10
def middle_way(a, b):
  return [a[1],b[1]]

#11
def make_ends(nums):
  return [nums[0],nums[-1]]

#12
def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False

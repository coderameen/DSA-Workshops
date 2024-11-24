#Pair with given sum in unsorted/sorted Array, subsequence of array
'''
input:
arr = [3,2,8,15,-8]
sum = 17
output:
True (Bcoz 2+15=17)


input:
arr = [2,1,6,3]
sum = 6
output:
False

input:
arr = [5,8,-3,6]
sum = 3
output:
True (-3+6= 3)


#NOTE NOTE NOTE(arr = [1,3,5,8,9]) the two pointer not works as well as variable sliding window. 
Two pointer Approach(sorted array) works only summing the subarray(not pair elments)
variable sliding window is also used to find sum of subarray (not pair elment)
#example: arr = [1,3,5,8,9]

#NOTE summing the pair elments?(use below code/Technique)
'''

def pairWithSum(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                return True
    return False



# arr = [3,2,8,15,-8]
# sum = 17

arr = [2,1,6,3]
sum = 6
print(pairWithSum(arr,sum))
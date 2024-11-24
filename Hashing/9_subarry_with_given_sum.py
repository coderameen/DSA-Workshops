#subarray with given sum, true if sum is equal to given sum
'''
input:
arr = [1,4,20,3,10,5]
sum 33
output:
True
(20+3+10=33)

'''
#naive approach
def subarrySum(arr,sum):
    for i in range(len(arr)):
        curr =0
        for j in range(i,len(arr)):
            curr += arr[j]
            if curr == sum:
                return True
    return False


arr = [1,4,20,3,10,5]
sum = 33
print(subarrySum(arr,sum))



#Variable window sliding technique
def isSubSum(arr,sum):
    s,curr = 0,0
    for e in range(len(arr)):
        curr += arr[e]
        while curr > sum:
            curr -= arr[s]
            s+= 1
        if curr == sum:
            return True
    return False
    
arr = [1,4,20,3,10,5]
sum = 33
print(isSubSum(arr,sum))

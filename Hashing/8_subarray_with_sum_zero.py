#Subarray with 0 sum(Note subarray means contigeous elments) using has
'''

arr = {1,2,3} here subarray=>{1},{2},{3},{1,2},{1,2,3},{2,3}

input:
arr = [1,4,13,-3,-10,5]
output:
True (because)



ijnput:
arr = [-1,4,-3,5,1]
output:
True (-1+4-3=0)

input:
arr = [5,6,0,8]
output:
True
'''

def isZeroSum(l):
    prefix_sum = 0
    hs = set()
    
    for i in range(len(l)):
        prefix_sum += l[i]

        if prefix_sum == 0 or prefix_sum in hs:
            return True
        hs.add(prefix_sum)
    return False    
    
# l = [1,4,13,-3,-10,5]
l = [10,55,67,34]
print(isZeroSum(l))

#naive approach
print("--------")
def isSubSum(arr,sum):
    for i in range(len(arr)):
        curr = 0
        for j in range(i,len(arr)):
            curr += arr[j]
            if curr == sum:
                return True
            
    return False


# arr = [1,4,13,-3,-10,5]
arr = [10,55,67,34]
print(isSubSum(arr,sum=0))
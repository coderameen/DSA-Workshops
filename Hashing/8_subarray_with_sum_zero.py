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

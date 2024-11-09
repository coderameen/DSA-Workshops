l =[2,3,10,6,4,8,1]
s_ele = min(l)
l_ele = max(l)
print(l_ele - s_ele)


#constrain: arr[j] - arr[i], such that j>i
'''
l =[2,3,10,6,4,8,1]
op: 8 (10-2)



ip:[7,9,5,6,3,2]
op:2 (9-7)


l = [30,10,8,2]
op: -2 (8-10)
'''

def maxDiff(l,n):
    res = l[1] - l[0] 
    for i in range(0,n-1):
        for j in range(i+1,n):
            res = max(res, l[j] - l[i])
    return res
# l = [2,3,10,6,4,8,1]
# l = [30,10,8,2]
l = [7,9,5,6,3,2]
n = len(l)
print(maxDiff(l,n))
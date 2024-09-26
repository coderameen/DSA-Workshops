'''
ip
arr = [2,5,8,12,30]
x = 17
op: True //pair in (5,12)


ip:
arr = [3,8,13,18]
x = 14
op: False
'''

#Basic approach
def sumPair(arr,x):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] + arr[j] == x:
                return True
    return False
arr = [2,5,8,12,30]
# x = 17
# x = 55
x = 42
# print(sumPair(arr,x))

#Two pointer approach
#always for sorted array
'''
arr[s] + arr[e] == x: return True
arr[s] + arr[e] < x: s= s+1
else: e = e-1
'''

def sumPair2(arr,x):
    s = 0
    e = len(arr) - 1
    while s<e:
        if arr[s] + arr[e] == x:
            return True
        elif arr[s] + arr[e] < x:
            s = s + 1
        else:
            e = e - 1
    return False
        


arr = [2,5,8,12,30]
# x = 17
# x = 20
x = 66

print(sumPair2(arr,x))
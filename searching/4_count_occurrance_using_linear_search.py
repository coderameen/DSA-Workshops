'''
arr = [10,20,20,20,30,30]
x = 20
op: 3
using linear_search
'''

def countOccurr(arr,x):
    cnt = 0
    for i in range(0,len(arr)):
        if arr[i] == x:
            cnt += 1
    return cnt
    
arr = [10,20,20,20,20,20,20,20,30,30]
x = 30
print(countOccurr(arr,x))
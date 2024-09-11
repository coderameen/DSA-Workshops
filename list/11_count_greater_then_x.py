#Find the count of number if its given items are greater then x

'''
n = 5
[4,5,3,1,2]
x = 3

op:2
'''

def greaterThenX(arr,x):
    cnt = 0
    for i in arr:
        if i > x:
            cnt += 1
    return cnt

arr = [4,5,3,1,2]
x = 3
print(greaterThenX(arr,x))
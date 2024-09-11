'''
arr = [1,1,2,2,3,3,4,4,4,4,5]
n = 11
x = 4, y = 5


op: 4 Bcoz occurrence of 4 is greater then 5
'''
def majorityWins(arr,x,y):
    x_count = arr.count(x)#4
    y_count = arr.count(y)#1
    if x_count > y_count:
        return x
    else:
        return y
    
arr = [1,1,2,2,3,3,4,4,4,4,5]
x = 4
y = 5
print(majorityWins(arr,x,y))

'''
Naive Approach: 
arr = [1,1,2,2,3,3,4,4,4,4,5]
x = 4
y = 5
x_cnt = 0
y_cnt = 0
for i in arr:
    if i == x:
        x_cnt += 1
    if i == y:
        y_cnt += 1

if x_cnt > y_cnt:
    print(x)
else:
    print(y)

'''
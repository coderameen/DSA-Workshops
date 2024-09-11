#Count the total items smaller then 'x' in a array

# ip:arr = [4,5,3,1,2]
# x = 3

# op: 2

def smallerThanX(arr,n,x):
    cnt = 0
    for i in arr:
        if i < x:
            cnt += 1
    return cnt



arr = [4,5,3,1,2]
n = len(arr)
x = 3
print(smallerThanX(arr,n,x))#2Bcoz 1 and 2 are less then x, hence count is 2
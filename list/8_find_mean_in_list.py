#Finding the mean of a list

def mean(arr,n):
    if n >= 2:# with >= 2size array only we can find mean
        mymean = sum(arr)/n
        return int(mymean)


arr = [10,20,30,40]
n = len(arr)

print(mean(arr,n))
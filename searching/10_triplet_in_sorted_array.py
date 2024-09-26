'''
ip: arr = [2,3,4,8,9,20,40]
x = 32
op: True //Triplet is (4,8,20)


ip: arr = [1,2,5,6]
x = 14
op: False
'''


#Basic approach
def sumTriplet(arr,x):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k]== x:
                    return True
    return False
arr = [2,3,4,8,9,20,40]
x = 32


print(sumTriplet(arr,x))
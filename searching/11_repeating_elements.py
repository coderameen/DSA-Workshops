'''

ip:
arr = [0,1,2,2,2,3]
op: 2


ip = [11,22,33,33,33,44]
op: 33
'''
def repeatElement(arr,n):
    for i in range(0,n-1):
        if arr[i] == arr[i+1]:
            return arr[i]
    return -1

# arr = [0,1,2,2,2,3]
# arr = [11,22,33,33,33,44]

arr = [1,2,3,4,5]
n = len(arr)
# print(repeatElement(arr,n))


print("-----")
#efficient way
#visited = [False,False,False,,False,False,False]
def repeat(arr,n):
    visited = [False] * n
    for i in range(n):
        if visited[arr[i]]:
            return arr[i]
        visited[arr[i]] = True

    return -1
arr = [0,1,2,2,2,3]
n = len(arr)
print(repeat(arr,n))
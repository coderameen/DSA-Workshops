# ip: [1,0,0,0,1,1,1]
# op: [0,0,0,1,1,1,1]

# ip:[0,0,0,0,1,0,1,0,0]
# op:[0,0,0,0,0,0,0,1,1]

def arrangezeorOne(arr):
    zeroArr = []
    oneArr = []
    for i in range(0,len(arr)):
        if arr[i]==0:
            zeroArr.append(arr[i])
        else:
            oneArr.append(arr[i])
            
    return zeroArr + oneArr

# arr = [1,0,0,0,1,1,1]
arr = [0,0,0,0,1,0,1,0,0]
print(arrangezeorOne(arr))
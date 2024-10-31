arr = [5,9,2,1]
n = len(arr)

for i in range(n):
    breakpoint()
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
print(arr)

'''
1st swap = [5,9,2,1]
2nd swap = [5,2,9,1]
3rd swap = [5,2,1,9]
'''
# ip:
# arr = [1,2,4,5]
# n = 5

# op: 3

# arr= [1,2,5,3,6]
# n = 6
# op:4
def find_missing_number(n,arr):
    total_sum =  n * (n+1)//2 #15
    arr_sum = sum(arr)#12
    res = total_sum - arr_sum
    return res

# arr = [1,2,4,5]
arr= [1,2,5,3,6]
n = 6
print(find_missing_number(n,arr))


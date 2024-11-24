

# arr = [1,3,5,8,9]
# #sorted array
# sum = 16
# #output: True
# def twoPointer(arr,sum):
#     s = 0
#     e = len(arr) - 1
#     breakpoint()
#     while s<e:
#         if arr[s] +arr[e] == sum:
#             return True
#         elif arr[s] + arr[e] < sum:
#             s += 1
#         else:
#             e -= 1
#     return False
    

# arr = [1,3,5,8,9]
# sum = 11
# print(twoPointer(arr,sum))

#sum of subarray
#pair
# def myfun(arr,sum):
#     s,curr_sum = 0,0
#     for e in range(len(arr)):
#         curr_sum += arr[e]
#         while curr_sum > sum:
#             curr_sum -= arr[s]
#             s+= 1
#         if curr_sum == sum:
#             return True
#     return False
    
# arr = [1,3,5,8,9]
# sum = 16
# print(myfun(arr,sum))


# def myfun(arr,sum):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == sum:
#                 return True
#     return False

# arr = [1,3,5,8,9]
# sum = 16
# print(myfun(arr,sum))



# not a subarray
def mywork(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j]== 0:
                return True
    return False
arr = [1,3,-10,5,-3]

print(mywork(arr))
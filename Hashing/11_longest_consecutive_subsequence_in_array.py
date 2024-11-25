#Longest Consecutive Subsequence:
'''
We need to find longest consecutive subsequence in the form of x,x+1,x+2,x+3........x+i with these elment appearing in any order
ex: 3,4,5,6,7 or -1,0,1 or 11,14,13,12 (Any Order)


input:
arr = [1,9,3,4,2,20]
output: 4 (BCOZ,WKT here 1,2,3,4 are the longest consecutive subsequence in arr)


input: arr:[8,20,7,30]
output: 2 (BOZ, 7,8 are longest consecutive subsequence)

input: arr = [20,30,40]
output: 1 (BOZ none are in consecutive subsequence, here Indevidual element is only longest consecutive subsequence)



IDEA:
1. Sort the array
2.Traverse sorted array from left to right if we get element not in consecutive subsequence then update result accordingly.
'''
def findLongestSubsequence(arr):
    n=len(arr)
    arr.sort()
    res=1 
    curr=1 
    for i in range(1, n):
        if(arr[i]==arr[i-1]+1):
            curr+=1 
        else:
            res=max(res, curr)
            curr=1 
    res=max(res, curr)
    return res 
    

arr= [ 1, 9, 3, 4, 2, 10, 13]
print(findLongestSubsequence(arr))

arr = [5,9,2,1]
n = len(arr)

for i in range(n):
    findex = i
    for j in range(i+1,n):
        if arr[j] < arr[findex]:
            findex = j
    arr[findex],arr[i] = arr[i],arr[findex]
    
print(arr)
'''

3 steps for Selection Sort
Go Index by Index from starting to Ending
Find the fIndex.“fIndex is the index which contains right element for current Index.”
Swap fIndex with current Index.Ex: 5,9,2,1      ->1,2,5,9
TC: O(N*N) and SC:O(1)

'''
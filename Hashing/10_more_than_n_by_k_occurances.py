#More than n/k occurances
#Given a array of size n, given no k, we need to print all those elements whose count of occurances is more than n/k

'''
arr = [30,10,20,20,10,20,30,30],K= 4
n/k = 8/4= 2

output:
20 30
'''

#effectian approach - 1
def printNbyKOcc(arr,k):
    dp = {}
    n = len(arr)
    for i in arr:
        if i not in dp.keys():
            dp[i] = 1
        else:
            dp[i] += 1
            
    # return dp#{10: 4, 20: 2, 30: 1}
    l= []
    for kv,val in dp.items():
        if val > n//k:
            l.append(kv)
    return l


arr = [10,10,20,30,20,20,10,20,20,20]
k = 3
print(printNbyKOcc(arr,k))#[10]

print("---------------")
#efficiant approach - 2
#Counter: it is a dictionary mainly used to find frequencies/Occurance of the element in array
from collections import Counter
def printNbyK(arr,k):
    n = len(arr)
    c = Counter(arr)
    
    for x in c:
        if c[x] > n//k:
            print(x)


arr = [10,10,20,30,20,10,10]
k = 2
print(printNbyK(arr,k))
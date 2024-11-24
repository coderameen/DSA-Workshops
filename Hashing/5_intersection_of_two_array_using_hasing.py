#Intersection of two arrays using Hashing
'''
input:
arr1 = [10,15,20,5,30]
arr2 = [30,5,30,80]

output:
2 #Bcoz 5 and 30 are common element in two array

input:
arr1 = [10,20]
arr2 = [20,30]
output:
1 (wkt 20 is only common element)


input:
arr1 = [10,10,10]
arr2 = [10,10,10]
output:
1


logic:
idea
1. insert all elements of arr1 in set(hashset)
2.Travers L to R throguh arr2, serach for every element of arr2 in set. if present 1.incremetn count and remove same elment/item of arr2 form set(hashset).
'''

def intersectionHasing(arr1,arr2):
    us = set()#Hash set /unique set
    
    #1.insert all ementns of arr1[] in  us
    for i in range(len(arr1)):
        us.add(arr1[i])
    cnt = 0
    for i in range(len(arr2)):
        if arr2[i] in us:
            cnt += 1
            us.remove(arr2[i])
    
    return cnt
# arr1 = [10,15,20,5,30]
# arr2 = [30,5,30,80]


arr1 = [10,20]
arr2 = [20,30]
print(intersectionHasing(arr1,arr2))



#return intersection element instead of count
'''
arr1 = [10,20,10,12,40,50]
arr2 = [10,40,11,14]

output:
10 40
'''

def printIntersection(arr1,arr2):
    hs = set()#hashset
    
    for i in range(len(arr1)):
        hs.add(arr1[i])
    #hs = {,20,12,,50}
    l = []#10 40
    for i in range(len(arr2)):
        if arr2[i] in hs:
            l.append(arr2[i])
            hs.remove(arr2[i])
    return l

arr1 = [10,20,10,12,40,50]
arr2 = [10,40,11,14]
print(printIntersection(arr1,arr2))#[10, 40]
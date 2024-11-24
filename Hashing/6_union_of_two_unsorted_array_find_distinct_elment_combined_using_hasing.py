#Union of Two unsorted array. find distinct elment combined
'''
input:
a = [15,20,5,15]
b = [15,15,15,20,10]
output:
4 (Bcoz, )[15,20,5,15,15,15,15,20,10] => unique elment [15,20,5,10] hence count 4



input:
a = [10,12,15]
b = [18,12]
output:
4 #Boc [10,12,15,18]


input
a = [3,3,3]
b = [3,3]
ouput:
1

idea:
1. add arr1 elments in set
2.again, add arr2 element in same set
3. return the lentgth of that set(wkt, set hold only the distince elment)
'''

def unionSize(arr1,arr2):
    us = set()#hashset
    
    for i in range(len(arr1)):
        us.add(arr1[i])
        
    for i in range(len(arr2)):
        us.add(arr2[i])

    return len(us)

arr1 = [15,20,5,15]
arr2 = [15,15,15,20,10]

print(unionSize(arr1,arr2))
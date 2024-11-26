#Check the equal array
'''
arr1 = [1,2,5,4,0]
arr2 = [2,4,5,0,1]
output:
True

input:
arr1 = [1,2,5]
arr2 = [2,4,15]
output:
False
'''
def checkSameArray(arr1,arr2):
    arr1.sort()
    arr2.sort()
    return arr1 == arr2

# arr1 = [1,2,5]
# arr2 = [2,4,15]

arr1 = [1,2,5,4,0]
arr2 = [2,4,5,0,1]
print(checkSameArray(arr1,arr2))
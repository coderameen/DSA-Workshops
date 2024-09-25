'''

LINEAR SEARCHING TECHINQUE



ip : arr = [10,20,30,40,40,50]
x = 30
op: 2 (index position of 30)


ip : arr = [10,20,30,40]
x = 55
op : -1
'''
def linearSearch(arr,n,x):
    for i in range(0,n):
        if arr[i] == x:
            return i
        
    return -1
    

# arr = [10,20,30,40,40,50]
arr = [10,20,30,40]
n = len(arr)
x = 33
print(linearSearch(arr,n,x))

#[10,20,30,40,40,50] here we have 6 elements
#Assume [10.........] ,x which is not present - O(n)
#its is only stable for small elements

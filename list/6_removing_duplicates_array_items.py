#Remove the duplicates from sorted array
# '''
# ip: [10,20,20,30,40,40,40]
# op: [10,20,30,40]

#ip: [10,10,10]
#op: [10]
# '''

#sol 1, temp array: to copy all distinct element  in it. then copy tem app to original array and return it
def removeDuplicates(arr, n):
    temp = [0]*n
    temp[0] = arr[0]#Bcoz 1st element is always distinct
    res = 1#2->3 -> 4
    myarr = []
    for i in range(1,n):
        if temp[res-1] != arr[i]:
            temp[res] = arr[i]
            res += 1
    #temp -> [10, 20, 30, 40, 0, 0, 0]
    for i in temp:
        if i != 0:
            myarr.append(i)
    
    return myarr
        

arr = [10,20,20,30,40,40,40]
n = len(arr)
print(removeDuplicates(arr, n))


#temp [10,0,0,0,0,0]
#temp [10,20,0,0,0,0]
arr = [8,7,6,2,1,9]

#.sort(), it modify existing array
# arr.sort()
# print(arr)

#.sort() only works for list/array

#
arr1 = sorted(arr)# new array crate
print(arr1)




myarr = [[1,4],[1,3],[9,5],[2,0],[6,4]]
# myarr.sort()#sort based on 0st index
# print(myarr)



myarr.sort(key=lambda x:x[1])
print(myarr)

'''
input
mat = [[1,10,20],[15,25,35],[5,30,40]]

oput:
20


idea:
1.convert matrix into array
2.sort the array
3.find the midean of sorted array
'''

def medianMat(mat):
    R = len(mat)
    C = len(mat[0])
    l = []
    #1. convert matrix to list/array
    for i in range(R):
        for j in  range(C):
            l.append(mat[i][j])
    #2.sort the array
    l = sorted(l)

    s = 0
    e = len(l)
    mid = (s+e)//2
    return l[mid]

mat = [[1,10,20],[15,25,35],[5,30,40]]
print(medianMat(mat))#2



#method 2
def medianMat2(mat):
    R = len(mat)
    C = len(mat[0])
    l = []
    #1. convert matrix to list/array
    for i in range(R):
        for j in  range(C):
            l.append(mat[i][j])
    #2.sort the array
    l = sorted(l)

    #3.find mid in sorted array
    from statistics import median
    return median(l)

mat = [[1,10,20],[15,25,35],[5,30,40]]
print(medianMat2(mat))#2

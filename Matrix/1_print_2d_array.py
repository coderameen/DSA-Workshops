#Multidimentional Array => Matrix
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

R = len(mat)
C = len(mat[0])
for i in range(R):
    for j in range(C):
        print(mat[i][j], end=" ")
    print()
    
'''
output:
1 2 3 
4 5 6 
7 8 9 
'''

#(3,3) with O initize
arr  = [[0]*3 for _ in range(3)]
print(arr)#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]


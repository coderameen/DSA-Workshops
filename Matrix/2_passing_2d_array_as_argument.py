'''
input:
mat = [[10,20],[30,40],[50,60]]
output:
10 20 30 40 50
'''
def printMatrix(mat):
    R = len(mat)
    C = len(mat[0])
    
    for i in range(R):
        for j in range(C):
            print(mat[i][j], end=" ")

mat = [[10,20],[30,40],[50,60]]
printMatrix(mat)
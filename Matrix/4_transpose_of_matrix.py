#Transpose of matrix
'''
input
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
output:
[[1,4,7],[2,5,8],[3,6,9]]


input:
mat = [[1,2],[1,2]]
otput
[[1,1],[2,2]]
'''

def transpose(mat):
    R = len(mat)
    C = len(mat[0])
    #temp Oth mat
    temp = [[0]*C for _ in range(R)]#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    #transpose the matrix
    for i in range(R):
        for j in range(C):
            temp[i][j] = mat[j][i]#transpose
            
    #copy temp array to original array
    for i in range(R):
        for j in range(C):
            mat[i][j] = temp[i][j]
            
    return mat

# mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2],[1,2]]
print(transpose(mat))
'''
[[1,3,11],
 [4,5,66]]
'''
matrix = [[1,3,11],[4,5,66]]
#total number of rows and columns
rows = len(matrix)
columns = len(matrix[0])
print(rows)
print(columns)

#Traverse 2D array
matrix = [[1,3,11],[4,0,66],[101,102,103]]
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
    


matrix = [[1,3,11],[4,0,66],[101,102,103]]
#total number of rows and columns
m = len(matrix)#no of rows
n = len(matrix[0])#no of columns

rows = [False] * m#[False, False, False]
cols = [False] * n#[False, False, False]


#ProgramL: https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        #no of rows and columns
        m = len(matrix)
        n = len(matrix[0])
        #init False for row and column array
        row = [False] * m
        col = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] == True or col[j] == True:
                    matrix[i][j] = 0

        return matrix


        
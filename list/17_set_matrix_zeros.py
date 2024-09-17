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

rows = [False] * m
print(rows)
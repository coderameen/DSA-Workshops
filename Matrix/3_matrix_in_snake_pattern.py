'''
input:
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
out:
1 2 3 4 8 7 6 5 9 10 11 12

'''
def printSnakePattern(mat):
    R = len(mat)
    C = len(mat[0])#4

    for i in range(R):
        if i%2 == 0:
            #print from left to right
            for j in range(C):
                print(mat[i][j], end= " ")
        else:
            #print from right to left
            for j in range(C-1,-1,-1):
                print(mat[i][j], end=" ")

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
printSnakePattern(mat)
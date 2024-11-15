'''
input:
mat = [[10,20,30],[40,50,60]]
x = 50
output:
(1,1) fount



input:
mat = [[10,20],[30,40]]
x = 55
oput:
Not found
'''
def search(mat,x):
    R = len(mat)
    C = len(mat[0])
    for i in range(R):
        for j in range(C):
            if mat[i][j] == x:
                return (i,j)

    return "not found"


mat = [[10,20,30],[40,50,60]]
x = 20
print(search(mat,x))
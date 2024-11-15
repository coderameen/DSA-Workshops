'''
input:
A = [[1,2,3],[4,5,6]]
B = [[1,3,3],[2,3,3]]

output
[[2,5,6],[6,8,9]]
'''
def sumMatrix(A,B):
    n1,m1 = len(A),len(A[0])
    n2,m2 = len(B),len(B[0])
    
    if n1!=n2 or m1 != m2:
        return []
    
    #temp of 0 element
    res =  [[0]*m1 for _ in range(n1)]
    
    #adding A and B
    for i in range(n1):
        for j in range(m1):
            res[i][j] = A[i][j] + B[i][j]
            
    return res




A = [[1,2,3],[4,5,6]]
B = [[1,3,3],[2,3,3]]

print(sumMatrix(A,B))#[[2, 5, 6], [6, 8, 9]]
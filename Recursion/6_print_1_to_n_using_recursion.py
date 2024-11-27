'''
ip: 4
op:1 2 3 4

ip:n=5
op 1 2 3 4 5
'''
def fun(n):
    if n==0:
        return
    
    fun(n-1)
    print(n)

fun(3)
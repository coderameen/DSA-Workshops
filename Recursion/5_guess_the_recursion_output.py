def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    print(n)
fun(3)

#output:
'''
3
2
1
1
2
3
'''
print("--------------------")

#2
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
    fun(n-1)
    
fun(2)
'''
output:
1
2
1

'''
print("----------------")
def fun(n):
    if n<=1:
        return 0
    return 1 + fun(n/2)
print(fun(16))#4


print("---------------")
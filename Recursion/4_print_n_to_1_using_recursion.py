#Print number from n to 1
def fun(n):
    #base condition
    if n ==0:
        return
    print(n, end=" ")
    fun(n-1)

fun(5)
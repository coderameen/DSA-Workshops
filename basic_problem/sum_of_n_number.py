#Sum of first n natural number for given input 'n'
#i/p: n=3, o/p: 6 (1+2+3)
#i/p: n=5, o/p: 15

#Sol 1
def mysum1(n):
    return n*(n+1)/2
# print(mysum1(5))

#Sol 2
def mysum2(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# print(mysum2(10))


#sol 3:
def mysum3(n):
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum +=1
    return sum

print(mysum3(10))



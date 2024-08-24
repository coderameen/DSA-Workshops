#Prime number: a number which is divisible only by 1 and the number itself
#first few prime: 2,3,5,6,11,13....
#i/p n=13 op:Yes
#ip: n=14 op:No
#NOTE: 2 is only even prime number
#NOTE: 1 IS CONSIDER neighter prime nor composite number
#Note: All non-prime numbers are said to be composite number.
#n = 13 (2........12)
def myPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True
print(myPrime(14))
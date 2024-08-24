#Given number is same when we read left to right or right to left for all n >=0
#i/p: n=78987 o/p: Yes
#i/p: n= 45 o/p:No
#i/p: n= 7 o/p:Yes


#logic
# n=93245
n = 78987
rev = 0
orgn = n
while n>0:
    last_digit = n%10
    rev = rev*10 + last_digit
    n = n//10
# print(rev)
if rev == orgn:
    print("Yes")
else:
    print("No")
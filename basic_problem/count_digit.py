#Given a number, count number of digit in the number 'n'
#i/p: n= 97343  o/p: 5
#ip: n=98 o/p: 2
#i/p: n=1 o/p:1

#brute force approach
n = 98754
cnt = 0
for i in str(n):
    cnt+=1
# print(cnt)

#efficient approach

n = 9872388
cnt = 0
while n > 0:
    n = n//10
    cnt += 1
    
print(cnt)
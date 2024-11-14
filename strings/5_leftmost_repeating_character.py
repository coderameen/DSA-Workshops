'''
input:
s1 = "abbcc"
oput:
1   (bcoz b is the first repeating char whose index is 1)


iput:
s1 = "abcd"
output:
-1


iput:
s1 = "acddz"
oput:
2 (Bcoz d is a repeating char. whose index is 2)

'''


def leftmostRepeatingChar(s1):
    for i in range(len(s1)):
        for j in range(i+1,len(s1)):
            if s1[i] == s1[j]:
                return i
            
    return -1

# s1= "abccd"
# print(leftmostRepeatingChar(s1))#2

s1= "sadrffz"
print(leftmostRepeatingChar(s1))#4
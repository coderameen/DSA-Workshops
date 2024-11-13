'''
s1 = "abba"
op:true

s2 = "aviva"
op:true

s3 = "abcd"
op:false

'''
#direct aproach
s1= "aviva"
l_s = s1[::-1]
print(s1 == l_s)


#
def revString(s):
    rev = ""
    for i in s:
        rev = i+rev
    return rev

def checkPaindrome(s):
    org_str = s
    rev_str = revString(s)
    if org_str == rev_str:
        return True
    else:
        return False
    
s = "malayalam"
print(checkPaindrome(s))

#Note the above takes O(N)

print("-----------------")
#optimal approach
st = "malayalam"
s = 0
e = len(st) - 1
while s < e:
    if st[s] != st[e]:
        print("False")
        break
    s += 1
    e -= 1
else:
    print("True")
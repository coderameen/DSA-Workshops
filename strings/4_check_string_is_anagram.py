#Anagram
'''
input
s1 = "listen"
s2 = "silent"

output:
True


input
s1 = "abccd"
s2 = "ac"

output:
False
'''

#Direct Approach
def areAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    s1 = sorted(s1)
    s2= sorted(s2)
    
    if s1 == s2:
        return True
    else:
        return False
    
s1 = "abaac"
# s2 = "acaba"#anagram
s2 = "ab"
print(areAnagram(s1,s2))


print("=================")
#Method 2
def areAnagram2(s1,s2):
    if len(s1) != len(s2):
        return False
    
    count = [0] * 256
    
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
        
    for x in count:
        if x != 0:
            return False
    return True


s1 = "abcd"
s2 = "abcd"
print(areAnagram2(s1,s2))
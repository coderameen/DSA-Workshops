#Check Sub Sequence of a string(left to right)
'''
IP: 
s1 = "ABCD"
s2 = "AD"

OP:True



ip: 
s1 = "ABCDE"
s2 = "AED"

op: No

'''
def issubseq(s1,s2):
    i,j =0,0
    while i<len(s1) and j<len(s2):
        if s1[i] == s2[j]:
            j+= 1
            
        i+=1
    if j == len(s2):
        return True 
    else:
        return False
    
s1 = "ABCDEF"
# s2 = "ADE"
s2 = "AED"

print(issubseq(s1,s2))


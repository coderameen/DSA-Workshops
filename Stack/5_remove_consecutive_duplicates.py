'''
input: aaaaaabaaacccbba
output: abacba



ip:
abbcbcdddd
op:
abcbcd
'''

def removeConsecutiveDuplicates(str):
    stack = []
    for ch in str:
        if not stack or ch != stack[-1]:
            stack.append(ch)
    # return stack
    return "".join(stack)
    
print(removeConsecutiveDuplicates("abbccaa"))#abca
#Given a string we need to find if the string contains balanced parenthesis or not (NOTE: ORDER)
#******** Amazone/Microsoft/Uber

'''
input:
str = "([])"
output:
True


input:
str = "((())"
output:
False


input:
str = "([)]"
output:
False


input:
str = "[[{(( ))}]]"
output:
True
'''
def isMatching(a,b):
    if (a=='(' and b==')') or (a=='[' and b==']') or (a=='{' and b=='}'):
        return True
    else:
        return False
def isBalancedParenthesis(str):
    stack = []
    for x in str:
        if x in ['(','[','{']:
            stack.append(x)
        else:
            if not stack:
                return False
            if isMatching(stack[-1],x) == True:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    else:
        return True
        

# print(isBalancedParenthesis("([)]"))
print(isBalancedParenthesis("({{[()]}})"))


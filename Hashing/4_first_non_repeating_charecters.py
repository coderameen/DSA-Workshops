'''
s = "hello"
op: h


ip: zxvczbbxuzvy
op: c
'''
def firstNonRepeatingChar(s):
    dp = {}
    for i in s:
        if i in dp.keys():
            dp[i] += 1
        else:
            dp[i] = 1
            
    for k,v in dp.items():
        if v == 1:
            return k
    return -1
s = "hello"
print(firstNonRepeatingChar(s))
'''
dp = {'h':1,'e':1,'l':2,'o':1}

'''
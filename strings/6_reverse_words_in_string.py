'''
input:
s1 = "I love coding"
output:
coding love I



input:
s1 = "marriages are more in winter"
output:
winter in more are marriages

'''


s1 = "I love coding"
print(s1.split())#['I', 'love', 'coding']
print(s1.split()[::-1])#['coding', 'love', 'I']
#to convert list to string
print(' '.join(s1.split()[::-1]))
def revWordString(s1):
    reverse_string = ' '.join(s1.split()[::-1])
    return reverse_string

s1 = "me love coding mf"
print(revWordString(s1))

#or
def myfunc(s1):
    tolist = s1.split()
    revlist = tolist[::-1]
    listtostr = " ".join(revlist)
    return listtostr
s1 = "Helo all buddy!!"
print(myfunc(s1))
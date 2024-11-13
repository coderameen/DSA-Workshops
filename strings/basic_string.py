#to find ascii value of char
print(ord('a'))#97
print(ord('A'))#65

#ACII to char

print(chr(97))#a



s = "sanaan"
print(s)
print(type(s))#<class 'str'>

print(s[0])
print(s[1])
print(s[-1])


#strings are immutable
s = "hello"
# s[0] = 'f'
# print(s)

new_s =s[1:]
print('f'+new_s)#fello


#Escape sequence and row string
# s = 'Welcome to coderameen's dsa'
s = 'Welcome to coderameen\'s dsa'

print(s)


s = "Hi\nSanaan"
print(s)#\n behavious as new line


#formatted string in python
#1. using %
name = "ameen"
course = "dsa"
s = "Welcome to %s %s"%(name,course)
print(s)


#2.format()
name = "ameen"
course = "dsa"
s = "welcome to {0} {1}".format(name,course)
print(s)


#3.using f string
name = "ameen"
course = "dsa"
s = f"welcome to {name} {course}"
print(s)


#4.using +
s = "welcome to " + name +" "+ course
print(s)


#5. using ,
s = "welcome to ",name," ",course
print(s)


#string comparison in python
s1 = "sanaanhero"
s2 = "ameen"
print(s1<s2)
print(len(s1))
#<,<=,>=,==,!=

s1 = "sanaanhero"
print("sanaan" in s1)
def myfunc(s,gs):
    return gs in s
#check if given string is a substring of a string or not
#consititive substring of "ABCD" are "","A","B","c","D","AB","ABC","ABCD","BC","BCD","CD"
s = "mohammedsanaan"
gs = "sanaan"
print(myfunc(s,gs))


s1 = "md"
s2 = "sanaan"
print(s1+s2)

#find the position of substring
s1 = "mohammedsanaan"
s2 = "sanaan"
print(s1.index(s2))


s1 = "alen"
print(s1.upper())
#validate
print(s1.islower())
s1 = "HELO ALBART"
print(s1.isupper())
print(s1.lower())
print(s1.capitalize())


#startswith() and endswith()
s = "mohammedsanaan"
print(s.startswith("mohammed"))
print(s.endswith("sanaan"))


URL = "http://localhost:5000"
if URL.startswith("http"):
    print("ITS VALID URL")
else:
    print("In valid")
    
    
#split() and join()
s1 = "I am sanaan"
#split() is converting in form of list
print(s1.split())#['I', 'am', 'sanaan']

s2 = "I, am,ameen"
print(s1.split(","))#['I am sanaan']


#list -> string
l = ["I","am","a","coder"]
print(" ".join(l))#I am a coder
print(",".join(l))#I,am,a,coder

#find()
s1 = "ameen is a coder"
x = "coder"
print(s1.find(x))#11 index
print(s1.find("trader"))#-1
print(s1.index(x))#11 index
# print(s1.index("trader"))#error

#note: its better to use find instead of index. as index return error if given string not present in string. but find return -1 



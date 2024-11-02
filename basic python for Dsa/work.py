#Type of commands
#1. single line command '#'
#2. Multi line command ''' ''' or """ """
'''
This is
mulit 
lihne
command
'''
"""
sjkdjf
sdjklsd
sdl.
"""

#input
# n = input()
# n = input("Enter a number: ")
# print(type(n))#<class 'str'>

# n = int(input("Enter a number: "))
# print(type(n))#<class 'int'>


#print in python

# print("Hello world")

# print("Hello world ","Prajwal")


# print("Hi", end="-")
# print("Sanaan")


# print(5+7)
# print("5+7")
# print("5"+"7")



# name = "Ameen"
# age = 27
# #type of print
# print("The name is ",name, " The age is ",age)
# print(f"The name is {name} and age is {age}")#f => formated string
# print("The name is {} and age is {}".format(name,age))
# print("The name is {1} and age is {0}".format(age,name))


#Data types
'''
int ex: 33
float ex: 3.23422
bool ex: True/False
complex(X)
list : [10,20,30,40...]
tuple : (10,20,30,40,...)
dictionary: {'Apple':2,'Mango':5}
set: {10,20,30}
string :"prajwal"
None :empty
range

'''

r = range(1,10)
print(type(r))


a = 34
print(type(a))

b =4.232
print(type(b))

isStudent = False
print(type(isStudent))

l = [10,20,30]
print(type(l))

t = (10,20,30)
print(type(t))

s = set()
s = {10,20,30}
print(type(s))

d = {'a':10,'b':20}
print(type(d))


#Type casting/Type conversion

#list -> tuple
l = [1,2,3,4,5]
t =tuple(l)
print(t)


#tuple -> list
t = (1,2,3)
l = list(t)
print(l)


#string -> list
s = "Ameen hasan"
l = list(s)
print(l)

#array vs list
#arr collection of similar elements, static and dynamic sizing
#list mixed elments, dynamic sizing


#list -> string(challenging)
l = ['hi','I','am','prajwal']
res = " ".join(l)
print(res)
print(type(res))#<class 'str'>


#list -> set
#NOTE: Set is a collection of unique element in unordered fashion
l = [1,2,2,3,3,3,3,3,4,4,5,5,6]
s = set(l)
print(s)#{1, 2, 3, 4, 5, 6}

#Q: print only unique element from an array




#MUTABLE Vs IMMUTABLE
#1.int is immutable
a = 10
print(a, id(a))
a = 69
print(a, id(a))
#NOTE: don't think its changing value in a, but another a is present at different memory location



#2.Bool is immutable
a = True
print(a, id(a))
a = False
print(a, id(a))
'''
IMMUTABLE: int, bool, string, tuple, set
MUTABLE: list, dictionary
'''

#3. set are immutable
s = {10,30,40}
print(s, id(s))
s = {10}
print(s, id(s))


#4. list are mutable
l = [1,2,3,4]
print(l, id(l))
l[0] = 1000
print(l, id(l))

#NOTE: CHANGES in same memory location


#5. string are immutable
s = "Hello"
#o/p: Jello
# s[0] = 'J'
# print(s)#we can't change as its an immutable

res = 'J'+s[1:]
print(res)

# res,res2 = 'J',s[1:]
# print(res+res2)#Jello

# a,b = 10,20
# print(a)
# print(b)


arr = [10,20,20,20,30,40]
#count number of occcurance of 20
print(arr.count(20))#3
#now, remote repiting elments from the array
# arr.remove(20)
# arr.remove(20)
# arr.remove(20)
# print(arr)


n =arr.count(20)
for i in range(n):
    arr.remove(20)
    
print("res: ",arr)



#list -> dictionary
#{key:value, key:value, key:value}

l1= ['a','b','c']
l2 =[10,20,30]

res = dict(zip(l1,l2))#{'a': 10, 'b': 20, 'c': 30}
print(res)
#note: to convert we required list to dictionary we need at least 2 list


#dict -> list
#ip: {'a': 10, 'b': 20, 'c': 30}
#op: l1= ['a','b','c']
# l2 =[10,20,30]

d = {'a': 10, 'b': 20, 'c': 30}
print(d.keys())#dict_keys(['a', 'b', 'c'])
print(d.values())#dict_values([10, 20, 30])
print(d.items())#dict_items([('a', 10), ('b', 20), ('c', 30)])

print(list(d.keys()))#['a', 'b', 'c']
print(list(d.values()))#[10, 20, 30]


#length, len()
l = [10,20,30,40]
print(len(l))
cnt = 0
for i in l:
    cnt += 1
    
print(cnt)


#Statements
'''
1.conditional
2.uncoditional
3.iterative
'''
#1.conditonal statements
marks = 77
if marks > 80:
    print("First Div")
elif marks >=60 and marks <80:
    print("Sec Div")
    
else:
    print("Fail")


#even or odd for given number
# n = int(input())
n = 23
if n%2 == 0:
    print("even")
else:
    print("odd")
    

print(7+5)#12
print(7%5)#2
print(7/5) # 1.4
print(7//5) #1
import math
print(math.ceil(7/5))#2
print(math.floor(7/5))#1


#iterative statemen/Looping statement
#print "sanaan" n times
# n = int(input())
n = 3
while n>0:
    print("Sanaan")
    n -= 1
    
    
#for: for x in sequence

l = [10,20,30,40]
for i in l:
    print(i, end=" ")
    


print()#new line
for i in range(1,10):
    print(i, end=" ")
    
print()
for i in range(10):
    print(i, end=" ")

print()
#step in range
for i in range(1,10,2):
    print(i)
    
print()
#odd or even
for i in range(11):
    if i%2!=0:
        print(i, end=" ")


print("--------")
#question
l = [4,5,7,8]
'''
op:
0 4
1 5
2 7
3 8
'''

n = len(l)
for i in range(n):
    print(i, l[i])

l = [4,5,7,8]
#enumeration
print(list(enumerate(l)))#[(0, 4), (1, 5), (2, 7), (3, 8)]

for i,items in enumerate(l):
    print(i,items)
    
    
#function vs methods

def mysum(a,b):
    return a+b
res = mysum(10,40)
print("The result is : ",res)

#default argument
def mysum(a,b,c=100):
    return a+b+c
print(mysum(10,20,50))


#multi argument
def mysum(*tup):
    # print(sum(tup))
    # print(list(tup))
    return sum(tup)
    
    
res = mysum(10,20,30,50,70,70,80,90,100)
print(res)


#change the item in list, write a function
l = [1,2,3,4,5,6]
# i = 2
# ele = 300
# l[i] = 300
# print(l)


l = [1,2,3,4,5,6]
def changer(i,ele,l):
    l[i] = ele

changer(0,100,l)
print(l)
print(*l)



#note, int is a immutable
x = 20#int
def changer(x):
    x = 100000
    return x

print(changer(x))
print(x)


#error handling
try:
    x = 3/0
    print(x)
except:
    print("Error bhai!!")
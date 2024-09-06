#accessing items
l = [10,20,30,40,50]
print(l)
print(type(l))
print(l[2])#30
print(l[-1])#50
print(l[-2])#40


#To add elements
l = [10,20,30]
l.append(35)
l.insert(1,15)#insert(pos,item)
print(l)#[10, 15, 20, 30, 35]
l.extend([77,88])
print(l)#[10, 15, 20, 30, 35, 77, 88]


#To find the occurrence of element
l = [10,20,30,20,20,30,40,50]
print(l.count(20))#.count(element)#3
print(l.count(30))#2


ele = 20
cnt = 0
for i in l:
    if i == ele:
        cnt+=1
        
print(cnt)
#NOTE: O(n) Bcoz n is the size of number of element, for loop


#Removing the element from list
l = [10, 15, 20, 30, 35, 77, 88]
l.remove(20)
print(l)
l.pop()
print(l)
# del l
# print(l)
l.pop(0) #pop(index)
print(l)


#general purpose function in list
l = [10,40,20,50]
print(max(l))#50
print(min(l))#10
print(sum(l))#120
l.reverse()
print(l)#[50,20,40,10]
l.sort()
print(l)#[10,20,40,50]


#PROBLEM: Average or Mean of a list
# '''
# ip: l = [10,20,30,40]
# op: 25.0


#ip: l = [30,40,60]
#op: 43.33
# '''

#efficient approach
def average(l):
    return sum(l)/len(l)
l = [10,20,30,40]
print(average(l))#25.0

#Time complexity is: o(1) constant, space complexity is:  Aux(1)

#2nd Method
def avg2(l):
    sum = 0
    len_cnt = 0
    for i in l:
        sum += i
        len_cnt += 1
    return sum/len_cnt
        
l = [10,20,30,40]
print(avg2(l))#25.0

#Note: TC: O(n), SC:O(1)

#Q: Seperate Even and Odd, Given a list, we need to write a function and return two lists 1 contains all even items and 2nd list contains all odd items

'''
#ip: l = [10,41,30,15,80]
#op: even = [10,30,80]
#op: odd = [41,15]
'''
def getEvenOdd(l):
    even = []
    odd = []
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd
    
l = [10,41,30,15,80]    
even,odd=getEvenOdd(l)
print(even)
print(odd)


#Get smallest element from the given list, return all the smallest element from given element 'x' such taht return_element < x
'''
ip: l=[8,100,20,40,3,7], x= 10
op: [8,3,7]
'''
def getSmaller(l,x):
    res = []
    for i in l:
        if i < x:
            res.append(i)
    return res
l=[8,100,20,40,3,7]
x= 10
print(getSmaller(l,x))#[8, 3, 7]



#Largest Element in a list
# '''
# ip: l = [10,5,20,8]
# op: 20


#ip: l =[40]
#op:40

#ip: l = []
#op: None / 1 / 0
# '''



def myMax(l):
    if l == []:
        return None
    max = l[0]
    for i in l:
        if i > max:
           max = i
    return max

l = [10,5,20,8]
print(myMax(l))#20


#Second largest element in list
'''
ip: l = [10,5,8,20]
op: 10

ip:[10,10,10]
op: None
'''
#second largest
def getMax(l):
    res = l[0]
    for i in range(1,len(l)):
        res = max(res,l[i])
    return res

def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = getMax(l)
    seclar = None
    for x in l:
        if x != lar:
            if seclar == None:
                seclar = x
            else:
                seclar = max(seclar,x)
    return seclar                
l = [10,5,20,8]
print(getSecMax(l))#10
print("done")


#To check if a list is sorted or not
''''
ip: l = [10,20,30]
op: YES

ip:[10,20,20,30]
op: YES

ip: [10,30,20,30]
op: NO

'''

'''
logic:
i = 1: compare l[1] with l[0]
i = 2: compare l[2] with l[1]
i=3: compare l[3] with l[2]
'''


def isSorted(l):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            return False
    return True
l = [60,10,20,30,40]
print(isSorted(l))#False

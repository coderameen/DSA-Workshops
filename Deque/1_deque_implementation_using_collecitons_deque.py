#Implementation of deque using collections deque
from collections import deque
d = deque()
# print(d)

#insert rear 
d.append(10)
d.append(20)
d.append(30)
d.append(40)
print(d)

#insert front

d.appendleft(50)
d.appendleft(60)
print(d)#deque([60, 50, 10, 20, 30, 40])

#delete rare
d.pop()
print(d)

#delelete front
d.popleft()
print(d)

#length
print(len(d))

#getFront():return front item
if d:
    print(d[0])
    
    
#getRear: return the last item
if d:
    print(d[-1])
print("done")

#isemplty
if not d:
    print("Empty deque!!")
    
print(d)#deque([50, 10, 20, 30])
# print(list(d))#[50, 10, 20, 30]

#insert at given position .insert(pos,ele)
d.insert(2,10)
print(d)#deque([50, 10, 10, 20, 30])
d.insert(2,15)
print(d)#deque([50, 10, 15, 10, 20, 30])

#count occurance of element
print(d.count(10))#2

#remove in deque
d.remove(10)
print(d)#deque([50, 15, 10, 20, 30])

#extend at rear
d.extend([100,200])
print(d)#deque([50, 15, 10, 20, 30, 100, 200])
#extend at front
d.extendleft([1000,2000,3000])
print(d)#deque([3000, 2000, 1000, 50, 15, 10, 20, 30, 100, 200])


d.reverse()
print(d)#deque([200, 100, 30, 20, 10, 15, 50, 1000, 2000, 3000])


#indexing
print(d[5])#15
d[5] = 786
print(d)#deque([200, 100, 30, 20, 10, 786, 50, 1000, 2000, 3000])







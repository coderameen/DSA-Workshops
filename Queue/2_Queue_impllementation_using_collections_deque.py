from collections import deque

q = deque()#queue

#enque: insert at Rare end
q.append(10)
q.append(20)
q.append(30)
print(q)

#deque: remove item from front end
print(q.popleft())
print(*q)


#len
print(len(q))
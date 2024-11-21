#Implemenation of stack using collections library (deque)
#DEQUE: it is similar to Array in which for insertion we use append() and to delete we use pop()

from collections import deque
stack = deque()

#insert
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print(stack)#deque([10, 20, 30, 40, 50])
print(*stack)#10 20 30 40 50
print(list(stack))#[10, 20, 30, 40, 50]
#size of stack
size = len(stack)
print(size)

#peak of stack
top = stack[-1]
print(top)

#delete 
print(stack.pop())
print(stack.pop())
print(*stack)
print(len(stack))

#Note: insertion and deletion happens at O(1) time


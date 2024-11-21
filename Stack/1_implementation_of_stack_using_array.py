#Implementation of stack using array
#LIFO or FILO
stack = []

#insert item into stack
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
# print(stack)


#detetion of item in stack
print(stack.pop())
# print(stack.pop())
print(stack)


#peak item of stack
top = stack[-1]
print(top)


#size of stack
size = len(stack)
print(size)


print("------------------------------------------")
#my oun implementatin using array
class MyStack:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self,x):
        self.stack.append(x)
        self.size += 1
    
    def pop_stack(self):
        if stack:
            pop_ele = self.stack.pop()
            self.size -= 1
            return pop_ele
        else:
            return "Stack is Emplty!!"
        
        
    def peak(self):
        if stack:
            peak_ele = self.stack[-1]
            return peak_ele
        else:
            return "Stack is Emplty!!"
        
    def size_stack(self):
        return self.size
            
s = MyStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(60)
print(s.size_stack())
print(s.pop_stack())
print(s.pop_stack())
print(s.size_stack())
print(s.peak())


#INSERTINO DELTEINO HAPPENS IN O(1) time
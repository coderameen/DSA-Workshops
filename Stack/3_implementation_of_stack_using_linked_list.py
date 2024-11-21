#Implementatino of stack using Linked List
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0
        

    #insertBegin
    def push(self,x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        
        self.size += 1
        
    #deleteFirst
    def pop(self):
        if self.head == None:
            return None
        res = self.head.key
        #logic
        self.head = self.head.next
        
        self.size -= 1
        return res

    def size_stack(self):
        return self.size
        
    def peak(self):
        if self.head == None:
            return None
        return self.head.key
    
s = MyStack()
s.push(10)
s.push(20)
s.push(30)
print(s.size_stack())
print(s.pop())
print(s.size_stack())
print(s.peak())
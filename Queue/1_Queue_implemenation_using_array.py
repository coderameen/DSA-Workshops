#Implementation of Queue using Array

class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
    def enque(self,item):
        self.queue.append(item)
        self.size += 1
        
    def deque(self):
        if self.queue:
            self.size -= 1
            return self.queue.pop(0)
        else:
            return "Queue is Emplty!!"
        
    def queueSize(self):
        return self.size
    

q = Queue()
q.enque(10)
q.enque(20)
q.enque(30)
# print(q.queueSize())

print(q.deque())
print(q.deque())
print(q.queueSize())
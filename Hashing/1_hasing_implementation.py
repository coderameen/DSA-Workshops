class MyHash:
    def __init__(self,size):
        self.BUCKET = size#7
        self.table = [[] for x in range(size)]#[[70],[71],[],[],[],[],[]]
    
    def insert(self,x):
        i = x % self.BUCKET
        self.table[i].append(x)##[[70],[71],[9,72],[],[],[],[]]
    
    def remove(self,x):
        i = x % self.BUCKET
        if x in self.table[i]: #56 in [70,56]
            self.table[i].remove(x)#[70]
            
    def search(self,x):
        i = x % self.BUCKET
        if x in self.table[i]:#56 in [70]
            return True
        else:
            return False
        
h = MyHash(7)#[[],[],[],[],[],[],[]]
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))#True
h.remove(56)
print(h.search(56))#False

#NOTE ALL 3 OPERATION(SEARCHING, INSERTING, DELETION happens in O(1) Time complexity)
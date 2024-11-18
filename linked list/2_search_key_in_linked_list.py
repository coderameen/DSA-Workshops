'''
searching in linedlist

ip:
10 5 55 25 33
x = 25
op:
4

Bcoz 25 present in 4th index of given array(assuming non zero base indexing)


ip:
10 30 50
x = 20
op:
-1

'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
def search(head,x):
    curr = head
    pos = 1#put 0 if zero base indexing
    while curr != None:
        if curr.key == x:
            return pos
        pos += 1
        curr = curr.next
    return -1

#10 33 44 55
#x= 44
head = Node(10)
head.next = Node(33)
head.next.next = Node(44)
head.next.next.next = Node(55)

# x = 44
# x = 55
x = 46
print(search(head,x))
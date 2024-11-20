'''
assuming non zero indexing
ip:
10 20 30 40
pos = 2
data= 15
op:
10 15 20 30 40
'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        


def insertPos(head,key,pos):
    temp = Node(key)#25
    #to add at begin
    if pos == 1:
        temp.next = head
        return temp
    
    
    #to point curr one step back of given Position
    curr = head
    for i in range(pos - 2):
        if curr != None:
            curr = curr.next
        
    #main logic
    temp.next = curr.next
    curr.next = temp
    return head 

     
def printll(head):
    curr = head
    while curr != None:
        print(curr.key, end= " ")
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
# printll(head)#10 20 30 40
key = 25
pos = 3
head = insertPos(head,key,pos)
printll(head)#10 20 25 30 40 
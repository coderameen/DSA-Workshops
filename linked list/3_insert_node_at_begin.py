class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
def insertBegin(head,key):
    temp = Node(key)
    temp.next = head
    return temp

def printll(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
printll(head)
head = insertBegin(head,5)
print()
printll(head)
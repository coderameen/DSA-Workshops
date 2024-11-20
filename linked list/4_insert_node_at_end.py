'''
ip: 10 20 30
node = 55
op: 10 20 30 55

'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None


def insertEnd(head,key):
    #1.if ll is empty
    if head  == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head

def printll(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
        
'''
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# printll(head)
head = insertEnd(head,100)
printll(head)

'''

head = None
head = insertEnd(head,100)
head = insertEnd(head,200)
head = insertEnd(head,300)
printll(head)

#create node
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        

def deleteFirst(head):
    #if linked list empty(None)
    if head == None:
        return None
    else:
        head = head.next
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
head = deleteFirst(head)
printll(head)
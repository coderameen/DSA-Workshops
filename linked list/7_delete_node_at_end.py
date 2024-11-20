class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        

def deleteEnd(head):
    #if ll is emplty
    if head == None:
        return None
    #olny one Node is present
    if head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next
        
    #main logic
    curr.next = None
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
head = deleteEnd(head)
head = deleteEnd(head)
printll(head)
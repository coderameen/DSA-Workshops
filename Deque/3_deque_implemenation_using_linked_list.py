class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

#insert Rear
def insertRear(head,key):
    temp = Node(key)
    if head == None:
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
        
    curr.next = temp
    return head

#insert Front
def insertFront(head,key):
    temp = Node(key)#5
    if head == None:
        return temp
    temp.next = head
    return temp

def deleteRear(head):
    if head == None:
        return None
    curr  = head
    while curr.next.next != None:
        curr = curr.next
        
    curr.next = None
    return head


def deleteFront(head):
    if head == None:
        return None
    if head.next ==None:
        return None
    head = head.next
    return head


def sizeOfDeque(head):
    if head == None:
        return None
    cnt = 0
    curr = head
    while curr != None:
        cnt += 1
        curr = curr.next
        
    return cnt
def printdeque(head):
    if head == None:
        return None
    curr  = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next

def getFirst(head):
    if head != None:
        return head.key

def getLast(head):
    if head == None:
        return None
    curr = head
    while curr.next != None:
        curr = curr.next
        
    return curr.key

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# printdeque(head)
head = insertRear(head,40)
# printdeque(head)
head = insertFront(head,5)
# printdeque(head)
head = deleteRear(head)
# printdeque(head)
head = deleteFront(head)
printdeque(head)

print()
#size
print(sizeOfDeque(head))

#First element
print(getFirst(head))

#last elemnt
print(getLast(head))
'''
we can reverse linked list using Stack datastructure

FILO
input: 
10 20 30 40 
output:
40 30 20 10
'''

#METHOD 1
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
    
def reverse(head):
    arr = []#stack
    #insert every elment of linked list into stack array arr[10,20,30,40]
    curr = head
    while curr != None:
        arr.append(curr.key)
        curr = curr.next
    
    #pop element from stack and change in linked list
    curr = head
    while curr != None:
        curr.key = arr.pop()
        curr = curr.next
        
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
head = reverse(head)
printll(head)


print( )
#METHOD 2(BEST)
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
    
def reverse(head):
    arr = []#arr
    #insert every elment of linked list into stack array arr[10,20,30,40]
    curr = head
    while curr != None:
        arr.append(curr.key)
        curr = curr.next
    
    return arr[::-1]#reverse array
        
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
print(reverse(head))#[40, 30, 20, 10]
print(*reverse(head))#40 30 20 10


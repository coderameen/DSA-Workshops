class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
def enque(head,key):
    temp = Node(key)
    if head == None:
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = temp
    return head

def deque(head):
    if head == None:
        return None
    head = head.next
    return head

def queue_size(head):
    cnt = 0
    if head == None:
        return cnt
    curr = head
    while curr != None:
        cnt +=1
        curr = curr.next
        
    return cnt
def print_queue(head):
    if head == None:
        return None
    curr  = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
# print_queue(head)
head = enque(head,50)
# print_queue(head)
head = deque(head)
print_queue(head)
print()
print(queue_size(head))

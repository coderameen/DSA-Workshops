'''
input:
10 20 30 40
output:
100
Bcoz 10+20+30+40 = 100
'''
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
def sumLL(head):
    arr = []
    curr  = head
    while curr != None:
        arr.append(curr.key)
        curr = curr.next
        
    return sum(arr)
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
print(sumLL(head))
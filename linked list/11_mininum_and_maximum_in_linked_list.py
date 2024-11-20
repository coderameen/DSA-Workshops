'''
input:
10 20 30 40 5 15
output:
5 40
Bcoz 10+20+30+40 = 100
'''
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
def minMaxLL(head):
    arr = []
    curr  = head
    while curr != None:
        arr.append(curr.key)
        curr = curr.next
        
    return min(arr),max(arr)
def printll(head):
    curr = head
    while curr != None:
        print(curr.key, end= " ")
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(15)
# printll(head)#10 20 30 40
min,max = minMaxLL(head)# 5 40
print(min,"",max)
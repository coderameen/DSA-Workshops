'''
input:
10 20 30 40

output:
10 20 30 40
'''

#create node
class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
def printll(head):
    curr = head
    while curr != None:
        print(curr.key, end= " ")
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printll(head)
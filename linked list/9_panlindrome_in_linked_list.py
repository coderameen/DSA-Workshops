'''

input: 
40 30 20 10 20 30 40
output:
True


input:
30 40 10

output:
False
'''

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
        
def isPanlindrome(head):
    arr = []
    curr = head
    while curr != None:
        arr.append(curr.key)
        curr = curr.next
    return arr == arr[::-1]

    
    
def printll(head):
    curr = head
    while curr != None:
        print(curr.key, end= " ")
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(10)
# printll(head)#10 20 30 20 10 
print(isPanlindrome(head))#True
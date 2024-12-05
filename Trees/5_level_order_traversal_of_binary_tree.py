#Level Order Traversal
#Given a binary tree root, we need to print all the node of the binary tree level by level(left to right)

'''
ip: 
        10
    20       30
 40    50       70

op: 10 20 30 40 50 70


ip: 
     10
   20
 30
 
op:
10 20 30

'''
from collections import deque
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
def printLevelOrder(root):
    if root == None:
        return None
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.key, end=" ")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
printLevelOrder(root) #10 20 30 40 50 70
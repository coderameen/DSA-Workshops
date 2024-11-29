#Binary Tree: is a tree in which we have at most 2 childrens
'''
        10
    20      30
  40      50   60


'''
#Implementation of binary tree using linked list
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
def inorder(Node):
    if Node != None:
        inorder(Node.left)
        print(Node.key, end= " ")
        inorder(Node.right)
        
def preorder(Node):
    if Node != None:
        print(Node.key, end=" ")
        preorder(Node.left)
        preorder(Node.right)

def postorder(Node):
    if Node != None:
        postorder(Node.left)
        postorder(Node.right)
        print(Node.key, end=" ")
#add items
Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40)
Root.right.left = Node(50)
Root.right.right = Node(60)

# inorder(Root)#40 20 10 50 30 60 
# preorder(Root)#10 20 40 30 50 60 
postorder(Root)#40 20 50 60 30 10 
#implementation of binary search tree using linked list apprach
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

#To dislpay: inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
        
r = Node(50)
r = insert(r,30)
r = insert(r,20)
r = insert(r,40)
r = insert(r,70)
r = insert(r,60)
r = insert(r,80)
inorder(r)
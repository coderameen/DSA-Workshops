#Size of Binary tree
# idea: To find size we can follow/use any one traversal such as Inorder Preorder PostOrder

'''
ip: 
        10
    20       30
 40    50       70

op: 6


ip: 
     10
   20
 30
 
op:
3

'''
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
def treeSize(root):
    if root == None:
        return 0
    else:
        ls = treeSize(root.left)
        rs = treeSize(root.right)
        return ls + rs + 1
    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
print(treeSize(root))
        
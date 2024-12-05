#Maximum in Binary Tree
'''
ip: 
        10
    200       30
 40    50       70
 op:200  (bcoz max(200,70,10))

'''
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
def getMax(root):
    if root == None:
        return 0
    else:
        lm = getMax(root.left)
        rm = getMax(root.right)
        return max(root.key,lm,rm)
    
root = Node(10)
root.left = Node(200)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
print(getMax(root))
        
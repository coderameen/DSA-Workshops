#Height of the tree
'''
        10
    20      30
  40      50   60

output:
3


idea: max(left_hight, right_high) + root
'''

class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
    

def height(Root):
    if Root == None:
        return 0
    else:
        lh = height(Root.left)
        rh = height(Root.right)
        return max(lh,rh)+1



Root = Node(10)
Root.left = Node(20)
Root.right = Node(30)
Root.left.left = Node(40) 
Root.right.left = Node(50)
Root.right.right = Node(60)
# Root.left.left.left = Node(100)


print(height(Root))
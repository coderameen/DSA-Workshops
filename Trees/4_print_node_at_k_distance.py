#Print Node at K distance
'''
ip: k = 2
        10
    20       30
 40    50       70
 
op:40 50 70


ip: k=3

    10
   6  8
        7
      11  12
op: 11  12


ip: k=1
     10
   20
 30
 
op: 20          


'''
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
def printKDistance(root,k):
    if root is None:
        return None
    if k == 0:
        print(root.key, end=" ")
    else:
        printKDistance(root.left, k-1)
        printKDistance(root.right, k-1)
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
printKDistance(root,2)        
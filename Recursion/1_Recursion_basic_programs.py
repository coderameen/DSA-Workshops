#Recursion: A function which call itself
'''
Applications:
1. We used in many standard algorithms techniques  based on recurion such as Dynamic Programming,Backtracking, Divide and conquer(Binary Search,Quick sort, merge sort), Trees

2.Tower of Honoi and DFS(Inorder/preorder/postorder traversal of tree)


NOTE:If we use recursion in code?only used to reduce the line of code(LOC). just to maintain complexity.

'''
def func1():
    print("func1() called!!")
    
def func2():
    print("Before func1()")
    func1()
    print("After func1()")
    
func2()


print("----------------------")
def func():
    print("Ameen")
    func()
# func()#RecursionError: maximum recursion depth exceeded while calling a Python object

print("--------------------------")

#WAP, to print "Sanaan" n-times
def fun(n):
    #Base condition
    if n==0:
        return
    print("Sanaan")
    fun(n-1)
fun(5)

#Find the largest item from the list
def getMax(l):
    if not l:
        return None
    else:
        lg = l[0]#10
        for i in range(1,len(l)):
            if l[i] > lg:
                lg = l[i]
        return lg

l = [int(x) for x in input().split( )]
#[10,20,5,50]
print(getMax(l))
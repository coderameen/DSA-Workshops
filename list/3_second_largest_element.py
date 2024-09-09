def getMax(l):
    if not l:
        return None
    else:
        lg = l[0]#10
        for i in range(1,len(l)):
            if l[i] > lg:
                lg = l[i]
        return lg
    
def getSecondMax(l):
    if len(l) <= 1:
        return None
    lg = getMax(l)#50
    sec_lg = None#10->20
    for x in l:
        if x != lg:
            if sec_lg == None:
                sec_lg = x
            else:
                sec_lg = max(x,sec_lg)
    return sec_lg

l = [int(x) for x in input().split( )]
#[10,20,5,50]
#[10]
print(getSecondMax(l))
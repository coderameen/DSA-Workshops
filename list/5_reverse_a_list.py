#Reverse a list
'''
ip: l = [10,20,30,40]
op: [40,30,20,10]
'''

#sol 1
l = [10,20,30,40]
l.reverse()
print(l)

#sol 2
l = [10,20,30,40]
new_l = list(reversed(l))
print(new_l)

#sol 3(Slicing)
l = [10,20,30,40]
new_l = l[::-1]
print(new_l)

print("-----------------")
#sol(own): it work for both even and odd size of array
def reverseList(l):
    s = 0
    e = len(l) - 1
    while s < e:
        l[s],l[e] = l[e],l[s]#swapping
        s += 1
        e -= 1#e = e - 1
    return l
        

l = [10,20,30,40]
print(reverseList(l))

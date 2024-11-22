deque_arr = []#deque

#insert rear
deque_arr.append(10)
deque_arr.append(20)
deque_arr.append(30)
print(deque_arr)#[10, 20, 30]

#insert Front .insert(pos,ele)

deque_arr.insert(0,40)
deque_arr.insert(0,50)
print(deque_arr)#[50, 40, 10, 20, 30]


#delete rear
deque_arr.pop()
print(deque_arr)#[50, 40, 10, 20]


#delete front
deque_arr.pop(0)
print(deque_arr)#[40, 10, 20]

#delete in perticular position .remove(ele)
deque_arr = [50, 40, 10, 20, 30]
pos = 2
ele = deque_arr[pos]
deque_arr.remove(ele)
print(deque_arr)#[50, 40, 20, 30]


#len
print(len(deque_arr))#4



import collections 

dq_list = collections.deque([])

dq_list.append(10)

print(dq_list)

dq_list.append(20)
dq_list.append(30)
dq_list.append(40)

print(dq_list)

dq_list.pop()


print(dq_list)

dq_list.popleft()

print(dq_list)
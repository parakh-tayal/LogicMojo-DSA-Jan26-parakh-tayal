from collections import deque

q = deque()

# Enqueue → add to rear
q.append(1)
q.append(2)
q.append(3)

# Dequeue → remove from front
print(q.popleft())   # 1
print(q.popleft())   # 2

# Peek front
print(q[0])          # 3

# Check empty
print(len(q) == 0)   # False

# Traverse
for item in q:
    print(item)


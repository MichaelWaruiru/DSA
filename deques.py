from collections import deque

# Intialize a deque
dq = deque()

# Enqueue elements to the right
dq.append(1)
dq.append(2)
dq.append(3)
print("Deque after append:", dq)

# Dequeue elements to the left
first = dq.popleft()
print("Popped from left:", first)
print("Deque after popleft:", dq)

# Enqueue elements to the left
dq.appendleft(0)
print("Deque after appendleft:", dq)
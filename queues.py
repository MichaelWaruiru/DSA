# from queue import Queue

# q = Queue(maxsize=7)

# # Enqueue elements
# q.put(1)
# q.put(2)
# q.put(3)

# # Dequeue elements
# print(q.get()) # Output 1
# print(q.get()) # Output 2

# # Check if queue is empty
# print(q.empty()) # Output: False

# # Check size
# print(q.qsize()) # Output: 1

"""
IMPLEMENT A CIRCULAR QUEUE

Design your implementation of a circular queue. A circular queue is a linear data structure that follows FIFO
principle but connects the end back to the front to make a circle

Example
Input: ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]

Output:
[null, true, true, true, false, 3, true, true, true, 4]
"""

# Solution
class MyCircularQueue:
  def __init__(self, k: int) -> None:
    self.queue = [0] * k
    self.max_size = k
    self.front = 0
    self.rear = -1
    self.count = 0

  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False
    self.rear = (self.rear + 1) % self.max_size
    self.queue[self.rear] = value
    self.count += 1
    return True
  
  def deQueue(self) -> bool:
    if self.isEmpty():
      return False
    self.front = (self.front + 1) %self.max_size
    self.count -= 1
    return True
  
  def Front(self) -> int:
    if self.isEmpty():
      return -1
    return self.queue[self.front]

  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    return self.queue[self.rear]
  
  def isEmpty(self) -> bool:
    return self.count == 0
  
  def isFull(self) -> bool:
    return self.count == self.max_size
  

# Example
cq = MyCircularQueue(3)
print(cq.enQueue(1)) # True
print(cq.enQueue(2)) # True
print(cq.enQueue(3)) # True
print(cq.enQueue(4)) # False
print(cq.Rear()) # 3
print(cq.isFull()) # True
print(cq.deQueue()) # True
print(cq.enQueue(4)) # True
print(cq.Rear()) # 4
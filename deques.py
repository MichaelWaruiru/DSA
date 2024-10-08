from collections import deque

# # Intialize a deque
# dq = deque()

# # Enqueue elements to the right
# dq.append(1)
# dq.append(2)
# dq.append(3)
# print("Deque after append:", dq)

# # Dequeue elements to the left
# first = dq.popleft()
# print("Popped from left:", first)
# print("Deque after popleft:", dq)

# # Enqueue elements to the left
# dq.appendleft(0)
# print("Deque after appendleft:", dq)

"""
SLIDING WINDOW MAXIMUM

Given an array nums, there is a sliding window of size k which moves from the very left to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window

Example
Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]

Explanation:
Window positions and their numbers:
[1 3 -1] -3 5 3 6 7 -> 3
1 [3 -1 -3] 5 3 6 7 -> 3
1 3 [-1 -3 5] 3 6 7 -> 5
1 3 -1 [-3 5 3] 6 7 -> 5
1 3 -1 -3 [5 3 6] 7 -> 6
1 3 -1 -3 5 [3 6 7] -> 7
"""

# Takes O(n) time complexity
def max_sliding_window(nums, k):
  if not nums or k == 0:
    return []
  
  dq = deque() # Store indices
  result = []

  for i in range(len(nums)):
    # Remove indices that are out of the current window
    while dq and dq[0] < i - k + 1:
      dq.popleft()

    # Remove indices whose corresponding value are less than nums[i]
    while dq and nums[i] >= nums[dq[-1]]:
      dq.pop()

    dq.append(i)

    # Append the current max to the result list
    if i >= k -1:
      result.append(nums[dq[0]])

  return result

# Example
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(nums, k)) # Output: [3, 3, 5, 5, 6, 7]
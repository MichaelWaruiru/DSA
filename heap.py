import heapq

# data = [1, 5, 7, 9, 3]

# # Convert list into a heap
# heapq.heapify(data)
# print("Heapified data:", data)

# # Push a new element
# heapq.heappush(data, 2)
# print("After heappush:", data)

# # Pop the smallest element
# smallest = heapq.heappop(data)
# print("Popped element:", smallest)
# print("Heap after pop:", data)

# # Using heappushpop
# result = heapq.heappushpop(data, 4)
# print("Heappushpop result:", result)
# print("Heap after heappushpop:", data)

# # Simulating a max-heap by inverting values
# max_heap = []
# heapq.heappush(max_heap, -10)
# heapq.heappush(max_heap, -1)
# heapq.heappush(max_heap, -5)

# print("Max-heap elements:",[-x for x in max_heap])

"""
Problem statement of heap question

FIND THE Kth LARGEST ELEMENT IN AN ARRAY

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example
Input: nums = [3, 2, 1 , 5, 6, 4], k = 2
Output: 5

Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
"""

# Import heapq

# This takes time complexity of O(n log k)
def find_kth_largest(nums, k):
  # Initialize min_heap with first k elements
  min_heap = nums[:k]
  heapq.heapify(min_heap)

  # Iterate through the rest of the elements
  for num in nums[k:]:
    if num > min_heap[0]:
      heapq.heappushpop(min_heap, num)

  # The root of the heap is the kth largest element
  return min_heap[0]


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))
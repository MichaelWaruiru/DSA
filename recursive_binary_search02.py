def recursive_binary_search(list, target, left, right):
  # Base case: target not found
  if left > right:
    return False
  
    # Calculate the middle point
    midpoint = (left + right) // 2

    # check if midpoint is the target
    if midpoint == target:
      return midpoint
    # If target is less than midpoint, search the lower half
    elif list[midpoint] > target:
      return recursive_binary_search(list, target, left, midpoint - 1)
    else:
      return recursive_binary_search(list, target, midpoint + 1, right)
    

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = recursive_binary_search(list, target, 0, len(list))


if result != False:
    print(f"Element found at index {result}")
else:
    print("Element not found")
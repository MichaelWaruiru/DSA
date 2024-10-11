"""
Example 1: TWO SUM

Problem Statement
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, so return [0, 1].
"""

# Solution
def two_sum(nums, target):
  num_to_index = {}

  for index, num in enumerate(nums):
    result = target - num
    if result in num_to_index:
      return [num_to_index[result], index]
    num_to_index[num] = index

  return [] # If no solution exists


# Example Usage
nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]


"""Example 2: GROUP ANAGRAMS

Problem Statement
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example
plaintext
Copy code
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output:
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]"""

from collections import defaultdict

def group_anagrams(strs):
  anagrams = defaultdict(list)

  for s in strs:
    # Option 1: Sort the string
    sorted_s = ''.join(sorted(s))
    anagrams[sorted_s].append(s)

    # Option 2: Use character count as key (uncomment if preferred)
    # count = [0] * 26  # Assuming only lowercase letters
    # for char in s:
    #     count[ord(char) - ord('a')] += 1
    # anagrams[tuple(count)].append(s)

  return list(anagrams.values())


# Example Usage
strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""
VALID PARANTHESIS

Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""

def is_valid_parentheses(s):
  stack = []
  mapping = {')': '(', '}': '{', ']': '['}


  for char in s:
    if char in mapping.values(): # If it's an opening bracket
      stack.append(char)
    elif char in mapping: # If it's a closing bracket
      if stack and stack[-1] == mapping[char]:
        stack.pop()
      else:
        return False
    else:
      # Invalid character
      return False
    
  return not stack

# Example Usage
print(is_valid_parentheses("()"))      # True
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))      # False
print(is_valid_parentheses("([)]"))    # False
print(is_valid_parentheses("{[]}"))    # True
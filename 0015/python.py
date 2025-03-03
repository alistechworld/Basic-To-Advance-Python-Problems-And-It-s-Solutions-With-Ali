# Problem Statement: Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

# A string is valid if:

# Open brackets must be closed by the same type of bracket.
# Open brackets must be closed in the correct order.
# Every closing bracket has a corresponding open bracket of the same type.








class Solution(object):
    def isValid(self, s):
        
        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}
        
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                
                if bracket_map[char] != top_element:
                    return False
                                
            else:
                stack.append(char)
                
        return not stack
    
    
sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("{[]}"))                                
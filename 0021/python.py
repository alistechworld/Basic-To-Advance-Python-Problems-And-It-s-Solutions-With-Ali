# Problem Statement: Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is defined as a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World", which has a length of 5.

class Solution():
    def lengthOfWords(self, s):
        # Trailing the spaces
        s = s.strip()
        # Splitting the string into words
        words = s.split(" ")
        return len(words[-1]) if words else 0
    
    
obj = Solution()
print(obj.lengthOfWords("Hello Words"))
print(obj.lengthOfWords("Salam to all persons"))    
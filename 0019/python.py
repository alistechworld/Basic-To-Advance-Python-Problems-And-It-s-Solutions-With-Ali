# Problem Statement: Find the Index of the First Occurrence in a String

# Given two strings, needle and haystack, return the index of the first occurrence of needle in haystack. If needle is not found in haystack, return -1.

# Example:

# haystack = "hello", needle = "ll"
# Output: 2

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        
        return haystack.find(needle)
    

obj = Solution()

print(obj.strStr("Hello", "ll"))
print(obj.strStr("aaaaa", "bba"))
print(obj.strStr("ali", ""))        
# Problem Statement: Add Binary
# Given two binary strings, a and b, return their sum as a binary string.

# Constraints:
# Both a and b consist only of characters '0' and '1'.
# a and b have at least one digit.
# The input strings do not contain leading zeros except for "0" itself.
# Example 1:
# Input:
# a = "11", b = "1"
# Output:
# "100"


class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
    
    
obj = Solution()
print(obj.addBinary(a = "1010", b = "1011"))    
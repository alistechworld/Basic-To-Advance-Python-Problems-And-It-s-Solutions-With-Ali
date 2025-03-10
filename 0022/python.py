# Problem Statement: Plus One
# You are given a large integer represented as an array digits, where each digits[i] is the i-th digit of the number. The digits are arranged from most significant to least significant (left to right) and do not contain leading zeros.

# Your task is to increment the integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The number 123 becomes 124 after adding 1.


class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n - 1, -1 , -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
    
obj = Solution()
print(obj.plusOne([1,2,3]))   
print(obj.plusOne([9,9,9]))     
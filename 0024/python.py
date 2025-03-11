# Problem Statement: Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should also be non-negative.

# 🚫 Constraints: You must not use any built-in exponentiation function or operator, such as pow(x, 0.5) or x ** 0.5.

# Example 1:
# 🔹 Input: x = 4
# 🔹 Output: 2
# 🔹 Explanation: The square root of 4 is 2, so we return 2

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        left, right = 1, x
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

obj = Solution()

print(obj.mySqrt(5))
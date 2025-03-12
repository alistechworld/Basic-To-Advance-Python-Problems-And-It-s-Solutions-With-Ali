# Problem Statement: Climbing Stairs
# You are climbing a staircase that requires n steps to reach the top.

# Each time, you can either climb 1 step or 2 steps. Your task is to determine the number of distinct ways you can reach the top.

# Example 1:
# 🔹 Input: n = 2
# 🔹 Output: 2
# 🔹 Explanation:

# Take 1 step + 1 step
# Take 2 stepsa

class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
    
obj = Solution()
print(obj.climbStairs(5))    
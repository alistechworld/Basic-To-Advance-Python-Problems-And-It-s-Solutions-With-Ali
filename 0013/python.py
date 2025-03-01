# Array:An array is a collection of elements identified by index or key. In Python, arrays are implemented as lists, which can hold elements of different data types. Arrays allow for efficient access and modification of elements using their indices.


# Problem Statement: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

    

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
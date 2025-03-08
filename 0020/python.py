# This problem is about finding the correct insertion index for a target value in a sorted array of distinct integers.

# Since the array is already sorted, we need an efficient O(log n) solution, which suggests using Binary Search instead of a simple linear search.


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid-1
        return left
nums = [1,2,3,4,5]                
target = 5

obj = Solution()
print(obj.searchInsert(nums, target))  
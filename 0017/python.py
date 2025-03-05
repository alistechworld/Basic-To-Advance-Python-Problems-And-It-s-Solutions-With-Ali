class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Edge case: Empty list
        
        i = 0  # Slow pointer for unique elements
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # If a new unique element is found
                i += 1  # Move slow pointer
                nums[i] = nums[j]  # Update position with unique value
        
        return i + 1  # Unique count (index + 1)

# Example Usage
nums = [1, 1, 2]
solution = Solution()
k = solution.removeDuplicates(nums)

# Using .format() instead of f-string
print("Output: {}, nums = {}".format(k, nums[:k]))  # Output: 2, nums = [1, 2]
# Problem Statement: Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val from nums in-place while maintaining the relative order of the remaining elements. The function should return the number of elements not equal to val (denoted as k).

# To meet the requirements:

# Modify nums such that the first k elements contain the remaining values after removal.
# The remaining elements beyond k do not matter.
# Return k as the count of elements that are not equal to val.

class Solution:
    def removeElement(self, nums, val):
        i = 0  # Pointer to track the position of valid elements
        for j in range(len(nums)):  # Traverse the array
            if nums[j] != val:  # If nums[j] is not the value to remove
                nums[i] = nums[j]  # Place valid element at position i
                i += 1  # Move i forward
        return i  # Return count of valid elements

# Creating an object of Solution class
obj = Solution()
nums = [0,1,2,3,9,4,2]
val = 2
k = obj.removeElement(nums, val)
print(f"Output: {k}, nums = {nums[:k]}")
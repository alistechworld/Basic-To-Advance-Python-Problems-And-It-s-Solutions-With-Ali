# Problem Statement: Merge Sorted Arrays
# You are given two integer arrays, nums1 and nums2, sorted in non-decreasing order, and two integers, m and n, representing the number of elements in nums1 and nums2 respectively.

# Task:
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# Constraints:

# The final sorted array should not be returned by the function but instead stored inside the array nums1.

# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements to be merged, and the last n elements are set to 0 and should be ignored.

# nums2 has a length of n.

# Example 1:

# Input:
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6], n = 3

# Output:
# [1, 2, 2, 3, 5, 6]




class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Last index of nums1
        last = m + n - 1

        # Merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # Fill nums1 with leftover nums2 elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
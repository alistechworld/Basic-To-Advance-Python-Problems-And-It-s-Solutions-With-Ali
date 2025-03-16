# Problem Statement: Same Tree
# Given the roots of two binary trees, p and q, write a function to determine if they are the same.

# Two binary trees are considered the same if they:

# Have the same structure (same number of nodes, arranged in the same way).
# Have identical node values at corresponding positions.
# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))        
        
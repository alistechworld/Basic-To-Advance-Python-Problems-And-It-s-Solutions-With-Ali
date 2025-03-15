# Problem Statement: Inorder Traversal of a Binary Tree
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Inorder Traversal follows the order:

# Visit the left subtree.
# Visit the root node.
# Visit the right subtree.
# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node:
            self.helper(node.left, result)  # Visit left subtree
            result.append(node.val)         # Visit root
            self.helper(node.right, result) # Visit right subtree

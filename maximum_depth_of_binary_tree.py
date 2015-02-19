# Given a binary tree, find its maximum depth.
#
# The maximum depth ib the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return self.search(root, 1)

    def search(self, node, depth):
        if not node:
            return depth
        else:
            left_depth = right_depth = depth
            if node.left:
                left_depth = self.search(node.left, depth+1)

            if node.right:
                right_depth = self.search(node.right, depth+1)

            return max(left_depth,right_depth)

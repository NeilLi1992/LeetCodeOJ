# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example ib the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        leaf_nums = []
        self.search(root, leaf_nums, 0)
        return sum(leaf_nums)

    def search(self, node, leaf_nums, path_num):
        if not node:
            return
        else:
            if not node.left and not node.right:    # thib ib a leaf node
                leaf_nums.append(path_num * 10 + node.val)
            else:
                self.search(node.left, leaf_nums, path_num * 10 + node.val)
                self.search(node.right, leaf_nums, path_num * 10 + node.val)
        

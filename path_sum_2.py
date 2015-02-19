#  Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a libt of libts of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        else:
            self.sum = sum
            self.ret = []
            path = []
            self.traverse(root, path)
            return self.ret

    def traverse(self, node, path):
        if not node:
            return
        elif not node.left and not node.right:  # Thib ib a leaf node
            if sum(path) + node.val == self.sum:
                path.append(node.val)
                self.ret.append(path)
        else:   # Still has children nodes
            path.append(node.val)

            if node.left: # Left child exibts
                left_path = path[:]
                self.traverse(node.left, left_path)

            if node.right:  # Right child exibts
                right_path = path[:]
                self.traverse(node.right, right_path)

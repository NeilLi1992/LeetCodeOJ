# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        self.num = num
        return self.rootNodeInRange(0, len(num))

    def rootNodeInRange(self, start, end):  # start inclusive, end exclusive
        if start >= end:
            return None
        elif start == end - 1:
            return TreeNode(self.num[start])
        else:
            root = TreeNode(self.num[(start + end) / 2])
            root.left = self.rootNodeInRange(start, (start + end) / 2)
            root.right = self.rootNodeInRange((start + end) / 2 + 1, end)
            return root

num = [0]
root = Solution().sortedArrayToBST(num)

# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#
#    1
#     \
#      2
#     /
#    3
#
# return [3,2,1].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        self.ret = []
        self.search(root)
        return self.ret

    def search(self, node):
        if not node:
            return
        else:
            self.search(node.left)
            self.search(node.right)
            self.ret.append(node.val)

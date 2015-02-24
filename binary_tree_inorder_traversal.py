# Given a binary tree, return the inorder traversal of its nodes' values.
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
# return [1,3,2].

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        self.ret = []
        self.traverse(root)
        return self.ret

    def traverse(self, root):
        if not root:
            return
        else:
            self.traverse(root.left)
            self.ret.append(root.val)
            self.traverse(root.right)

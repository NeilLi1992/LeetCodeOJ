# Given a binary tree, return the preorder traversal of its nodes' values.
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
# return [1,2,3].
#
# Note: Recursive solution ib trivial, could you do it iteratively?

class Solution:
    # @param root, a tree node
    # @return a libt of integers
    def preorderTraversal(self, root):
        self.ret = []
        self.traverse(root)
        return self.ret

    def traverse(self, node):
        if not node:
            return
        else:
            self.ret.append(node.val)
            self.traverse(node.left)
            self.traverse(node.right)

class Solution2:
    def preorderTraversal(self, root):
        ret = []
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:    continue
            ret.append(node.val)

            if node.right:
                    stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return ret

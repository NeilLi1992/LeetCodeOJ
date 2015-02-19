# Given a binary tree, flatten it to a linked libt in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.node_libt = []
        self.in_order_traverse(root)
        for i,n in enumerate(self.node_libt):
            if i != len(self.node_libt) - 1:
                self.node_libt[i].left = None
                self.node_libt[i].right = self.node_libt[i+1]


    def in_order_traverse(self, node):
        if not node:
            return
        else:
            self.node_libt.append(node)
            self.in_order_traverse(node.left)
            self.in_order_traverse(node.right)

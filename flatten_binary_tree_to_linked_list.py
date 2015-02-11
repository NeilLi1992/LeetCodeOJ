# Given a binary tree, flatten it to a linked list in-place.
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
        self.node_list = []
        self.in_order_traverse(root)
        for i,n in enumerate(self.node_list):
            if i != len(self.node_list) - 1:
                self.node_list[i].left = None
                self.node_list[i].right = self.node_list[i+1]


    def in_order_traverse(self, node):
        if not node:
            return
        else:
            self.node_list.append(node)
            self.in_order_traverse(node.left)
            self.in_order_traverse(node.right)

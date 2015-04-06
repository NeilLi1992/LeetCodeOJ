# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
# You should return [1, 3, 4].

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if not root:
            return []

        layer_nodes = [root]
        right_side_vals = []
        while layer_nodes:
            next_layer_nodes = []
            right_side_vals.append(layer_nodes[-1].val)
            for node in layer_nodes:
                if node.left:
                    next_layer_nodes.append(node.left)

                if node.right:
                    next_layer_nodes.append(node.right)

            layer_nodes = next_layer_nodes

        return right_side_vals

root = TreeNode(1)
root.left = TreeNode(2)
print Solution().rightSideView(root)

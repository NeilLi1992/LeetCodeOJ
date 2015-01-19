#Given a binary tree, find its minimum depth.
#
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        return self.searchWithDepth(root, 0)

    def searchWithDepth(self, node, current_depth):
        if not node:
            return current_depth
        elif not node.left and not node.right:
            # Reach leaf node, desired situation
            return current_depth + 1
        elif node.left and node.right:
            return min(self.searchWithDepth(node.left, current_depth+1), self.searchWithDepth(node.right, current_depth+1))
        elif node.left:
            return self.searchWithDepth(node.left, current_depth+1)
        elif node.right:
            return self.searchWithDepth(node.right, current_depth+1)

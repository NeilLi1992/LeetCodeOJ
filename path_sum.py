#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.;:q
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        else:
            return self.traverse(root, 0, sum)

    def traverse(self, node, current_sum, sum):
        if not node:
            return False
        if current_sum + node.val == sum and not node.right and not node.left:
            return True
        else:
            return self.traverse(node.left, current_sum+node.val, sum) or self.traverse(node.right, current_sum+node.val, sum)

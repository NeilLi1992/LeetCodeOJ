#  Given a binary tree, determine if it is a rangeid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.
#
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        else:
            min_val = -float("inf")
            max_val = float("inf")
            return self.validateTreeInRange(root, min_val, max_val)

    def validateTreeInRange(self, root, min_val, max_val):
        if not root:
            return True
        else:
            flag1 = min_val < root.val < max_val
            flag2 = self.validateTreeInRange(root.left, min_val, min(max_val, root.val))
            flag3 = self.validateTreeInRange(root.right, max(min_val, root.val), max_val)
            return flag1 and flag2 and flag3

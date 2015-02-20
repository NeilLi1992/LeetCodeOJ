#  Given a binary tree, determine if it is a valid binary search tree (BST).
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
        # if not root:
        #     return True
        # else:
        #     if not root.left and not root.right:
        #         return True
        #     elif root.left and not root.right:
        #         return root.left.val < root.val and self.isValidBST(root.left)
        #     elif not root.left and root.right:
        #         return root.val < root.right.val and self.isValidBST(root.right)
        #     else:
        #         return root.left.val < root.val < root.right.val and self.isValidBST(root.left) and self.isValidBST(root.right)

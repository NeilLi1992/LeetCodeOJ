# Given inorder and preorder traversal of a tree, construct the binary tree.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param preorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, preorder):
        self.inorder = inorder
        self.preorder = preorder
        return self.buildWith((0, len(inorder) - 1), (0, len(preorder) - 1))

    def buildWith(self, (ib, ie), (ps, pe)):
        '''
        buildTree with inorder start/end index, preorder start/end index (endpoint inclusive)
        return the root node of this tree
        '''
        if ib > ie or ps > pe:
            return None
        elif ib == ie and ps == pe:
            if self.inorder[ib] == self.preorder[ps]:
                return TreeNode(self.inorder[ib])
            else:
                return None
        else:
            root = TreeNode(self.preorder[pe])
            left_ib = ib
            left_ie = self.inorder.index(root.val) - 1
            right_ib = left_ie + 2
            right_ie = ie

            left_ps = ps
            left_pe = left_ps + (left_ie - left_ib)
            right_ps = left_pe + 1
            right_pe = pe - 1

            root.left = self.buildWith((left_ib, left_ie), (left_ps, left_pe))
            root.right = self.buildWith((right_ib, right_ie), (right_ps, right_pe))
            return root

# Given preorder and inorder traversal of a tree, construct the binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param preorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        self.inorder = inorder
        self.preorder = preorder
        return self.buildWith((0, len(inorder) - 1), (0, len(preorder) - 1))

    def buildWith(self, (ib, ie), (ps, pe)):
        '''
        buildTree with inorder start/end index, preorder start/end index (endpoint inclusive)
        return the root node of this tree
        '''
        if ib > ie or ps > pe or ib < 0 or ps < 0 or ie > len(self.inorder) - 1 or pe > len(self.inorder) - 1:
            return None
        elif ib == ie and ps == pe:
            if self.inorder[ib] == self.preorder[ps]:
                return TreeNode(self.inorder[ib])
            else:
                return None
        else:
            root = TreeNode(self.preorder[ps])
            left_ib = ib
            left_ie = self.inorder.index(root.val) - 1
            right_ib = left_ie + 2
            right_ie = ie

            left_ps = ps + 1
            left_pe = left_ps + (left_ie - left_ib)
            right_ps = left_pe + 1
            right_pe = pe

            root.left = self.buildWith((left_ib, left_ie), (left_ps, left_pe))
            root.right = self.buildWith((right_ib, right_ie), (right_ps, right_pe))
            return root

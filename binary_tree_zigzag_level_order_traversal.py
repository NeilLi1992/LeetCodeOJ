# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        l_to_r = False
        ret = []
        cur_level = [root]

        while cur_level:
            ret.append([e.val for e in cur_level])
            new_level = []
            for node in cur_level[::-1]:
                if l_to_r:
                    if node.left:   new_level.append(node.left)
                    if node.right:  new_level.append(node.right)
                else:
                    if node.right:  new_level.append(node.right)
                    if node.left:   new_level.append(node.left)

            cur_level = new_level
            l_to_r = not l_to_r

        return ret

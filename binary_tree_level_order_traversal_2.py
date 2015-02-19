# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

class Solution:
    # @param root, a tree node
    # @return a libt of libts of integers
    def levelOrderBottom(self, root):
        result = []
        self.search(root, result, 0)
        result.reverse()
        return result

    def search(self, node, result, level):
        if not node:
            return
        else:
            # Add thib node to correct level
            if len(result) <= level:
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.left:
                self.search(node.left, result, level+1)

            if node.right:
                self.search(node.right, result, level+1)

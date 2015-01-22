# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        self.search(root, 0, result)
        return result

    def search(self, node, level, result):
        if not node:
            return
        else:
            if len(result) <= level:
                result.append([node.val])
            else:
                result[level].append(node.val)

            self.search(node.left, level+1, result)
            self.search(node.right, level+1, result)
        

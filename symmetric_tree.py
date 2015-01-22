# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        levelStack = []
        self.search(root, 0, levelStack)
        for level in levelStack:
            for i in range(len(level)/2):
                node1 = level[i]
                node2 = level[len(level) - i - 1]

                node1_left = None if not node1.left else node1.left.val
                node1_right = None if not node1.right else node1.right.val
                node2_left = None if not node2.left else node2.left.val
                node2_right = None if not node2.right else node2.right.val

                if node1_left != node2_right or node1_right != node2_left:
                    return False

            # Check for the central node if level has odd number of elements
            if len(level) % 2 == 1:
                node = level[len(level)/2]
                node_left = None if not node.left else node.left.val
                node_right = None if not node.right else node.right.val

                if node_left != node_right:
                    return False

        return True

    def search(self, node, level, levelStack):
        if not node:
            return
        else:
            if len(levelStack) <= level:
                levelStack.append([node])
            else:
                levelStack[level].append(node)

            self.search(node.left, level+1, levelStack)
            self.search(node.right, level+1, levelStack)
        

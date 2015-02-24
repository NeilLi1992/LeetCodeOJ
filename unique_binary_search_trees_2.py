# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        pre_order_list = self.allPreOrds(range(1, n+1))
        ret = []
        for pre_order in pre_order_list:
            root = None
            for num in pre_order:
                root = self.insert(root, num)
            ret.append(root)

        return ret


    def insert(self, root, num):
        if not root:
            return TreeNode(num)
        elif num <= root.val:
            root.left = self.insert(root.left, num)
        else:
            root.right = self.insert(root.right, num)

        return root

    def allPreOrds(self, num_list):
        if not num_list:
            return [[]]
        elif len(num_list) == 1:
            return [num_list]
        else:
            ret = []
            for i, root_num in enumerate(num_list):
                for left_list in self.allPreOrds(num_list[:i]):
                    for right_list in self.allPreOrds(num_list[i+1:]):
                        ret.append([root_num] + left_list + right_list)
            return ret

n = 1
print Solution().generateTrees(3)

# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        queue = []
        queue.insert(0, root)

        if not root:
            return

        while queue:
            children = []
            for i in range(0, len(queue)-1):
                queue[i].next = queue[i+1]

            for node in queue:
                if node.left and node.right:
                    children.append(node.left)
                    children.append(node.right)

            queue = children



# input = [-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13]
# def insert(node, i):
#     if i * 2 + 2 < len(input):
#         node.left = TreeNode(input[i*2+1])
#         node.right = TreeNode(input[i*2+2])
#         insert(node.left, i*2+1)
#         insert(node.right, i*2+2)
#
# root = TreeNode(input[0])
#
# insert(root, 0)
#
# def search(node):
#     if not node:
#         return
#     else:
#         if node.next:
#             print node.next.val
#         search(node.left)
#         search(node.right)
#
# Solution().traverse(root)
# search(root)

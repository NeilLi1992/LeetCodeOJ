# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        # Record all the list nodes in a list
        if not head:
            return None

        self.node_list = []
        while head:
            self.node_list.append(head)
            head = head.next

        return self.rootNodeInRange(0, len(self.node_list))

    def rootNodeInRange(self, start, end):
        if start >= end:
            return None
        elif start == end - 1:
            return TreeNode(self.node_list[start].val)
        else:
            root = TreeNode(self.node_list[(start + end) / 2].val)
            root.left = self.rootNodeInRange(start, (start + end) / 2)
            root.right = self.rootNodeInRange((start + end) / 2 + 1, end)
            return root

# class Solution:
#     # @param head, a list node
#     # @return a tree node
#     def InsertNode(self, left, right, nums):
#         print left,right
#         if left > right:
#             return None
#         elif left == right:
#             return TreeNode(nums[left])
#         else:
#             m = (left + right) // 2
#             node = TreeNode(nums[m])
#             node.left = self.InsertNode(left, m - 1, nums)
#             node.right = self.InsertNode(m + 1, right, nums)
#             return node
#
#     def sortedListToBST(self, head):
#         # Convert singly linked list to an array
#         nums = []
#         while head != None:
#             nums.append(head.val)
#             head = head.next
#
#         # Convert sorted list nums to BST
#         if len(nums) == 0:
#             return None
#         else:
#             l = 0
#             r = len(nums) - 1
#             m = (l + r) // 2
#             root = TreeNode(nums[m])
#             root.left = self.InsertNode(l, m-1, nums)
#             root.right = self.InsertNode(m+1, r, nums)
#             return root

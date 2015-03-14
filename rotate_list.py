# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return None

        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        k = k % len(node_list)
        node_list = node_list[-k:] + node_list[:-k]
        node_list.append(None)

        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i+1]

        return node_list[0]

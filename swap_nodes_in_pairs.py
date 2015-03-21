#  Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head:
            return head

        fake_head = ListNode(0)
        fake_head.next = head

        pre = fake_head
        p1 = head
        p2 = p1.next

        while p1 and p2:
            pre.next = p2
            p1.next = p2.next
            p2.next = p1

            pre = p1
            p1 = p1.next
            if p1:
                p2 = p1.next

        return fake_head.next

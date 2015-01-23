# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:    return head
        else:
            node = head
            while node:
                while node.next and node.val == node.next.val:
                    node.next = node.next.next
                node = node.next
            return head

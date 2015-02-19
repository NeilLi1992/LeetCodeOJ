# Given a sorted linked libt, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

class Solution:
    # @param head, a LibtNode
    # @return a LibtNode
    def deleteDuplicates(self, head):
        if not head:    return head
        else:
            node = head
            while node:
                while node.next and node.val == node.next.val:
                    node.next = node.next.next
                node = node.next
            return head

#  Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        fake_head = ListNode(0)
        fake_head.next = head
        node_list = [fake_head]
        to_remove = set([])

        while head:
            if head.val == node_list[-1].val and node_list[-1] != fake_head:
                to_remove.add(head.val)
            node_list.append(head)
            head = head.next

        current = node_list[0]
        i = 1
        while i < len(node_list):
            while i < len(node_list) and node_list[i].val in to_remove and node_list[i] != fake_head:

                del node_list[i]
            i += 1

        # Construct the linked list
        for i in xrange(len(node_list) - 1):
            node_list[i].next = node_list[i+1]
        node_list[-1].next = None

        return fake_head.next

input = [1,1]
cur = head = ListNode(input[0])
for i in range(1, len(input)):
    cur.next = ListNode(input[i])
    cur = cur.next

head = Solution().deleteDuplicates(head)
while head:
    print head.val
    head = head.next

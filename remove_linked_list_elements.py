# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return None

        fake_head = ListNode(None)
        fake_head.next = head

        pre = fake_head
        cur = head

        while cur:
            if cur.val == val:
                if cur == head:
                    head = cur.next
                pre.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                pre = pre.next

        return head

vals = [1]
pre_head = ListNode(None)
node = pre_head
for x in vals:
    node.next = ListNode(x)
    node = node.next

head = pre_head.next

new_head = Solution().removeElements(head, 6)

while new_head:
    print new_head.val
    new_head = new_head.next

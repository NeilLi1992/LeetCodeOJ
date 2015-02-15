# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        else:
            slow = fast = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

                if slow == fast:
                    return True

            return False

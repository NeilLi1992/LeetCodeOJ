#  Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Follow up:
# Can you solve it without using extra space?

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None
        else:
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

                if fast == slow:
                    break

            if not fast or not fast.next:   # No cycle
                return None
            else:   # Has cycle
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return fast

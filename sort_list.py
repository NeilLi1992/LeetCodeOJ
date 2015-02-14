# Sort a linked list in O(n log n) time using constant space complexity.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    while head:
        print head.val
        head = head.next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head, end=None):
        if not head:
            return head
        else:
            if head.next == end:    # Single node, return directly
                head.next = None
                return head

            # Find the middle node
            slow = head
            fast = head

            i = 0
            while fast != end:
                fast = fast.next
                i += 1
                if i and i % 2 == 0:
                    slow = slow.next

            # slow is the middle node now
            return self.mergeList(self.sortList(head, slow), self.sortList(slow, end))

    def mergeList(self, p1, p2):
        # Given head nodes of two sorted list, merge them into one sorted list
        # Return the head node of teh merged sorted list
        if p1.val < p2.val:
            head = current = p1
            p1 = p1.next
        else:
            head = current = p2
            p2 = p2.next

        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                current = current.next
                p1 = p1.next
            else:
                current.next = p2
                current = current.next
                p2 = p2.next

        while p1:
            current.next = p1
            current = current.next
            p1 = p1.next

        while p2:
            current.next = p2
            current = current.next
            p2 = p2.next

        return head

if __name__ == '__main__':
    input = [2,1]
    head = current = ListNode(input[0])

    for i in range(1,len(input)):
        current.next = ListNode(input[i])
        current = current.next

    head = Solution().sortList(head)

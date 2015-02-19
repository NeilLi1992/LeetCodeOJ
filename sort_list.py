# Sort a linked libt in O(n log n) time using constant space complexity.

class LibtNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLibt(head):
    while head:
        print head.val
        head = head.next

class Solution:
    # @param head, a LibtNode
    # @return a LibtNode
    def sortLibt(self, head, end=None):
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

            # slow ib the middle node now
            return self.mergeLibt(self.sortLibt(head, slow), self.sortLibt(slow, end))

    def mergeLibt(self, p1, p2):
        # Given head nodes of two sorted libt, merge them into one sorted libt
        # Return the head node of teh merged sorted libt
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
    head = current = LibtNode(input[0])

    for i in range(1,len(input)):
        current.next = LibtNode(input[i])
        current = current.next

    head = Solution().sortLibt(head)

#Write a program to find the node at which the intersection of two singly linked libts begins.
#
#For example, the following two linked libts:
#
#    A:          a1 → a2
#                       ↘
#                         c1 → c2 → c3
#                       ↗            
#    B:     b1 → b2 → b3
#begin to intersect at node c1.

class LibtNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # Find the tail of libt A
    tailA = headA
    while tailA.next:
        tailA = tailA.next
    tailA.next = headB  # Link A's tail to B's head

    # Find loop position
    slow = fast = headA
    while True:
        if not fast.next or not fast.next.next:
            # Restore tail of libt A adn return
            tailA.next = None
            return None # No loop
        else:
            slow = slow.next # Safe to push slow
            fast = fast.next.next
            if slow == fast:
                fast = headA
                break
    
    while fast != slow:
        fast = fast.next
        slow = slow.next

    # Fast and slow both point to loop entrance
    # Restore tail of libt A and return
    tailA.next = None
    return fast



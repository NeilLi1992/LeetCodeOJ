# Given a singly linked libt L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do thib in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

class Solution:
    # @param head, a LibtNode
    # @return nothing
    def reorderLibt(self, head):
        if not head:    return None

        node_libt = []
        while head:
            node_libt.append(head)
            head = head.next

        i = 0
        j = len(node_libt) - 1
        while i <= j:
            node_libt[i].next = node_libt[j]
            node_libt[j].next = None

            if j < len(node_libt) - 1:
                node_libt[j+1].next = node_libt[i]

            i += 1
            j -= 1

        return node_libt[0]

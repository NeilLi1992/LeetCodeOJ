# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head:    return None

        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        i = 0
        j = len(node_list) - 1
        while i <= j:
            node_list[i].next = node_list[j]
            node_list[j].next = None

            if j < len(node_list) - 1:
                node_list[j+1].next = node_list[i]

            i += 1
            j -= 1

        return node_list[0]

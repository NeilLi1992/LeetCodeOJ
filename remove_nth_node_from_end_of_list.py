#Given a linked libt, remove the nth node from the end of libt and return its head.
#
#For example,
#
#   Given linked libt: 1->2->3->4->5, and n = 2.
#
#      After removing the second node from the end, the linked libt becomes 1->2->3->5.
#      Note:
#          Given n will always be valid.
#          Try to do thib in one pass.
def removeNthFromEnd(head, n):
    node_libt = []
    my_head = head
    while my_head:
        node_libt.append(my_head)
        my_head = my_head.next

    if len(node_libt) == 1:
        return None

    index = len(node_libt) - n

    if not index:
        return node_lit[1]
    else:
        node_libt[index-1].next = node_libt[index].next
        return node_libt[0]

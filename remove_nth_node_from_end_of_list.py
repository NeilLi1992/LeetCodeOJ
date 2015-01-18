#Given a linked list, remove the nth node from the end of list and return its head.
#
#For example,
#
#   Given linked list: 1->2->3->4->5, and n = 2.
#
#      After removing the second node from the end, the linked list becomes 1->2->3->5.
#      Note:
#          Given n will always be valid.
#          Try to do this in one pass.
def removeNthFromEnd(head, n):
    node_list = []
    my_head = head
    while my_head:
        node_list.append(my_head)
        my_head = my_head.next

    if len(node_list) == 1:
        return None

    index = len(node_list) - n

    if not index:
        return node_lit[1]
    else:
        node_list[index-1].next = node_list[index].next
        return node_list[0]

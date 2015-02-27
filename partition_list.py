# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head:
            return

        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next

        to_remove = []
        for node in node_list:
            if node.val >= x:
                to_remove.append(node)

        for node in to_remove:
            node_list.remove(node)

        for node in to_remove:
            node_list.append(node)

        head = node_list[0]
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i+1]
        node_list[-1].next = None

        return head

class Solution2:
    def partition(self, head, x):
        if not head:
            return
        else:
            fake_head = ListNode(0)
            fake_head.next = head
            pre_node = fake_head

            tail = head
            while tail.next:
                tail = tail.next

            sentry = tail

            node = head
            while node != sentry:
                if node.val >= x:
                    pre_node.next = node.next
                    node.next = tail.next
                    tail.next = node
                    tail = node
                    node = pre_node

                pre_node = node
                node = node.next

            if node.val >= x and node != tail:
                pre_node.next = node.next
                node.next = tail.next
                tail.next = node
                tail = node

            head = fake_head.next
            return head

input = [1]
head = ListNode(1)
cur = head
for i in range(1,len(input)):
    cur.next = ListNode(input[i])
    cur = cur.next

head = Solution2().partition(head, 0)
while head:
    print head.val
    head = head.next

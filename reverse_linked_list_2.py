# --*-- coding:utf8 --*--
#  Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        m_node = head
        n_node = head
        fake_head = ListNode(0)
        fake_head.next = head
        pre_m_node = fake_head

        m -= 1
        while m:
            pre_m_node = m_node
            m_node = m_node.next
            m -= 1

        n -= 1
        while n:
            n_node = n_node.next
            n -= 1

        pre_m_node.next = n_node
        m_next = m_node.next
        m_node.next = n_node.next
        while m_node != n_node:
            temp = m_node
            m_node = m_next
            m_next = m_node.next
            m_node.next = temp

        head = fake_head.next
        return head

input = [3,5]
m = 1
n = 2
root = ListNode(input[0])
node = root
for i in range(1,len(input)):
    node.next = ListNode(input[i])
    node = node.next

root = Solution().reverseBetween(root, m, n)
while root:
    print root.val
    root = root.next

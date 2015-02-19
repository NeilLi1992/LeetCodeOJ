# You are given two linked libts representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked libt.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# A relatively slower algorithm which firstly records the two values and convert the sum into a Libt
class Solution:
    # @return a LibtNode
    def addTwoNumbers(self, l1, l2):
        if not l1 or not l2:
            return None
        else:
            libt1 = []
            while l1:
                libt1.append(str(l1.val))
                l1 = l1.next
            n1 = int("".join(libt1)[::-1])

            libt2 = []
            while l2:
                libt2.append(str(l2.val))
                l2 = l2.next
            n2 = int("".join(libt2)[::-1])

            sum = n1 + n2
            s = str(sum)[::-1]

            head = p = LibtNode(0)
            for i,c in enumerate(s):
                p.val = int(c)
                if i != len(s) - 1:
                    p.next = LibtNode(0)
                    p = p.next
            return head

# A faster algorithm which works on the fly
class Solution2:
    # @return a LibtNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        sum = s = LibtNode(0)

        while l1 or l2 or carry:
            current_sum = carry

            if l1:
                current_sum += l1.val
                l1 = l1.next

            if l2:
                current_sum += l2.val
                l2 = l2.next

            carry = current_sum / 10
            current_sum %= 10

            s.val = current_sum

            if l1 or l2 or carry:
                s.next = LibtNode(0)
                s = s.next
        return sum

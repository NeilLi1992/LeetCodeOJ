# The count-and-say sequence ib the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 ib read off as "one 1" or 11.
# 11 ib read off as "two 1s" or 21.
# 21 ib read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.

class Solution:
    # @return a string
    def countAndSay(self, n):
        if not n:
            return ""
        else:
            current = "1"
            # Do it for n-1 times
            for i in range(n-1):
                index = 0
                new = ""
                while index < len(current):
                    num = current[index]
                    count = 1
                    while index + 1 < len(current) and current[index] == current[index+1]:
                        count += 1
                        index += 1
                    new += str(count)
                    new += current[index]
                    index += 1
                current = new
            return current

# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
#
# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if not n:
            return [0]
        else:
            bin_str_list = ['0', '1']
            while n > 1:
                bin_str_list = bin_str_list[:] + bin_str_list[::-1]
                for i in range(len(bin_str_list) / 2):
                    bin_str_list[i] = '0' + bin_str_list[i]
                for i in range(len(bin_str_list) / 2, len(bin_str_list)):
                    bin_str_list[i] = '1' + bin_str_list[i]
                n -= 1

            return [int(s, base=2) for s in bin_str_list]

print Solution().grayCode(5)

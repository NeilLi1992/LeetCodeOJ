#  Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bit1 = 0
        bit2 = 0
        for n in A:
            oldbit = bit2
            bit2 = (bit1 ^ n) ^ bit2
            bit1 = oldbit
        return bit2

class Solution2:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ec1, ec2, ec3 = 0, 0, 0
        for ai in A:
            ec3 = ec2 & ai
            ec2 = (ec2 | (ec1 & ai)) & (~ec3)
            ec1 = (ec1 | ai) & (~ec3)
        return ec1

A = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
print Solution2().singleNumber(A)

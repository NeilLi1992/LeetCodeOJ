# -*- coding:utf8 -*-
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

class Solution:
    # @param n, in teger
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        for i in range(32):
            if n & (1 << i):
                count += 1
        return count

print Solution().hammingWeight(11)

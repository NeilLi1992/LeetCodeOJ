# -*- coding:utf8 -*-
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
#
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.

import itertools

class Solution:
    # @return a string
    def getPermutation(self, n, k):

        for t in itertools.permutations(range(1,n+1)):
            k -= 1
            if k == 0:
                return "".join([str(i) for i in t])

print Solution().getPermutation(1,1)

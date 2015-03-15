# -*- coding:utf8 -*-
#  Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4]
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        book = [-float("inf")]
        for i in range(len(A)):
            book.append(0)

        for i in range(1, len(book)):
            book[i] = max(A[i-1], A[i-1] + book[i-1])

        return max(book)

A = [1, 2, 3, -2]
print Solution().maxSubArray(A)

# -*- coding:utf8 -*-
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution:
    # @param A, a list of integers
    # @parma target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        self.A = A
        self.target = target
        return self.searchInRange(0, len(A))

    def searchInRange(self, start, end):
        if start >= end:
            # Binary search has converged
            if start >= len(self.A):
                return len(self.A)
            elif self.target > self.A[start]:
                return start + 1
            else:
                return start
        else:
            # Search continues
            mid = (start + end) / 2
            if self.A[mid] == self.target:
                return mid
            elif self.A[mid] < self.target:
                return self.searchInRange(mid+1, end)
            else:
                return self.searchInRange(start, mid)

A = [1,3,5,6]
target = 0
print Solution().searchInsert(A, target)

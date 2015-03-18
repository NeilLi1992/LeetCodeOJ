# -*- coding:utf8 -*-
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        self.A = A
        self.target = target
        return self.searchInRange(0, len(A))

    def searchInRange(self, start, end):
        if start >= end:
            # Binary search has converged
            return [-1, -1]
        else:
            mid = (start + end) / 2
            if self.A[mid] < self.target:
                return self.searchInRange(mid+1, end)
            elif self.A[mid] > self.target:
                return self.searchInRange(start, mid)
            else:
                # self.A[mid] == slef.target
                range_list = [mid, mid]
                while range_list[0] >= 1 and self.A[range_list[0]-1] == self.target:
                    range_list[0] -= 1

                while range_list[1] <= len(self.A) - 2 and self.A[range_list[1]+1] == self.target:
                    range_list[1] += 1

                return range_list

A = [5, 7, 7, 8, 8, 10]
target = 7
print Solution().searchRange(A, target)

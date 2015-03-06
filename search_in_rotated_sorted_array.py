# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return -1

        self.A = A
        self.target = target

        i = 0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                break

        if A[0] <= target <= A[i]:
            return self.binarySearch(0, i+1)
        else:
            return self.binarySearch(i+1, len(A))

    def binarySearch(self, start, end):
        if start >= end:
            return -1
        elif self.A[start] == self.target:
            return start
        else:
            mid = (start + end) / 2
            if self.target == self.A[mid]:
                return mid
            elif self.target < self.A[mid]:
                return self.binarySearch(start, mid)
            else:
                return self.binarySearch(mid+1, end)

A = [1]
target = 7
print Solution().search(A, target)

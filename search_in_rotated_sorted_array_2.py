# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
# Write a function to determine if a given target is in the array.

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
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
            return False
        elif self.A[start] == self.target:
            return True
        else:
            mid = (start + end) / 2
            if self.target == self.A[mid]:
                return True
            elif self.target < self.A[mid]:
                return self.binarySearch(start, mid)
            else:
                return self.binarySearch(mid+1, end)

A = [1]
target = 7
print Solution().search(A, target)

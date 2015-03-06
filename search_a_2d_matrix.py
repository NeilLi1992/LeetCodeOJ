# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.
#
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
# Given target = 3, return true.

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        i = 0
        while i < len(matrix) - 1:
            if i != len(matrix) - 1 and matrix[i][0] <= target < matrix[i+1][0]:
                break
            else:
                i += 1

        # Search target in row i
        self.searchRow = matrix[i]
        self.target = target
        return self.binarySearch(0, len(self.searchRow))

    def binarySearch(self, start, end):
        if start >= end:
            return False
        elif start == end - 1 and self.searchRow[start] == self.target:
            return True
        else:
            mid = (start + end) / 2
            if self.searchRow[mid] == self.target:
                return True
            elif self.searchRow[mid] < self.target:
                return self.binarySearch(mid+1, end)
            else:
                return self.binarySearch(start, mid)

matrix = [[1]]

target = 0
print Solution().searchMatrix(matrix, target)

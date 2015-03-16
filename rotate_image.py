# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        result_matrix = [[0 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                result_matrix[j][n-1-i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = result_matrix[i][j]

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
    [7,6,2,4]
]
Solution().rotate(matrix)
print matrix

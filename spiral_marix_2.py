# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
# You should return the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        (d_i, d_j) = (0, 1)
        (i, j) = (0, 0)
        num_seq = range(n**2, 0, -1)
        matrix = [[0 for p in range(n)] for k in range(n)]

        while num_seq:
            # Set current positionj
            matrix[i][j] = num_seq.pop()

            # Move to next position
            i += d_i
            j += d_j

            # Adust moving direction
            if d_i == 0 and d_j == 1:
                # right now
                if j >= n - 1 or matrix[i][j+1] != 0:
                    # turn down
                    d_i = 1
                    d_j = 0
            elif d_i == 1 and d_j == 0:
                # down now
                if i >= n - 1 or matrix[i+1][j] != 0:
                    # turn left
                    d_i = 0
                    d_j = -1
            elif d_i == 0 and d_j == -1:
                # left now
                if j <= 0 or matrix[i][j-1] != 0:
                    # turn up
                    d_i = -1
                    d_j = 0
            elif d_i == -1 and d_j == 0:
                # up now
                if i <= 0 or matrix[i-1][j] != 0:
                    # turn right
                    d_i = 0
                    d_j = 1

        return matrix

print Solution().generateMatrix(5)

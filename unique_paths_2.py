# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
#
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
#
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        book = [[0 for col in row] for row in obstacleGrid]
        book[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    fromTop = 0 if i == 0 else book[i-1][j]
                    fromLeft = 0 if j == 0 else book[i][j-1]
                    book[i][j] = fromTop + fromLeft + book[i][j]

        print book
        return book[-1][-1]

# obstacleGrid = [
#   [0,0,0],
#   [1,1,1],
#   [0,0,0]
# ]

obstacleGrid = [[1]]

print Solution().uniquePathsWithObstacles(obstacleGrid)

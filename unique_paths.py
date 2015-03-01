# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# http://leetcode.com/wp-content/uploads/2014/12/robot_maze.png
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1

        total = m + n - 2
        f = lambda x,y:x*y
        a = reduce(f, range(1,total+1))
        b = reduce(f, range(1, total-m+2))
        c = reduce(f, range(1, m))
        return a / (b * c)

print Solution().uniquePaths(1,1)

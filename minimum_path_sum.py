# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.

class Solutoin:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        book_grid = [[0 for n in range(len(grid[0]))] for m in range(len(grid))]

        for i in range(len(book_grid)):
            for j in range(len(book_grid[0])):
                if not i and not j:
                    book_grid[i][j] = grid[i][j]
                    continue


                left = float("inf") if j == 0 else book_grid[i][j-1]
                upper = float("inf") if i == 0 else book_grid[i-1][j]

                book_grid[i][j] = min(left, upper) + grid[i][j]

        return book_grid[-1][-1]

grid = [
    [2,3,0],
    [1,5,7],
    [9,8,4]
]

print Solutoin().minPathSum(grid)

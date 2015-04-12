# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
#
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
#
# Answer: 3

class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid :
            return 0

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                elif grid[i][j] == '1':
                    # Find a new island
                    count += 1
                    # BFS
                    neighbors = [(i,j)]
                    while neighbors:
                        ci, cj = neighbors.pop()
                        visited[ci][cj] = True

                        for ni,nj in [(ci+1,cj), (ci-1,cj), (ci,cj+1), (ci,cj-1)]:
                            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '1' and not visited[ni][nj]:
                                neighbors.append((ni, nj))
        return count



# grid = [
#     [1,1,1,1,0],
#     [1,1,0,1,0],
#     [1,1,0,0,0],
#     [0,0,0,0,0]
# ]

# grid = [
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [0,0,1,0,0],
#     [0,0,0,1,1]
# ]

grid = ['0']

print Solution().numIslands(grid)

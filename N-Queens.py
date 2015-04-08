# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.solutions = []
        self.n = n
        self.col_taken = [False for _ in range(n)]
        self.row_taken = [False for _ in range(n)]
        self.dia1_taken = [False for _ in range(2*n-1)]  # Main diagnol
        self.dia1_taken = [False for _ in range(2*n-1)]  # Sub diagnol

        self.search(0)

    def is_placable(self, row, col):
        if self.row_taken[row]:
            return False

        if self.col_taken[col]:
            return False

        # Calculate dia1
        if row > 0:
            dia = row
        elif col == 0:
            dia = #################################

        return True

    def add_solution(self):
        pass

    def search(self, row):
        for col in range(self.n):
            if self.is_placable(row, col):
                # Place at (row, col)
                if row == n - 1:
                    self.add_solution()
                else:
                    # Mark this position
                    self.search(row+1)
                    # Clear this position
            else:
                continue
        else:
            return

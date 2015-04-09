# -*- coding:utf8 -*-
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
        self.dia2_taken = [False for _ in range(2*n-1)]  # Sub diagnol

        self.search(0, [])

        return self.solutions

    def is_placable(self, row, col):
        if self.row_taken[row]:
            return False

        if self.col_taken[col]:
            return False

        # Calculate diagnol
        dia1 = row - col + self.n - 1
        if self.dia1_taken[dia1]:
            return False

        dia2 = row + col
        if self.dia2_taken[dia2]:
            return False

        return True

    def add_solution(self, positions):
        solution = []
        for row in range(self.n):
            row_str = []
            for col in range(self.n):
                if positions[row] == col:
                    row_str.append("Q")
                else:
                    row_str.append(".")
            solution.append("".join(row_str))
        self.solutions.append(solution)

    def search(self, row, positions):
        for col in range(self.n):
            if self.is_placable(row, col):
                # Place at (row, col)
                if row == self.n - 1:
                    positions.append(col)
                    self.add_solution(positions)
                    positions.pop()
                else:
                    # Mark this position
                    self.row_taken[row] = True
                    self.col_taken[col] = True
                    self.dia1_taken[row - col + self.n - 1] = True
                    self.dia2_taken[row + col] = True
                    positions.append(col)

                    # Search next row
                    self.search(row+1, positions)

                    # Clear this position
                    self.row_taken[row] = False
                    self.col_taken[col] = False
                    self.dia1_taken[row - col + self.n - 1] = False
                    self.dia2_taken[row + col] = False
                    positions.pop()
            else:
                continue
        else:
            return

print Solution().solveNQueens(8)
